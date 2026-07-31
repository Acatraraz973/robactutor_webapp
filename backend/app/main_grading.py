"""
Cloud Run entry point for the public grading service. Serves the built
React frontend (single entry point for teachers) AND the grading API
(/api/subjects, /api/practice/start, /api/practice/grade) from the same
origin -- no CORS needed for these calls.

Ask-mode (/ask) is NOT here -- the frontend calls the separate HF Spaces
Gradio app directly, cross-origin, using a build-time env var
(VITE_ASK_API_BASE). See docs/deployment.md.

/demo/grade-comparison is intentionally absent from this entry point --
it stays local-dev only (backend/app/main.py + robactutor_backend.py,
unchanged). This file deliberately does NOT import robactutor_backend.py,
so none of its transformers.AutoModelForCausalLM / peft / bitsandbytes
imports happen here -- that's what keeps this deployment's image and RAM
footprint CPU-only sized. See requirements-grading.txt.
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .grading_service import router as grading_router, question_bank
from .rag_common import chunk_metadata

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/
FRONTEND_DIST = BASE_DIR.parent / "frontend" / "dist"  # ../frontend/dist

app = FastAPI(title="RoBacTutor Grading Service")

SUBJECTS = [
    {"id": "matematica", "label": "Matematică", "icon": "Σ"},
    {"id": "limba_romana", "label": "Limba Română", "icon": "Aa"},
    {"id": "istorie", "label": "Istorie", "icon": "⛨"},
    {"id": "limba_engleza", "label": "Limba Engleză", "icon": "GB"},
]


@app.get("/api/subjects")
async def subjects():
    return SUBJECTS


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "question_bank_size": len(question_bank),
        "chunk_count": len(chunk_metadata),
    }


app.include_router(grading_router, prefix="/api")

# ---------------------------------------------------------------------
# Serve the built React app (frontend/dist) -- same single-origin pattern
# as local main.py, so teachers only ever see this one Cloud Run URL.
# ---------------------------------------------------------------------
if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIST / "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_react(full_path: str):
        candidate = FRONTEND_DIST / full_path
        if full_path and candidate.exists() and candidate.is_file():
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")
