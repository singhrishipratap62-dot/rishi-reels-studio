# System Overview

## Shape of the system
Creative OS has four layers. Numbering in the folder names follows roughly this order.

| Layer | Sections | Role |
|---|---|---|
| Knowledge | 01 Design System, 03 Design Principles, 05 Reverse Engineering | What good looks like, and why |
| Memory | 04 Feedback & Learning Log | What has been tried, corrected and learned |
| Toolbox | 02 Animation Library, 07 Resources, 09 Audio, 11 Asset Library | Things you reuse |
| Production | 08 Editing Projects, 10 Workflows & SOPs, 12 Quality Control | How work gets made, checked and shipped |
| Control | 00 Start Here, 06 Management | Index, rules, upkeep |

## How the sections interact
- **A new reel starts in 10.** The workflow docs for the right style (Daniel Presley Style or Minimal Edit Style) say the steps. Those steps pull rules from **01** (tokens, type, color), **03** (scene principles, editing psychology) and **04** (`DECISIONS.md` outranks other rules).
- **Motion and sound come from 02 and 09.** `MOTION_LIBRARY.md` (in 02) names the moves; code references in `02/GitHub & Code References` show how to build them; SFX in 09 are matched to cuts using the sound-design notes.
- **Reverse engineering feeds the knowledge layer.** Breakdowns in 05 (cut statistics, pattern stills, transcripts) are the evidence behind the style docs in 01, 02, 03 and 09. The scripts that produced them are in `07/Automation Scripts/style-reverse-engineering`.
- **Finished and in-progress work lives in 08**, with notes and cue sheets. Those notes are the raw material for lessons in 04.
- **Feedback flows back.** When you correct an edit, record it in 04. Durable rules get promoted into 01/03 or the relevant skill in 07.
- **12 is the gate.** Before delivery, check the QC docs and export spec (9:16, 1080x1920, 30 fps, H.264 High, CRF 18, AAC 192k, -14 LUFS).

## Two styles, one structure
Two creator-style knowledge bases were found and kept separate to avoid collisions. Wherever both exist, files sit in sibling subfolders: `Daniel Presley Style/` and `Minimal Edit Style/`. The Gradnext brand material is kept in its own folders.

## Provenance
Every copied file is traceable through `06. Management/Master Index/MANIFEST.csv` (original path, new path, status, reason). Files with the same name but different content were kept side by side with a `__dupN` suffix; identical fonts and project SFX were stored once and logged as `deduped`.
