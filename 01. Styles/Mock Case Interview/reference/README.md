# Mock case interview edit — pack index
Built from the 4 Nov 2026 mock case (beer client, kegs vs canning; Kashish × Aditya). **`SKILL.md` (pack root) is the only mandatory read**; everything here is read on demand (see its "Read only when…" table).

| File | What |
|---|---|
| ../SKILL.md | Workflow with STOPs, all hard rules, compiled lessons, engine usage |
| ../FEEDBACK_LOG.md | Rishi's raw notes during a reel (folded into SKILL/reference on approval) |
| WORKFLOW.md | Long-form step list with exact MCP parameters and the ffmpeg composite command |
| DESIGN_SYSTEM.md | 16:9 70/30 layout in pixels, colour tokens, radii, components G1–G14, motion, beat grammar |
| SOUND_DESIGN.md | SFX trigger map + level offset |
| ../history/ | DECISIONS (M1–M23), LESSONS_LEARNED (L1–L23), SKILL v1.0, RULE_AUDIT (where every rule went), CHANGELOG |
| ../engine/ | silence_plan.py · timeline_map.py · transcribe.sh · transcript.py · fix_words.py · captions.py · speakers.py · board_beer_case.py (board renderer + beer-case beats; copy per case) · sfx_mg.py · case.example.json · corrections.beer-case.json |
| ../sfx48/ | SFX library (48 kHz WAV + peak info) |

## Reference project (first edit)
- Project folder: `03. Projects/Mock Case Interview/R_mock_4nov_MG/` (board.py, words.json, events, renders, SFX stem, cue sheet).
- Case media folder (`inbox_folder`): `03. Projects/Mock Case Interview/mock case, 4th November/` (motion_graphics_plan.md, kashish.srt).
- Transcripts/captions from that edit: `03. Projects/Mock Case Interview/Transcripts (4 Nov)/` (formerly in the old inbox; new runs write to the `inbox_folder`).
- Sequences produced in Premiere: "4 nov-cld" (silence-cut) → "4 nov-cld Copy" (self-assessment removed + captions) → "4 nov-cld MG" (motion graphics V6 + SFX A3).

## Open items (decide next time / ask if it matters)
- Caption placement/style (default bottom-centre can touch the candidate card; Rishi will decide).
- gradnext logo: the board header currently uses typeset "gradnext"; Rishi may supply the correct logo file (or use "Gradnext logo - Blue (2).png" from the project).
- Active-speaker glow on the speaker cards (not built yet).
