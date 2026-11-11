# Content Inventory

What was found in the Reels Studio workspace on 2026-11-03 (about 12 GB, 59,000 files) and where it went. File-level detail is in `06. Management/Master Index/MANIFEST.csv`.

## Found and copied

| Source in workspace | What it is | Now in |
|---|---|---|
| `Daniel Presley Editing Style/` (13 docs, `stills/`, `.work/`) | Reverse-engineered editing-style knowledge base: design system, psychology, scene principles, motion, sound, workflow, QC, lessons, decisions | Split by topic into 01, 02, 03, 04, 06, 07, 09, 10, 12 under `Daniel Presley Style/`; stills and extracted data in 05 |
| `Minimal Edit Style/` (docs, `references/`, `sfx/`) | Minimal Editorial style knowledge base, 22 SFX | Same mapping under `Minimal Edit Style/`; SFX in 09 |
| `Minimal Edit Style/edits/` (4 projects) | Tesseract edits: first-principles, R017, R018, series intro | `08/Video Editing/Minimal Edit Style Projects/` (notes, cue sheets, transcripts, JSON, small previews) |
| `Minimal Edit Style/Experimental Podcast/` | Podcast-to-reels skill, clip plans, SRT | `08/Video Editing/Experimental Podcast/` |
| `IG Grad Next Motion Explainer/gradnext-design-system/` | Gradnext tokens, components, fonts, brand README | `01/Brand Guidelines/Gradnext Design System/` (whole) |
| `IG Grad Next .../_brand-build/` | Wordmark and Besley font build | `01/Logos & Identity/Gradnext _brand-build/` |
| `IG Grad Next .../Gradnext motion explainer instagram-v2/` | Plugin: skill, motion production guide, feedback log, build template | `07/Plugins/` (feedback log also in `04/User Feedback/`) |
| `IG Grad Next .../Video Projects/` (003 to 006) | Gradnext reel projects | `08/Motion Graphics Projects/IG Gradnext Reels/` (lightweight) |
| `exports/` | Three finished reels (R003 to R005) | `08/Completed Projects/` |
| `30 Days of Consulting Series Announcement/` | Finished stills and HTML build source | `08/Image Editing/` |
| `skills/animation-skills/` | Remotion, GSAP, text-to-lottie, three.js skill repos | `02/GitHub & Code References/animation-skills/` |
| `.claude/skills/` (4) and `.claude-home/skills/` (5) | Reel skills; Tesseract and Impeccable skills | `07/AI Tools, Skills & Automation/Claude Skills/` |
| `tools/style_*.py`, `style_extract.sh`, `start-claude.sh` | Reverse-engineering and launcher scripts | `07/.../Automation Scripts/` |
| `CLAUDE.md`, `TASK- ...txt` | Workspace rules (reference copy), build spec | `06/Organization Rules/`, `06/System Documentation/` |

## Recorded by path only (not copied)
- 28 raw reference videos (about 4.5 GB), the podcast video (855 MB), `Mental Maths/IMG_4176.MOV` (520 MB).
- All `.tsrct` project files, `Versions/` folders, videos over 20 MB inside projects, and `source_clip.mov` files.
- Two large GIFs in the Remotion repo.
- 73 items in total; each row in the manifest has status `path-only`.

## Skipped on purpose
- `tools/venv-style`, `.uv-cache`, `.uv-python`, `uv-tools`, `models/ggml-base.bin` (about 2.1 GB of regenerable environment).
- `.mcp.json`, `.claude/settings.json`, `.claude/settings.local.json` (configuration).
- `.tesseract-work/` scratch and generated JSON (notes, cue sheets and SFX libraries inside it were copied).
- Extracted frame JPGs (about 10,000) under `Daniel Presley Editing Style/.work/*/frames/`.
- `.DS_Store`, empty sandbox `.claude` stubs, `node_modules`, `.git`.

## Not present in the workspace
`assets/` (fonts, luts, music, sfx, stickers), `inbox/` and `projects/` were empty. No LUTs, music library, prompt history, icon set or illustration set existed.

## Needs a human look
- The Daniel Presley docs spell the creator's name two ways ("Presley" in the folder and "Priestley" in `DECISIONS.md`).
- The Gradnext design system `NOTE.txt` says logo, imagery and PDF assets could not be downloaded from the source; those folders hold only READMEs.
- R018 and Gradnext 006 appear to be in progress (no export in `exports/`). R017, first-principles and series-intro have no export there either; whether they are finished is unknown.

## Update 2026-11-05
- Five design-system zips were added to `01. Design System/` after the build (not from the workspace) and are now extracted under `Brand Guidelines/Design System Exports/` and listed in `MANIFEST.csv` (status `added`).
- This resolves the missing Gradnext logo, imagery and industry-primer assets noted above: they are in `Design System Exports/gradnext-shared/assets/`. The original `Gradnext Design System/` folder was left unchanged.
