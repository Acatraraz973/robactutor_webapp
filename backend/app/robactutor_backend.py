"""
RoBacTutor backend module -- Testeaza-te (practice + grade) and Ask (free question).

Everything here is built directly from what was validated in the Colab pipeline:
hybrid similarity grading (Cell 23) + real barem + RAG manual reference (Cell 29/31),
NOT raw generative grading -- that failed reliably across subjects (see dissertation Ch5 notes).

SECURITY NOTE:
- /practice/start returns a question WITHOUT its barem/answer key.
- /practice/grade looks the barem up server-side by question_id. Never trust a
  barem or points_total sent from the client -- it would let a student see or
  fake the answer key from the browser's network tab.

ASK MODE STATUS: validated across all 4 subjects (matematica, istorie, limba_romana,
limba_engleza) via ask_mode_colab.ipynb, comparing extractive/base/adapter answers
on the same questions. Result:
  - Adapter-enabled generation: unusable. Failed all 4 subjects differently --
    barem-format intrusion, a hallucinated self-instruction + verbatim repeat
    (matematica), a fabricated "ANCE 2024" citation AND a wrong date (istorie:
    said 23 iunie 1939, correct is 23 august 1939), a complete non-sequitur
    (limba_romana: answered about punctuation when asked about metaphor), and
    a degenerate repetition loop that never answered the question (limba_engleza).
  - Base model (adapter disabled): accurate and on-topic on all 4 subjects.
  - Extractive (no generation): relevant real passages on all 4 subjects.
ASK_MODE_USE_ADAPTER is therefore False below -- do not set it True without new
evidence. /ask uses base-model generation grounded in RAG context, with the
retrieved passages always returned alongside so the student can verify the
answer against the real source, same principle already validated for grading.
Only 4 questions were tested per subject; broader testing before full production
launch is still worthwhile, but the pattern here is consistent with every other
generative-grading failure seen in this project, so this is not a weak signal.

DEMO COMPARISON: /demo/grade-comparison runs the validated hybrid grader and
the raw adapter side by side on the same answer, so the negative-result finding
(adapter reliably fails at grading) is visible live in the demo/viva, not just
described in the write-up. The generation model is loaded once, with the
adapter attached, and disable_adapter() toggles base-vs-adapter behaviour on
the same weights -- this is why /ask and /demo/grade-comparison share one
loader (_get_generation_model) instead of two separate model instances.
"""

import json
import random
import re
import uuid
from pathlib import Path
from typing import Optional

import faiss
import torch
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

from .config import settings

router = APIRouter()

# Ask mode: validated via ask_mode_colab.ipynb across all 4 subjects.
# Adapter-enabled generation failed all 4 (barem-format intrusion, a fake
# citation + wrong historical date, an off-topic non-sequitur, and a
# degenerate repetition loop). Base model (adapter disabled) was accurate
# on all 4. Keep this False.
ASK_MODE_USE_ADAPTER = False


# ---------------------------------------------------------------------------
# Pydantic schemas
# ---------------------------------------------------------------------------

class QuestionOut(BaseModel):
    question_id: str
    subject: str
    instruction: str
    points_total: int
    # Deliberately no barem/answer field here -- see security note above.


class StartPracticeRequest(BaseModel):
    session_id: Optional[str] = None
    subject: str


class GradeRequest(BaseModel):
    session_id: str
    question_id: str
    student_answer: str


class ReferencePassage(BaseModel):
    text: str
    filename: str
    score: float


class GradeResponse(BaseModel):
    punctaj_estimat: float
    punctaj_total: int
    similaritate: float
    raspuns_final_potrivit: Optional[bool]  # None = subject has no single extractable final answer
    barem_oficial: str
    material_referinta: list[ReferencePassage]


class AskRequest(BaseModel):
    subject: str
    question: str


class AskResponse(BaseModel):
    answer: str
    experimental: bool
    material_referinta: list[ReferencePassage]


class DemoCompareRequest(BaseModel):
    question_id: str
    student_answer: str


class DemoCompareResponse(BaseModel):
    validated_result: GradeResponse
    adapter_raw_output: str
    disclaimer: str


# ---------------------------------------------------------------------------
# Loaded once at import time (mirrors what was validated in Colab)
# ---------------------------------------------------------------------------

def extract_total_points(response_text: str) -> int:
    match = re.search(r"\((\d+)\s*puncte\)", response_text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r"(\d+)\s*puncte", response_text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))
    fragments = re.findall(r"\((\d+)\s*p\.?\)", response_text)
    if fragments:
        return sum(int(f) for f in fragments)
    return 0


