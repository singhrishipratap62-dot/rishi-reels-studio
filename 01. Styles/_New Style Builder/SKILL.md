---
name: "reverse-engineer-style"
description: "Reverse-engineer a creator's video graphic style from reference videos into a reusable design system plus an edit skill. Use when Rishi gathers reference videos to copy a style."
---

# Reverse Engineer Style

Turns a set of reference videos (creators whose graphic/editing style Rishi likes) into (1) a written design-system knowledge base and (2) an edit skill that builds new videos in that style.

This skill is a PROCESS only. It carries no style of its own. Every colour, font, size, scene type, motion, caption rule, sound cue and pacing number in the output must come from the new reference videos and from Rishi's answers, never from any style made before. Do not reuse tokens, scene lists, motion libraries or rules from earlier styles as defaults, examples or starting points, unless Rishi explicitly says to build on or fuse with a named one.

Work on Rishi's laptop (local shell / Claude terminal) for ffmpeg, transcription, frame and audio work. Keep token use low: analyse from contact sheets and measurements, not hundreds of individual frames. Write "gradnext" in lowercase.

## Saved styles (pointers only)
A list of styles already made, so Rishi can say how the new one relates to them. Entries hold only: name, one-line identity, where its pack/skill/artifact lives. No rules or values are stored here. If Rishi picks one to build on or fuse with, read its live pack then; otherwise ignore it completely.

Active packs are in `01. Styles/` of the studio (`/Users/rishi/Documents/Teaching Claude`). Each has its own skill command:
- Consulting Case: "Solving real consultant cases" reels with a self-building case board. Skill: consulting-case-reel-edit. Pack: 01. Styles/Consulting Case.
- Before-After: raw vs edited comparison reel. Skill: before-after-reel. Pack: 01. Styles/Before-After.
- IG Motion Explainer: gradnext motion-graphic explainer from a topic. Skill: gradnext-motion-explainer-instagram. Pack: 01. Styles/IG Motion Explainer (also holds the gradnext design system).
- Rishi v2: Hinglish talking head with premium-minimal graphics around the face. Skill: rishi-v2. Pack: 01. Styles/Rishi Style v2.
- Mock Case Interview: long-form two-camera Premiere edit. Skill: mock-case-interview-edit. Pack: 01. Styles/Mock Case Interview.
- Minimal Editorial: Arthur Brooks-style talking head. Skill: minimal-editorial-edit. Pack: 01. Styles/Minimal Edit. Artifact: https://claude.ai/artifact/NDguL5ottfkuCUcQQKzCoP
- Archived (09. Archive/Unused Styles, read only if Rishi asks): Daniel Priestley, Azma Paper Stage, Claude Edits / Prompt-to-Reel, Rishi's Editing Style v1.3.
- Other brands: rishi.docx (never mixed with gradnext), Kashish Carousel.

When a new style is finished, add one pointer line for it and propose the updated skill with the complete file.

## Stage 0 - Ask up front (AskUserQuestion, one batch, with defaults)
Do not analyse anything before these are answered:
1. **Style name and creator(s)** being studied, and where the videos are (default folder: `01. Styles/<Style Name>/references/` in the studio).
2. **What to copy**: the whole identity, or only parts (captions, colour/type, scene types, motion, transitions, sound, pacing, B-roll treatment). Anything to explicitly NOT copy.
3. **How strictly**: exact clone / core fixed with room to vary (default) / loose inspiration. Which tokens may vary (accent hue, fonts, textures).
4. **Brand relationship**: standalone new brand, or fused with a saved style or brand (rishi.docx, gradnext, other). Brand colours and fonts to use instead of the originals, if any.
5. **Video type it is for**: talking head, green-screen talking head, AI voiceover, mute/UI demo, split-screen, podcast clip, carousel, other. Aspect ratio and platform safe zone (default platform template: Instagram Reels, x120-960, y250-1600, icon column clear; ask if another platform).
6. **Languages**: caption language(s); Hinglish in Roman script only, never Devanagari.
7. **Build target**: Claude Motion artifact (default), Tesseract, or Premiere Pro automation.
8. **Sound**: analyse reference audio? SFX library folder (default <Style>/sfx)? Licensed music available?
9. **Any tutorial/transcript/notes** supplied with the references, and any rules Rishi already knows he wants.
Record every answer in DECISIONS.md at the top of the pack, tagged `[R1.0]` (Rishi-set rules outrank all estimates).

