# ENGINE_NOTES — Consulting Case engine lessons (current truth)
Reference only. Open when an engine script fails, hangs, drifts, or you are changing engine code. Compiled from history/LESSONS_LEARNED.md [E1.x]; most are already built into the scripts — this says why, so nobody undoes them.

## Footage + disk
- [E1.1] Raw is iPhone 4K HEVC 60 fps, ~1.3 GB per 3 min. Never write a 4K intermediate (disk filled mid-cut). Working cut = 1440x2560 (headroom for the punch-in), ~25 Mb/s videotoolbox. `df` before rendering: need ~3 GB free.
- [E1.23] A project folder is ~1.7 GB (cut.mp4 ~450 MB, board/ ~900 MB of qtrle chunks). board/b_*.mov chunks are only a render cache; finalize_reel.sh clears them after approval.
- [E1.3] Rishi sometimes records a second file to redo the back half. Treat multiple raw files as one take sequence; the later file wins for overlapping lines.

## Transcription
- [E1.2] whisper ggml-base word timestamps drift up to ~1 s on a long file; `-dtw` gives nothing with this build. Split into speech islands (20 ms RMS envelope, speech > −50 dB, merge gaps < 0.18 s), transcribe each island alone; for cut segments that aren't whole islands transcribe each alone with `-ml 1 -sow`, then align.py (difflib to the corrected script + onset snapping). Parallel whisper jobs (6) occasionally drop an output (Metal contention): retry missing ones sequentially.
- [E1.20] islands.py does islands + per-island whisper in one script (`islands.py <16k.wav> <outDir> [model]`). When every cut segment is one island, map island word times to cut time instead of re-transcribing.
- [E1.24] Claude Code sandbox blocks Metal and VideoToolbox: whisper-cli aborts ("failed to allocate Metal buffer" / in `whisper_init`) → run islands.py with `WHISPER_NG=1` (CPU, ~1–2 s per island). `h264_videotoolbox` fails (-12908 / "Could not open encoder") → run cut.py, render.js, compose.sh, speed_music.sh, run_build.sh outside the sandbox. render.js also needs `~/.npm` and `~/Library/Caches/ms-playwright`. Two terminals at once: each reel owns its own R### project folder and export prefix, claimed before creating the folder (R008/R009 clash).

## Cut
- [E1.12] cut.py's per-segment `fps=30000/1001` loses ~0.5 s of video vs audio over ~60 segments (last word without picture). cut.py/compose.sh pad with `tpad=stop_mode=clone` + `-shortest` to the audio; QC compares video vs audio STREAM durations.
- [E1.26] Premiere pre-cut → EDL via MCP; see PRODUCTION_WORKFLOW §2.

## Board render
- [E1.4] Never pipe the whole board render into the final encode: the Playwright→ffmpeg pipe stalled and ffmpeg finished a truncated reel with no error. compose.sh renders 400-frame chunks (3 in parallel, env CHUNK/JOBS), checks each chunk's frame count, then composites. QC's duration check is what catches truncation.
- [E1.11] Root cause: chrome-headless-shell `page.screenshot` hangs intermittently. render.js uses a 4 s timeout, forces a repaint, retries up to 6x; chunks with wrong frame counts are re-rendered on the next compose.sh run (finished chunks kept).
- [E1.15] ~0.15 s/frame normally; 9 s/frame happened while the Mac idled — keep it awake (request_keep_awake).
- [E1.22] compose_green.sh composites the bg loop + transparent board.mov like compose.sh: always run it with `BGVIDEO=…` (board/board.mp4 no longer exists since R1.17).

## Image filters
- [E1.13] ffmpeg gblur via sendcmd: `sigmaV` stays at its initial value unless sent too → permanent vertical smear. Send `sigma` AND `sigmaV` every step and bypass with `enable='lt(t,…)'` once done. QC measures sharpness at 0.05 / 1.5 / 3.0 s.
- [E1.17] `scale=…:eval=frame` + `crop` animated zoom snaps to whole pixels → wobble. Zooms are per-frame affine transforms (PIL, bicubic, sub-pixel) in s2zoom.py.

## Audio
- [E1.14] [E1.18] [E1.19] limiter and duck settings: see SOUND_DESIGN.md "Limiting + ducking notes".
- [E1.27] `sfx48/` (48 kHz SFX copies + info.json with measured peak times) is not produced by any script; copy it from the previous reel. Without info.json sfx.py crashes; run_build.sh checks for it first.

## QC
- [E1.21] qc.py reads S1_END/S2_END from the project's crops.env (never hard-coded) and checks the tail from the last word END (+0.2–0.6 s).
- [E1.25] OCR "readable ≥85 %" heuristic: see QUALITY_CONTROL.md caveat.

## Assets
- [E1.9] Check stock hook photos visually for brand logos (first Unsplash pick had AGV/Dainese marks); blur number plates. Credit in `05. Asset Library/photos/CREDITS.md`.
- [E1.16] Images pasted in chat don't reach the disk: ask Rishi to save them into `05. Asset Library/` and continue other fixes meanwhile; a hook-only asset change needs just the S1 overlay + composite (~5 min).