def clean_barem_text(raw_barem: str) -> str:
    """Strip the fabricated citation artifact found across the training
    dataset (see dissertation Ch5 data-quality audit -- dataset_quality_audit.py).
    The line 'Notă: Acest răspuns este bazat pe baremul oficial ANCE <year>.'
    does not correspond to any real official source and must never be shown
    to a student as if it were part of the genuine barem. Stripping it also
    removes irrelevant text from the hybrid-grading similarity calculation,
    which was previously embedding this boilerplate as if it were content."""
    cleaned = re.sub(
        r"\*?Not[ăa]:\s*Acest r[ăa]spuns este bazat pe baremul oficial ANCE\s*\d{4}\.?\*?",
        "", raw_barem, flags=re.IGNORECASE,
    )
    return cleaned.strip()


def load_question_bank(dataset_path: Path) -> list[dict]:
    bank = []
    with open(dataset_path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            bank.append({
                "id": f"q{i}",
                "subject": item["metadata"]["subject"],
                "instruction": item["instruction"],
                "barem": clean_barem_text(item["response"]),
                "barem_raw": item["response"],  # unmodified, for /demo/grade-comparison only
                "points_total": extract_total_points(item["response"]),
            })
    return bank


print("[robactutor_backend] Loading question bank...")
question_bank = load_question_bank(Path(settings.DATASET_PATH))
question_by_id = {q["id"]: q for q in question_bank}

print("[robactutor_backend] Loading RAG index + embedder...")
rag_index = faiss.read_index(settings.RAG_INDEX_PATH)
with open(settings.RAG_CHUNKS_PATH, encoding="utf-8") as f:
    chunk_metadata = json.load(f)
rag_embedder = SentenceTransformer(settings.RAG_EMBEDDER_NAME)

print("[robactutor_backend] Loading hybrid grading embedder...")
hybrid_embed_model = SentenceTransformer(settings.HYBRID_EMBEDDER_NAME)

# Generation model: loaded lazily since it's the heaviest piece. Always loads
# WITH the adapter attached (PeftModel), regardless of ASK_MODE_USE_ADAPTER --
# the demo comparison endpoint needs both adapter and base output from the
# same loaded weights. Use disable_adapter() to get base-model behaviour;
# never call the underlying base model directly -- PEFT modifies it in-place,
# so a direct call would still run adapter-modified weights (bug caught
# earlier in the Testeaza-te notebook, Cell 10).
_gen_model = None
_gen_tokenizer = None


def _get_generation_model():
    global _gen_model, _gen_tokenizer
    if _gen_model is None:
        print("[robactutor_backend] Loading generation model + adapter...")
        _gen_tokenizer = AutoTokenizer.from_pretrained(settings.ADAPTER_PATH)
        base = AutoModelForCausalLM.from_pretrained(
            settings.BASE_MODEL_NAME, load_in_4bit=True, device_map={"": 0},
        )
        _gen_model = PeftModel.from_pretrained(base, settings.ADAPTER_PATH)
        _gen_model.eval()
    return _gen_model, _gen_tokenizer


def generate_answer(system_prompt: str, instruction: str, use_adapter: bool,
                     max_new_tokens: int = 400, temperature: float = 0.3) -> str:
    model, tokenizer = _get_generation_model()
    prompt = f"<s>[INST] {system_prompt}\n\n{instruction} [/INST]"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    def _run():
        with torch.no_grad():
            output_ids = model.generate(
                **inputs, max_new_tokens=max_new_tokens, temperature=temperature,
                do_sample=True, top_p=0.9, pad_token_id=tokenizer.eos_token_id,
            )
        return tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()

    if use_adapter:
        return _run()
    with model.disable_adapter():
        return _run()


# Per-session "no repeats until pool exhausted" state.
# In-memory dict is fine for a single-instance dissertation demo; swap for
# Redis/DB if this ever runs behind more than one worker process.
_session_asked: dict[str, set[str]] = {}


# ---------------------------------------------------------------------------
# RAG retrieval (matches Cell 27/29 in the validated notebook)
# ---------------------------------------------------------------------------

# ~57% of matematica chunks are unusable PDF-extraction garbage (math notation
# -- fractions, integrals, exponents -- breaks plain text extraction; other
# subjects are ~0-1% affected). See dissertation Ch5. Threshold 0.25 was
# calibrated against real corpus data: clears known-garbled chunks (score
# ~0.20) with margin below known-good formula-dense chunks (~0.38-0.55),
# while keeping matematica's index large enough to still retrieve well
# (1,567 of 2,924 chunks survive; other subjects barely affected, 94-100%).
MIN_READABILITY = 0.25

_word_re = re.compile(r"^[A-Za-zĂÂÎȘȚăâîșț]{2,}$")


def readability_score(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0
    real_words = sum(1 for w in words if _word_re.match(w))
    return real_words / len(words)


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


def get_reference_material(instruction: str, subject: str, top_k: int = 2) -> list[dict]:
    retrieved = retrieve(instruction, subject=subject, source_type="manual", top_k=top_k)
    if not retrieved:
        retrieved = retrieve(instruction, subject=subject, top_k=top_k)
    return retrieved


# ---------------------------------------------------------------------------
# Hybrid grading (matches Cell 23 -- validated, not raw generative grading)
# ---------------------------------------------------------------------------

def extract_final_answer_tokens(barem_text: str) -> list:
    """Extract the final numeric answer(s) from barem text, e.g. '84' from
    'Coeficient = C(9,6) = 84', or ['-2/3'] from 'S = {-2/3}'. Lines
    mentioning 'punct' are excluded first -- those are point-value
    annotations (e.g. 'Punctaj: 8 puncte'), not the mathematical answer;
    naively taking the last number in the whole text would otherwise grab
    the point value instead of the real answer."""
    lines = re.split(r"[\n•]", barem_text)
    candidate_lines = [l for l in lines if l.strip() and "punct" not in l.lower()]
    if not candidate_lines:
        return []
    last_line = candidate_lines[-1]

    set_match = re.search(r"\{([^}]+)\}", last_line)
    if set_match:
        parts = re.split(r"[;,]", set_match.group(1))
        return [p.strip() for p in parts if p.strip()]

    if "=" in last_line:
        after_eq = last_line.split("=")[-1].strip()
        num_match = re.search(r"[-+]?\d+(?:[.,]\d+)?(?:/\d+)?", after_eq)
        if num_match:
            return [num_match.group(0)]
    return []


def normalize_number_token(token: str) -> str:
    return token.strip().replace(",", ".").replace(" ", "")


def final_answer_match_ratio(barem_text: str, student_answer: str) -> Optional[float]:
    """Fraction of the barem's final-answer token(s) found as standalone
    numbers in the student's answer. Returns None if the barem has no
    single extractable final numeric answer (typical for istorie/limba
    subjects), in which case grading falls back to pure similarity,
    unchanged from before this fix."""
    barem_tokens = [normalize_number_token(t) for t in extract_final_answer_tokens(barem_text)]
    barem_tokens = [t for t in barem_tokens if t]
    if not barem_tokens:
        return None
    student_numbers = {
        normalize_number_token(m)
        for m in re.findall(r"[-+]?\d+(?:[.,]\d+)?(?:/\d+)?", student_answer)
    }
    matched = sum(1 for t in barem_tokens if t in student_numbers)
    return matched / len(barem_tokens)


def grade_answer_hybrid(question: dict, student_answer: str) -> dict:
    emb_student = hybrid_embed_model.encode(student_answer, convert_to_tensor=True)
    emb_barem = hybrid_embed_model.encode(question["barem"], convert_to_tensor=True)
    similarity = max(0.0, util.cos_sim(emb_student, emb_barem).item())

    # Calibration testing found pure similarity rewards matching the barem's
    # phrasing/notation over actually being correct: a wrong final answer
    # wrapped in barem-like steps scored HIGHER (6.7/8) than a fully correct
    # but differently-worded answer (5.8/8) on a real test item. Fix: for
    # items with an extractable final numeric answer, gate the score on
    # whether the student's answer contains it. Correct final answer floors
    # the score at a strong minimum regardless of phrasing; wrong/missing
    # final answer caps it, so surface similarity to the barem can no longer
    # substitute for being right. See dissertation Ch5 calibration notes --
    # tested against the real failure case before shipping (evaluation/calibration_test.py).
    final_match = final_answer_match_ratio(question["barem"], student_answer)
    if final_match is None:
        adjusted = similarity  # no extractable final answer -- unchanged fallback
        final_correct = None
    elif final_match >= 0.999:
        adjusted = max(similarity, 0.75)
        final_correct = True
    else:
        cap = 0.35 + 0.35 * final_match
        adjusted = min(similarity, cap)
        final_correct = False

    estimated_points = round(adjusted * question["points_total"], 1)

    return {
        "punctaj_estimat": estimated_points,
        "punctaj_total": question["points_total"],
        "similaritate": round(similarity, 3),  # raw similarity, kept for transparency/debugging
        "raspuns_final_potrivit": final_correct,
        "barem_oficial": question["barem"],
    }


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
# NOTE: GET /subjects is intentionally not defined here -- main.py already
# serves it (richer shape, with display labels/icons for the sidebar).

@router.post("/practice/start", response_model=QuestionOut)
def start_practice(req: StartPracticeRequest):
    if req.subject not in settings.SUBJECTS:
        raise HTTPException(400, f"Unknown subject: {req.subject}")

    session_id = req.session_id or str(uuid.uuid4())
    asked = _session_asked.setdefault(session_id, set())

    pool = [q for q in question_bank if q["subject"] == req.subject and q["id"] not in asked]
    if not pool:
        pool = [q for q in question_bank if q["subject"] == req.subject]
        asked.clear()
    if not pool:
        raise HTTPException(404, f"No questions available for subject: {req.subject}")

    chosen = random.choice(pool)
    asked.add(chosen["id"])

    return QuestionOut(
        question_id=chosen["id"],
        subject=chosen["subject"],
        instruction=chosen["instruction"],
        points_total=chosen["points_total"],
    )


@router.post("/practice/grade", response_model=GradeResponse)
def grade_practice(req: GradeRequest):
    question = question_by_id.get(req.question_id)
    if question is None:
        raise HTTPException(404, f"Unknown question_id: {req.question_id}")

    result = grade_answer_hybrid(question, req.student_answer)
    reference = get_reference_material(question["instruction"], question["subject"])

    return GradeResponse(
        **result,
        material_referinta=[ReferencePassage(**r) for r in reference],
    )


@router.post("/ask", response_model=AskResponse)
def ask_question(req: AskRequest):
    """Validated across all 4 subjects with base-model generation (adapter
    disabled) -- see ASK_MODE_USE_ADAPTER notes above. Still flagged
    `experimental=True` in the response because only 4 questions per subject
    were tested; keep the reference passages visible to the student regardless
    so the answer is always independently checkable, not just trusted."""
    if req.subject not in settings.SUBJECTS:
        raise HTTPException(400, f"Unknown subject: {req.subject}")

    reference = get_reference_material(req.question, req.subject, top_k=3)
    context = "\n\n".join(r["text"] for r in reference)

    system_prompt = (
        "Esti un tutor pentru Bacalaureatul din Republica Moldova. "
        "Raspunde folosind DOAR informatia din materialul de referinta de mai jos. "
        "Daca materialul nu contine raspunsul, spune ca nu ai suficiente informatii."
    )
    instruction = f"Material de referinta:\n{context}\n\nIntrebare: {req.question}"
    answer = generate_answer(system_prompt, instruction, use_adapter=ASK_MODE_USE_ADAPTER)

    return AskResponse(
        answer=answer,
        experimental=True,
        material_referinta=[ReferencePassage(**r) for r in reference],
    )


# ---------------------------------------------------------------------------
# Demo comparison endpoint -- shows the adapter's raw (unvalidated) grading
# attempt alongside the actual validated hybrid result. Exists specifically
# so the negative-result finding is visible live in the app/viva, not just
# described in Ch5/6 -- see dissertation notes on adapter failure modes.
# NEVER use adapter_raw_output as an actual grade; it is display-only.
# ---------------------------------------------------------------------------

ADAPTER_GRADING_SYSTEM_PROMPT = (
    "Esti un profesor care corecteaza raspunsuri de examen conform unui barem oficial. "
    "Primesti cerinta, baremul oficial si raspunsul elevului. "
    "Evalueaza STRICT raspunsul elevului fata de barem -- nu genera propriul raspuns la intrebare. "
    "Raspunde DOAR in format JSON cu cheile: scor_acordat, scor_total, "
    "criterii_indeplinite (lista), criterii_lipsesc (lista), explicatie."
)


def build_adapter_grading_instruction(question: dict, student_answer: str) -> str:
    return (
        f"Cerinta: {question['instruction']}\n\n"
        f"Barem oficial ({question['points_total']} puncte): {question['barem_raw']}\n\n"
        f"Raspunsul elevului: {student_answer}"
    )


@router.post("/demo/grade-comparison", response_model=DemoCompareResponse)
def demo_grade_comparison(req: DemoCompareRequest):
    """Runs both the validated hybrid grader AND the raw fine-tuned adapter
    on the same answer, for side-by-side display. See module docstring --
    the adapter reliably fails here (barem-format intrusion, fabricated
    citations, occasionally factual errors); this endpoint exists to make
    that comparison visible, not to offer the adapter as a real option."""
    question = question_by_id.get(req.question_id)
    if question is None:
        raise HTTPException(404, f"Unknown question_id: {req.question_id}")

    hybrid_result = grade_answer_hybrid(question, req.student_answer)
    reference = get_reference_material(question["instruction"], question["subject"])
    validated = GradeResponse(
        **hybrid_result,
        material_referinta=[ReferencePassage(**r) for r in reference],
    )

    instruction = build_adapter_grading_instruction(question, req.student_answer)
    adapter_output = generate_answer(
        ADAPTER_GRADING_SYSTEM_PROMPT, instruction, use_adapter=True, temperature=0.2,
    )

    return DemoCompareResponse(
        validated_result=validated,
        adapter_raw_output=adapter_output,
        disclaimer=(
            "Acest raspuns este generat de modelul fine-tuned FARA validare si este afisat "
            "doar in scop demonstrativ/comparativ pentru disertatie. Nu reprezinta un punctaj real."
        ),
    )
