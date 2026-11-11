# DECISIONS — Consulting case reel edit
> HISTORY ONLY (since pack v1.5, 2026-11-11). Every rule here is compiled into ../SKILL.md or ../reference/; reversed rules are marked in RULE_AUDIT.md. Do not read before an edit. Paths below were updated to the new studio layout.

Rishi-set rules. Tag [R1.0]. These outrank every estimate in the pack.

- [R1.0] Style name: Consulting case reel edit. Pack: Documents/Teaching Claude/01. Styles/Consulting Case.
- [R1.0] References: R1 = "27 octexp.mp4" (mosquito repellent pricing, Part 40), R2 = "28 octexp.mp4" (expressway toll pricing, Part 39). Our own finished edits; no raw available for them.
- [R1.0] Strictness: exact clone. Copy the whole identity: layout, board, captions, motion, cuts, pacing.
- [R1.0] Brand: gradnext. Platform: Instagram Reels 9:16 1080x1920. Write "gradnext" lowercase.
- [R1.0] Input: one-camera talking head, normal background (not green screen). English only.
- [R1.0] Goal: raw video in, finished MP4 out, end to end on Rishi's laptop terminal.
- [R1.0] Build engine: HTML/CSS board + captions rendered frame by frame with headless browser (Playwright), composited with ffmpeg. Not Premiere, not Claude Motion. Tesseract = OCR QC only (text legible, inside safe zone, matches transcript).
- [R1.0] Raw contains retakes, flubs and pauses. Keep the LAST complete take of any repeated line; drop partial/flubbed lines; tighten pauses.
- [R1.0] Board content is planned automatically from the transcript.
- [R1.0] One approval stop only: the board plan (beat table + numbers + retake choices). Everything else runs automatically.
- [R1.0] Hook image (case photo): skill sources or generates it (licence-safe), flagged in the plan for approval.
- [R1.0] Hook logo strip: always McKinsey, BCG, Bain, every video.
- [R1.0] Punch-in: one camera, so the close shot is a digital punch-in. Exactly one per video, only on the credibility line right after the hook question ("This is a real BCG case interview"). Never elsewhere.
- [R1.0] Part number: read it from the speech ("This is part 40 of solving real consulting cases"). End card says Part N and "Follow for Part N+1".
- [R1.0] No black after the speech. The ~10 s black tail in both references is an export error; do not copy it.
- [R1.0] Sound: match references as-is. Voice only, no music, no SFX, loudness left as recorded (no forced normalisation).
- [R1.0] Font: Avenir Next (system font on Rishi's Mac), Demi Bold / Medium / Regular.

## Round 1 notes on pilot R006 (2026-11-05) — these override the [R1.0] lines above where they conflict
- [R1.1] Three exports every reel: final, `_green` (graphics on #00FF00 where video shows), `_raw` (trimmed, uncropped, source res) + placement guide.
- [R1.3] Revisions touch the final export only.
- [R1.4] Hook caption centred, inside the white panel (y≈625, R1.14).
- [R1.5] Captions max 4 words / 680 px per line (overrides 2–7 words).
- [R1.6] Hook question shown from frame 0 in light grey; each word darkens as spoken.
- [R1.7] Opening blur-in: whole frame Gaussian-blurred at 0 s, sharp by ~1 s.
- [R1.8] Real MBB logos (05. Asset Library/stickers/mbb_logos_trim.png), same strip layout.
- [R1.9] No header anywhere (no "gradnext", no "Solving real consultant cases · Part NN"); no "gradnext" on the end card.
- [R1.10] SFX wanted (overrides "voice only, loudness as recorded"): Minimal Edit sound rules, −15 LUFS program. See ../reference/SOUND_DESIGN.md.
- [R1.11] Blur-in on the white panel only, subtle (σ 12), done by 0.8 s.
- [R1.12] No SFX on captions; SFX only on animations.
- [R1.13] S2 punch-in: 110% → 100% eased settle over the full S2 span.
- [R1.15] Final = 1.2x speed + supplied music bed ~21 dB under the voice (speed_music.sh); keep `_1x.mp4`.
- [R1.16] Music bed 13 dB under the voice (21 dB was inaudible).
- [R1.17] Header back on hook + board (not on end card). Board-scene background = 05. Asset Library/videos/gradnext-background-loop-9-16.mp4 loop (reverses R1.9 header part).
- [R1.18] (2026-11-06) The posted reel is Instagram 9:16 **1080x1920**. Never output 4K. Decode the 4K source once (cut.py → 1440x2560 working cut, kept only for the S2 punch-in headroom); every deliverable — final, `_1x`, `_green`, `_raw` — is 1080x1920. `_raw` = the working cut scaled to 1080x1920 (no second 4K decode).
- [R1.19] (2026-11-06) This pack IS the workflow for every consulting case reel. New footage goes in `03. Projects/Consulting Case/Raw Footage/Video N/`; default input = the newest Video N folder.
