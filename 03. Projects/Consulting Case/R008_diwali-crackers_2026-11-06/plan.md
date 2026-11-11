# R008_diwali-crackers_2026-11-06 — board plan (approval gate)

Pack v1.4 · source: `Video Projects/video 3/IMG_4609.MOV` (4K HEVC 60 fps, 3:24) · cut: `cut.mp4` (162.8 s, 1440x2560 working res, 29.97 fps)
Times = **cut time at 1x** (s), from words.json (aligned; build syncs to the exact word). The posted final is 1.2x → every time ÷ 1.2.

## Summary
| Item | Value |
|---|---|
| Part number | **43** (spoken "This is part 43 … follow for part 44") → end card "Part 43" · "Follow for Part 44" |
| Final duration | 1x **162.8 s (2:43)** → posted 1.2x **≈ 2:16**. No pause over 0.3 s left. |
| Hook question (panel = spoken) | "How many crackers does India burst on Diwali?" |
| S1 hook | 0.00 – 2.96 (frames 0–88) |
| S2 punch-in (110 → 100 %, no caption) | 2.96 – 5.27 "This is a real BCG interview question." (frames 89–157) |
| S3 board | 5.27 – 157.6 |
| Phase switch FACTS → SOLVE | 52.80 "So, how do we estimate it?" |
| Method tabs | **Demand side · Supply side** (2 tabs). Demand = the build; Supply = the check. |
| Answer zone (replaces the ₹ number line, see ⚠ below) | Crackers bar 0 – 400 cr: **Cities 160 cr** + **Villages 200 cr** stacked → **answer 360 cr** marker (highlight) |
| S4 end card | 157.65 "This is part 43…" → "Follow for Part 44" pill at 160.88 → end ≈ 162.8 (last word end + 0.4 s) |
| Exports (R1.18) | final 1.2x + `_1x` + `_green` + `_raw`, **all 1080x1920**, + placement guide |

### ⚠ First market-sizing reel: pack grammar adapted (please confirm)
The pack's SOLVE phase is built for pricing (₹ number line with floor / ceiling / answer). This case is a **sizing** question with no price range, so:
- Tabs = the two methods spoken (Demand side / Supply side), same tab component (M10).
- Middle = the equation chips, then a **Cities table** and a **Villages table** (rows Rich / Middle / Low; columns Homes · % buy · Crackers each), filled cell by cell on the words.
- Bottom (where the ₹ line sits) = a horizontal **count bar 0–400 cr crackers**, same position and style as the number line: Cities segment lands at 115.1, Villages segment at 132.6, answer marker 360 cr with highlight strip at 136.5 (M06 + M09).
- Supply check = equation chips (₹16 × 360 cr ≈ ₹6,000 cr) + "✓ holds up".
If you'd rather keep a literal number line (markers at 160 / 200 / 360 on a 0–400 cr axis), say so. It's a one-line change in beats.js.

## Retakes / cut decisions (70 segments kept, 9 islands dropped)
| Source time | Kept | Dropped | Why |
|---|---|---|---|
| 13.7–15.6 | "The CEO asks: how many crackers will India burst this Diwali?" (15.7) | "The question is…" | abandoned start, restarts as "The CEO asks". **Please confirm** |
| 92.8 | — | 0.3 s blip ("the f…", ASR noise) | not a word; breath/noise |
| 99.5–102.1 | "About 40 crore live in cities at 4 per home" (102.8) | "about 40 crore live in cities and" | repeated line → last take |
| 131.0–133.0 | "I'd assume only about half the rich and middle homes buy" (133.6) | "I'd assume only about the…" | false start → last take |
| 137.5 | — | stretched "and…" (0.9 s) | hesitation; joins as "…middle homes buy, about 40% of the low income ones". **Please confirm** it reads fine |
| 192.3 | — | "the…" | hesitation before "the cracker market" |
| 0.5, 148.4, 181.5 | — | three breath blips | noise |
| all | pre-roll (0–2.6 s), pauses > 0.18 s | — | tightened, 10 ms audio fades at joins; S2 split at an RMS min (−71 dB) at 8.225 s |

