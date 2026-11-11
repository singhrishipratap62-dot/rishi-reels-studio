# Daniel Priestley Editing Style — pack v1.0

Reverse-engineered from 28 Daniel Priestley YouTube videos (`raw reference videos/`), for Rishi's 16:9 YouTube and 9:16 Reels edits, set in Inter + Playfair Display and gradnext colours.

**Live demo (Claude Motion film):** https://claude.ai/artifact/BDZx9noBfRT4SdBLoHyTn1. It shows the hook title, name sting, chapter arc wipe, chip pops, whiteboard + PiP and quote card in gradnext colours.

## Read in this order
1. `LESSONS_LEARNED.md`: Rishi's corrections (override everything)
2. `DECISIONS.md`: Stage-0 rules `[R1.0]`
3. `SKILL.md`: the edit skill (`priestley-style-edit`), with gates and summaries
4. `DESIGN_SYSTEM.md`: philosophy, canvas, gradnext colour mapping, type scale, shapes, layout, components, 9:16 rules, core/optional
5. `SCENE_PRINCIPLES.md`: 20 scene types (S01–S20)
6. `MOTION_LIBRARY.md`: M01–M20 with measured timings
7. `EDITING_PSYCHOLOGY.md`: R22 beat map + function → scene framework + anti-patterns
8. `SOUND_DESIGN.md`: loudness, music bed, cue groups, listening step
9. `PRODUCTION_WORKFLOW.md`: pacing targets, structure templates, build pipeline
10. `QUALITY_CONTROL.md`: tick-box checklist
11. `VISUAL_REFERENCE_LIBRARY.md`: capture method and limits, stills, strips, per-video stats
12. `CHANGELOG.md`

## Folders
- `raw reference videos/`: the 28 source videos (private study)
- `stills/`: 16 key frames (private study, never publish)
- `.work/`: frames, contact sheets, cut logs, animation strips, audio measurements, R22 transcript
- Tools used (in workspace `tools/`): `style_extract.sh`, `style_sheets.py`, `style_strip.py`, `style_audio.py`, venv `venv-style`

## Install the edit skill
The sandbox blocks writing to `.claude/skills/`. To install it, run:
```
! mkdir -p "/Users/rishi/Documents/Teaching Claude/DIff Acc/.claude/skills/priestley-style-edit" && cp "/Users/rishi/Documents/Teaching Claude/DIff Acc/Daniel Presley Editing Style/SKILL.md" "/Users/rishi/Documents/Teaching Claude/DIff Acc/.claude/skills/priestley-style-edit/SKILL.md"
```
