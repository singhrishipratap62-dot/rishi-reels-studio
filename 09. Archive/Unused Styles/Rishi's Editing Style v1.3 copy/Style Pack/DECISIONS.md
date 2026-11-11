# DECISIONS — Rishi's Editing Style

Rishi-set rules. They outrank every estimate in every other file. Tag `[R1.0]` = set 2026-11-06 at Stage 0 (Phase 3). Later corrections from the pilot go in LESSONS_LEARNED as `[R1.1]`, `[R1.2]`… and outrank this file.
Source of the style: 15 reference reels, analysed in `teardown-workspace/main-session/scratchpad/reel-teardowns/` (BREAKDOWNs + `SYNTHESIS.md`).

## [R1.1] override (2026-11-06)
Copy the reference style exactly (colours, type, animations, graphics). rishi.docx is NOT used at all. Rishi's own colours are added later by explicit iteration. Rows 4-9 and the token table below are kept only as history.

## Precedence (highest first)
1. Rishi's corrections during real edits (`[R1.x]` in LESSONS_LEARNED). These are final once given.
2. This file (`[R1.0]`).
3. **The reference editing style** (SYNTHESIS.md, Family B CORE + OPTIONAL). It owns scene types, layout, UI elements, motion curves and timings, caption logic, pacing, transitions and the sound pattern.
4. **rishi.docx**, as a light personal-taste layer only: colours, fonts, small taste notes. It is **not** an override of the editing style. `[R1.0]`

