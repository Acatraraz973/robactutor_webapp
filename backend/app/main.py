from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .robactutor_backend import router as robactutor_router, question_bank, chunk_metadata

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/
FRONTEND_DIST = BASE_DIR.parent / "frontend" / "dist"  # ../frontend/dist

app = FastAPI(title="RoBacTutor API")

# CORS: allows the React dev server (Vite, default port 5173) to call this
# API during development. In production, the React app is served by this
# same FastAPI process (see the static mount below), so CORS isn't even
# needed then — but leaving it open for localhost is harmless.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


app.include_router(robactutor_router, prefix="/api")

# ---------------------------------------------------------------------
# Serve the built React app (frontend/dist) if it exists, so the whole
# site can be run from a single `uvicorn` process in production:
#   cd frontend && npm run build
#   cd ../backend && uvicorn app.main:app
# If frontend/dist doesn't exist yet (e.g. you're running `npm run dev`
# separately), this backend simply behaves as a JSON-only API and the
# lines below are skipped.
# ---------------------------------------------------------------------
if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIST / "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_react(full_path: str):
        candidate = FRONTEND_DIST / full_path
        if full_path and candidate.exists() and candidate.is_file():
            return FileResponse(candidate)
        return FileResponse(FRONTEND_DIST / "index.html")
