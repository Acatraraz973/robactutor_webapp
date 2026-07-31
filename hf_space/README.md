---
title: RoBacTutor Ask Mode
emoji: 📘
colorFrom: blue
colorTo: yellow
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
---

# RoBacTutor -- ask-mode API

Internal service, called by the main RoBacTutor frontend's **Întreabă**
screen. Not meant to be opened directly by teachers -- they only ever see
the main app's single URL; this Space's URL is a build-time env var the
frontend calls behind the scenes.

**Hardware**: after creating this Space, set its hardware to **ZeroGPU**
in the Space's Settings tab (this isn't something the `app.py` code or this
README can set on its own -- it's a Space-level setting).

**Before pushing**: copy these two folders in next to `app.py` (same names
as their source in the main project repo):

```
artifacts/lora_adapter/   <- backend/artifacts/lora_adapter/
artifacts/rag/            <- backend/artifacts/rag/
```

See `docs/deployment.md` in the main repo for the full walkthrough.