## Decisions
| # | Decision | Rule |
|---|---|---|
| 1 | Style name | **Rishi's Editing Style**. Pack: `Rishi's Editing Style copy/Style Pack/`; edit skill name `rishi-editing-style`. `[R1.0]` |
| 2 | What to copy | **Family B** (V05-V15: flat UI cards as proof, one graphic ground per reel, split pane, chapter badges, sans + one italic-serif word captions, card walls, literal demos, keyword CTA). Rishi likes both families; Family A moves (V01-V04 glass/glow panels, holograms, orbit, cylinder carousel, font-cycle) stay EXPERIMENTAL and are not used by default. The colour style is Rishi's own (#4). `[R1.0]` |
| 3 | Strictness | **Core fixed, room to vary.** Fixed: scene system, layout geometry, motion curves/timings, caption logic, pacing. May vary: accent use, textures, which optional moves appear. `[R1.0]` |
| 4 | Brand layer | **Colours and fonts from rishi.docx, with Playfair as the serif.** rishi.docx is only light personal taste (see Precedence). Do **not** import from rishi.docx: its green-screen layout, its square/radius-0 card rule, its motion/pacing rules, its "swoosh on every move" sound rule, or its strict 3-colour rule (a money green is allowed, #6). `[R1.0]` | **SUPERSEDED by [R1.1]**
| 5 | Grounds | **Paper default + ink for heavier beats.** Paper `#f4f1ea` plays the reference cream ground (#EBE7E1). Ink `#141414` replaces the reference blue ground for heavier beats (deadline, verdict, question, drum-roll words). Keep the reference's faint grid; draw it in rishi.docx `--line` (`#1414141f` on paper, `#f4f1ea24` on ink). One ground per scene; switching ground between scenes is allowed. `[R1.0]` | **SUPERSEDED by [R1.1]**
| 6 | Accent colours | **Signal red + one money green.** Signal red `#e2432a` = the frame's one emphasis: the italic key word on paper, the key number, or a pen mark (hand-drawn ellipse, strike, arrow, underline). Money/good outcome = green (proposed `#1FA463`, the reference's cream-scene green [EST]; confirm in the pilot). Use green only for money/prices/positive results. This exception to the 3-colour rule is deliberate. `[R1.0]` | **SUPERSEDED by [R1.1]**
| 7 | UI elements / cards | **Follow the reference for now**: rounded white cards with soft shadows, UI recreations (posts, toasts, comment bar, chat, product cards), diamond chapter badge, recoloured into rishi.docx tokens. Open to change: Rishi may change any of it during real edits, and those changes become final (`[R1.x]`). `[R1.0]` | **SUPERSEDED by [R1.1]**
| 8 | Fonts | Sans = **General Sans** (rishi.docx). Serif/italic emphasis = **Playfair Display Italic** (replaces rishi.docx Gambetta and the reference's unconfirmed italic serif). `[R1.0]` | **SUPERSEDED by [R1.1]**
| 9 | Caption size | **rishi.docx sizes**: 46px General Sans Semibold captions on the 1080x1920 canvas; the one Playfair Italic key word ≈ 1.3× (≈ 60px). Nothing readable under 44px (micro UI text inside recreated cards excepted). Position follows the reference: A-roll captions centred around y ≈ 60-64% H (≈ 1150-1230px), never over the face; on graphic scenes the top band (below the 250px IG top-safe line). `[R1.0]` | **SUPERSEDED by [R1.1]**
| 10 | Format | **9:16 Reels only**: 1080x1920, 30 fps. IG safe zone: text between y 250 and y 1500, right icon column (last 160px) clear. Landscape sources (e.g. Vid 1.mp4, 1920x1080) are reframed to vertical. `[R1.0]` |
| 11 | Footage | **Real talking-head footage, no green screen.** A-roll is cut in the edit; the split pane slides over the real A-roll. `[R1.0]` |
| 12 | Language | **English + Hinglish.** Captions follow speech; Hinglish only in Roman script, never Devanagari. Uncertain words are verified with Rishi, never guessed. `[R1.0]` |
| 13 | Reel types | **All four**: teach-a-rule/tips, story/case study (consulting cases fit here), offer/launch, AI/tool workflow. Each gets a scene recipe. These are **not a limit**: other formats are allowed and get adapted from the same system. `[R1.0]` |
| 14 | Build target | **Remotion** (measured cubic-beziers and timings carry over exactly; render 1080x1920 locally). `[R1.0]` | Kept as Remotion (Rishi, 2026-11-06). Render where headless Chrome is allowed (see LESSONS_LEARNED G1).
| 15 | Sound | **Follow the reference pattern; add sound later.** The pack writes the measured cue pattern (≈ 0.4 cues/s, cuts mostly dry, cues on pane/card moves and keyword typing, quiet bed ≈ −19.6 dB rms p50). Sound is built only after visuals are approved, once Rishi puts SFX into `assets/sfx` (empty at v1.0; `assets/music` has 1 file). Sound types are never claimed from the references (not verified). `[R1.0]` |
| 16 | CTA | **Varies per reel**, decided in each edit plan. The reference default (comment bar typing a KEYWORD) is one option, not a rule. `[R1.0]` |
| 17 | Notes / known rules | None supplied beyond the answers above. `[R1.0]` |

## Token mapping (reference role → Rishi's token) — SUPERSEDED by [R1.1]; see DESIGN_SYSTEM §3 (reference values)
Proposed from #4-#9. Rows marked *proposed* are first guesses to check in the pilot.
| role in the reference | reference value | Rishi's Editing Style |
|---|---|---|
| light graphic ground | cream #EBE7E1 [MEAS] | paper `#f4f1ea` |
| heavy graphic ground | blue #4279BB → #205AA4 + rays [MEAS] | ink `#141414` + faint grid (no rays) *proposed* |
| raised surface / panel | white cards #FDFDFD | white `#FFFFFF` cards with soft shadow on paper; `#1f1e1c` cards on ink *proposed* |
| body text on light ground | navy #103D7B / #193452 [MEAS] | ink `#141414`; secondary `#5f5c56` |
| text on A-roll / dark | white | paper `#f4f1ea` |
| italic key word on light ground | blue ≈ #2A5FA0 [EST] | Playfair Italic in signal red `#e2432a` |
| italic key word on A-roll | white italic serif | Playfair Italic in paper `#f4f1ea` *proposed* (red only if it is the frame's single emphasis and ≥ 60px) |
| chapter diamond badge | blue ≈ #2F80FF [EST] | signal red fill, paper numeral *proposed*; it counts as the frame's red |
| money / good outcome | green ≈ #1FA463-#4CE38B [EST] | money green `#1FA463` *proposed* |
| scarcity pen marks | red ≈ #E83A3A [EST] | signal red `#e2432a`, 10px pen stroke |
| hairlines / grid | faint grid [OBS] | `--line` / `--line-strong` |
