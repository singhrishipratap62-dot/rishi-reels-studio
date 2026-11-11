# How Claude Should Use Creative OS

This file applies to work done with Creative OS. It does not replace or edit the workspace `CLAUDE.md` or any Claude Code settings; where they overlap, the workspace `CLAUDE.md` wins.

## Before starting any editing or design task
1. Read `06. Management/Master Index/MASTER_INDEX.md` to find the relevant style and resources.
2. Read `04. Feedback & Learning Log/Corrections & Improvements/Daniel Presley Style/DECISIONS.md`. Its rules outrank estimates in the other docs.
3. Pick the style being asked for (Daniel Presley Style, Minimal Edit Style, or Gradnext brand) and read that style's files in this order: `SKILL.md` (07/Claude Skills), `DESIGN_SYSTEM.md` (01), `EDITING_PSYCHOLOGY.md` and scene principles (03), `MOTION_LIBRARY.md` (02), `SOUND_DESIGN.md` (09), `PRODUCTION_WORKFLOW.md` (10), `QUALITY_CONTROL.md` (12), `LESSONS_LEARNED.md` (04).
4. For Gradnext work, also read the plugin skill, `MOTION_PRODUCTION.md` and `FEEDBACK_LOG.md` (07/Plugins, 04/User Feedback) and the tokens in `01/Brand Guidelines/Gradnext Design System/`.
5. Look at similar past projects in `08. Editing Projects` (NOTES.md, sound_cue_sheet.md, edit plans) before planning.

## Common tasks
| Task | Do this |
|---|---|
| Recreate a creator's style | Read `05. Reverse Engineering` (pattern stills, cut stats, transcripts) and the `reverse engineer style SKILL.md`; scripts are in `07/Automation Scripts/style-reverse-engineering` |
| Reuse an animation or component | Search `02. Animation Library/GitHub & Code References` and the Gradnext plugin templates |
| Pick sound effects | `09/Sound Effects` and the style's `SOUND_DESIGN.md`; match SFX to cuts as in the cue sheets |
| Export or deliver | `12` docs and the export spec; use the `reel-export` skill |
| Recommend resources | Cite the file path from the index and say whether it is copied or path-only |

## Rules when working with this system
- **Treat it as a reference library, not live project state.** Real work happens in the workspace folders (`inbox/`, `projects/<REEL_ID>/`, `exports/`). Do not edit files in Creative OS to change a live project.
- **Check status before relying on a file.** Anything in `MANIFEST.csv` marked `path-only` is not in Creative OS; open it from its original path and say so.
- **Do not assume identical filenames are identical files.** Look for `__dupN` suffixes and the `Daniel Presley Style/` vs `Minimal Edit Style/` split.
- **Do not copy or expose secrets.** No `.env`, keys or config were copied; keep it that way.
- **Never delete or overwrite** anything here without being asked. Add; do not replace.

## Learning from feedback
When the user corrects an edit or states a preference:
1. Add a dated entry to `04. Feedback & Learning Log/User Feedback/` (what was asked, what was wrong, the fix).
2. If the correction is durable, add it to the relevant `LESSONS_LEARNED.md` or `DECISIONS.md` and add an index line to `MASTER_INDEX.md`.
3. Never silently change a rule; say which rule changed and why.

## When something is missing
Folders marked as empty carry a `_README.md` pointer. If nothing relevant exists, say so and ask rather than guessing a style or brand decision.
