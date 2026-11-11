# Creative OS

Creative OS is a single place that holds the creative knowledge, references, reusable code, workflows and finished work behind your reels and motion graphics. It was built on 2026-11-03 by **copying** relevant material out of the Reels Studio workspace. The originals were not moved, renamed or changed.

## Who it is for
You, and Claude Code. Claude reads it before starting an edit, so it can reuse what already exists and follow your documented preferences instead of starting from scratch.

## How to navigate
1. Read `SYSTEM_OVERVIEW.md` for how the 13 sections fit together.
2. Use `FOLDER_INDEX.md` to find what belongs where.
3. Use `06. Management/Master Index/MASTER_INDEX.md` to jump to the most important resources.
4. Use `MANIFEST.csv` (same folder) to trace any file back to its original location.
5. Claude should start with `CREATIVE_OS_CLAUDE_INSTRUCTIONS.md`.

## Where things are, in one line each
| Need | Go to |
|---|---|
| Brand, fonts, tokens, style design systems | `01. Design System` |
| Motion styles, code references (Remotion, GSAP, Lottie, three.js) | `02. Animation Library` |
| Why a style works (psychology, scene principles) | `03. Design Principles` |
| What you corrected, what was learned | `04. Feedback & Learning Log` |
| Creator breakdowns, stills, extracted cut data | `05. Reverse Engineering` |
| Rules for filing and maintaining this system | `06. Management` |
| Claude skills, plugins, scripts | `07. Resources` |
| Edit projects and exported reels | `08. Editing Projects` |
| SFX and sound-design notes | `09. Audio & Sound Design Library` |
| How a reel gets produced | `10. Production Workflows & SOPs` |
| Fonts, backgrounds, logos | `11. Asset Library` |
| Quality bars and export specs | `12. Quality Control & Standards` |

## Important limits
- **Large media was not copied.** The 28 raw reference videos (about 4.5 GB), the podcast and Mental Maths source footage, large `.tsrct` project files and large renders are listed in `MANIFEST.csv` with status `path-only` and their original path. Open them from the original location.
- **Environment folders were not copied** (Python venv, uv caches, the whisper model). See `06. Management/Maintenance/MAINTENANCE.md` for how to get them back.
- **Config files were not copied** (`.mcp.json`, `.claude/settings*.json`). The existing `CLAUDE.md` was copied for reference only and is unchanged in the workspace root.
- Folders with no existing material contain a short `_README.md` saying so and pointing to the nearest related content.
- Nothing here is "live": editing a copy does not change the original, and the reverse.
