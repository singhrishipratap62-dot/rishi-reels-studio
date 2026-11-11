# Rishi v2 batch: vid6, vid7, vid8, vid9, vid11, vid12 (vid10 missing)

Hand-off between sessions. One reel per session; `/clear` between reels.

## Status (2026-11-11)
| Reel | Folder | Length | CTA | Intake | Options | Storyboard | Build |
|---|---|---|---|---|---|---|---|
| vid6 | `Video 6/` | 18.7 s | CLAUDE | ✓ | shared board, waiting for picks | — | — |
| vid7 | `Video 7/` | 25.6 s | CLAUDE | ✓ | " | — | — |
| vid8 | `Video 8/` | 38.1 s | CLAUDE | ✓ | " | — | — |
| vid9 | `Video 9/` | 50.0 s | EDIT | ✓ | " (trim question open) | — | — |
| vid11 | `Video 11/` | 29.6 s | CLAUDE | ✓ | " | — | — |
| vid12 | `Video 12/` | 25.8 s | EDIT | ✓ | " | — | — |

Intake per folder: `vidN.mp4` (raw, already tight: no cuts, so no SRT remap), `vidN_*.srt` (original), `roman_map.json`, `vidN_words.json`, `vidN_captions_roman.srt`, `vidN.face.json`, `vidN_matte.mp4`.

## Decisions so far (Rishi, this session)
- Shared options board for all six, then one reel at a time (storyboard → build), starting with vid6.
- Accent: different per reel. Proposals are on the board (section 11): vid6 mono+mesh · vid7 duo+ice · vid8 clay+paper.warm · vid9 jacket+mesh (ink.spot for the verdict) · vid11 blue+dots/mesh · vid12 duo+mesh.

## Open questions (on the board)
- vid6 "every other guy in **a** feed": "my feed"?
- vid11 "this vlog": "these vlogs"?
- vid9 is 50 s: keep it whole, or trim the prompts tangent (10.1–21.9 s)?
- Mishearing fixed: vid8 "claude's law" → "claude slop".

## Board
`Batch vid6-12/storyboard/options_v1/index.html` (+ `options_board.png`). Rishi pastes "Copy my picks"; turn the picks into one F-list per reel, then storyboard each reel in `Video N/storyboard/vidN_v1/`.

## Next session
1. Paste the picks → per-reel F-lists (append to the style's FEEDBACK_LOG.md).
2. `/rishi-v2` → storyboard vid6 [Opus] → stop for approval → build `Video 6/vid6_edit_v1/` [Sonnet].
