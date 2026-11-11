# LESSONS LEARNED — Daniel Priestley Editing Style

Read this first once it has content. Rishi's corrections are tagged `[R1.1]`, `[R1.2]`… and override every estimate in the other files.

## Rishi corrections
_(none yet — v1.0)_

## Build-engine gotchas (from the v1.0 analysis run)
- whisper-cli crashes in the sandbox with Metal (out-of-memory on buffer alloc) → use `-ng` (CPU). CPU mode then needs OpenMP's /tmp; one run completed (19 min for an 8-min video), the rest aborted. Budget time or transcribe outside the sandbox.
- `uv` needs `UV_CACHE_DIR` inside the workspace (`tools/.uv-cache`); system Python 3.14 is too new for torch/demucs → venv `tools/venv-style` (Python 3.11).
- Demucs model download fails through the proxy (hash mismatch on huggingface redirect) → analyse full mix, or pre-download `htdemucs` weights outside the sandbox into `TORCH_HOME`.
- ffmpeg `-hwaccel videotoolbox` fails in sandbox → software decode (~20× realtime on 1080p is fine).
- `assets/sfx` is empty → sound cue matching deferred.