## ASR corrections (captions use the corrected text)
| Heard | Caption | Confidence |
|---|---|---|
| "the valley", "this tibali" | Diwali | sure |
| "Anything you like to once" | anything you light once | sure |
| "full-jody stick", "a Larry" | phuljhadi stick, a ladi | likely, **please confirm spelling** (phuljhadi / ladi) |
| "are resizing" | Are we sizing | sure |
| "band crackers", "bands and apartments" | banned crackers, bans and apartments | sure |
| "Demonside", "and you supply to check" | the demand side, and use supply to check | sure |
| "share that biased cracker" | share that buy crackers | sure |
| "How's old?" | households | sure |
| "at 5 p.m" | at 5 per home | sure |
| "20-caror", "karar", "6000 crores" | 20 crore, 360 crore, 6,000 crore | sure |
| "2nd" | Second | sure |
| "Third villagers" | Third, villages | sure |
| "more of them by" | more of them buy | sure |
| "160 crackers from cities" | **160 crore crackers** from cities | **unsure: ASR heard no "crore". Please confirm**; the board shows 160 cr either way |
| "villages dhan cities" | villages than cities | sure |
| "No. the check" | Now, the check | sure |
| "16 rupees a karaka" | 16 rupees a cracker | sure |
| "Cracker Market" | the cracker market | sure |

## Hook image
`hook_cand/chakra.jpg`: "Diwali crackers - chakra.JPG", Wikimedia Commons, **Rishabh Tatiraju, CC BY-SA 3.0** (credit required; will log in 05. Asset Library/photos/CREDITS.md). Spinning chakra throwing sparks, unmistakably Diwali crackers, no logos, no people. Crop 4:3, rounded.
Rejected: "Sparkles phuljhari…" (identifiable child), "Diwali Fire crackers 1" (generic aerial burst, reads as any fireworks). Contact sheet: `hook_cand/cands.jpg`.
MBB strip `05. Asset Library/stickers/mbb_logos_trim.png`. Header (R1.17), bg loop video (R1.17).

## Beat table — FACTS (S3, 5.27 → 52.80)
| Time | Spoken | Board action | Motion |
|---|---|---|---|
| 5.34 / 6.26 | Your client is a firecracker manufacturer | Full card: label CLIENT, h1 "Firecracker manufacturer"; left: rocket/cracker line icon | M03, M04 |
| 8.96 | planning next year's production | pill "Planning next year's production" | M03 |
| 10.31 | The CEO asks | label "CEO asks" | M03 |
| 11.35 | how many crackers will India burst this Diwali? | **root box "How many crackers will India burst this Diwali?"** (card clears to tree layout); left: placeholder "? ? cr crackers" | M03 |
| 19.50 | clarifying questions | label CLARIFYING QUESTIONS | M03 |
| 22.02 / 24.82 | what counts as one cracker? → anything you light once | row Q "What counts as one?" → A "Anything lit once" | M03 |
| 27.95 / 31.37 | a phuljhadi counts as 1, so does a ladi | left: two line-icon tiles "Phuljhadi = 1", "Ladi = 1" (each on its word) | M04, M03 |
| 32.59 / 36.38 / 38.26 | All of India or one region? → all of India, only Diwali | row Q "All India or a region?" → A "All India" then "· Diwali only" appended; left: India outline icon | M03, M04 |
| 40.64 / 42.84 | Anything holding demand back? → yes | row Q "Anything holding demand back?" → A "Yes" | M03 |
| 46.15 | banned crackers | left: chip ① "Banned in some states & cities" | M03 |
| 50.54 | apartments where they can't burst them | left: chip ② "Apartments: can't burst" | M03 |

