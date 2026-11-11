---
name: consulting-case-reel-edit
description: Edit a raw gradnext "Solving real consultant cases" talking-head video end to end (cuts, self-building case board, captions, end card) into a finished 9:16 reel on Rishi's laptop.
---

# Consulting case reel edit (pack v1.5)

Raw talking head → finished gradnext Instagram reel. THE workflow for every consulting case reel [R1.19]; exact clone of the R1/R2 references (layout, board, captions, motion, cuts, pacing) [R1.0]. Build = HTML/CSS board rendered with Playwright + ffmpeg; never build in Premiere or Claude Motion (Premiere may only supply the cut, E1.26). Tesseract = OCR QC only. Write "gradnext" lowercase. This file is the only mandatory read; studio layout/toolchain: `02. Shared Core/STUDIO.md`, `GOTCHAS.md`, `BRAND.md`.

Paths: `R` = studio root `~/Documents/Teaching Claude`. `E` = `R/01. Styles/Consulting Case/engine`. `P` = `R/03. Projects/Consulting Case/<ID>/`, ID = `R###_<topic>_YYYY-MM-DD`. Raw = newest `R/03. Projects/Consulting Case/Raw Footage/Video N/`. Exports `X` = `R/04. Exports/Consulting Case/`.

## Model gate
Check `MODEL_MODE` in the studio root CLAUDE.md, or what Rishi said this session. If it is `opus-only`, skip this section. Otherwise, steps marked [OPUS] (creative planning, storyboard or options, first look-dev of a new scene type, judging QC failures that need taste) need a check: if you are not running on Opus, stop and ask "Next step is creative (<step>). Switch to Opus with /model opus, or continue on Sonnet?" Steps marked [SONNET] (transcribe, cut, captions, building from an approved plan, applying a listed revision, renders, cleanup) run on whatever model is active; if that is Opus, mention once that Sonnet would be cheaper for this stretch.

## The look (fixed)
- **Canvas** 1080x1920, 29.97 fps, H.264 High, AAC 48 kHz. Four scenes only. Hard cuts only at S1→S2 and S2→S3; no other transitions; no zoom/move on the face card.
- **S1 hook**: white panel y 0–750: header, case photo (rounded, ~45 % width, left), hook question right (= spoken hook verbatim), real McKinsey · BCG · Bain logos below (`05. Asset Library/stickers/mbb_logos_trim.png`, never typeset) [R1.8]. Full-bleed face below, no card/glow. Question shown from frame 0 in light grey; each word turns dark as spoken [R1.6]. Caption centred INSIDE the panel, y≈625 [R1.4, R1.14]. Blur-in on the panel only, σ 12 → 0 ease-out, done by 0.8 s (max 1 s); face never blurred [R1.11].
- **S2 punch-in**: exactly once, only on "This is a real <firm> case (interview)", ~1.3x crop, no graphics, NO caption; settles 110 % → 100 % over the whole span, centred, sine ease-in-out, sub-pixel (s2zoom.py) [R1.13, R1.14].
- **S3 board**: background = `05. Asset Library/videos/gradnext-background-loop-9-16.mp4` looped under a transparent board [R1.17]. Board card x 38–1041, y 141–705; caption centred ~y 800; face card x 136–945, y ≈858–1766, radius ~28, lavender glow. Board empty (card + header) ~0.3 s after the cut.
- **Header** (hook panel + board card): "Solving real consultant cases" + "Part NN" pill top-left, "gradnext" top-right; fades out at the end card [R1.17].
- **S4 end card** (on "This is part NN…"): "Solving real consultant cases" · "Part NN" · "Follow for Part NN+1" (pops in on "Follow"). No "gradnext", no header [R1.9]. Part number from the speech. End = last word END + ~0.4 s; never black [R1.0].
- **Captions**: Avenir Next Demi Bold ~52 px navy #2C3552; one line, 2–4 words, ≤680 px (x 200–880); all text within y 140–830 (Reels UI) [R1.5]. Word-by-word rise-in M01, hard line change M02. Split at punctuation and scene boundaries, merge 1-word clauses forward, then split long clauses evenly; never cross a sentence or span S2 [E1.5]. Corrected script words only.
- **Board grammar**: FACTS = persistent right-column tree (root question box, "CLARIFYING QUESTIONS", Q pill → A pill rows, kept) + left-column visual per beat. SOLVE on "So how do we <price/grow> it?": board clears ~0.3 s, root box to top-centre, one tab per method on "…in N ways", working in the middle, number line/bar at the bottom (pricing: ₹ floor / ceiling / answer + highlight; sizing: tables + count bar). Every element on its word ±2 frames. Close values: grey reference marker below the axis, floor/ceiling tier 1, answer tier 2 [E1.6]. Rejected number = strike-through + small ✗, never a big ✗ over it [E1.7].
- **Never**: two-line captions, visuals off the word, decorative motion, anything over the face, extra punch-ins, visuals for filler, rewording the root question. **Flexible**: visual per beat, hook photo, count-up ranges.

