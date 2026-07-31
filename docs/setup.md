# RoBacTutor — Setup & Run Guide

**React frontend + FastAPI backend.** Two pieces that talk over a JSON API:

```
robactutor_webapp/
  backend/     FastAPI — serves /api/practice/*, /api/ask, /api/demo/*
               (and, once built, the React app itself)
  frontend/    React (Vite) — Testează-te / Întreabă / Demo comparativ UI
```

There is no demo/mock mode: the RAG index, hybrid grading embedder, and
practice question bank all load at import time, and the generation model
(base model + LoRA adapter) loads lazily on first `/api/ask` or
`/api/demo/grade-comparison` call. **A CUDA GPU with ~5GB+ free VRAM is
required** for `/api/ask` and `/api/demo/grade-comparison`; `/api/practice/*`
runs fine on CPU (hybrid grading only, no generation).

---

## 0. One-time setup: install Node.js and Python

You need Node.js for the React side (separate from Python). Go to
**[nodejs.org](https://nodejs.org)**, download the **LTS** installer, run it
with default options. Confirm it worked — open Command Prompt and run:

```
node --version
npm --version
```

Get Python from [python.org/downloads](https://python.org/downloads)
(remember to tick **"Add python.exe to PATH"** during install). Confirm with:

```
python --version
```

**Use Python 3.11, 3.12, or 3.13 — not 3.14+.** As of this writing,
`pydantic-core` (a `requirements.txt` dependency) has no prebuilt wheel for
3.14 and fails to compile from source (PyO3 doesn't support it yet). If
`python --version` shows 3.14 or newer, install 3.11 from python.org
alongside it and use `py -3.11 -m venv .venv` in the steps below instead of
`python -m venv .venv`.

---

## 1. Artefacts you need before first run

Place these under `backend/artifacts/` (paths are configurable via
`backend/.env` — see `backend/.env.example` — but these are the defaults):

| Path | Contents | Source |
|---|---|---|
| `backend/artifacts/lora_adapter/` | `adapter_config.json`, `adapter_model.safetensors`, tokenizer files | `robactutor_lora_adapters_BRI23222497.zip` |
| `backend/artifacts/rag/` | `robactutor_faiss.index`, `robactutor_chunks.json` | `robactutor_rag_BRI23222497.zip` |
| `backend/artifacts/dataset/` | `robactutor_sft_dataset_reviewed.jsonl` (157 instruction/response pairs — the practice question bank) | Training dataset export |

---

## 2. Quick start — single server, one URL

Open Command Prompt in the `robactutor_webapp` folder:

```
cd frontend
npm install
npm run build
cd ..\backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app
```

Open **http://127.0.0.1:8000**. `requirements.txt` includes the heavy deps
(torch, transformers, peft, bitsandbytes, faiss-cpu, sentence-transformers) —
there's no lightweight/mock mode to fall back to.

`pip install` gives you a default `torch` build, which may be CPU-only or
built for the wrong CUDA version depending on your GPU/driver. Check with:

```
python -c "import torch; print(torch.cuda.is_available())"
```

If that prints `False` on a machine with a CUDA GPU, reinstall torch for
your specific setup from the selector at
[pytorch.org/get-started](https://pytorch.org/get-started/locally/), e.g.
for a very recent GPU (RTX 50-series / Blackwell):

```
pip uninstall torch -y
pip install torch --index-url https://download.pytorch.org/whl/cu128
```

---

## 3. Active development mode (hot-reload while editing the UI)

Two Command Prompt windows, both open in `robactutor_webapp`.

**Window 1 — backend:**
```
cd backend
.venv\Scripts\activate
uvicorn app.main:app --reload
```

**Window 2 — frontend:**
```
cd frontend
npm run dev
```

Open **http://127.0.0.1:5173** (the Vite dev server, not port 8000). Vite
forwards `/api/...` requests to the FastAPI backend on port 8000
(`frontend/vite.config.js`), so the app works identically but hot-reloads
as you edit `frontend/src/`.

---

## 4. Project structure

```
robactutor_webapp/
  backend/
    app/
      main.py                 FastAPI app: mounts the router below at /api,
                               serves /api/subjects, /api/health, and
                               frontend/dist in production
      config.py                Settings, all overridable via backend/.env
      robactutor_backend.py    /practice/start, /practice/grade, /ask,
                                /demo/grade-comparison — hybrid grading,
                                RAG retrieval, generation
    artifacts/
      lora_adapter/              LoRA adapter (unzip here)
      rag/                       FAISS index + chunk metadata
      dataset/                   Practice question bank (JSONL)
    requirements.txt            All deps — no lightweight/mock-mode split
    .env.example                 Copy to .env to override artifact paths

  frontend/
    src/
      App.jsx                  Top-level layout, view/subject state
      api.js                    fetch wrapper for the backend API
      i18n.js                   RO / EN interface strings
      index.css                 Design system (colours, type, layout)
      components/
        Sidebar.jsx              Mode switcher + subject tabs + language toggle
        PracticeScreen.jsx       Testează-te: question → answer → graded result
        AskScreen.jsx             Întreabă: free-form Q&A
        DemoScreen.jsx            Demo comparativ: validated vs. raw adapter
        MarkdownLite.jsx          Shared **bold**/bullet renderer
        ReferencePassages.jsx     Shared source-citation list
    vite.config.js             Dev server + API proxy config
    package.json
```
