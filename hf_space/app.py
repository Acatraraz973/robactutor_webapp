"""
RoBacTutor ask-mode -- HF Spaces (ZeroGPU) deployment.

ZeroGPU Spaces only support the Gradio SDK, not plain FastAPI routes
(confirmed against current HF docs/forums, not assumed) -- so /ask is
wrapped as a Gradio function decorated with @spaces.GPU instead of a
FastAPI route. The frontend calls it via Gradio's HTTP API
(POST /gradio_api/call/ask, then GET /gradio_api/call/ask/<event_id> for
the SSE result -- confirmed against the deployed Space; Gradio 5.x moved
these routes under /gradio_api/, not top-level /call/ as in Gradio 4.x),
not a plain fetch -- see frontend/src/api.js.

This is a self-contained deployment: it does NOT import anything from
backend/app/, since this file lives in its own HF Spaces git repo,
separate from the main project repo. Retrieval logic is duplicated from
backend/app/rag_common.py on purpose -- see that file's docstring for why
each deployable service keeps its own copy instead of sharing imports
across two different git remotes.

Before pushing to your Space, copy these in next to this file:
    artifacts/lora_adapter/   <- same contents as backend/artifacts/lora_adapter/
    artifacts/rag/            <- same contents as backend/artifacts/rag/
See docs/deployment.md for the exact steps.

/demo/grade-comparison is NOT included here -- it stays local-dev only,
per the deployment plan (never deployed publicly, on this Space or
anywhere else).
"""
import json
import re
from pathlib import Path
from typing import Optional

import faiss
import gradio as gr
import spaces
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"
BASE_MODEL_NAME = "OpenLLM-Ro/RoMistral-7B-Instruct"
ADAPTER_PATH = str(ARTIFACTS_DIR / "lora_adapter")
RAG_INDEX_PATH = str(ARTIFACTS_DIR / "rag" / "robactutor_faiss.index")
RAG_CHUNKS_PATH = str(ARTIFACTS_DIR / "rag" / "robactutor_chunks.json")
RAG_EMBEDDER_NAME = "all-MiniLM-L6-v2"
SUBJECTS = ["matematica", "limba_romana", "limba_engleza", "istorie"]

SYSTEM_PROMPT = (
    "Esti un tutor pentru Bacalaureatul din Republica Moldova. "
    "Raspunde folosind DOAR informatia din materialul de referinta de mai jos. "
    "Daca materialul nu contine raspunsul, spune ca nu ai suficiente informatii."
)

# Ask mode: validated across all 4 subjects via ask_mode_colab.ipynb, adapter
# disabled. Adapter-enabled generation failed all 4 subjects differently
# (barem-format intrusion, fabricated citation + wrong historical date,
# off-topic non-sequitur, degenerate repetition loop). See dissertation Ch5.
# Do not set this True without new evidence.
ASK_MODE_USE_ADAPTER = False

# ---------------------------------------------------------------------------
# RAG retrieval (same logic as backend/app/rag_common.py)
# ---------------------------------------------------------------------------
MIN_READABILITY = 0.25
_word_re = re.compile(r"^[A-Za-zĂÂÎȘȚăâîșț]{2,}$")


def readability_score(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0
    real_words = sum(1 for w in words if _word_re.match(w))
    return real_words / len(words)


print("[hf_space] Loading RAG index + embedder...")
rag_index = faiss.read_index(RAG_INDEX_PATH)
with open(RAG_CHUNKS_PATH, encoding="utf-8") as f:
    chunk_metadata = json.load(f)
rag_embedder = SentenceTransformer(RAG_EMBEDDER_NAME)


def retrieve(query: str, subject: Optional[str] = None,
             source_type: Optional[str] = None, top_k: int = 3) -> list[dict]:
    query_embedding = rag_embedder.encode(
        [query], convert_to_numpy=True, normalize_embeddings=True
    ).astype("float32")
    scores, indices = rag_index.search(query_embedding, top_k * 8)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0:
            continue
        meta = chunk_metadata[idx]
        if subject and meta["subject"] != subject:
            continue
        if source_type and meta.get("source_type") != source_type:
            continue
        if readability_score(meta["text"]) < MIN_READABILITY:
            continue
        results.append({
            "text": meta["text"],
            "filename": meta.get("filename", "necunoscut"),
            "score": float(score),
        })
        if len(results) >= top_k:
            break
    return results


def get_reference_material(instruction: str, subject: str, top_k: int = 3) -> list[dict]:
    retrieved = retrieve(instruction, subject=subject, source_type="manual", top_k=top_k)
    if not retrieved:
        retrieved = retrieve(instruction, subject=subject, top_k=top_k)
    return retrieved


# ---------------------------------------------------------------------------
# Generation model -- loaded lazily on first call, inside the @spaces.GPU
# function (ZeroGPU only attaches a physical GPU for the duration of a
# decorated call, so CUDA/4-bit loading can't happen at plain import time).
# ---------------------------------------------------------------------------
_gen_model = None
_gen_tokenizer = None


def _get_generation_model():
    global _gen_model, _gen_tokenizer
    if _gen_model is None:
        print("[hf_space] Loading generation model + adapter...")
        _gen_tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        base = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL_NAME, quantization_config=bnb_config, device_map={"": 0},
        )
        _gen_model = PeftModel.from_pretrained(base, ADAPTER_PATH)
        _gen_model.eval()
    return _gen_model, _gen_tokenizer


@spaces.GPU
def ask(question: str, subject: str) -> dict:
    """The public API function -- called by the main frontend as
    POST /gradio_api/call/ask, matching the api_name set on the Blocks
    event below."""
    if subject not in SUBJECTS:
        return {"error": f"Unknown subject: {subject}"}

    reference = get_reference_material(question, subject, top_k=3)
    context = "\n\n".join(r["text"] for r in reference)
    full_instruction = f"Material de referinta:\n{context}\n\nIntrebare: {question}" if context else question
    prompt = f"<s>[INST] {SYSTEM_PROMPT}\n\n{full_instruction} [/INST]"

    model, tokenizer = _get_generation_model()
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    def _generate():
        with torch.no_grad():
            output_ids = model.generate(
                **inputs, max_new_tokens=400, temperature=0.3,
                do_sample=True, top_p=0.9, pad_token_id=tokenizer.eos_token_id,
            )
        return output_ids

    # Mirrors robactutor_backend.py's generate_answer(): ASK_MODE_USE_ADAPTER
    # actually gates which weights run, rather than being a documented-but-dead
    # constant next to a hardcoded disable_adapter() call.
    if ASK_MODE_USE_ADAPTER:
        output_ids = _generate()
    else:
        with model.disable_adapter():
            output_ids = _generate()
    new_tokens = output_ids[0][inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

    return {
        "answer": answer,
        "experimental": True,
        "material_referinta": reference,
    }


with gr.Blocks(title="RoBacTutor -- Ask mode (internal API)") as demo:
    gr.Markdown(
        "## RoBacTutor ask-mode API\n"
        "This Space is called internally by the RoBacTutor web app's "
        "**Întreabă** screen -- it isn't meant to be used directly here. "
        "Open the main app instead."
    )
    question_in = gr.Textbox(label="Question")
    subject_in = gr.Dropdown(choices=SUBJECTS, value="matematica", label="Subject")
    output = gr.JSON(label="Response")
    btn = gr.Button("Ask")
    btn.click(fn=ask, inputs=[question_in, subject_in], outputs=output, api_name="ask")

if __name__ == "__main__":
    demo.launch()
