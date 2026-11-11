# Motion-graphics plan: "4 nov-cld Copy" (mock case: beer client, kegs vs canning)

Status: **brainstorm, for review.** Nothing has been changed in Premiere. After sign-off, all work happens on a **new duplicate** of "4 nov-cld Copy" (for example "4 nov-cld MG"), so "4 nov-cld" (35:52) and "4 nov-cld Copy" (34:35.71) stay untouched.

**Sources**
- Captions: `inbox/4-nov-cld-copy_captions_final_v2.srt`. These are corrected, and all times below are on the copy's timeline.
- Style pack: `01. Styles/Consulting Case/` (DESIGN_SYSTEM, MOTION_LIBRARY, EDITING_PSYCHOLOGY, SCENE_PRINCIPLES, DECISIONS).
- Pack look reused: the self-building case board. White card on lavender, navy Avenir Next, every element appears on the word that says it (±2 frames), motions M01–M10.
- Daniel Priestley style (an assumption; the pack doesn't cover it): calm, premium and explanatory. Frameworks drawn step by step, one idea on screen at a time, big clean numbers, key phrases pulled out as text cards, no flashy transitions. If you have a specific reference video, share it.

---

## 1. Layout (16:9, 1920 × 1080), confirmed with Rishi
```
┌─────────────────────────────────────┬──────────────┐
│  chapter tabs                       │   KASHISH    │
│ ┌─────────────────────────────────┐ │  576 × 540   │
│ │                                 │ │  (top half)  │
│ │   CASE BOARD (white card)       │ ├──────────────┤
│ │   beat visual | issue tree      │ │   ADITYA     │
│ └─────────────────────────────────┘ │  576 × 540   │
│        caption line                 │ (bottom half)│
└─────────────────────────────────────┴──────────────┘
 x 0 ──── graphics area 70% ──── 1344 │ 1344 ─ 30% ─ 1920
```
- **Graphics area, the left 70% (x 0–1344):** chapter tabs at the top (Problem · Clarify · Structure · Kegs · Canning · Recommend · Feedback), the persistent case board (about 1260 × 820), and the caption line under the board. Captions move from Premiere's default position into this band.
- **Speaker column, the right 30% (x 1344–1920):** split horizontally. Kashish is on top (y 0–540) and Aditya on the bottom (y 540–1080).
- **Face crop:** each cell is 576 × 540, close to square, so each face needs a head-and-shoulders crop from its own camera. Check the framing before building.
- **Optional active-speaker cue:** a soft lavender glow on whoever is talking, while the other dims to about 85%. It would be driven by the transcript's speaker labels and smoothed so it doesn't flicker on short replies.
- **Background:** the gradnext lavender look. It needs a 16:9 version of `05. Asset Library/videos/gradnext-background-loop-9-16.mp4`, or the CSS gradient fallback.

## 2. Graphics toolkit
| # | Type | Used for | Motion (pack ids) |
|---|---|---|---|
| G1 | Client card: icon + label + big number | client intro, scale | M03, M05 count-up |
| G2 | Growth bars | 100K → 500K barrels | M06 |
| G3 | Split bar | 60% cans / 40% kegs | M06 |
| G4 | Two option cards, "A vs B" | kegs vs canning | M03, M04 icon draw |
| G5 | Issue tree (root question + Q pill → A pill rows) | clarifying questions, facts | M03 per row |
| G6 | Structure tree (Investment → Savings → Time/NPV) | candidate's framework | M03 + strike-through |
| G7 | Equation chips, "a × b = c" | every calculation | M03 + M05 on the result |
| G8 | Old vs New comparison table | machine specs | M03 per row |
| G9 | Paired / stacked bars | labour + wastage cost, totals | M06 |
| G10 | Persistent scoreboard: Kegs vs Canning | running result, tie, winner | M05 + highlight strip |
| G11 | Checklist with ticks | considerations, next steps | M03 per item |
| G12 | Gauge / clock | capacity, 20 h of 24 h a day | M06 fill |
| G13 | Quote card (big pulled phrase) | key feedback lines | M03, word darken (R1.6) |
| G14 | Feedback scorecard: Strengths / Work on | feedback section | M03 per row |
| G15 | Chapter title card (on the board, ~2 s) | start of each chapter | M08 clear + M03 |

## 3. Beat plan (times on "4 nov-cld Copy")
**Ch 1 · Problem (00:00 – 01:30)**
- 00:00 G15 "Mock case · Beer manufacturer", then the G1 client card: beer icon, "Craft beer · US".
- ~00:08 G2 "100K → 500K barrels in 3 years".
- 00:24 "two channels": Kegs → restaurants & bars, Cans → wine & liquor stores.
- ~00:45 "$20 million to invest": a big $20M count-up.
- 00:58 "two options": G4 cards, A "Buy kegs upfront (stop leasing)" vs B "Upgrade canning system". The root question box appears, **"Which option should get the $20M?"**, and stays for the whole case.

**Ch 2 · Clarify (01:30 – 03:40)**: the issue tree builds one row per question and answer.
- 01:50 Target? → "Best cost savings, invest now"
- ~02:20 Scale / geography? → "US · 500K barrels"
- 02:48 "value chain is pretty clear" → mini chain: Manufacture → Distribute (2 channels)
- 03:09 Channel split → G3 60% cans / 40% kegs, then 03:16 "300K barrels cans · 200K kegs"
- ~03:30 Margins? → "Not known"

**Ch 3 · Structure (03:40 – 05:05)**
- 03:44 G6 tree: Upfront investment ($20M) → Cost today vs after → Savings over time → NPV
- 04:24 Kashish drops NPV, so the NPV node greys out with a strike-through and "Cost savings only" lights up.

**Ch 4 · Option A, Kegs (05:05 – 10:55)**
- 05:56 "200K barrels × 2 kegs = 400K kegs"
- 06:16–06:28 "400K × $10/yr = **$4M a year** lease"
- 06:51 "$20M ÷ 400K = **$50 per keg**"
- 07:09 useful life → "10 years" chip; 07:21 exit costs → "ignore"
- ~07:45–09:30 G11 checklist: quality · storage/upkeep · damage & loss · depreciation · exit value
- 08:51 → "Replace 5% a year = $1M"
- 10:17 "$4M − $1M = **$3M/yr saved**"
- 10:40 "$3M × 10 − $20M = **$10M**" → **Scoreboard: Kegs $10M**

**Ch 5 · Option B, Canning (10:55 – 20:55)**
- 11:26–11:35 "300K barrels × 14 cases = **4.2M cases**"
- 11:54–12:30 G8 Old vs New, one row at a time: operators 4 / 4 · rate 600 / 1,200 cases per hour · wastage 10% / 7% · cost $10M / $20M
- 12:55–13:07 "Salvage $1.3M → net investment **$18.7M**"
- 14:04–17:30: the wastage/labour back-and-forth, partly confusing. Keep the board quiet (table only), with at most a "540 vs 1,116 cases/hr" chip. **Rishi to decide whether this stretch needs graphics at all.**
- 17:34–17:39 chips: "Labour $25/hr · Waste $20/case"
- 17:55–18:55 G9 labour: 7,000 hrs → $175K × 4 operators = **$700K** vs 3,500 hrs → **$350K**
- 19:27–19:38 G9 wastage: 420K × $20 = **$8.4M** vs **$5.9M**
- 19:58–20:14 totals **$9.1M vs $6.25M → $2.85M a year saved**
- 20:32 "$28.5M − $18.5M ≈ **$10M**" → **Scoreboard: Canning $10M**. A "Tie" highlight lands on "exactly the same".

**Ch 6 · Recommendation (20:55 – 25:03)**
- 21:15 G11 next-step chips: Operational feasibility · Risks · Scenario analysis
- 22:04 "Is demand growing?" → ~22:40 Kashish's answer: the G2 growth chart comes back (100K → 500K)
- 23:34 G12 gauge: "7,000 hrs ÷ 365 ≈ **20 h of 24 h** → near capacity"
- ~24:00 risk: "Wastage 10% → 7% = $2.8M a year" sensitivity bar
- ~24:20–25:00 verdict card **"Recommend: Upgrade canning"**, with pros (capacity for growth, $2.85M/yr) vs kegs (safer, predictable). The scoreboard winner gets a highlight strip.

**Ch 7 · Feedback (25:03 – 34:35)**: the board becomes a G14 scorecard with two columns.
- 25:03 G15 "Interviewer feedback"
- Strengths (25:10–26:40): "Analytical thinking" and "Business insight", with example ticks: exit costs · depreciation & storage · salvage of the old machine · capacity insight
- 27:01 G13 quote: **"Did the interviewer enjoy speaking to you?"**
- Work on (27:27–32:30), one row each:
  - 28:01 Bring your personality into the opening
  - ~28:20 Clarifying questions: stay on cost
  - 28:44 Make the first structure comprehensive (operations + risks)
  - 30:08 Communication: record yourself
  - 30:43 **Lead the case: always propose the next step** (G13 quote)
  - 31:52 Use the case's data, not assumptions
- ~32:20 summary card: **1 Communication · 2 Approach · 3 Personality**
- 33:21–34:35 framing demo, G13 script card: "To be comprehensive, I'd like to look at operational capabilities next. Does that sound good?"

## 4. Where NOT to add graphics
- Filler and back-and-forth ("Sure.", "Got it.", "Correct.") and the 14:04–17:30 stretch: keep the current board state with nothing new.
- At most one new element every ~1.5 s, nothing decorative, nothing over the speaker cells (EDITING_PSYCHOLOGY anti-patterns).
- No punch-ins or zooms on the speakers (M12).

## 5. Will it look good? Risks
- **Density:** about 70 beats in 34 min, roughly one every 30 s, which reads as calm, not busy. The persistent board, tabs and scoreboard keep the screen alive between beats.
- **Face crops:** they must hold up in the 576 × 540 cells. Check both camera framings first.
- **Numbers:** must pass an arithmetic check against the case (the corrections CSV is done; recheck $87.5K and $350K).

## 6. Open decisions for Rishi
1. **Build route:** (a) render the board as a transparent overlay video with the reel engine (HTML + Playwright, `01. Styles/Consulting Case/engine/`) and import it into Premiere on the new copy (recommended, because it reuses the pack), or (b) build in Premiere with MOGRTs.
2. **Scope:** start with a pilot chapter (suggest Ch 4 · Kegs, ~6 min) to judge the look, or do the whole case?
3. **Extras:** keep the chapter tabs and the active-speaker glow?
4. **Daniel Priestley:** link to a specific reference video, if any.
5. **The 14:04–17:30 stretch:** graphics or quiet?

## 7. Next steps after sign-off
1. Duplicate "4 nov-cld Copy" → "4 nov-cld MG". All motion-graphics work happens only there.
2. Re-layout the speakers into the 30% column (Kashish top, Aditya bottom) and move the captions under the board.
3. Pilot one chapter → review → roll out.

## Verification (build phase)
- Every element appears within ±2 frames of its word (check against `4-nov-cld-copy_transcript_words.json`).
- Arithmetic table: kegs $10M, canning ≈ $10M, labour/wastage totals.
- Review stills at the start of each chapter: captions and board never overlap the speaker cells.
- "4 nov-cld" and "4 nov-cld Copy" stay untouched.
