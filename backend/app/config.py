"""
Central configuration for the RoBacTutor web app.

Everything here can be overridden with environment variables (or a .env file —
see .env.example). All paths default to backend/artifacts/<type>/, the
project's convention for shipped model/data artefacts.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Settings:
    # --- Base model + fine-tuned adapter -----------------------------------
    # From robactutor_lora_adapters_BRI23222497.zip
    BASE_MODEL_NAME: str = os.getenv("BASE_MODEL_NAME", "OpenLLM-Ro/RoMistral-7B-Instruct")
    ADAPTER_PATH: str = os.getenv("ADAPTER_PATH", str(BASE_DIR / "artifacts" / "lora_adapter"))

    # --- RAG artefacts (from robactutor_rag_BRI23222497.zip) --------------
    RAG_INDEX_PATH: str = os.getenv("RAG_INDEX_PATH", str(BASE_DIR / "artifacts" / "rag" / "robactutor_faiss.index"))
    RAG_CHUNKS_PATH: str = os.getenv("RAG_CHUNKS_PATH", str(BASE_DIR / "artifacts" / "rag" / "robactutor_chunks.json"))
    RAG_EMBEDDER_NAME: str = os.getenv("RAG_EMBEDDER_NAME", "all-MiniLM-L6-v2")  # MUST match the model used to build the FAISS index

    # --- Practice question bank ---------------------------------------------
    DATASET_PATH: str = os.getenv(
        "DATASET_PATH", str(BASE_DIR / "artifacts" / "dataset" / "robactutor_sft_dataset_reviewed.jsonl")
    )

    # --- Hybrid grading embedder ---------------------------------------------
    HYBRID_EMBEDDER_NAME: str = os.getenv("HYBRID_EMBEDDER_NAME", "paraphrase-multilingual-mpnet-base-v2")

    SUBJECTS: list = ["matematica", "limba_romana", "limba_engleza", "istorie"]


settings = Settings()
