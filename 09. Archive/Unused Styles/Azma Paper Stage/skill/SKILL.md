---
name: paper-stage-edit
description: "Edit Rishi's talking-head reels in the Paper Stage style (from @asmaijazkhann refs): SRT → planning doc → Rishi plans → Motion build of paper-stage graphics, ink headlines, articles, UI mocks → revisions → sound."
---

# Paper Stage — talking-head edit skill (v1.0)

A clean explainer look: white "paper" scenes with one coloured floor and one hero prop, words that darken as they are spoken, articles that blur in and get highlighted, UI mock-ups, quote cards and timelines over the A-roll, small captions under the chin. Reverse-engineered from 15 @asmaijazkhann reels and adapted to Rishi's choices (A10).

## Knowledge pack — load in this order
1. `RULEBOOK.md` — what to show when, density, captions, fonts, palette, motion defaults. Always.
2. `REFS_INDEX.md` — one row per key: when to use it, refs path. Always (it is the menu for the planning doc).
3. `LOOKBOOK.md` — build spec for each key. Open only the sections for keys used in this edit.
4. `refs/<key>/` — stills + motion strips. Open only for keys being built for the first time or when a build "doesn't feel like her".
5. `SOUND.md` — at the sound step only.
6. `LESSONS.md` — read the last 20 lines before planning; append after every edit.
Folder on the laptop: `Documents/Teaching Claude/Azma's style/skill/`. Raw research (don't load unless asked): `breakdown/`, `work/`.

## Where things run
- All ffmpeg, face tracking and file work on Rishi's laptop (device_bash), not the cloud.
- Build target: the Claude **Motion** artifact (decided in A11; same as Minimal Editorial). Create it from the Motion type and follow that type's own instructions; implement each key as one reusable scene function with the timings from LOOKBOOK.
- Output 1080×1920, 30 fps (or the A-roll's native fps).

## Gates (never skip)
1. **Intake.** Rishi gives a rough cut (Gling/manual) + SRT in `Video Projects/<name>/`. Work only on the video he names, only when he asks. Run `tools/face_track.py <video>` → `<video>.face.json` (chin_y for captions, nose for K03). Note silences > 0.6 s.
2. **Planning doc, then STOP.** One row per SRT sentence: time · exact line · trigger type (number / name / quote-article / list / tool-or-site / chronology / thesis / opinion) · up to 4 suggested keys from REFS_INDEX with a one-line visual each · recommended pick. Mark A-roll lines plainly. Show the density check (graphic % of runtime, longest A-roll stretch, first graphic time). Ask the colour questions for K18/K19 (brand colour) and whether any K03/K14 moments are wanted. Wait for Rishi's plan (~15 min). Never build before.
3. **Assets.** List what each chosen scene needs: Rishi's cut-out photos, face photos for stickers, product PNGs, article screenshots (real URL + screenshot), tool UI references. Pixel art, cursors, coins, floors, cards are drawn in code. Ask for anything missing; never fake an article or quote.
4. **Build.** Captions first (K01 under the chin), then scenes in timeline order. New key → Opus; a key already proven in LESSONS → Sonnet. Render a **design sheet** (one still per scene) for approval before the full render.
5. **Revise.** Numbered table: timestamp · note · fix · status. Small fixes on Sonnet; "doesn't feel like her" → Opus + reopen `refs/<key>/`.
6. **Sound.** Only after visual approval. Follow SOUND.md; deliver the cue sheet + SFX stem; music −20 dB under voice.
7. **QC + lessons.** RULEBOOK QC list, render, then append what Rishi changed to LESSONS.md.

## Hard rules (from A10)
- Fonts: Inter + Playfair Display accent only (Patrick Hand only inside notebook props, Helvetica only for scribble notes).
- No memes, no podcast split, no "and today" card, no gold-tag labels. No b-roll (K14) or greyscale beat (K03) unless Rishi asks.
- Brand-coloured pieces (K18 quote card, K19 lower-third) — ask the colour first; recommend the brand's own colour.
- Ends on plain A-roll.
