---
name: "priestley-style-edit"
description: "Edit talking-head videos (16:9 YouTube long-form or 9:16 Reels) in the Daniel Priestley editorial style: cream paper cards, serif + sans, blue/crimson logic, numbered arc-wipe chapters, glowing PiP whiteboards, name pills, quote cards. Use when Rishi asks for a Priestley-style edit."
---

# Priestley Style Edit (v1.0)

Pack: `Documents/Teaching Claude/DIff Acc/Daniel Presley Editing Style/`
Design-system artifact: see README.

## Read first
1. `LESSONS_LEARNED.md` — Rishi's corrections override everything else.
2. `DECISIONS.md` — `[R1.0]` rules (Inter + Playfair Display; gradnext colours replace placeholders; both 16:9 and 9:16; English only).
3. Then as needed: DESIGN_SYSTEM · SCENE_PRINCIPLES · MOTION_LIBRARY · EDITING_PSYCHOLOGY · SOUND_DESIGN · PRODUCTION_WORKFLOW · QUALITY_CONTROL.

## Fixed (do not vary)
- Talking head is the spine; every graphic echoes a word he says.
- Cream paper (`--paper`) cards; serif titles (Playfair) + sans body (Inter); blue = idea, crimson = number/label/problem.
- Numbered chapters: arc wipe (≈0.12 s) carrying a white tile with crimson numeral.
- PiP on the right, rounded, blue glow, fixed while left content changes.
- Quote card: ghost marks → blue mark scale-in; keywords bold in same blue.
- White name pill on every real person/company/product.
- Hard cuts between scene types; entrances 0.1–0.5 s; builds land on the spoken word.
- No running captions on the speaker, no emoji/shake/zoom-bounce, no whooshes on ordinary cuts.

## Flexible
Accent hues (→ gradnext), textures, which optional scenes (chips, pill stacks, iris+neon stat, framed screens, data viz, principle cards), music genre, 9:16 layout details.

## Gates (in order; stop where marked)
1. **Ask up front**: format (16:9 / 9:16 / both), framing, safe zone, brand name for the name sting, SFX folder, licensed music, words/names to verify.
2. **Analyse**: word timings (whisper; add `-ng` if Metal fails), silences, stray words; tighten to no pause > 0.3 s.
3. **Plan, then STOP for approval**: one row per beat — time · script · core idea · function · options A/B/C (from EDITING_PSYCHOLOGY §2) · why · notes.
4. **Assets** with source + licence (no Priestley footage, frames or photos).
5. **Build** (Claude Motion artifact default; Premiere via premiere-handoff, ffmpeg otherwise) using DESIGN_SYSTEM tokens/components and MOTION_LIBRARY timings.
6. **Revise**: numbered table — timestamp · problem · expected · fix · status. Fix all in one pass.
7. **Sound** only after visuals are approved (SOUND_DESIGN §4).
8. **QC** (QUALITY_CONTROL) and export (reel-export spec: 30 fps, H.264 High CRF 18, AAC 192k, −14 LUFS).

## Scene selection summary
Hook → kinetic serif keyword · name-drop → clip + name pill · proof → 1 s montage · brand → name sting → name card · "N things" → whiteboard/list PiP or chips · section → arc wipe + tile · definition/aphorism → quote card · model → whiteboard PiP · example → B-roll card + PiP + "Example N" · person + number → iris + neon stat · stat → red-vs-blue data viz · analogy → film/stock B-roll 1–3 s · tool → framed screen + pill · end → calm sign-off.

## Text rules
Title Case for titles/labels, sentence case for quotes/body. Titles 1–5 words; quotes 10–25 words; bullets 3–8 words with "- " lead. One emphasis method per element (bold same colour / crimson word / crimson circle / yellow highlighter / underline). English only.

## Sound summary
Voice steady (LRA 2–3 LU), export −14 LUFS. One continuous bed ≈15 dB under voice. Optional soft swell on name sting and chapter wipes only. Rishi verifies by ear.

## Evolve the system
Every Rishi correction → LESSONS_LEARNED `[R1.x]` → update affected files → bump version (1.x rules, 2.0 visual language change) → CHANGELOG → re-propose this skill if rules changed.
