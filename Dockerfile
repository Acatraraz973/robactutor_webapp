# Cloud Run image for the public grading service (Testeaza-te only).
# Named plain "Dockerfile" (not Dockerfile.grading) so `gcloud run deploy
# --source .` auto-detects it -- this repo has no other Dockerfile, so
# there's no naming conflict to worry about.
# Build from the repo root: docker build -t robactutor-grading .
#
# Two stages: build the React frontend, then a slim Python runtime that
# serves it + the grading API. Deliberately does NOT copy
# backend/artifacts/lora_adapter/ -- this service never loads the
# generation model, so shipping the ~170MB adapter here would be pure
# waste. See docs/deployment.md for the RAM/size math this was built for.

# --- Stage 1: build the React frontend ---
FROM node:20-slim AS frontend-build
WORKDIR /build/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# --- Stage 2: Python runtime ---
FROM python:3.11-slim
WORKDIR /app

COPY backend/requirements-grading.txt backend/requirements-grading.txt
RUN pip install --no-cache-dir -r backend/requirements-grading.txt

COPY backend/app backend/app
COPY backend/artifacts/rag backend/artifacts/rag
COPY backend/artifacts/dataset backend/artifacts/dataset
COPY --from=frontend-build /build/frontend/dist frontend/dist

WORKDIR /app/backend
ENV PORT=8080
EXPOSE 8080
CMD ["sh", "-c", "uvicorn app.main_grading:app --host 0.0.0.0 --port ${PORT}"]
