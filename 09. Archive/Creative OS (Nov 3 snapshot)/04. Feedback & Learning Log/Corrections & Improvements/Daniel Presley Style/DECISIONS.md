# DECISIONS — Daniel Priestley Editing Style

Rishi-set rules. These outrank every estimate in every other file. Tag: `[R1.0]` (set 2026-11-03, Stage 0).

| # | Decision | Rule |
|---|---|---|
| 1 | Style name / creator | "Daniel Priestley Editing Style". Creator studied: Daniel Priestley (YouTube long-form). References: `raw reference videos/` (28 files, R01–R28 = file numbers 01–28). Folder name keeps Rishi's spelling "Presley". `[R1.0]` |
| 2 | What to copy | The whole identity: scene types, layout, motion, transitions, text logic, pacing, B-roll treatment, sound. `[R1.0]` |
| 3 | Fonts (override) | **Inter** (sans) + **Playfair Display** (serif) replace Priestley's fonts. His fonts are recorded only for reference. `[R1.0]` |
| 4 | Colours (override, pending) | Final palette = **gradnext** colours. gradnext hex values were not available at build time, so Priestley's measured colours are used as **placeholder tokens** (each marked `PLACEHOLDER → gradnext`). Swap them when Rishi supplies the gradnext palette. `[R1.0]` |
| 4a | Colours (resolved, pending approval) | gradnext palette was found in Rishi's gradnext Design System artifact after Stage 0. DESIGN_SYSTEM §3a maps each Priestley colour role to a gradnext token. Rishi to approve the mapping (chrome-yellow standing in for Priestley's crimson). |
| 5 | Strictness | Core fixed, room to vary. Fixed: scene system, layout geometry, motion grammar, text logic, pacing. May vary: accent hues (→ gradnext), fonts (already overridden), textures. `[R1.0]` |
| 6 | Formats | **Both**: 16:9 1920×1080 YouTube long-form **and** 9:16 1080×1920 Instagram Reels. Reels safe zone: x 120–960, y 250–1600, right icon column kept clear. `[R1.0]` |
| 7 | Language | English only. `[R1.0]` |
| 8 | Build target / deliverables | (a) this pack folder with the full design system; (b) a published Claude Motion / Design-System artifact (tokens, type, scene previews, live motion demos), built in Inter/Playfair with no third-party frames. `[R1.0]` |
| 9 | Sound | Analyse reference audio; match cues to `assets/sfx`. Note: `assets/sfx` was **empty** at build time, so no file matching was possible; cue groups are described by measurement for later matching. `[R1.0]` |
| 10 | Analysis depth | Deep visual / graphics / motion analysis on **all 28**. Transcripts only on 3–5 videos ("if Whisper doesn't work, proceed without it"). Result: 1 transcript (R22) succeeded; see VISUAL_REFERENCE_LIBRARY. `[R1.0]` |
| 11 | Notes / tutorial supplied | None. `[R1.0]` |