## Stage 1 - Capture references (local)
Target roughly 7-20 of the best reels, plus any tutorial video about the style. Work in `<Style>/references/`; keep scratch in `<Style>/.work/`.
- **Inventory**: ffprobe each file (duration, fps, resolution). Name them R1..Rn (tutorial = T).
- **Transcripts**: mlx-whisper with word timestamps for every video with speech; snap edges to `silencedetect`; flag words with confidence < 0.7.
- **Cut detection** per reel: `ffmpeg -i f.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null -` to get shot lengths and average shot length.
- **Contact sheets** (what Claude actually looks at): `ffmpeg -i f.mp4 -vf "fps=1,scale=270:480,tile=6x5" sheet_%02d.jpg`. Choose the sampling interval by video length and how fast it changes.
- **Animation strips** for motion timing: for each interesting moment cut 1-2 s at the native fps and tile the frames. Measure timings from native-fps frames, not from sparse samples; mark anything estimated from sparse samples as such.
- **Stills**: keep only the best frame per distinct scene type or notable element, named `P##_<src>-<mmss>_<what>.jpg`. Stills are third-party; private study only, never publish.
- Skip promo sections of tutorials. Say what was not viewed.

## Stage 2 - Analyse
Tag every claim with an evidence tag: `[OBS]` seen directly (timestamp), `[TX]` said in a tutorial/transcript, `[EST]` measured/estimated by me, `[INF]` my interpretation, `[R#.#]` set by Rishi (outranks the rest).
1. **Tokens**: sample pixel medians (PIL) at timestamps for backgrounds, accents and text; cluster into a small palette. Fonts: crop headline text, compare with likely Google Fonts candidates, mark uncertain ones. Sizes as ratios of the frame and of the main text. Text colour per background.
2. **Text/caption logic**: words per group, hierarchy, placement, alignment, position as % of height, how emphasis is chosen, language handling, how text enters and leaves.
3. **Scene taxonomy**: discover the scene types the references actually use (do not start from a preset list). For each: what it looks like, background, textures, when used, common mistakes, frequency and share of runtime.
4. **Motion library**: name each animation `M##` with initial -> final state, duration, delay, easing and use. Mark measured vs estimated.
5. **Textures and treatments**: grain, overlays, glows, blurs, vignettes, masks; whether they move with their layer.
6. **Editing psychology**: map each line of script to the scene chosen and why; derive the per-beat selection framework (function -> first choice -> alternates) and anti-patterns from the references.
7. **Pacing**: average shot length per reel, time to first visual, share of each scene type, rhythm of backgrounds.
8. **Core / optional / experimental**: classify every finding. Core only if it appears in most references or the creator states it. Do not let one reference rewrite the identity.
9. **Gaps**: list what is low-evidence.

## Stage 3 - Audio by measurement
Claude cannot hear. Never claim to know how something sounds. Measure instead, locally:
- Stems: Demucs to split voice / music / effects (or analyse the full mix if separation fails).
- Onsets: librosa onset detection; align each onset to the nearest visual event from the cut/animation timeline; report hit rates and typical offsets in ms.
- Levels: peak and LUFS per cue and per stem (`ffmpeg ... loudnorm=print_format=json`, ebur128); music-under-voice gap; ducking; cues per second.
- Cue character: duration, spectral centroid (brightness), attack sharpness, pitch rise/fall; cluster into cue groups and match each group to the closest files in the SFX library by those numbers.
- Write a cue-group table: visual event -> cue group -> candidate library file -> peak level -> timing offset. Mark every row measured / matched / unverified.
- If a reference has no meaningful audio or only a trending song, say so and ask Rishi for the sound direction.
- Add a listening step: Rishi listens on a phone and corrects; log corrections as Rishi rules. Measurement is a starting point, taste is his.

