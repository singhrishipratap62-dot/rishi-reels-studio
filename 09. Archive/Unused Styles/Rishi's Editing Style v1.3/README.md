# Rishi's Editing Style: pack v1.3

Edit system for 9:16 talking-head Reels, reverse-engineered from 15 reference reels (private study) and adjusted by Rishi. **v1.3 = Ink blue palette + Editorial serif captions `[R1.3]`** on the reference scene/motion grammar, plus the signature depth family (`DEPTH_AND_ORBIT.md`, person matte in `engine/matte/`). It is a **working starting point**: the first real video and Rishi's feedback define the final system. Build target: Remotion, 1080×1920, 30 fps.

Teardowns live in `teardown/` (15 `V##_slug/BREAKDOWN.md` + `animations.json`, `SYNTHESIS.md`, `QUALITY_NOTES.md`, `PROGRESS.md`; `index.txt` maps V## to the source file). The reference videos are in `a reference to Rishi's editing style/`; measuring scripts in `engine/measure-scripts/`. **v1.2** adds the signature depth family (`DEPTH_AND_ORBIT.md`) and the design-chat decisions `[R1.2]`.

## Read in this order
1. `LESSONS_LEARNED.md`: Rishi's corrections `[R1.x]` (override everything; empty at v1.0)
2. `DECISIONS.md`: Stage 0 rules `[R1.0]`, with the `[R1.1]` override (brand rows and the token mapping are superseded)
3. `SKILL.md`: the edit skill `rishi-editing-style` (fixed rules, gates, scene selection)
4. `DESIGN_SYSTEM.md`: philosophy, canvas, tokens, type, layout, components, core/optional/experimental
5. `SCENE_PRINCIPLES.md`: scene types S1-S8, scene-selection table, genre recipes
6. `MOTION_LIBRARY.md`: named moves with measured cubic-beziers and Remotion helpers
7. `EDITING_PSYCHOLOGY.md`: why the style works, hook/body/CTA logic, per-beat checklist
8. `PRODUCTION_WORKFLOW.md`: pacing targets, plan-table template, build pipeline, folders, export spec
9. `SOUND_DESIGN.md`: measured cue statistics, rules for adding sound later
10. `QUALITY_CONTROL.md`: tick-box checklist before export
11. `VISUAL_REFERENCE_LIBRARY.md`: where each device is best seen in the 15 references (index, no copied frames)
12. `CHANGELOG.md`

## Status at v1.0
| item | state |
|---|---|
| Style rules (SKILL, DESIGN_SYSTEM, SCENE_PRINCIPLES, MOTION_LIBRARY, EDITING_PSYCHOLOGY) | written (Opus/Fable, Phase 4.1-4.2) |
| Formatting files (this README, CHANGELOG, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, PRODUCTION_WORKFLOW, SOUND_DESIGN) | written (Sonnet, Phase 4.3) |
| Values marked [EST] (accent hexes, badge fill, dark sheet) | confirm in the pilot edit (Phase 5) |
| Fonts Inter (variable) + Playfair Display Italic | downloaded (Google Fonts, SIL OFL) into `pilot/vid1/Vid1_Tesseract/.tesseract-work/fonts/` and `pilot/vid1/remotion/public/fonts/`; copy into `assets/fonts/` before the first production render |
| Sound | not built; `assets/sfx` is empty, `assets/music` has 1 file |
| Pilot edit of `Video Projects/Vid 1.mp4` | not started (Phase 5) |

## Evidence honesty
Rules rest on measured curves where marked [MEAS] (rmse ≤ .05) and on observation/estimate otherwise. The references' native frames were viewed for only a few reels, fonts were never confirmed, and no glow/blur/shadow/radius was measured. The pilot is where these get fixed; anything Rishi corrects becomes `[R1.x]` in `LESSONS_LEARNED.md`.

## Rights
The reference reels belong to their creators. Frames from them are for private study only: never publish them, never reuse their assets (faces, logos, thumbnails, UI captures) in Rishi's edits. Rebuild UIs as recreations; use Rishi's or licensed material.

## Install the edit skill (optional)
`SKILL.md` is the entry point. To make it available as a Claude Code skill, run in the session (the sandbox blocks writing to `.claude/skills/` directly):
```
! mkdir -p "/Users/rishi/Documents/Teaching Claude/DIff Acc/.claude/skills/rishi-editing-style" && cp "/Users/rishi/Documents/Teaching Claude/DIff Acc/Rishi's Editing Style/SKILL.md" "/Users/rishi/Documents/Teaching Claude/DIff Acc/.claude/skills/rishi-editing-style/SKILL.md"
```
The skill reads the other pack files by relative path, so keep the pack where it is or update the paths in `SKILL.md`.
