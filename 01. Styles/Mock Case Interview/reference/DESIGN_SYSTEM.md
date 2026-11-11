# DESIGN_SYSTEM — mock case 16:9 motion graphics (v1.0)
Visual language inherited from `01. Styles/Consulting Case/reference/DESIGN_SYSTEM.md` (white board card, lavender, navy Avenir Next, word-synced builds), re-laid out for 16:9 two-speaker long-form. Taste reference: `09. Archive/Unused Styles/Daniel Presley Editing Style/` (Daniel Priestley: calm, premium, one idea at a time — guidance, not a layout) [M22]. Implementation: `../engine/board_beer_case.py` (hard-coded to the beer case; copy to the project as `board.py` and adapt). Read from SKILL.md at steps 8–9 and for any visual change.

## Layout (1920×1080, 29.97 fps) [M17]
| Zone | Pixels |
|---|---|
| Graphics area (left 70 %) | x 0–1344 |
| Chapter tabs | y 44–82, from x 40 |
| Board card | x 40–1312, y 100–900, radius 12, soft shadow |
| Caption band (kept free) | y 910–1070 under the board |
| Speaker column (right 30 %) | x 1344–1920, bg #E9ECFD |
| Interviewer card | x 1360, y 16, 544×516, radius 10, label at (+16, +456) |
| Candidate card | x 1360, y 548, 544×516, radius 10, label at (+16, +456) |
Inside the card: header "Mock case interview · <client>" (grey 19 Medium) left, "gradnext" (Demi 26) right [logo file pending]; left column x 88–668 = current beat visual; right column x 716–1268 = root question box + case facts / clarifying-questions rows; bottom strip y ~750–870 = scoreboard.

## Tokens
- Navy text #2C3552, ink #2B2F3A, grey #8A8FA0, accent #5670FC, light accent #E3E6FD / #EEF0FE, highlight #FFECC4, alert red #D65C5C / #FDE4E4.
- Background: diagonal near-white → lavender gradient + 36 px dot grid (#CDD2F5).
- Font: Avenir Next (.ttc faces 0 Bold, 2 Demi, 5 Medium, 7 Regular). No "→" glyph — write it out [L18].
- **Corner radii [M19]: card 12 · boxes/chips/cells 8 · pills/tabs/name labels 6 · bars 4 · speaker cards 10.** Never pill-round.

## Components (G-ids from the plan)
G1 client card (label + big title + line icon) · G2 growth bars · G3 split bar · G4 option cards (A/B square badge) · G5 facts/questions rows (Q pill light-accent → A pill white with accent outline) · G6 approach list with strike-through + "Skip X" pill · G7 equation chips (result chip = highlight fill, larger) · G8 Old vs New table (header cells: old light, new accent) · G9 cost table · G10 scoreboard (A vs B, "?" until solved, count-up, "Tie" / "Recommended" tags) · G11 checklist (square ticks) · G12 capacity bar · G13 quote card (highlight fill, accent left rule, small uppercase kicker) · G14 feedback scorecard (Strengths with sub-rows | Work on numbered chips, key point highlighted) · chapter tabs (active = accent fill).

## Motion (from `01. Styles/Consulting Case/reference/MOTION_LIBRARY.md`)
- In: opacity 0→1 + rise 8 px, 220 ms ease-out (cubic), on the word's start time.
- Bars / strike: grow left→right 500 ms. Big numbers: count from 60 % to the value over 450 ms.
- Beat visual replaced: previous group fades out 250 ms as the new one starts. Persistent: root question, facts rows, scoreboard (until the feedback chapter), tabs.
- Feedback chapter clears the whole card and builds the scorecard.
- Renderer only writes frames that change (≈1,000 unique frames for 34 min) + an ffmpeg concat list.

## Beat grammar (how to plan from the transcript)
1. Problem: client, scale, channels, budget, the two options → root question box on "which one".
2. Clarify: one Q/A row per clarifying question (Q on the question, A on the answer); left side shows the answer's visual (value chain, split bar, big numbers).
3. Structure: candidate's approach as numbered chips; interviewer redirects → strike + pill.
4. Each option: its maths as equation chips in spoken order; considerations as a checklist; the result lands on the scoreboard.
5. Recommendation: next steps checklist, the deciding facts (demand, capacity bar, risk), verdict line + "Recommended" tag.
6. Feedback: Strengths (with the interviewer's examples), Work on (numbered), quote cards for the big lines.
Quiet zones: confusing back-and-forth and filler stay on the current board state.
