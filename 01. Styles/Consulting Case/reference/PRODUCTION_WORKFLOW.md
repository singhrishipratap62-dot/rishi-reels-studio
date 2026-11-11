# PRODUCTION_WORKFLOW (v1.5) — raw talking head → finished reel, on Rishi's Mac terminal
Reference only: SKILL.md is the mandatory read and wins on any conflict. Use this when running steps by hand instead of the previous reel's `run_build.sh` (R011's is the template).
Studio root R = `~/Documents/Teaching Claude` (`.studio-root` marker; layout in `02. Shared Core/STUDIO.md`). Raw footage: `R/03. Projects/Consulting Case/Raw Footage/Video N/` (newest N by default) [R1.19]. Work in P = `R/03. Projects/Consulting Case/<REEL_ID>/`, exports in X = `R/04. Exports/Consulting Case/`. REEL_ID = `R###_<topic>_YYYY-MM-DD`.
Sandbox: run islands.py with `WHISPER_NG=1`; run cut.py, render.js, compose.sh, speed_music.sh and run_build.sh OUTSIDE the Claude Code sandbox (Metal/VideoToolbox blocked; render.js needs `~/.npm` + `~/Library/Caches/ms-playwright`) [E1.24]. Engine debugging notes: ENGINE_NOTES.md.
Tools: ffmpeg-full (`/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`), ffprobe, whisper-cli + `06. Tools/models/ggml-base.bin`, Node + Playwright (chrome-headless-shell; render.js has the paths), tesseract (QC only), python venv `06. Tools/venv-style` for sfx.py / s2zoom.py.
Scripts live in `01. Styles/Consulting Case/engine/` (reuse, don't rewrite). E = that folder, P = the project folder.
**Resolution rule [R1.18]:** decode the 4K source once into the 1440x2560 working cut; every export is 1080x1920. Never write 4K files.

## 0. Preflight
`df -h /` (need ~3 GB free; a project is ~1.7 GB, E1.23). node + Playwright present (render.js paths). Keep the Mac awake during renders (E1.15). `P/sfx48/info.json` present (copy `sfx48/` from the previous reel, E1.27).

## 1. Ingest + transcribe
ffprobe the raw (fps, res, rotation, duration). `ffmpeg -i raw -vn -ac 1 -ar 16000 P/raw_<n>.wav`.
`WHISPER_NG=1 python3 E/islands.py P/raw_<n>.wav P/isl_<n>` → speech islands + per-island whisper word timings (`isl/isl.json`, `isl/words.json`) [E1.2, E1.20].

## 2. Cut (automatic)
- Read the island transcript. Retakes: a clause whose first words repeat within ~20 s, or an abandoned fragment followed by a restart → keep the LAST complete take [R1.0]; drop fragments, flubs, breath blips, pre/post-roll. Multiple raw files = one take sequence, later file wins (E1.3).
- Split inside an island at the RMS minimum between takes.
- `edl.json` segments = kept islands with 40 ms head / 60 ms tail handles (pauses end up ~0.1–0.18 s; never > 0.3 s). Tail ≈ 0.4 s after the last word.
- `python3 E/cut.py edl.json cut.mp4` → 1440x2560 working cut, CFR 29.97, 10 ms audio fades.
- Word timings in cut time: map island words through the EDL (`words_cut_raw.json`; R011's `map_words.py` does this); re-transcribe only segments that aren't whole islands (each alone, `-ml 1 -sow`, E1.2).
- Premiere pre-cut (E1.26): Rishi's sequence is the EDL. Re-read V1 with the premiere-pro MCP `get_active_sequence` (track_type video, clip_limit 200) right before building: source name + inPoint/outPoint → `edl.json` → cut.py from the 4K sources (no 4K export out of Premiere). Don't re-judge his takes; whisper 2–6 s windows of the assembled cut audio around every suspicious join; flag content changes in plan.md. Premiere silence trims leave ~0.06 s after the last word: extend the last out-point to last word + ~0.4 s. Nothing is imported back into Premiere.

## 3. Correct + align
Fix ASR with case logic (numbers must add up; lakh/crore; "floor" not "flow"). Write the corrected `script.txt`. `python3 E/align.py words_cut_raw.json script.txt cut.wav edl.json` → `words.json`.

## 4. Plan → STOP for approval (the only gate) [R1.0]
`plan.md`: summary (part, durations at 1x and 1.2x, hook, S1/S2 spans, phase switch, tabs, number line), retakes, ASR corrections with "please confirm" flags, hook image + licence, beat table (time · spoken · board action · motion), arithmetic check.

## 5. Assets + config
Hook photo: licence-safe (Wikimedia/Unsplash/Pexels), logo-free, literal; crop 4:3 → `P/hook.jpg`; log source + licence in `05. Asset Library/photos/CREDITS.md`. MBB strip `05. Asset Library/stickers/mbb_logos_trim.png`. Write `P/beats.js` (copy the previous reel's as a template), `P/crops.env` (S1/S2/S3 crops on the 1440x2560 cut, S1_END/S2_END frames; check against a still, e.g. `crops_check.jpg`), `P/mask.png`. E1.8 starting crops for Rishi's usual framing: S1 full-bleed 1440:1560:0:360, S2 punch-in 1108:1969:166:220, S3 card 1100:1233:170:450 (first guesses clipped the hair; R011 used S1 1440:1560:0:560, S2 1108:1969:136:560, S3 1360:1525:20:600 — always re-check).

## 6. Build (final only; see the previous project's run script for the exact chain)
1. `BGVIDEO="R/05. Asset Library/videos/gradnext-background-loop-9-16.mp4" AUDIO=P/mix.wav E/compose.sh P X/<ID>_1x.mp4` — board chunks (Playwright, transparent) over the bg loop, S1 hook overlay + panel blur-in, S2 sub-pixel settle (s2zoom.py), S3 face card. Needs `node render.js … --events` → `events.json` → `R/06. Tools/venv-style/bin/python E/sfx.py P "R/01. Styles/Minimal Edit/sfx"` first, which writes mix.wav + sound_cue_sheet.md.
2. `E/speed_music.sh P X/<ID>.mp4 "R/05. Asset Library/music/Background music.mp3" 1.2 15` → the posted final (1.2x, music 13 dB under the voice) [R1.15, R1.16].
3. `BGVIDEO=… E/compose_green.sh P X/<ID>_green.mp4` (1080x1920; needs BGVIDEO, E1.22).
4. `_raw`: `ffmpeg -i P/cut.mp4 -vf scale=1080:1920:flags=lanczos -c:v libx264 -preset medium -crf 18 -profile:v high -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart X/<ID>_raw.mp4` (as in R011's run_build.sh) [R1.18].
5. Placement guide `X/<ID>_green_PLACEMENT.md` (copy the previous reel's format) with scales for the 1080 raw.
Always render to a temp name and move into place (R1.2).

## 7. QC (QUALITY_CONTROL.md) then report.
`python3 E/qc.py P X/<ID>.mp4 <part> 1.2` + face freezedetect (`crop=810:908:136:858,freezedetect=n=0.002:d=1.0`) + frame counts of all four files + contact sheet. Fix and re-check before reporting.

## 8. Revisions
Numbered table in `P/revisions.md` (where · problem · expected · fix · status). Final only (R1.3). Raw notes → `../FEEDBACK_LOG.md`; fold durable rules per the SKILL.md learning loop.

## 9. Close-out
After Rishi approves the final export: `"R/06. Tools/finalize_reel.sh" "P"` (deletes only regenerable intermediates, e.g. board/b_*.mov chunks, after confirming the export exists; E1.23).
