# R011_motorcycle-growth_2026-11-10 — board plan (approval gate)

Pack v1.4, pack engine (board.html + Playwright + ffmpeg). **Cut = Rishi's Premiere "Sequence 01"** (47 clips, read via MCP → `edl.json`, rendered by cut.py from the 4K sources) · `cut.mp4` **190.76 s**, 1440x2560, 29.97 fps.
Board design = R010's (same case), re-anchored to this cut's words. Times below are **cut time at 1x**; the posted final is 1.2x (divide by 1.2).

## Summary
| Item | Value |
|---|---|
| Part number | **45** (spoken). End card "Part 45" · "Follow for Part 46" |
| Duration | 1x **190.8 s (3:11)** → posted 1.2x **≈ 2:39** |
| Hook question (panel = spoken) | "How would you grow a motorcycle brand that's about to shut down?" |
| S1 hook | 0.00 – 3.57 (frames 0–107) |
| S2 punch-in (110 → 100 %, no caption) | 3.57 – 5.67 "This is a real BCG interview question." |
| S3 board | 5.67 – 185.44 |
| Phase switch FACTS → SOLVE | **62.50 "So how do we grow it?"** (the 17.94 "how do we grow it?" is the CEO's question = root box) |
| Method tabs | ① Fans 82.51 · ② Trials 105.98 · ③ Fix the bike 139.93 · ④ Accessories 158.97; at 173.06 "start with the first two" ① ② on, ③ ④ neutral |
| Number line | Sales bar 0–6,000 bikes/mo: Today 2,000 → +1,000 (① at 103.87) → +1,000 (② at 137.77); target "3x · capacity" 6,000; unlabelled ghost 4,000→6,000 at 173.06 |
| S4 end card | 185.44 "This is part 45…"; "Follow for Part 46" at 189.11 |
| Exports | final 1.2x + `_1x` + `_green` + `_raw` (all 1080x1920) + placement guide + sound cue sheet, in exports/ only (Premiere hand-off dropped; Sequence 01 untouched) |

## Cut: Rishi's Premiere edit, kept as-is
Every join was checked by transcribing the cut audio. All clean, no surviving retakes:
"…buying from us? She said customers think that…" · "…take a test ride, one in five end up buying" · "how do we grow it? We need to 3x" · "…5 more bikes a month this way, that's about 1,000…" · "…Why don't people buy? Because it's heavy, it breaks down. So fix exactly…" · "…again. This is part 45 of…"

Differences from R010 (both your choices in Premiere):
1. **"She said"** is now kept before "customers think…" (captioned).
2. "Why don't people buy" uses the **4621 take**, so **"the gear is on the opposite side" is gone**. The ③ board drops the "Gear on the wrong side" ✗ chip (now just ✗ Heavy · ✗ Breaks down).

⚠ **Tail:** the last word ("46.") ends at ~190.54 and the cut ends at 190.60, so the tail is only ~0.06–0.2 s, against the pack's ~0.4 s [R1.0 / QC]. Unless you say no, I'll extend the last clip's out-point by +0.3 s (source 6.13 → 6.43, which is silence in IMG_4622) and re-render the cut (~9 min). Sequence 01 itself won't be touched.

## ASR corrections (captions use the corrected text, same as R010)
"YokLind" → "Your client" · "solve it a consultant style" → "solve it, consultant style" · "I asked few clarification questions" → "I asked a few clarifying questions" (**light grammar; say if you want verbatim**) · "customer thinks… heavy, old, fashion" → "customers think… heavy, old-fashioned" · "the bikes, thump" → "the bike's thump" · "eat selling" → "each selling" · "1 & 5" → "1 in 5" · "ansof" → "Ansoff" · "two few" → "too few" · "Goa Manali and Lay" → "Goa, Manali and Leh" · "those step test drives" → "doorstep test drives" (**please confirm**) · "full strides" → "first rides" · "keep the thumb" → "keep the thump" · "need new factory or new product" → "need a new factory or a new product" (light grammar) · "add accessory" → "add accessories".

## Arithmetic check
200 dealers × 10 = **2,000/mo** ✓ (= "selling only 2,000") · capacity 6,000 = **3x** ✓ · ① 200 × 5 = **+1,000** ✓ · ② 5,000 extra first rides ÷ 5 = **+1,000** ✓ · after ①+② = 4,000; ③/④ unquantified → ghost segment, no claim.

## Hook image
`hook.jpg` = R010's: Royal Enfield Himalayan in Ladakh, Gopal Vijayaraghavan via Wikimedia Commons, **CC BY 3.0**, number plate blurred (logged in 05. Asset Library/photos/CREDITS.md). MBB strip `05. Asset Library/stickers/mbb_logos_trim.png`. Header (R1.17), bg loop video (R1.17).

## Beat table — FACTS (S3 5.67 → 62.50)
| Time | Spoken | Board action | Motion |
|---|---|---|---|
| 5.7 | Your client is a 100-year-old motorcycle company | lbl CLIENT, h1 "Motorcycle maker", pill "100 years old"; left: motorcycle line icon | M03, M04 |
| ~10 | factory can make 6,000 bikes a month | pill "Factory · 6,000 / mo"; left bar Capacity 6,000 grows | M06 |
| ~12 | selling only 2,000 | pill "Selling · 2,000 / mo"; bar Selling ⅓ | M06 |
| ~15 | thinking about shutting it down | stamp "SHUT DOWN?" | pop |
| 17.94 | CEO asks: how do we grow it? | root box "How do we grow it?"; left "2,000 / 6,000 bikes a month" | M03 |
| ~25 | a few clarifying questions | lbl CLARIFYING QUESTIONS; left "? ? ?" | M03 |
| ~27–37 | Why aren't people buying? → heavy, old-fashioned, unreliable; Japanese cheaper, better mileage | row "Why not buying? → Heavy · dated · unreliable"; left ✗ chips on each word + "vs Japanese commuters: Cheaper · Better mileage" | M03 |
| ~38–46 | who still buys? → loyal fans, older men, thump, history | row "Who still buys? → Loyal fans · older men"; left ❤ The thump / ❤ The history | M03 |
| ~47–54 | how do we sell? → 200 dealers × 10 | row "How do we sell? → 200 dealers × 10 / mo"; left count-up 200 × 10 = 2,000 / mo | M05 |
| ~55–59 | test ride → 1 in 5 buy | row "Test ride → 1 in 5 buy"; left 5 dots, one lights on "buying" | grid |
| ~60 | very few people ever take one | row "Problem → Very few test rides"; chip "But very few take one" (dark) | M03 |

## Beat table — SOLVE (62.50 → 185.44)
| Time | Spoken | Board action | Motion |
|---|---|---|---|
| 62.50 | So how do we grow it? | board clears; root box moves top-centre | M08 |
| 64.55 | We need to 3x our sales | sales bar: Today 2,000 + target 6,000 "3x · capacity" | M06, M09 |
| 66.67 → ~78 | 4 ways… same/same, same/new, new/same, new/new | Ansoff 2×2 axes; cells ①–④ fill on each phrase | M03 |
| 80.88 | the Ansoff matrix | pill "Ansoff matrix" | M03 |
| 82.51 | First: same bike, same customers | tabs appear, ① on; matrix → mini-matrix | M10, M08 |
| ~85–104 | fans → channel; group ride; buyer → free service; 200 × 5 | chips; "= +1,000 / mo" + bar 2,000→3,000 at 103.87 | M03, M06 |
| 105.98 | Second: same bike, new customers | tab ② | M10 |
| ~108–138 | riders love it ✓ / too few ✗ / more first rides / rentals Goa·Manali·Leh / doorstep test drives / 5,000 ÷ 5 | chips each on its word; "= +1,000 / mo" + bar 3,000→4,000 at 137.77 | M03, M06 |
| 139.93 | Third: new products, same customers | tab ③ | M10 |
| ~143–158 | heavy · breaks down · fix reliability · lighter · keep thump/shape/history · legacy | ✗ Heavy, ✗ Breaks down; ✓ Fix reliability, ✓ Lighter version; Keep: thump · shape · history; "Don't lose the legacy" (dark) | M03 |
| 158.97 | Fourth: new products, new customers | tab ④ | M10 |
| ~162–172 | jackets, helmets, saddlebags, custom parts · dealers + online · every bike on the road | 4 chips on their words; sub; dark chip | M03 |
| 173.06 | start with the first two… | ① ② on; "Start: ① + ② · no new factory or product" (dark); "③ in parallel", "④ once growing again"; ghost bar to 6,000 | M10 |
| 185.44 | This is part 45… | end card (header fades) | — |

Captions: auto (≤4 words, ≤680 px), one line, rise-in, none in S2. Sound: SFX on board animations only (sfx.py), −15 LUFS, music 13 dB under voice on the 1.2x final.
