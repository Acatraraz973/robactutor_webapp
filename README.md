# RoBacTutor

Practical implementation for the dissertation: a Bacalaureate-prep tool for
Moldovan high school students, fine-tuning `OpenLLM-Ro/RoMistral-7B-Instruct`
(LoRA) with a RAG layer over official ANCE exam papers and textbooks. Full
run instructions: **[docs/setup.md](docs/setup.md)**.

## Repo map

| Folder | What's in it | Dissertation chapter / finding |
|---|---|---|
| **`notebooks/`** | The 4 Colab notebooks behind the pipeline, in run order | |
| &nbsp;&nbsp;`01_finetuning.ipynb` | LoRA fine-tuning of the base model | Ch5 §5.7 — 4-bit NF4 quantization, PEFT adapter |
| &nbsp;&nbsp;`02_rag_pipeline.ipynb` | Embedding + FAISS index construction | Ch4 §4.10.4 / Ch5 §5.6 |
| &nbsp;&nbsp;`03_testeaza_te_grading.ipynb` | Hybrid similarity grading, developed against real baremas | Ch5 — validated as the alternative to raw generative grading, which failed |
| &nbsp;&nbsp;`04_ask_mode_comparison.ipynb` | Adapter-enabled vs. base-model generation, same questions | Ch5 — the negative result behind `ASK_MODE_USE_ADAPTER = False` in the backend |
| **`evaluation/`** | Standalone scripts that produced the findings above | |
| &nbsp;&nbsp;`dataset_quality_audit.py` | Fabricated-citation count + duplication-candidate screening | Ch5 — **100% of the 157-pair training set** carries a fabricated "ANCE \<year\>" citation; 136 duplication candidates flagged for manual review (not a confirmed count — see the script's own docstring) |
| &nbsp;&nbsp;`calibration_test.py` | Runs 5 answers of known quality through `/practice/grade` on the same question | Ch5 — caught the bug where a wrong final answer wrapped in barem-like phrasing outscored a correct-but-reworded one; re-run after the fix confirmed it resolved |
| &nbsp;&nbsp;`results/` | Raw output from the two scripts above | Cite the specific numbers from these files, not summarized claims |
| **`backend/`**, **`frontend/`** | The shipped web app implementing the validated findings — hybrid grading with final-answer gating, readability-filtered RAG retrieval, citation-cleaned baremas, and the adapter-vs-base demo comparison endpoint | Ch5 — architecture matches the dissertation's stated standalone-API-backend / separate-frontend-client split |
| **`docs/`** | Setup guide; add further write-up-support docs here | |

## A note on what's *not* validated

The adaptive-difficulty mechanism described in the Methodology chapter is
**not implemented** in the web app — consistent with the dissertation's own
framing of it as a designed-but-deferred component, not a claim that it
works. Ask-mode is flagged `experimental: true` in its own API response:
only 4 questions per subject were tested (`04_ask_mode_comparison.ipynb`),
so treat it as a documented direction, not a validated result on the level
of the grading pipeline.
