# Organization Rules

How to decide where a new file goes. The rule of thumb: **file by what it is for, not by which project it came from.**

## Decision order
1. **Is it a live project file** (footage, project files, render in progress)? Keep it in the workspace (`inbox/`, `projects/<REEL_ID>/`, `exports/`). Only bring it here when finished, as a lightweight copy in `08`.
2. **Is it a rule, principle or taste decision?** `01` for brand/system, `03` for principles. Corrections go to `04`.
3. **Is it reusable code, a motion or a template?** `02` (components, code references) or `07` (skills, scripts, plugins).
4. **Is it audio?** `09`. Fonts, logos, images, backgrounds go to `11`.
5. **Is it a how-to or checklist?** `10` for process, `12` for quality bars and specs.
6. **Is it evidence from studying someone else's work?** `05`.
7. **Is it about the system itself?** `06`.

## Routing table for common new items
| New item | Destination |
|---|---|
| Creator breakdown, pattern stills | `05/Creator References` or `Animation Breakdowns` |
| New style doc set | New `<Style Name>/` subfolder inside each relevant category, mirroring the existing two styles |
| User correction | `04/User Feedback`, then promote durable rules to `Corrections & Improvements` |
| New Claude skill or plugin | `07/AI Tools, Skills & Automation/Claude Skills` or `07/Plugins` |
| New script | `07/AI Tools, Skills & Automation/Automation Scripts/<topic>/` |
| Reusable Remotion/GSAP/Lottie component | `02/Motion Components/<type>` |
| SFX or music | `09/Sound Effects`, `09/Background Music` |
| Export spec or platform rule | `12/Export Specifications`, `12/Platform Requirements` |
| Finished render | `08/Completed Projects` |

## Naming
- Reel IDs: `R###_topic_YYYY-MM-DD` (from workspace `CLAUDE.md`).
- Keep original filenames. If two files share a name but differ, keep both: put each in a source-named subfolder, or suffix `__dupN`. Never overwrite.
- Style-specific files go in a subfolder named for the style so two styles never collide.

## What not to put here
- Secrets, `.env` files, API keys, tokens.
- Environments and caches (`node_modules`, venvs, `.git`, uv caches, model weights).
- Large media over about 100 MB. Record its path in the manifest instead.
- Scratch and generated files (`.tesseract-work`, `.DS_Store`, extracted frames).

## Duplicates
- Store identical fonts and SFX once. Note other locations in the manifest.
- A deliberate second copy (for discoverability) must say so in the manifest `notes` column.

## Always record
Every addition gets one `MANIFEST.csv` row (original path, new path, type, category, status, reason, notes) and, if important, a line in `MASTER_INDEX.md`.
