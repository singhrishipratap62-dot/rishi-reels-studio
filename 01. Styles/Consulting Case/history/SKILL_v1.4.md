---
name: consulting-case-reel-edit
description: Edit a raw gradnext "Solving real consultant cases" talking-head video end to end (cuts, self-building case board, captions, end card) into a finished 9:16 reel on Rishi's laptop.
---

> HISTORY ONLY: the v1.4 SKILL.md as it was before the v1.5 restructure (2026-11-11), paths updated. Superseded by ../SKILL.md. The frontmatter above is inert here.

# Consulting case reel edit

Raw one-camera talking-head video in → finished gradnext reel out (`04. Exports/Consulting Case/<REEL_ID>.mp4`, 1080x1920 for Instagram). This is THE workflow for every consulting case reel [R1.19]. Runs in Rishi's Claude terminal inside the studio (`~/Documents/Teaching Claude`). Build engine: ffmpeg + HTML/CSS board rendered with Playwright. Tesseract is OCR QC only. Never Premiere, never Claude Motion. Write "gradnext" lowercase.

## Knowledge base (read before every edit)
Pack: `01. Styles/Consulting Case/`
1. LESSONS_LEARNED.md first — its [R1.x] rules override everything.
2. DECISIONS.md (Rishi rules), DESIGN_SYSTEM.md (tokens, layout px, board grammar), SCENE_PRINCIPLES.md, MOTION_LIBRARY.md, EDITING_PSYCHOLOGY.md (beat → visual framework), PRODUCTION_WORKFLOW.md (exact commands/steps), SOUND_DESIGN.md, QUALITY_CONTROL.md.
3. Reuse `engine/` scripts if present; only fix or extend them. Log anything that cost a re-render in LESSONS_LEARNED.

## Fixed rules (exact clone)
- 1080x1920, 29.97 fps. Four scenes only: S1 hook (opens with a ~1 s Gaussian blur-in; top white panel with header ("Solving real consultant cases · Part NN" left, "gradnext" right): case photo, question in light grey with each word darkening as spoken, real McKinsey/BCG/Bain logo strip, centred caption inside the panel; full-bleed face below) → S2 one punch-in (~1.3x, no graphics, no caption) on the "This is a real <firm> case" line only → S3 board scene (background = 05. Asset Library/videos/gradnext-background-loop-9-16.mp4 loop; board header back, board card 38–1041 x 141–705, one-line caption centred ~y 800, face card 136–945 x ~858–1766 with glow) → S4 end card (Solving real consultant cases · Part NN · Follow for Part NN+1; no "gradnext" and no header on the end card).
- Hard cuts only between scenes; no other transitions; no zooms on the face card.
- Board: FACTS phase (left beat visual + right persistent clarifying-question tree) then SOLVE phase on "So how do we price it?" (method tabs, working area, ₹ number line with floor / ceiling / answer).
- Every board element appears on the word that says it (±2 frames). Caption: one line, 2–4 words (max 680 px), word-by-word rise-in (M01), hard phrase changes. Avenir Next.
- Cut: keep the LAST complete take of a repeated line; drop flubs and fragments; no pause over 0.3 s; 8–12 ms audio crossfades.
- Sound: SFX per the Minimal Edit sound rules (engine/sfx.py, SOUND_DESIGN.md), voice chain, program −15 LUFS / ≤ −1 dBTP. Deliver sound_cue_sheet.md.
- Deliver: final (1.2x + music bed 13 dB under voice), `_1x`, `_green` (graphics on #00FF00), `_raw` (trimmed, uncropped) + placement guide. **Every file 1080x1920 — never 4K** [R1.18]; 4K source is decoded once into the 1440x2560 working cut. Revisions touch the final only.
- Part number comes from the speech. No black after the last word (end = last word + ~0.4 s).

## Flexible
Which visual per beat (icon / photo / grid / bar / number) within the EDITING_PSYCHOLOGY framework; hook photo choice; number count-up ranges.

## Gates
1. **Ask up front only if missing**: the raw file path (default: newest `03. Projects/Consulting Case/Raw Footage/Video N/` folder [R1.19]). Nothing else — all style choices are fixed by the pack.
2. **Analyse**: ffprobe; whisper word timings; silencedetect; retake detection; correct ASR errors with case logic (numbers must add up; lakh/crore; "floor" not "flow").
3. **Cut** automatically, re-transcribe the cut for exact timings.
4. **Plan, then STOP for approval (the only stop)**: `plan.md` table, one row per beat: time · spoken line · board action (zone, component, exact text/number) · motion id · notes. Plus: retakes kept/dropped, ASR corrections, hook question + image candidate with source/licence, punch-in span, phase-switch time, tabs, number-line markers, part number, final duration, arithmetic check.
5. **Assets**: hook photo (licence-safe stock or generated; record source + licence), logo strip and icons from `05. Asset Library/`.
6. **Build**: render overlay frames with Playwright (deterministic `seek(t)`), composite with ffmpeg, export to `04. Exports/Consulting Case/`.
7. **QC**: run every box in QUALITY_CONTROL.md (blackdetect, silencedetect, OCR with tesseract, one punch-in, timings, arithmetic, part number). Fix and re-check before reporting.
8. **Revise**: Rishi's notes go into a numbered table (timestamp, problem, expected, fix, status); fix all in one pass and re-export.

## Evolve the system
Every Rishi correction → LESSONS_LEARNED as [R1.n], update the affected pack file, bump version in CHANGELOG (1.x rules, 2.0 visual-language change). If a rule in this skill changes, re-propose the skill.
