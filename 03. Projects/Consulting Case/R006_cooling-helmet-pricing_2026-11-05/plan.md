# R006_cooling-helmet-pricing_2026-11-05 — board plan (approval gate)

Pack v1.0 · source: `Video Projects/Video 1/IMG_4598.MOV` + `IMG_4599.MOV` · cut: `cut.mp4` (160.8 s, 1440x2560 working res, 29.97 fps)
Times below are **cut time** (seconds). Word times are whisper-base and will be snapped to audio onsets (±2 frames) in the build.

## Summary
| Item | Value |
|---|---|
| Part number | **41** (spoken: "This is part 41 … follow for part 42") → end card "Part 41" · "Follow for Part 42" |
| Final duration | **≈ 160.8 s (2:41)**. That's about a minute longer than R1/R2 (1:41–1:44), because the script is longer, not because of pauses. No pause over 0.3 s remains. |
| Hook question (panel text = spoken) | "How do you price a helmet that keeps your head 10 degrees cooler?" |
| S1 hook | 0.00 – 3.86 |
| S2 punch-in (1.3x, no caption) | 3.86 – 6.00 "This is a real BCG interview question." |
| S3 board | 6.00 – 155.7 (board empty 6.00–6.32, then builds) |
| Phase switch FACTS → SOLVE | 61.34 "So, how do we price it?" |
| Method tabs | Cost · Competition · Value (Competition greyed out at 69.98 "out") |
| Number line | ₹0 – ₹20,000 linear. Markers: ₹1,000 regular helmet (grey) · ₹1,500 **floor** · ₹4,000 **answer** (highlight) · ₹18,000 **ceiling** |
| S4 end card | 155.78 "This is part 41…" → "Follow for Part 42" pill at 159.40 "follow" → end 160.8 |

## Retakes / cut decisions
| Source | Kept | Dropped | Why |
|---|---|---|---|
| IMG_4598 0:02–2:09 | Hook → "…just to feel cooler." | "She said it." (0:38.8) · "She said it's" (1:01.9) | false starts, restarted right after |
| IMG_4598 1:44 | "So each one costs us about 1500 rupees." | "…so each one costs us." (1:44.1–1:46.0) | fragment, repeated in full |
| IMG_4598 2:09–2:46 | — | "So who really cares … 80,000 the helmets" | **re-recorded in full in IMG_4599** → keep last take |
| IMG_4599 0:02–1:06 | "So who really cares…" → "Follow for part 42." | "follow for part… 40/14" (1:03.0–1:04.3) | flubbed number, clean retake follows |
| Both | — | pre-roll (0–2.4 s), post-roll, all pauses > 0.18 s | tightened to ~0.16 s, 10 ms audio fades at joins |

## ASR corrections (caption text = corrected)
| Heard | Caption | Confidence |
|---|---|---|
| "patent is spending" | patent is pending | sure |
| "slow down on log of" | slow down or log off | sure |
| "worth 80,000" (take 1) / "18,000" (take 2) | ₹18,000 (6,000 × 3) | sure |
| "and hence the problem" | and here's the problem | sure |
| "make an R&D cost" | make, and R&D cost | sure |
| "2500KKKK" | ₹2,500 | sure |
| "sell him. Straight" | sell straight | sure |
| "A regular? Riders stands" | A regular rider stands | sure |
| "Did I ask / That I asked" | Then I asked | likely, **please confirm** |
| "I asked clarification questions" | **? please confirm**: "I asked clarifying questions" or "I'd ask clarifying questions" | unsure |
| "If we price our helmet let's hit double" | **? please confirm**: "If we price our helmet at, let's say, double" | unsure |
| "cover about lakhs of riders" | **? please confirm**: "lakhs of riders" vs "a lakh riders" | unsure |
| Numbers shown as ₹ with Indian grouping | ₹1,000 · ₹1,200 · ₹30 cr · ₹6 cr · 2 lakh · ₹300 · ₹1,500 · ₹3,000 · ₹6,000 · ₹18,000 · ₹4,000 · ₹2,500 | — |

## Arithmetic check ✔
- Cost: ₹30 cr ÷ 5 yrs = **₹6 cr/yr**; ÷ 2,00,000 helmets = **₹300/helmet**; + ₹1,200 to make = **₹1,500 floor** ✔
- "Double our cost" = 2 × ₹1,500 = **₹3,000** ✔ (= 3x the ₹1,000 regular helmet)
- Value: 2 extra deliveries/day × 100 hot days = **200 orders**; × ₹30 = **₹6,000 / rider / summer**; × 3 summers = **₹18,000 ceiling** ✔
- Price ₹4,000: company gets ₹18,000 ÷ ₹4,000 = **4.5x** ("more than 4 times") ✔; our margin ₹4,000 − ₹1,500 = **₹2,500** ✔
- Order on number line: ₹1,000 < ₹1,500 floor < ₹4,000 answer < ₹18,000 ceiling ✔

