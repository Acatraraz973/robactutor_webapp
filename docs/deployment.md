# RoBacTutor — Public Deployment Guide

Deploys RoBacTutor for a small external evaluation (e.g. a handful of
teachers at one school) as **one URL**, backed by two separate services.
The split is a backend implementation detail — nobody using the site sees
a second URL or needs to know it exists.

```
Teachers → https://<cloud-run-url>/          (ONE url, this is what they get)
              │
              ├─ Serves the built React frontend (static files)
              ├─ /api/subjects, /api/practice/start, /api/practice/grade
              │  → same-origin, CPU-only, this Cloud Run service
              │
              └─ /ask calls, made client-side by the frontend's JS
                 → cross-origin, to a separate HF Spaces (ZeroGPU) app
                 → build-time env var, never shown in the UI
```

`/demo/grade-comparison` is **not** part of either public deployment — it
only exists in local dev (`backend/app/main.py` +
`backend/app/robactutor_backend.py`, unchanged by any of this).

---

## Why this split, and why not simpler

Two research findings (checked directly against current provider docs/specs
at the time this was written, not assumed) shaped this:

1. **Render/Railway free tiers don't fit the grading service.** Combined
   runtime RAM for the RAG index + both embedding models + framework
   overhead is ~1.5–1.6 GB; both platforms' free tiers cap around 500–512
   MB — roughly 3x too small, not a marginal squeeze. Render's cheapest
   *paid* tier ($7/mo) is also only 512 MB; you'd need Standard ($25/mo,
   2 GB) for this to fit there. **Google Cloud Run** was chosen instead:
   configurable memory well beyond 512 MB, billed by actual GB-seconds
   used, and its free monthly quota (360,000 GB-seconds) comfortably
   covers a low-traffic pilot. Tradeoff: cold starts after idle periods
   (the two embedding models reload from disk), typically 10–30s for the
   first request after a gap.

2. **HF Spaces ZeroGPU is Gradio-only.** Confirmed against current HF
   docs and forum threads: plain FastAPI routes are not supported for
   ZeroGPU's dynamic GPU allocation to work. `/ask` is therefore a Gradio
   function (`hf_space/app.py`) called via Gradio's own HTTP API
   (POST-then-SSE), not a REST endpoint. VRAM itself is not a constraint —
   ZeroGPU allocates far more (70–96 GB depending on the backing GPU) than
   the ~4.5 GB the 4-bit model needs.

---

## Part 1 — Grading service (Cloud Run)

Covers `/api/subjects`, `/api/practice/start`, `/api/practice/grade`, plus
serving the built frontend. CPU-only — never loads the generation model.

### Build and deploy

From the repo root:

```
gcloud run deploy robactutor-grading \
  --source . \
  --region <your-region> \
  --memory 4Gi \
  --cpu 2 \
  --allow-unauthenticated \
  --min-instances 0 \
  --timeout 300
```

**`--memory 4Gi`, not the 2Gi originally estimated.** First deploy attempt
used 2Gi based on the ~1.5-1.6GB RAM estimate above and got OOM-killed at
startup: actual measured usage was **2192 MiB** before the container even
finished loading both embedding models (Cloud Run's own log:
`Memory limit of 2048 MiB exceeded with 2192 MiB used`). The estimate
undercounted real sentence-transformers + FAISS + framework overhead.
4Gi (deployed and confirmed working, revision `robactutor-grading-00002`)
gives real headroom instead of running right at the edge. `--cpu 2`
speeds up the cold-start model loading; `--timeout 300` extends the
request timeout for that same reason. `--min-instances 0` is what makes
this stay inside the free quota (scales to zero between requests); raise
it only if the cold-start latency becomes a real problem for testers, at
the cost of leaving it billed continuously.

Confirmed live at `https://robactutor-grading-294554506260.europe-west1.run.app`:
`/api/health`, the frontend root page, and a full
`/api/practice/start` → `/api/practice/grade` round trip all verified
working end-to-end post-deploy.

The command prints a `*.run.app` URL — that's the one link teachers get.

### What's in the image

- `backend/app/main_grading.py` — entry point, imports only
  `grading_service.py` + `rag_common.py`. Never imports
  `robactutor_backend.py`, so `transformers.AutoModelForCausalLM` / `peft`
  / `bitsandbytes` never get imported (and aren't even in
  `requirements-grading.txt`) — that's what keeps this deployment
  CPU/RAM-sized instead of needing a GPU-class image.
- `backend/artifacts/rag/` and `backend/artifacts/dataset/` — copied in.
  `backend/artifacts/lora_adapter/` is deliberately **not** copied — this
  service never loads it, so shipping its ~170 MB would be pure waste.
- The built `frontend/dist/` — built in the Dockerfile's first stage.

---

## Part 2 — Ask-mode service (HF Spaces, ZeroGPU)

Covers `/ask` only. Lives in `hf_space/` as a separate, self-contained
deployment (its own git remote — HF Spaces are their own git repos, not a
subfolder push from this one).

**Deployed and confirmed working** at
`https://alcatraz973-robactutor-ask.hf.space` (Space:
`Alcatraz973/robactutor-ask`, hardware `zero-a10g`, stage `RUNNING`).
Creating a Space requires an **HF PRO subscription** ($9/mo) — this only
surfaced as a live 402 Payment Required error when creating the repo, not
from ZeroGPU-usage docs (which only cover runtime allocation, not Space
creation). Uploaded via `huggingface_hub.HfApi.upload_folder()` rather
than a manual git push — same effect, simpler from a script/CLI context.