## Sound (fixed)
- SFX on board animations and board scene cuts only; NEVER on captions or hook darkening; none at S1→S2 [R1.10, R1.12]. Minimal Edit rules + library `01. Styles/Minimal Edit/sfx/` via sfx.py: many quiet cues; louder wins within 110 ms; +3 dB first 5 s easing to 0 by 6 s.
- Program −15 LUFS ±1, true peak ≤ −1 dBTP, measured on the final MP4 [E1.14, E1.18].
- Final = 1.2x (pitch kept). Music (`05. Asset Library/music/`) not sped, from 0:15 of the track, **13 dB under the voice**; 2 dB steps on request; light duck (threshold 0.1, ratio 2); 1 s fade-in, 2 s fade-out [R1.15, R1.16].
- Deliver `P/sound_cue_sheet.md`. Rishi listens on a phone; numbers aren't a listening check.

## Deliverables (all 1080x1920, never 4K) [R1.1, R1.18]
In X: `<ID>.mp4` (1.2x + music), `<ID>_1x.mp4`, `<ID>_green.mp4` (graphics + captions, #00FF00 where the face shows, same audio/timing), `<ID>_raw.mp4` (cut.mp4 scaled, uncropped), `<ID>_green_PLACEMENT.md` (copy R011's format). `_1x`/`_green`/`_raw` share a frame count. Decode 4K once into the 1440x2560 working cut. Revisions touch the final only [R1.3]. Render to a temp name then move; warn before replacing a file Rishi has [R1.2].

## Workflow
0. **Preflight** [SONNET]. `df -h /` ≥ 3 GB free [E1.1, E1.23]; keep the Mac awake for renders [E1.15]; parallel terminals: claim a distinct R### first [E1.24].
1. **Input** [SONNET]. Ask only if missing: the raw path. Several raw files = one take sequence, later file wins [E1.3].
2. **Transcribe** [SONNET]. ffprobe; `ffmpeg -i raw -vn -ac 1 -ar 16000 P/raw_<n>.wav`; `WHISPER_NG=1 python3 E/islands.py P/raw_<n>.wav P/isl_<n>` [E1.2, E1.20, E1.24].
3. **Cut** [SONNET]. Retake = a clause whose first words repeat within ~20 s, or an abandoned fragment followed by a restart; keep the LAST complete take; drop flubs, fragments, blips, pre/post-roll; split at the RMS minimum. `edl.json` handles 40 ms head / 60 ms tail, no pause > 0.3 s, tail ~0.4 s. `python3 E/cut.py P/edl.json P/cut.mp4` (1440x2560, 10 ms join fades). Map island words to cut time (R011 `map_words.py`). **Premiere pre-cut** [E1.26]: re-read V1 via MCP `get_active_sequence` (track_type video, clip_limit 200) just before writing `edl.json`; don't re-judge his takes; whisper 2–6 s windows around joins; flag content changes in plan.md; extend the last out-point to last word + ~0.4 s.
4. **Correct + align** [SONNET]. Fix ASR with case logic (numbers add up; lakh/crore; "floor" not "flow"; real place names) → `script.txt`; `python3 E/align.py words_cut_raw.json script.txt cut.wav edl.json`.
5. **Plan → STOP for approval (the only stop)** [OPUS]. `P/plan.md` (R011's as template): part, durations 1x/1.2x, hook question + photo with source/licence, S1/S2 spans, phase switch, tabs, number line, retakes, ASR corrections with "please confirm", beat table (time · spoken · board action: zone, component, exact text · motion id), arithmetic check. Wait for Rishi.
6. **Assets + config** [SONNET]. Hook photo licence-safe, literal, no logos/plates, 4:3 → `P/hook.jpg`, logged in `05. Asset Library/photos/CREDITS.md` [E1.9]; chat-pasted images don't reach disk, ask Rishi to save them [E1.16]. Copy from the previous reel: `beats.js`, `crops.env` (check on a still, don't clip hair [E1.8]), `mask.png`, `sfx48/` with `info.json` [E1.27]. Face card: head + shoulders, eyes at ~33 % of card height, never clip hair.
7. **Build** [SONNET; new board component = OPUS look-dev]. Copy R011's `run_build.sh` (events → sfx.py → compose `_1x` → speed_music final → green → raw → qc → face freezedetect), change P, X, part; run OUTSIDE the sandbox [E1.24]. Then write the placement guide.
8. **QC** [SONNET; taste calls OPUS]. Fix and re-run until all pass: every file 1080x1920 29.97; video = audio ±2 frames [E1.12]; no black (d=0.2); no silence gaps (−45 dB, 0.35 s); no surviving retake; hook (header, question = spoken, darkening, logos, centred caption); panel sharp ≤1 s [E1.13]; one smooth punch-in; cut points; elements ±2 frames; captions; OCR every 2 s (~83 % fail with all-correct words in `qc_ocr.txt` = pass [E1.25]); arithmetic; end card; loudness/TP; final 1.2x; contact sheet. Short duration = truncated render; never skip QC [E1.4].
9. **Revise** [SONNET]. Notes → `P/revisions.md` (timestamp · problem · expected · fix · status) + FEEDBACK_LOG.md; fix all in one pass.
10. **Close-out** [SONNET]. After Rishi approves the final export, run `"<studio root>/06. Tools/finalize_reel.sh" "<project folder>"` (it deletes only regenerable intermediates after confirming the export exists). Then the learning loop.

## Read only when…
| Trigger | Open |
|---|---|
| Writing the beat table / choosing a visual per beat | reference/EDITING_PSYCHOLOGY.md + previous plan.md |
| Building a new board beat type, editing board.html | reference/MOTION_LIBRARY.md, reference/DESIGN_SYSTEM.md |
| Exact colours, type sizes | reference/DESIGN_SYSTEM.md |
| Scene timing questions | reference/SCENE_PRINCIPLES.md |
| Changing SFX triggers or voice chain | reference/SOUND_DESIGN.md |
| Running steps by hand | reference/PRODUCTION_WORKFLOW.md |
| A QC check fails / editing qc.py | reference/QUALITY_CONTROL.md |
| An engine script fails, hangs or drifts | reference/ENGINE_NOTES.md |
| Comparing with the R1/R2 references | reference/VISUAL_REFERENCE_LIBRARY.md |
| A rule is questioned | history/RULE_AUDIT.md |

## Learning loop
During a reel, append Rishi's raw notes to `FEEDBACK_LOG.md` (date, reel, note). When the reel is approved, fold the durable rules into this SKILL.md or the right reference/ doc, delete any rule they reverse, add a line to `history/CHANGELOG.md`, and mark the log entries as folded. Keep SKILL.md under about 1,500 words; move detail to reference/ instead of growing it.
