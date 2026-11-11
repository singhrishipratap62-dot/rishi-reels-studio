# Changelog

Versioning: 1.x adds or refines a rule; 2.0 is a meaningful change to the visual language. Every entry says whether it touches **core**, **optional**, **experimental** or **proposed** parts.

## 1.2 — 2026-11-11
Restructure for token cost; no visual rule changed except where LESSONS v1.1 already overrode the older docs.
- **SKILL.md is now the only mandatory read** (786 → ~1,770 words; mandatory reading before was SKILL + LESSONS ≈ 2,840 words, plus whichever deep docs got opened). It compiles every LESSONS rule into current-truth form, adds the Model gate ([OPUS]/[SONNET] steps), the Learning loop, a close-out step (`06. Tools/finalize_reel.sh`) and a "Read only when…" table.
- **Moved:** DESIGN_SYSTEM, MOTION_LIBRARY, TEN_SCENE_PRINCIPLES, EDITING_PSYCHOLOGY, PRODUCTION_WORKFLOW, SOUND_DESIGN, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY → `reference/`. CHANGELOG, LESSONS_LEARNED → `history/`. New: `reference/TESSERACT_BUILD.md` (pipeline + engine gotchas + matte recipe), `FEEDBACK_LOG.md`, `history/RULE_AUDIT.md`. Root `SOUND_DESIGN.md` is a pointer stub so other styles' links keep working.
- **Core (folded from the older archived copy of LESSONS, series intro 2026-11-03, tag `[R1.2]`):** Bold Italic stays the A-roll hero default (upright only offered); measure each SFX file's peak inside the trimmed window; graphics behind the subject via a MediaPipe person matte; intros keep the take continuous (no pause trims, ~0.4 s lead); Rishi's own overlay geometry beats the safe-zone template (captions still obey); move captions below a graphic shirt print (standing: hero y ≈ 1480–1510); one build script per series.
- **Conflicts resolved in reference docs (marked `[v1.2]`):** quote-mark close position (bottom-right after the last line, not top-right); side margin superseded by the safe zone; no shots < 0.5 s added next to the 0.3 s micro-clip rule; A-roll heroes always serif (TEN_SCENE meaning-based serif/sans split now graphic-scenes only); M03 no longer a default (M02 for all heroes); text-centric animation → M01/M02; silence padding 60 ms/>200 ms→~120 ms as the proven default (30 ms kept as tutorial value); linear-easing exception includes M06; old paths (`edits/`, `SFX/`, `minimal-edit-system/`) updated.
- Design System artifact not yet synced with the `[R1.2]` items.

## 1.1 — 2026-11-02
Source: Rishi's notes across the first full edit in Tesseract (*First principles in consulting*, `03. Projects/Minimal Edit/first-principles-kashish/`). New file: **LESSONS_LEARNED.md** (read first). Tag `[R1.1]` marks Rishi-set rules.
- **Core: text motion.** Support text reveals word by word on spoken times and rises from below (M01 revised). Impact text reveals character by character, left → right, with blur, and finishes ≥350 ms before the cut (M02 revised). Applies in captions and graphic scenes.
- **Core: caption type.** A-roll heroes are always Playfair Bold Italic, including *not*; bold sans only inside graphic scenes. Support text goes from 26–36 px to **48 px (≈36 %)**, tight to the hero (above inset from the left, below inset from the right). A lone trailing word sits above-right. Hero capped at 740 px.
- **Core: safe zone.** Replaced the estimated 8–92 % / 10–80 % with Rishi's Instagram Reels template: x 120–960, y 250–1600, icon column clear. Applies after push-ins and is audited on every build.
- **Core: A-roll.** Constant subtle push-in on every shot (+1.2 %/s; M06 revised).
- **Core: sound.** Rewritten SOUND_DESIGN: dense but quiet, a sound on every text entry, `sfx/` library first, trigger map with peak levels, +3 dB opening, measure the final program, effects-only and lip-sync checks.
- **Optional → core details:** quote marks must bracket the text; multi-part builds overlap with no dead time (new M28); highlight box grows visibly from zero over 480 ms (M25 revised); grain strength 0.8 light / 1.0 dark.
- **Layout addition:** split-screen sources put captions on the seam band over a gradient scrim.
- **Workflow:** new Stage 0 (ask style, framing, safe zone, SFX library, music). The Tesseract pipeline is documented as a build target alongside Motion. QC checklist extended to match.
- **Synced 2026-11-02** to the live **Minimal Editorial** Design System artifact (https://claude.ai/artifact/NDguL5ottfkuCUcQQKzCoP): README brand book rewritten for v1.1; tokens updated (`support` 48 px, hero usage notes, Reels safe-zone spacing `safe-x` 120 / `safe-top` 250 / `safe-bottom` 320, new `safe-icon-x` and `hero-max-width`, Tesseract grain note); motion, scenes, qc and workflow sections replaced with v1.1; new **Sound** and **Lessons** sections; CinematicCaption preview now shows serif heroes, 48 px support and the word-rise + character reveal; GraphCard, TextCentric, CenterIllustration and PaperSurfaces guidelines updated. Psychology section and the other previews unchanged.

## 1.0 — 2026-11-01
- Initial system from Joseph's tutorial (video + transcript) and 7 reference reels (R1–R7).
- Docs: DESIGN_SYSTEM, TEN_SCENE_PRINCIPLES, MOTION_LIBRARY (M01–M27), EDITING_PSYCHOLOGY, PRODUCTION_WORKFLOW, SOUND_DESIGN, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, SKILL.
- 44 reference stills and 26 contact sheets.
- Native Design System artifact "Minimal Editorial": tokens, brand book, 6 live component previews and a cover.
- Decisions from Rishi:
  - **Core:** standalone brand (not rishi.docx or gradnext).
  - **Core:** fidelity is "core kept, room to vary". The caption logic, textures, 10 scenes and A-roll logic are fixed. The accent hue (via the `accent` alias) and the serif partner may vary.
  - **Core:** build target is the Claude Motion artifact.
  - **Core:** captions in English and Hinglish (Roman script), with Hinglish hero rules.
- Known gaps: sound is inferred; motion timings are estimated from 1–6 fps samples; few examples for P5B, P8 and P9.
