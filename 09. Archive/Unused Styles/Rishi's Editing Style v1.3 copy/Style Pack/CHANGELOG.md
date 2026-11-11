# CHANGELOG: Rishi's Editing Style

Version rule: 1.x = a rule changed, 2.0 = a new visual language. Each entry is classified core / optional / experimental / proposed (same classes as `SYNTHESIS.md`).

## v1.1: 2026-11-06 — [R1.1] exact reference copy
Rishi rejected the rishi.docx-adapted pilot ("bland"). The pack's look reverts to the reference values; rishi.docx is removed entirely. Rishi's colours will be layered in later by iteration.

| change | class |
|---|---|
| Grounds back to reference: blue `#4279BB→#205AA4` + light streaks + faint grid; cream `#EBE7E1` (corner `#E6E2DD`) + faint grid | core |
| Captions back to reference build: white Inter-class sans, mixed sizes (connectors small, key words bold, one white italic serif word), unspoken words grey `≈#8E8E8E` → white; cream scenes dark sans + navy-blue italic | core |
| Accents back to reference: diamond `≈#2F80FF` + ghost word, red hand-drawn ellipse/strike `≈#E83A3A`, money green `≈#2FD26B`, white icon tiles with blue glyph, orange Claude asterisk `≈#D97757` | core |
| CTA = dark Comments sheet (dark input pill, blue send button), not a white bar | core |
| A-roll graded toward the reference's dark, cool, low-key look | core |
| Build engine stays Remotion (Rishi); headless Chrome must run outside Claude Code's sandbox (LESSONS_LEARNED G1). Tesseract notes G2-G4 kept as a fallback reference | build |
| Superseded: paper/ink grounds, signal red / `#1FA463`, General Sans 46px captions, rishi.docx token mapping | removed |

## v1.0: 2026-11-06
Initial pack. Source: 15 reference reels (teardowns V01-V15, `SYNTHESIS.md`, `QUALITY_NOTES.md`) + Rishi's Stage 0 answers `[R1.0]`.

| change | class |
|---|---|
| Edit skill `rishi-editing-style` (gates: ask → analyse → plan + approval → assets → build → revise → sound → QC) | core |
| Scene system S1-S8 (A-roll, split pane, demonstration, proof/UI step, wall, counter, type beat, CTA) with runtime mix and genre recipes | core |
| Caption system: General Sans Semibold 46px, 1-4 words/line, exactly one Playfair Italic key word (~60px), bold numbers/keywords | core |
| Grounds: paper `#f4f1ea` (default), ink `#141414` (heavy beats); one ground per scene; faint grid | core `[R1.0]` |
| Accents: signal red `#e2432a` (one emphasis per frame, pen marks), money green `#1FA463` (money only) | core `[R1.0]`; hexes *proposed* |
| Motion grammar: ease-out entrances ≤ 3% overshoot, two duration tiers, pane moves ease-in-out/in, springs on small objects only | core |
| Chapter diamond badge (lower-left or centred), 1-2-3 tracker | core / optional |
| UI recreations as proof (post, profile, toast, DM, comment bar, product card) | core |
| Optional moves: counter, red ellipse/strike, card wall, carousel, proof zoom, defocus bridge, drum-roll words, spring pop, reel strip, tutorial card, pixelated hidden price, confetti | optional |
| Family A moves (glass/glow panels, holograms, orbit, cylinder carousel, font-cycle, countdown/percentage rings, particles, iris wipe, 3D post push) | experimental (off by default) |
| Sound: measured cue statistics only (≈ 0.4 cues/s, cuts mostly dry); sound built after visual approval; no sound named as fact | core (pattern) / proposed (library) |
| Formatting files added in Phase 4.3: README, CHANGELOG, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, PRODUCTION_WORKFLOW, SOUND_DESIGN, LESSONS_LEARNED | n/a |

### Known open items at v1.0 (to settle in the pilot)
- *Proposed* values: green `#1FA463`, red badge fill, `card.ink`, ink-ground card colour.
- Reference measurements that are [EST] only: caption sizes/positions, typing speed, blur radii, glow/shadow/radius, caption-word fade, counter curve shape (see `SYNTHESIS.md` §8-9).
- Fonts General Sans / Playfair Display must be placed in `assets/fonts/` (empty at v1.0).
- Sound library absent (`assets/sfx` empty).