### Steps

1. Copy the two artifact folders next to `hf_space/app.py`:
   ```
   hf_space/artifacts/lora_adapter/   <- backend/artifacts/lora_adapter/
   hf_space/artifacts/rag/            <- backend/artifacts/rag/
   ```
   (Both are gitignored under `hf_space/` for the same reason
   `backend/artifacts/lora_adapter/` already is — see `.gitignore`.)

2. Create a new Space on huggingface.co: SDK = **Gradio**. Note the Space
   name — its URL will be `https://<username>-<space-name>.hf.space`.

3. Push `hf_space/`'s contents (app.py, requirements.txt, README.md, and
   the two artifact folders you just copied in) to that Space's git remote,
   same as pushing to any git repo. Large files (`.safetensors`, the FAISS
   index) go through git-lfs automatically on Spaces — no extra setup
   needed for repos under a few GB.

4. **In the Space's Settings tab**, set Hardware to **ZeroGPU**. This is a
   Space-level setting, not something `app.py` or `README.md` can set on
   their own.

5. Once it's running, the Space exposes the `ask` function at
   `POST https://<username>-<space-name>.hf.space/gradio_api/call/ask`
   (see `hf_space/app.py`'s docstring for the exact protocol).
   **Not** `/call/ask` — that was this doc's (and `frontend/src/api.js`'s)
   original assumption based on older Gradio 4.x docs; the actually
   deployed Gradio 5.x Space 404s on `/call/ask` and only responds on
   `/gradio_api/call/ask`, confirmed by live testing against the running
   Space, both fixed.

---

## Part 3 — Wiring the frontend to both services

Only one build-time env var is needed — the grading API is same-origin
(bundled into the Cloud Run image), so it needs no configuration.

```
cd frontend
cp .env.production.example .env.production
# edit .env.production, set:
#   VITE_ASK_API_BASE=https://<username>-<space-name>.hf.space
npm run build
```

That's the build that goes into `Dockerfile` (its frontend-build stage
runs `npm run build` itself — make sure `.env.production` exists *before*
running `gcloud run deploy --source .` / `docker build`, since Vite bakes
env vars in at build time, not runtime, and `.gcloudignore` is what
guarantees this gitignored file actually reaches Cloud Build — see
`.gcloudignore`'s own header comment).

If `VITE_ASK_API_BASE` is unset, `frontend/src/api.js` falls back to the
same-origin `/api/ask` route — this is what keeps local dev (`npm run dev`
+ local `uvicorn app.main:app`) working completely unchanged.

---

## Verifying the single-entry-point property

After deploying, the only thing a teacher should ever need is the Cloud
Run URL. To sanity-check this actually holds:

1. Open the Cloud Run URL in a browser with dev tools open.
2. Use Testează-te — confirm all requests stay on the Cloud Run origin.
3. Use Întreabă — confirm the request goes to the HF Spaces origin
   *silently*, i.e. nothing in the UI shows that URL, no visible redirect,
   no second link anywhere.
4. Confirm `/demo/grade-comparison` has no real functionality on both
   public deployments — it should only work when running
   `backend/app/main.py` locally. On the deployed grading service this
   was verified as: `POST /api/demo/grade-comparison` → **405** (not 404
   — `main_grading.py`'s SPA catch-all route `@app.get("/{full_path:path}")`
   syntactically matches every path, so Starlette reports "method not
   allowed" rather than "not found"), and `GET /demo/grade-comparison` →
   200 with the SPA shell (`index.html`), not the comparison feature.
   Either way, no grade-comparison logic is reachable — `grading_service.py`
   never defines that route at all.

---

## Status: fully deployed and verified (2026-07-31)

Both services are live, wired together, and the single-entry-point
property holds:

- Grading service (Cloud Run): `https://robactutor-grading-294554506260.europe-west1.run.app`
  — revision `robactutor-grading-00003-9w7`, serving 100% traffic.
- Ask-mode service (HF Space, ZeroGPU): `https://alcatraz973-robactutor-ask.hf.space`
  — Space `Alcatraz973/robactutor-ask`, stage `RUNNING`, hardware `zero-a10g`.
- The Cloud Run frontend bundle was rebuilt with
  `VITE_ASK_API_BASE=https://alcatraz973-robactutor-ask.hf.space` baked in
  and redeployed — confirmed present in the live served JS bundle.
- Full round trip tested directly against the HF Space
  (`POST /gradio_api/call/ask` → SSE `GET .../ask/<event_id>`) with a real
  question and returned a correct `{answer, experimental, material_referinta}`
  payload, including retrieved reference passages with filenames/scores.
- A source-level `.gcloudignore` was added (previously absent) to
  guarantee `frontend/.env.production` — gitignored, but required at
  Docker build time for Vite to bake in `VITE_ASK_API_BASE` — actually
  reaches Cloud Build's upload. Without it, `gcloud run deploy --source .`
  would have auto-derived its ignore rules from `.gitignore` and silently
  dropped that file, which would have made ask-mode silently fall back to
  a same-origin `/api/ask` route that doesn't exist in `main_grading.py`.