## Beat table — SOLVE (52.80 → 157.65)
| Time | Spoken | Board action | Motion |
|---|---|---|---|
| 52.80 | So, how do we estimate it? | board clears; root box moves top-centre | M08 |
| 55.37 | two ways to go about it | tab row appears (empty dots) | M03 |
| 57.60 / 60.93 | demand side… supply side | tabs "Demand side", "Supply side" on their words; count bar 0–400 cr fades in at bottom | M10, M03 |
| 64.51 | I'll build it from demand side | Demand tab active | M10 |
| 66.38 | use supply to check | small grey tag "check" under Supply tab | M03 |
| 68.97 / 70.36 / 72.66 | households × share that buy × crackers per household | equation chips "Households" × "Share that buy" × "Crackers / home" | M03 |
| 76.54 | households | "Households" chip highlighted | M10 |
| 77.94 | 140 crore people | big "140 cr people" count-up | M05 |
| 79.87–83.97 | 40 crore in cities at 4 per home → 10 crore urban households | bar 140 cr split: "Urban 40 cr ÷ 4" → chip "= 10 cr urban homes" | M06, M03 |
| 86.31–90.31 | other 100 crore rural at 5 per home → 20 crore rural households | "Rural 100 cr ÷ 5" → chip "= 20 cr rural homes" | M06, M03 |
| 92.14 / 93.79 | Second, cities | middle clears to **Cities table** (Rich / Middle / Low × Homes · % buy · Each) | M03 |
| 94.91–100.35 | split 10 crore homes: 1 cr rich, 4 cr middle, 5 cr low | Homes column fills 1 cr / 4 cr / 5 cr on each number | M03 |
| 102.20 | because of bans and apartments | small chip "Bans + apartments" beside % column header | M03 |
| 105.91 / 108.53 | half the rich and middle… 40% of low | % buy fills 50% / 50% (on "half"), 40% (on "40%") | M03 |
| 111.03–112.78 | at 100, 40 and 15 crackers each | Each column fills 100 / 40 / 15 | M03 |
| 115.11 | about 160 crore crackers from cities | table total "≈ 160 cr" count-up; **Cities 160 cr** segment grows on the count bar | M05, M06 |
| 117.25 | Third, villages | middle clears to **Villages table** | M03 |
| 118.67–123.87 | 20 crore homes: 1 cr rich, 5 cr middle, 14 cr low | Homes column 1 cr / 5 cr / 14 cr | M03 |
| 126.20–128.32 | 80%, 60% and half | % buy 80% / 60% / 50% | M03 |
| 128.81–130.17 | at 50, 30 and 10 crackers each | Each column 50 / 30 / 10 | M03 |
| 132.59 | 200 crore from villages | table total "≈ 200 cr" count-up; **Villages 200 cr** segment grows on the bar | M05, M06 |
| 136.50 | India bursts about 360 crore crackers | **answer marker "360 cr crackers"** at the bar end, highlight strip; root-box placeholder fills "≈ 360 cr" | M09, M05 |
| 141.46 | more go off in villages than cities | Villages segment outlined accent, chip "Villages > cities" | M03 |
| 143.23 | Now, the check from the supply side | Supply tab active (Demand neutral) | M10 |
| 146.74 | 16 rupees a cracker | chip "₹16 / cracker" | M03 |
| 148.73 | × 360 crore crackers | chip "× 360 cr crackers" | M03 |
| 151.07 | is about 6,000 crore | chip "≈ ₹6,000 cr" count-up | M05 |
| 154.07 | what the cracker market does in a year | chip "≈ industry's yearly sales" | M03 |
| 157.18 | So the number holds up | ✓ on the answer marker + chip "Holds up ✓" | M03 |
| 157.65 | This is part 43… | end card: "Solving real consultant cases" · "Part 43"; header fades | — |
| 160.88 | Follow for part 44 | pill "Follow for Part 44" | M03 |

## Arithmetic check ✔
- Urban: 40 cr ÷ 4 = **10 cr homes** ✔ · Rural: 100 cr ÷ 5 = **20 cr homes** ✔ · 40 + 100 = 140 cr people ✔
- Cities: 1 + 4 + 5 = 10 cr homes ✔ → buyers 0.5 + 2 + 2 = 4.5 cr → crackers 0.5×100 + 2×40 + 2×15 = 50 + 80 + 30 = **160 cr** ✔
- Villages: 1 + 5 + 14 = 20 cr homes ✔ → buyers 0.8 + 3 + 7 = 10.8 cr → crackers 0.8×50 + 3×30 + 7×10 = 40 + 90 + 70 = **200 cr** ✔
- Total 160 + 200 = **360 cr** ✔; villages 200 > cities 160 ✔
- Supply: ₹16 × 360 cr = ₹5,760 cr ≈ **₹6,000 cr** ✔

## Please confirm (reply "approved" or list changes)
1. Sizing adaptation of the board (tables + count bar instead of the ₹ floor/ceiling line).
2. Caption flags: "160 crore crackers", phuljhadi / ladi spelling, dropping "The question is…" and the stretched "and…".
3. Hook photo (chakra, CC BY-SA 3.0, credit required).
4. Board plan as above.
