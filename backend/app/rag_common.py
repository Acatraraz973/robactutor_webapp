"""
Shared RAG retrieval logic -- used by both deployable services (the
Cloud Run grading service and the HF Spaces ask-mode Gradio app), each of
which loads its own copy of the FAISS index + chunk metadata + MiniLM
embedder. Split out from robactutor_backend.py so neither deployment target
has to import the other's generation/hybrid-grading dependencies just to
get retrieval.

The local dev backend (robactutor_backend.py, main.py -- includes
/demo/grade-comparison) is untouched and does NOT import this module; it
keeps its own copies of these functions so local dev behaves exactly as it
always has, independent of how the two public deployments are split.
"""
import json
import re
from typing import Optional

import faiss
from sentence_transformers import SentenceTransformer

from .config import settings

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


print("[rag_common] Loading RAG index + embedder...")
rag_index = faiss.read_index(settings.RAG_INDEX_PATH)
with open(settings.RAG_CHUNKS_PATH, encoding="utf-8") as f:
    chunk_metadata = json.load(f)
rag_embedder = SentenceTransformer(settings.RAG_EMBEDDER_NAME)


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
