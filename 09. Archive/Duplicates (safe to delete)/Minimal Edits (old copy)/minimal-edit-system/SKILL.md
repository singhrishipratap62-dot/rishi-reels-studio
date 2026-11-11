---
name: minimal-editorial-edit
description: Plan and build premium minimal talking-head reel edits (Arthur Brooks style) in the Minimal Editorial design system: transcript, scene plan for approval, Motion build, revisions, sound.
---

# Minimal Editorial — talking-head edit skill (v1.1)

Turns a raw talking-head clip (or its SRT) into a premium minimal edit: cinematic captions, then paintings, B-roll, lines, illustrations, quotes, object callouts and graphs, each chosen by what the speaker is doing in that line.

## Knowledge base — load first
- **`LESSONS_LEARNED.md` (local, v1.1):** Rishi's corrections from the first Tesseract edit. Its rules override the v1.0 defaults below.
- **Design System artifact "Minimal Editorial"**: https://claude.ai/artifact/NDguL5ottfkuCUcQQKzCoP. Read `project/README.md` first, then `project/tokens.json`, and when needed the sections `scenes.md`, `psychology.md`, `motion.md`, `workflow.md`, `qc.md`, plus `components/*/README.md` and `components/bundle.css` (reusable texture and caption CSS).
- Fixed: the caption logic, texture on every graphic, the 10 scene types + A-roll, announce → face / explain → show, and one accent per video. Can vary: the `accent` hue (alias) and the serif partner.
- Build target: the Claude **Motion** artifact, or **Tesseract** when asked. The Tesseract pipeline is proven: see `LESSONS_LEARNED.md` §7–8. Captions: English and Hinglish (Roman script only).

## Gates (never skip)
0. **Ask up front:** style source, split-screen framing, platform safe zone (default Instagram Reels), SFX library (default `SFX/`), music.
1. **Analyse.** Get word-level timings (from the SRT, or by transcribing). List silences and propose cuts with 30 ms padding (raise it if attacks get clipped). Flag stray micro-words.
2. **Plan, then STOP.** Make an edit-plan page with one row per beat: time, exact script, core idea (≤3 words), function (hook/announce/explain/example/person/number/progression/quote/emotion/joke/close), three design options A/B/C (scene type, one-line visual, motion IDs, assets), a "why this" line, and a notes box. Recommend one option. Wait for the user's picks and edits. Never animate before approval.
3. **Assets.** Build an asset list with source + licence (public-domain paintings from Wikimedia, stock from Pexels, the user's own photos). Ask for anything missing; never substitute an unrelated visual.
4. **Build in Motion.** Make one reusable function per scene type; texture layers go inside the camera group. Build captions first, then the scenes in order. Render the first draft and say it's a draft.
5. **Revise.** Keep a numbered table (timestamp · problem · expected · fix · status), apply all fixes in one pass, re-render, then ask: "ready for sound design, or more revisions?"
6. **Sound.** Only after visual approval. Follow `SOUND_DESIGN.md` v1.1:
   - Dense but quiet, from the `SFX/` library first.
   - Hi-Tech Click on impact words, a quiet flick on every support word, Highlighter on every line extension, Swoosh/Woosh on scene changes. First 5 s +3 dB.
   - Final mix −15 LUFS, true peak ≤ −1 dBTP.
   - Run the effects-only placement check and the lip-sync check, then deliver the cue sheet.
7. **QC.** Run `qc.md`. Export 1080×1920, 30 fps.

## Scene selection (per beat)
Announce/hook/emotion/joke/close → A-roll + captions (vary framing with zoom cuts). Number/trend → Graph. Story vignette/historic/romantic/person → Painting (character callout for a person). Felt action → B-roll. One concept → Center illustration. Two things at once → Side illustration. Real artefact → Object callout. Stages → Line + illustration zigzag. Chain of abstract terms → Line + text. Quote/thesis → Text-centric with quote marks. If you can't say why a visual beats A-roll, use A-roll. Target an average shot of 1.5–3 s and a first visual within ~2 s, and alternate grounds.

## Captions (v1.1)
- ≤5 words per group. Hero = the meaning word, centred, at 55–70 % height (on the seam band for split screens).
- **On A-roll the hero is always Playfair Bold Italic**; bold sans heroes only inside graphic scenes.
- Support words are **48 px (≈36 %)**, tight to the hero: the line above is inset from the hero's left, the line below inset from its right.
- **Support text reveals word by word**, rising on spoken times (M01). **Impact text reveals character by character, left → right, with blur** (M02), finishing ≥350 ms before the cut.
- Everything stays inside the Instagram Reels safe zone (x 120–960, y 250–1600, icon column clear), with the hero ≤740 px wide. Hinglish: the hero may be a Hindi word; helper verbs and particles stay small; never split compound verbs; numbers stay digits.

## Evolving the system
When the user gives a new reference: analyse it separately, compare it with the brand book, and classify each finding as core, optional, experimental or proposed. Update only the affected files in the Design System artifact (read first, change only what's needed), bump the version (1.x, or 2.0 for a real change in the visual language), and log it in the changelog. Don't let one reference rewrite the identity.