## Assets
| Asset | Plan | Status |
|---|---|---|
| Hook photo | Literal object: a two-wheeler helmet (ideally on a rider in daylight). Candidates (Unsplash Licence: free commercial use, no attribution needed): [person wearing helmet holding motorcycle](https://unsplash.com/photos/person-wearing-helmet-while-holding-motorcycle-pFq73TQlpvo) · [black and blue helmet](https://unsplash.com/photos/black-and-blue-helmet-on-black-surface-btHOXvYX3H0). Crop 4:3, rounded. | **needs your OK to download** (I'll check it visually first, record source + licence in `assets/CREDITS.md`) |
| MBB strip | `assets/` has no logo files. Option A: you drop McKinsey/BCG/Bain logo PNGs (the ones used in R1/R2) into `05. Asset Library/stickers/`. Option B: I typeset the three wordmarks in navy Avenir Next. | **your call** |
| Icons | Drawn as stroke SVGs in board style (2.5–3 px navy, light-accent fill): helmet, snowflake, thermometer, weight, battery, shop, delivery scooter, sun, rider | I make them |
| Font | Avenir Next (system) | ✔ installed |

## Beat table
Zones: **FULL** = full card (before root box) · **L** = left beat visual · **R** = right tree · **TOP** = root box / tabs · **MID** = working area · **NL** = ₹ number line.
Motion: M03 fade/rise · M04 icon draw · M05 count-up · M06 bar grow · M07 unit grid · M08 board clear · M09 marker · M10 tab.

| # | Time | Spoken line (corrected) | Board action (zone · component · exact text) | Motion | Notes |
|---|---|---|---|---|---|
| — | 0.00 | How do you price a helmet that keeps your head 10 degrees cooler? | S1 hook panel: header "Solving real consultant cases · Part 41 · gradnext", helmet photo, question text, MBB strip | — | face full-bleed below; caption word-by-word |
| — | 3.86 | This is a real BCG interview question. | S2 punch-in 1.3x, no graphics, no caption | M11 hard cuts | |
| 1 | 6.32 | Your client is a helmet company | FULL · label "CLIENT" + "Helmet company" (6.92 "helmet") + helmet line icon | M03, M04 | board empty 6.00–6.32 |
| 2 | 9.01 | that has invented a two-wheeler helmet with built-in cooling. | FULL · pill "Two-wheeler helmet" (9.01) · pill "Built-in cooling" + snowflake icon (10.46) | M03, M04 | |
| 3 | 11.92 | On a 45 degree afternoon, the rider feels like it's 35. | FULL · thermometer "45°C" (11.92) → arrow → "Feels like 35°C" (15.34), chip "−10°" | M05 (count 27→45), M03 | comparison A → B |
| 4 | 16.20 | The marketing director asks, | FULL · label "MARKETING DIRECTOR" | M03 | |
| 5 | 18.10 | "How do we price this?" | R · root box "How do we price this?" (on "How"); card switches to two columns, FULL visuals move/fade to L | M03 | root wording fixed from here |
| 6 | 19.32 | This is how you'd solve it, consultant style. | — (filler, no board change) | — | |
| 7 | 22.45 | Before jumping to a number, I asked clarifying questions, | R · label "CLARIFYING QUESTIONS" (24.34 "clarifying") | M03 | wording pending your confirm |
| 8 | 26.08 | such as: what is the objective of our client? | R · Q pill "Objective?" (26.83 "What") | M03 | |
| 9 | 28.85 | She said to make as much profit as possible over the next five years. | R · A pill "Max profit · 5 yrs" (30.10 "profit") · L · years bar 1→5 (32.04 "five") | M03, M06 | |
| 10 | 32.90 | Is there anything like it in the market already existing? | R · Q pill "Anything similar?" (32.90) · L · "? ? ?" placeholder box | M03 | |
| 11 | 36.56 | She said no, it is completely new and the patent is pending. | R · A pill "Nothing · patent pending" (37.08 "no") · L · placeholder → "0 competitors" (37.08), stamp "PATENT PENDING" (39.09) | M03 | |
| 12 | 40.34 | Then I asked: does it have any downside? Is it heavier, or does it need charging, or anything like that? | R · Q pill "Downsides?" (42.73 "downside") · L · weight icon + "?" (43.72 "heavier"), battery icon + "?" (45.64 "charging") | M03, M04 | |
| 13 | 47.72 | She said it charges overnight like a phone and weighs the same as a normal helmet. | R · A pill "Charges overnight · same weight" (48.21) · L · battery "?"→"✓ overnight" (48.70), weight "?"→"✓ same" (50.34) | M03 | |
| 14 | 52.66 | A regular helmet sells for about 1000 rupees, | R · fact row "Regular helmet" → "₹1,000" · L · big "₹1,000" | M03, M05 | |
| 15 | 55.93 | the new one costs 1200 rupees to make, | R · fact row "Cost to make" → "₹1,200" · L · big "₹1,200" | M03, M05 | |
| 16 | 59.54 | and R&D cost of 30 crore. | R · fact row "R&D" → "₹30 cr" · L · big "₹30 cr" | M03, M05 | tree now: root + 3 Q/A + 3 facts |
| 17 | 61.34 | So, how do we price it? | **SOLVE**: board clears; root box moves top-centre | M08 | phase switch |
| 18 | 62.63 | There are three approaches that we can take: first is cost, second is competition, and third is value. | TOP · tabs appear one by one: "Cost" (65.61) · "Competition" (66.67) · "Value" (68.42) · NL · empty ₹ axis 0–20,000 fades in with "Cost" | M03, M10 | |
| 19 | 69.10 | Competition is out because nothing like this exists in the market. | TOP · "Competition" tab greys + strike (69.98 "out") | M10 | |
| 20 | 73.28 | First is the cost. | TOP · "Cost" tab active | M10 | |
| 21 | 74.84 | Spread over 5 years, the 30 crore of R&D is 6 crore a year. | MID · chip "R&D ₹30 cr ÷ 5 yrs" (75.74) → "= ₹6 cr / yr" (78.28) | M03, M05 | |
| 22 | 79.70 | If we sell 2 lakh helmets a year, that's 300 rupees a helmet. | MID · chip "÷ 2 lakh helmets / yr" (80.31) → "= ₹300 / helmet" (82.43) | M03, M05 | |
| 23 | 84.46 | So each one costs us about 1500 rupees. | MID · stacked bar "Make ₹1,200" + "R&D ₹300" = "₹1,500" (85.99) | M06, M05 | |
| 24 | 87.65 | That's our floor. | NL · marker "Floor ₹1,500" (88.13 "floor") | M09 | |
| 25 | 88.71 | The second is the value. | TOP · "Value" tab active (89.54); MID clears | M10 | |
| 26 | 90.17 | And here's the problem. | — | — | |
| 27 | 91.19 | A regular rider stands in a shop next to a 1000 rupee helmet. | MID · shop icon (93.24 "shop") + helmet tag "₹1,000" (94.14) · NL · grey marker "Regular ₹1,000" (94.14) | M04, M09 | |
| 28 | 96.16 | If we price our helmet at, let's say, double, which is about 3000 rupees, of our cost, | MID · second tag "Ours ₹3,000" (99.41), "vs" between, chip "3x" | M03, M05 | wording pending your confirm |
| 29 | 101.22 | he might not purchase it just to feel cooler. | MID · "✗" over "₹3,000" (101.98 "purchase") | M03 | |
| 30 | 104.20 | So who really cares about a cool head in the summer? | MID clears; "?" placeholder (104.54 "who") | M03 | |
| 31 | 107.86 | Food delivery companies. | MID · delivery-scooter icon + "Food delivery companies" | M04 | |
| 32 | 109.16 | Their riders slow down or log off in the afternoon heat. | MID · sun icon + chips "slow down" (110.11) / "log off" (110.98) | M04, M03 | |
| 33 | 113.15 | In a pilot, she said riders with the new helmet did two extra deliveries a day | MID · label "PILOT" (113.64) · chip "+2 deliveries / day" (117.01) | M03 | |
| 34 | 118.50 | across about 100 hot days, | MID · chip "× 100 hot days" (119.25) | M03 | |
| 35 | 120.34 | and the company earns about 30 rupees per order. | MID · chip "× ₹30 / order" (121.96) | M03 | |
| 36 | 123.60 | That's 200 extra orders, or 6000 rupees per rider every summer. | MID · "= 200 orders" (124.11) → "= ₹6,000 / rider / summer" (125.99) | M05 | |
| 37 | 129.22 | The helmet lasts three summers, so it's worth 18,000 rupees to a company. | MID · 3-step summers bar (130.98 "three") → "₹6,000 × 3 = ₹18,000" (132.38) | M06, M05 | |
| 38 | 134.52 | That's our ceiling. | NL · marker "Ceiling ₹18,000" (135.21); floor–ceiling range fills light accent | M09 | |
| 39 | 136.04 | So I'd skip the shop shelf altogether | MID · shop icon with strike (137.08 "shop") | M03 | |
| 40 | 138.57 | and sell straight to delivery companies at around 4000 rupees a helmet. | MID · chip "Sell B2B → delivery companies" (on "delivery") · NL · answer marker "₹4,000" + highlight strip (on "4,000") | M03, M09 | word times here are bunched by ASR; will snap to audio onsets |
| 41 | 143.94 | The company gets back more than 4 times what it pays, | MID · "Pays ₹4,000 → gets ₹18,000" · chip "4.5x" (146.22 "four") | M03, M05 | |
| 42 | 148.10 | and we make about 2500 on every helmet, | MID · stacked bar "Cost ₹1,500" + "Margin ₹2,500" = "₹4,000" (149.82) | M06 | |
| 43 | 152.42 | and one contract can cover lakhs of riders. | MID · unit grid of rider squares (154.42 "lakhs") + label "1 contract → lakhs of riders" | M07 | wording pending your confirm |
| — | 155.78 | This is part 41 of solving real consulting cases. Follow for part 42. | S4 end card: "gradnext" · "Solving real consultant cases" · pill "Part 41" · pill "Follow for Part 42" (159.40 "follow") | M03 | end 160.8 = last word + ~0.4 s, no black |

Captions: corrected text above, one line, 2–7 words per phrase, broken at commas/clauses, word-by-word rise-in (M01), hard phrase changes (M02). No caption in S2.