## Stage 4 - Write the knowledge base
**Studio pack format (required; keeps token cost low):** the pack lives at `01. Styles/<Style>/`. Its edits go in `03. Projects/<Style>/` and its exports in `04. Exports/<Style>/`. `SKILL.md` is the only mandatory read; keep it to about 1,500 words. It holds the gates, hard rules and numbers, and a "Read only when…" table. Deep docs (DESIGN_SYSTEM, MOTION_LIBRARY, SCENE_*, PSYCHOLOGY, SOUND, QC, VISUAL_REFERENCE) go in `reference/`. CHANGELOG, raw lessons and the rule audit go in `history/`. Add `FEEDBACK_LOG.md`, and add the Model gate and Learning loop sections the other packs use (copy them from `01. Styles/Rishi Style v2/SKILL.md`). Don't restate brand, toolchain or retention rules; link `02. Shared Core/`. Then register it: `ln -s "<pack>" ~/.claude/skills/<skill-name>`, and add a row to the studio root CLAUDE.md table.
Create `<Style>/` as a pack containing: README (index), SKILL (entry point), DECISIONS, LESSONS_LEARNED (empty at v1.0; read first once it has content), DESIGN_SYSTEM (philosophy, canvas, colour, type, textures, layout, scene list, components, core vs optional), SCENE_PRINCIPLES (one section per discovered scene type), MOTION_LIBRARY, EDITING_PSYCHOLOGY, PRODUCTION_WORKFLOW, SOUND_DESIGN, QUALITY_CONTROL (tick-box checklist), VISUAL_REFERENCE_LIBRARY (how frames were captured and their limits, stills index, contact sheets, beat maps, reference stats), CHANGELOG. Everything inside comes from this style's own references. Write files section by section, not in one giant pass. If a Design System artifact is wanted, publish tokens and previews there and keep the files as the written source.

## Stage 5 - Package the edit skill
Generate `SKILL.md` for the new style (propose it with the propose_skills tool; the proposal is the deliverable). It must contain: knowledge-base pointers (read LESSONS_LEARNED first), fixed vs flexible rules, the gates, scene selection summary, text rules, sound summary, and the evolve-the-system rule. Gates for the edit skill: ask up front (style, framing, safe zone, SFX, music, words to verify) -> analyse (word timings, silences, stray words) -> plan then STOP for approval (one row per beat: time, script, core idea, function, options A/B/C, why, notes) -> assets with source and licence -> build -> revise (numbered table: timestamp, problem, expected, fix, status; fix in one pass) -> sound only after visuals approved -> QC and export.
Also add the new style's pointer line to the Saved styles list in this skill.

## Stage 6 - Pilot edit and corrections loop
1. Do one real edit with the new style. Expect the first draft to be only partly right.
2. Rishi's corrections go into LESSONS_LEARNED tagged `[R1.1]`, `[R1.2]`...; they override every estimate in the other files. Update the affected files, bump the version (1.x for rule changes, 2.0 for a real change in the visual language), log it in CHANGELOG as core/optional/experimental/proposed.
3. Record build-engine gotchas (anything that cost a rebuild) in LESSONS_LEARNED.
4. Re-propose the edit skill if its rules changed.

## Rules
- Ask before analysing; never assume what to copy or how strictly.
- Derive everything from the new references; no inherited style defaults.
- Plan, then stop for approval before any build; no sound before visuals are approved.
- Never state an uncertain transcript word, font or sound as fact.
- Do work locally via the laptop shell; stage to the cloud only for steps that need it (looking at images/PDFs).
- Third-party frames are for private study; do not publish them or put creators' photos into outputs.
- Say plainly what could not be seen or heard.
- Everything Rishi sets outranks my estimates.