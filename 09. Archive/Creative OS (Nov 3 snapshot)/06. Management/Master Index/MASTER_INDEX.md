# Master Index

Most important resources, by purpose. Paths are relative to `Creative OS/`. Search this file (Cmd-F or grep) for a keyword such as `sfx`, `caption`, `gradnext`, `tokens`, `feedback`.

Status key: **copied** = in Creative OS. **path-only** = not copied; original path is in `MANIFEST.csv`.

## Rules that outrank everything else
- `04. Feedback & Learning Log/Corrections & Improvements/Daniel Presley Style/DECISIONS.md` (copied)
- `06. Management/Organization Rules/Reels Studio Workspace/CLAUDE.md` (copied; reference copy of workspace rules, default export spec)

## Style knowledge bases
Each is split by topic; both exist under `Daniel Presley Style/` and `Minimal Edit Style/` in the folders named.
| Topic | Folder | File |
|---|---|---|
| Overview | `06/System Documentation/<style>/` | `README.md` |
| Style skill | `07/AI Tools, Skills & Automation/Claude Skills/<style>/` | `SKILL.md` (Daniel also has `reverse engineer style SKILL.md`) |
| Design system | `01/Brand Guidelines/<style>/` | `DESIGN_SYSTEM.md` |
| Visual references | `01/Design References/<style>/` | `VISUAL_REFERENCE_LIBRARY.md` |
| Editing psychology | `03/Creative Intelligence/Design Reasoning/<style>/` | `EDITING_PSYCHOLOGY.md` |
| Scene principles | `03/Storytelling & Visual Communication/<style>/` | `SCENE_PRINCIPLES.md` / `TEN_SCENE_PRINCIPLES.md` |
| Motion library | `02/Animation Styles/<style>/` | `MOTION_LIBRARY.md` |
| Sound design | `09/Sound Design References/<style>/` | `SOUND_DESIGN.md` |
| Production workflow | `10/Video Production/<style>/` | `PRODUCTION_WORKFLOW.md` |
| Quality control | `12/Visual Quality/<style>/` | `QUALITY_CONTROL.md` |
| Lessons | `04/Synthesized Learnings/<style>/` | `LESSONS_LEARNED.md` |
| Change log | `04/Claude Iterations/<style>/` | `CHANGELOG.md` |

## Gradnext brand
- Design system (tokens.css, tokens.json, design-system.json, components, fonts): `01/Brand Guidelines/Gradnext Design System/` (copied)
- Wordmark and Besley font: `01/Logos & Identity/Gradnext _brand-build/` (copied)
- Reel plugin and skill, motion production guide, build template: `07/Plugins/Gradnext Motion Explainer Plugin/` (copied)
- User feedback log: `04/User Feedback/Gradnext FEEDBACK_LOG.md` (copied)
- Background loop 9:16: `11/Backgrounds/` (copied)

## Reusable code and components
- Remotion skill and example scenes/components: `02/GitHub & Code References/animation-skills/remotion/`
- GSAP, text-to-lottie, three.js skills: `.../animation-skills/gsap|text-to-lottie|threejs/`
- Gradnext reel build script: plugin `skills/gradnext-motion-explainer-instagram/templates/build_reel.py`

## Claude skills and automation
- Reel pipeline skills (rough cut, captions, export, Premiere handoff): `07/.../Claude Skills/Reels Studio Skills/`
- Tesseract design/editor/motion/video and Impeccable: `07/.../Claude Skills/Tesseract and Impeccable Skills/`
- Reverse-engineering scripts: `07/.../Automation Scripts/style-reverse-engineering/` (`style_extract.sh`, `style_sheets.py`, `style_strip.py`, `style_audio.py`)
- Launcher: `07/.../Automation Scripts/start-claude.sh`

## Reverse engineering evidence
- Daniel Presley pattern stills P01 to P16: `05/Creator References/Daniel Presley Style/stills/`
- Daniel Presley per-video cut data, contact sheets, transcripts, audio analysis: `05/Animation Breakdowns/Daniel Presley Style/work-data/`
- 28 raw reference videos: **path-only**, `Daniel Presley Editing Style/raw reference videos/`
- Minimal style stills and contact sheets: `05/Creator References/Minimal Edit Style/references/`

## Audio
- 22 SFX: `09/Sound Effects/Minimal Edit Style/`
- Project SFX libraries (deduped): `09/Sound Effects/Project Libraries/`

## Projects
- Finished reels R003 to R005: `08/Completed Projects/`
- Gradnext reels 003 to 006: `08/Motion Graphics Projects/IG Gradnext Reels/`
- Minimal edits: `08/Video Editing/Minimal Edit Style Projects/` (first-principles, R017, R018, series-intro)
- Podcast experiment: `08/Video Editing/Experimental Podcast/` (video is **path-only**)
- Announcement stills: `08/Image Editing/30 Days of Consulting Announcement/`
- Large `.tsrct` files and `Versions/` renders: **path-only** (see `MANIFEST.csv`)

## Provenance
- `MANIFEST.csv` (this folder): every file, with original path, new path, status, reason.

## Design system exports (added 2026-11-05)
Extracted from the zips in `01. Design System/` (zips kept). All **copied/added**, not path-only. Each has `README.md`, `tokens.json`, `components/`.
| Brand / style | Folder | What it adds |
|---|---|---|
| Gradnext (full) | `01/Brand Guidelines/Design System Exports/gradnext-shared/` | Superset of the original Gradnext design system. Includes the logos, motifs, imagery, industry-primer PDFs, presentations and thumbnails that `Gradnext Design System/NOTE.txt` says were missing. **Prefer this one for Gradnext assets.** |
| Gradnext (subset) | `01/Brand Guidelines/Design System Exports/gradnext/` | Same tokens and components, no logo/imagery/primer assets. Kept for completeness. |
| @rishi.docx | `01/Brand Guidelines/Design System Exports/rishi-docx/` | Brand book for the AI-explainer account: taste rules, motion references, pacing, talking-head layout, stickers, icons |
| Kashish Malhotra reel | `01/Brand Guidelines/Design System Exports/kashish-malhotra-reel/` | House style for talking-head reels: Avenir fonts, RisingCaption and Cover components |
| Minimal Editorial | `01/Brand Guidelines/Design System Exports/minimal-editorial/` | Tokens, ten scene components and scenes/motion/sound/QC/workflow docs for the Minimal Edit Style |
