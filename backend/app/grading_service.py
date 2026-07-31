"""
RoBacTutor grading service -- Testeaza-te (practice + grade) only.
Deployment target: Cloud Run, CPU-only, no GPU/generation dependencies.

Covers /practice/start and /practice/grade. Deliberately excludes /ask and
/demo/grade-comparison -- those need the 4-bit generation model and live
elsewhere (HF Spaces ZeroGPU for /ask; /demo/grade-comparison is local-dev
only, never deployed publicly). Keeping this service free of
transformers.AutoModelForCausalLM / peft / bitsandbytes imports is what
keeps its Docker image and runtime RAM small enough to fit a normal
CPU-only host -- see docs/deployment.md for the sizing math.

This is a leaner sibling of robactutor_backend.py (which stays local-dev
only, unchanged, and still has everything including /demo/grade-comparison).
The hybrid-grading logic here is copied rather than imported from
robactutor_backend.py on purpose, so this module has zero import-time
dependency on that file's torch/peft/bitsandbytes imports.
"""
import json
import random
import re
import uuid
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

from .config import settings
from .rag_common import get_reference_material

router = APIRouter()


# ---------------------------------------------------------------------------
# Pydantic schemas
# ---------------------------------------------------------------------------

class QuestionOut(BaseModel):
    question_id: str
    subject: str
    instruction: str
    points_total: int
    # Deliberately no barem/answer field here -- see security note below.


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


# ---------------------------------------------------------------------------
# Question bank (loaded once at import time)
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
                "points_total": extract_total_points(item["response"]),
            })
    return bank


print("[grading_service] Loading question bank...")
question_bank = load_question_bank(Path(settings.DATASET_PATH))
question_by_id = {q["id"]: q for q in question_bank}

print("[grading_service] Loading hybrid grading embedder...")
hybrid_embed_model = SentenceTransformer(settings.HYBRID_EMBEDDER_NAME)

# Per-session "no repeats until pool exhausted" state.
# In-memory dict is fine for a single-instance low-traffic deployment; swap
# for Redis/DB if this ever runs behind more than one worker process.
_session_asked: dict[str, set[str]] = {}


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
    subjects), in which case grading falls back to pure similarity."""
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
    # whether the student's answer contains it. See dissertation Ch5
    # calibration notes -- tested before shipping (evaluation/calibration_test.py).
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
        "similaritate": round(similarity, 3),
        "raspuns_final_potrivit": final_correct,
        "barem_oficial": question["barem"],
    }


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
# SECURITY NOTE: /practice/start returns a question WITHOUT its barem/answer
# key. /practice/grade looks the barem up server-side by question_id. Never
# trust a barem or points_total sent from the client -- it would let a
# student see or fake the answer key from the browser's network tab.

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
