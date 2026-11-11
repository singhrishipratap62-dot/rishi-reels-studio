# V10 teardown — "This 16-year-old makes $3,000 a month editing videos" (Wade case study, 3 steps)
720x1280 @30fps, 1890 frames (#0-#1889, 63.0 s). Coordinates x%/y% and px in 1080x1920 (= src x1.5). Frame #N = N/30 s. ms = (end_f − start_f)·1000/30. Q3 fit gate, Q5 sheet timings "~", Q10 no sound named as fact, Q18 on-screen text over ASR (ASR "Axis" = on-screen "ACCESS").

## 1. Overview
- Hook: "This 16-year-old makes $3,000 a month editing videos and you won't believe how he does it." (0-4.7 s). Story of one student (Wade): joined Feb 1st → Step 1 "He got amazing at video editing" → Step 2 "He built a premium brand" (X profile, May 17th, 2 clients, first $1,600) → Step 3 "He scaled" ("Just hit $3,000 in total!") → 3-line recipe → offer closes in ~20 days → CTA comment "ACCESS". [OBS]
- Structure: HOOK #0-140 (0-4.7 s) → INTRO #141-239 (4.7-8.0 s) → STEP 1 #240-632 (8.0-21.1 s) → STEP 2 #633-1059 (21.1-35.3 s, includes Step 2 payoff) → STEP 3 #1060-1278 (35.3-42.6 s) → RECAP #1279-1530 (42.6-51 s) → OFFER/CTA #1531-1889 (51-63 s). [OBS]
- Runtime share [EST from cut list + sheets]: A-roll full frame (with small overlays) ≈ 37.5 s (60%); cream-ground graphic scenes ≈ 19.8 s (31%); split (cream pane top / A-roll bottom) ≈ 5.7 s (9%).
- Shots: 9 true hard cuts (#141, #240, #311, #472, #633 (diff 62, soft), #750, #1060, #1123 (diff 67), #1279; diffs 62-210). events.md lists 27 shots / avg 2.33 s but 17 of those "cuts" at #1174-1272 (diff 12-19, hist-chi 0.6-1.0) are a continuous 3D camera move on one post card, not edits. Real average shot ≈ 7 s; a new visual state ≈ every 2.0 s [EST].
- Distinct animations catalogued: 19 (V10-A01…A19, all in animations.json); 7 curve sets measured (13 fits ≤ .12 rmse) — the best-measured reel after V01.
- Look: teal-lit studio A-roll (plant, grey hoodie, wall #0E1117 left / lit #56555C right [MEAS f5]), cream paper ground #EBE7E1 [MEAS f200/f400] with soft grid, real UI recreations (community post, X profile, Stripe toast), one blue diamond badge, white sans + italic-serif script captions, hand-drawn red ellipse once.

## 2. Beat-by-beat timeline
| frames | time | words | screen layers back→front | anim | camera | onset (MEAS) | WHY |
|---|---|---|---|---|---|---|---|
| 0-140 | 0.00-4.67 | This 16-year-old digs $3,000 a month editing videos and you won't believe how he does it | A-roll; caption "This 16-year-old makes $3,000 a month editing videos" (script "This"); round avatar of the student with white ring (0.5-3.0 s) + "$3,000" large numeral with "per month · editing videos" (1.2-3.0 s); top caption "You won't *believe*" (3.5-4.5 s) and "how he does" bold | A01,A02,A03,A04 | static | 4.3 s (attack 522 ms) | the surprising number + a face = curiosity gap |
| 141-239 | 4.70-7.97 | Wade joined Ultimate Editors back on February 1st and got straight to work | hard cut (diff 191) → cream: community post card "Introduction — Wade Buhrman" wipes in (4.8 s); caption above "Joined *Ultimate Editors* back in **February** 1st" builds word by word (5.0-6.8 s) | A05,A06 | — | — | real post = receipt of identity |
| 240-310 | 8.00-10.33 | Step 1, he got amazing at video editing | hard cut (diff 193) A-roll: diamond "1" at centre (x 50%, y 57%), ghost "Step One" behind it, caption "He got amazing at video editing" below (y≈ 64%) | A07 | cut | 8.82, 9.2 s | chapter marker |
| 311-471 | 10.37-15.70 | He went through 30 viral animation breakdowns, the design fundamentals and the viral talking head masterclass | hard cut (diff 196) → cream: dense field of ≈ 30 course/product cards (UI snippets, posters, "Noise" product card) with one dark focus card swapping its title: "Viral Animation Breakdowns" (11-12 s) → "Editing Fundamentals" (13 s) → "Viral Talking Head" (14.2 s); the field drifts slowly | A08 | slow drift [OBS] | 12.19, 12.72 s | scale of what he studied: many tiles, one titled at a time |
| 472-632 | 15.73-21.07 | This was when he started blowing us all away with his short-form edits. Step 2, he built a premium personal brand | hard cut (diff 136): A-roll with blurred cards behind him; caption "This was when he started *blowing* us all away with his *Short-form* edits"; diamond "2" at 19.3 s "He built a premium" | A09,A07 | — | 18.72 s (attack 12 ms, centroid 4537 Hz) | pay-off line on face |
| 633-749 | 21.10-24.97 | on X, using the personal branding workflow … and on May 17th it all paid off | soft cut (diff 62, 46-f burst): X profile page ("Wade | Video Editor", Rendered Vision banner) blurs → sharp, shrinks to a card over the card field | A10 | pull-back | — | evidence of the brand |
| 750-1059 | 25.00-35.30 | He closed two clients from his viral talking head post and that was his first $1,600 | hard cut (diff 112): A-roll; "And on May 17th it all Paid off" (script "Paid off"); Stripe payout toast ("+$727.00" → "+$800.00") grows from left at 27.8 s, second toast under it ("+$800.00"); caption "He closed two clients / from his viral talking head post", "And that was his first $1,600 for video editing" | A11,A12 | — | 25.05 s (+1 f after cut), 27.82 s | money received as a bank toast |
| 1060-1122 | 35.33-37.40 | Step 3, he scaled what worked | hard cut (diff 210) → cream: wall of dark UI cards (Noise product card, posters) in perspective; diamond "3" appeared on A-roll at 33.5-35.0 s ("Step three / He scaled what worked") | A07,A08 | — | 35.97, 36.32 s | scale = repeat of the card wall |
| 1123-1278 | 37.43-42.60 | Two months later he posted this: $3,000 per month editing short form for his clients | hard cut (diff 67): "Two months later" + white post card ("Wade Buhrman · Just hit $3,000 in total!") → 3D tilt + push-in (39.0-42.5 s) with a green highlight box around "$3,000" | A13,A14 | slow push (≈ +8%) + ≈ −8° yaw [EST] | 37.5 s (+2 f after cut) | the climax artifact |
| 1279-1360 | 42.63-45.33 | If you want to make money as a video editor it's super simple | hard cut (diff 180): A-roll; "If you want to make *Money* as video editor"; "It's super *Simple*" | A15 | cut | 45.07 s | return to speaker for the lesson |
| 1361-1530 | 45.37-51.0 | first get really good… build a premium brand… service your clients | blur → split screen: cream top pane, A-roll bottom; "Get really *good*" + a carousel of 5 portrait cards (46-47.5 s); X profile card (47.5-49.5 s) "build a premium brand"; "*Service* your clients" on pure cream (50.0-51.0 s) | A16 | split ≈ 50/50 | — | recap of the 3 steps in 3 images |
| 1531-1740 | 51.0-58.0 | And if you don't know where you can learn that … Ultimate Editors 2.0. But I have to let you know… | A-roll; stacked captions; course banner ("From Beginner Editor to Viral Editing Styles & $2,000/mo in 90 days", "Ultimate Editors 2.0" tag) rises at 54.1 s | A17 | — | 52.52, 56.61, 57.7 s | name of the program + proof of product |
| 1741-1889 | 58.03-63.0 | the program closes forever in around 20 days. So comment down the word "Axis" | captions "the program closes *forever* in around **20 days**" (red ellipse on "20 days" at 59.3 s); "So comment down" + dark comments sheet rises (60.5 s) and types "ACCESS", cursor clicks send, comment posts (62.5 s) | A18,A19 | — | 58.91, 60.53, 61.18 s | urgency + literal CTA |

## 3. Animation catalogue
Format: element · trigger (word@frame → start, Δ) · frames/ms · from→to · easing (rmse) · exit · rebuild. Tracks are work/t_*.csv (src px; px@1080 = ×1.5).

**V10-A01 Student avatar pop** — circular profile photo with white ring (≈ 15% W, centre x 42%→41%, y 77% H) at chest: tracker t_avatar bw 0→109 px (0→15.1% W), bh 0→119 px (9.3% H), #15-26 (367 ms), bh bez (0.1,0.9,0.2,1.1) rmse .021 → bezier [MEAS]; bw rmse .086 named easeOutSine ≈. Peak/final 1.00. Trigger "16"@#6 → start #15 (Δ +9). Rebuild: scale 0→1 `cubic-bezier(.1,.9,.2,1.1) .37s` on a circle with 3 px white border.

**A02 "$3,000" lockup** — big bold white "$3,000" (≈ 5% H cap) with soft glow, to the right of the avatar, "per month · editing videos" in small text below: tracker t_pill (#37-48; box around lockup) bw 139→317 px (19%→44% W), cx 345→455 (right-growing: text types left→right), 367 ms, bw bez (0.5,1.4,0.9,1) rmse .014, cx rmse .016 → bezier [MEAS], peak/final 1.03/1.01. Trigger "$3,000"@#35 → start #37 (Δ +2). Exit: fades with the avatar ≈ 3.5 s [OBS]. Rebuild: clip-path inset(0 100% 0 0)→0 `cubic-bezier(.5,1.4,.9,1) .37s` (numerals revealed left→right).

**A03 Hook caption lines** — white sans ≈1.5% H cap with script words ("This", "believe"): "This 16-year-old makes $3,000 a month editing videos" builds in 3 lines (0.2-2.5 s, 1 word per ≈ 6 f [EST]), left-centre at y≈ 62%; later top caption "You won't *believe*" (top, x≈ 57-66% W centre, y≈ 5% H): tracker t_believe (#105-114) bw 137→249 px (19%→35% W), bh 45→79, centre cx 414→473 px (57.5%→65.7% W; text grows rightwards), cy ≈ 63 px (4.9% H), 300 ms, bw bez (0,0.9,0.4,1.1) rmse .036 → bezier [MEAS]; bh rmse .095 named ≈. Trigger "you"@~#100 → start #105 (Δ ≈ +5). Then "how he **does**" bold two-line caption 4.0 s.

**A04 Hook hand gesture + defocus** — A-roll defocused behind the lockup at 0.3-3.5 s (blur ≈ 8 px [EST]) and sharp by 4.0 s; no tracking.

**A05 Community post card (cream)** — hard cut #141 (diff 191): white post card ("Wade Buhrman · Introduction", paragraph, reactions) wipes in from the left: tracker t_postcard (#145-156): bw 35→645 px (5%→89.6% W), bh 21→343 px (1.6%→26.8% H), centre cx 82→281 (the bbox is clipped at the frame edge; visually the card is centred at x 50%), cy 512→650 (y 40%→51%), 367 ms; bh bez (0,0.9,0,0.9) rmse .035, cx (0.4,0.3,0,1.1) .043, bw (0.3,0.9,0,1) .050 → bezier [MEAS]; cy rmse .057 named ≈. Trigger "Wade"@#144 → start #145 (Δ +1). Exit: card stays 3.3 s then cut #240. Rebuild: clip-path/scaleX 0.05→1 + translateY with `cubic-bezier(0,.9,0,1) .37s`; card radius ≈ 2.5% W [EST].

**A06 Joined-line caption (cream)** — "Joined *Ultimate Editors* back in **February** 1st": black sans ≈1.6% H cap, script "Ultimate Editors" (navy-blue ≈ #2A5FA0 [EST]), line 1 at y≈ 36-38% H, line 2 bold below; word-by-word fade ≈ 6-8 f per word [EST]. Trigger "February"@#192 → word ≈ #195 (Δ +3).

**A07 Step diamond badge (centre)** — blue diamond (≈ 16% W, white numeral) at frame centre (x 50%, y 57% H) with a ghost outline "Step One" behind it and the title below ("He got amazing at video editing", "He built a premium", "He scaled what worked"): tracker t_diamond (#241-254): bw 13→119 px (1.8%→16.5% W), bh 14→116 px, centre (359, 731) px src = (49.9%, 57.1% H) → (539, 1097 px@1080), 433 ms; bh bez (0,0.6,0.2,0.6) rmse .019 → bezier [MEAS], bw rmse .053 → named easeOutQuart ≈. Trigger "Step"@#249 → start #241 (Δ −8). Used at #241 (Step 1), ≈ #580 (Step 2), ≈ #1025 (Step 3) [OBS]. Differs from V04/V06/V08 (lower-left badge): here centred.

**A08 Card wall (cream)** — field of ≈ 30 white/black/gradient product and course cards (posters, UI, "Noise" earbud case, "Smooth" tutorial) with soft shadows; one dark focus card (centre-left, ≈ 40% W × 8% H) whose title swaps with a blur-cross-fade ≈ 0.4 s: "Viral Animation Breakdowns" (≈ 11.5 s) → "Editing Fundamentals" (≈ 12.8 s) → "Viral Talking Head" (≈ 14.2 s) [OBS tiles]; the wall drifts ≈ 6-10 px/s and appears as the cut #311 (diff 196) hits, outer cards slightly blurred; at 35.3-37.4 s a second wall of dark UI cards in perspective (rotateY ≈ 12°, [EST]) with "Noise" case. Triggers "breakdowns"@#363 → title ≈ #345 (Δ −18), "fundamentals"@#394 → ≈ #390 (Δ −4), "viral"@~#420 → ≈ #425 (Δ +5). Onsets 12.19, 12.72 s. Rebuild: absolutely positioned cards, `transform: translate3d` slow drift, focus-card text cross-fade.

**A09 Blurred card field behind speaker** — after cut #472 (diff 136) the A-roll sits in front of the cards which slide out to both sides and blur (15.6-19.0 s; ≈ 40 px/s [EST]); captions "This was when he started *blowing* us all away with his *Short-form* edits" (script on "blowing", "Short-form"); soft cut to diamond 2 at 19.3 s. Onset 18.72 s.

**A10 X profile page → card** — at ≈ 21.0 s a full-frame X (Twitter) profile ("Wade | Video Editor", blue banner) blurs in and sharpens ≈ 0.5 s (21.0-21.5 s); then shrinks to a ≈ 80% W card centred over the card field with perspective-less drop shadow (21.5-22.3 s ≈ 0.8 s [EST]); the field cards remain visible around it; hold until 25.0 s; burst #629-674 peak 61.6 (46 f). Trigger "personal"@#627 → start ≈ #630 (Δ +3).

**A11 Stripe payout toast** — dark glass card ("Stripe · now", "Client 1 · Monthly retainer", "+$727.00" → "+$800.00" green numerals, "Succeeded" green tag) grows from the left into the centre: tracker t_stripe (#833-846): bw 116→548 px (16%→76% W), cx 154→353, bh 54→139 px (4.2%→10.9% H), 433 ms; bw bez (0,0.9,0,1) rmse .017, cx (0,0.9,0.2,1.1) rmse .019 → bezier [MEAS], bh rmse .171 EST; a second toast ("Client 2") follows ≈ 0.5 s later below it (28.5 s [OBS]); the first number counts "+$727.00 → +$800.00" (≈ 0.5 s [OBS]). Trigger "two"@#833 → start #833 (Δ 0); "clients"@#839. Onset 27.82 s (#835, attack 41 ms, centroid 2993 Hz) = +2 f. Rebuild: translateX(-100%→0) `cubic-bezier(0,.9,0,1) .43s`, glass: rgba(20,20,24,.7), blur 12 px.

**A12 Captions with sans + script + bold number** — "He closed *two* clients" (bold "clients", script "two"), "from his viral talking head post", "And that was his first **$1,600** for video editing" (bold $1,600); y≈ 62-66% H; word-by-word fade ≈ 5-6 f [EST]; the earlier "And on May 17th it all *Paid off*" (script on "Paid off").

**A13 Post card 3D push (climax)** — hard cut #1123 (diff 67); the post card "Just hit $3,000 in total!" starts flat on cream at 37.6 s (small, ≈ 55% W), then, from ≈ 38.8 s, a continuous 3D camera move: card tilts (≈ −8° yaw [EST]) and scales ≈ +45% (to ≈ 100% W, cropped) by 39.5 s and then drifts ≈ +10% more to 42.5 s (slow push) [OBS tiles 38.5-42.5 s]; background fades to a white-grey glass surface. This explains events.md's 17 low-diff "cuts" (#1174-1272, diff 12-19). Not tracked (perspective). Trigger "$3,000"@#1177 → push already under way (start ≈ #1165, Δ −12).

**A14 Green highlight box on "$3,000"** — rounded green-tinted rectangle (≈ #CFEAD9 fill, #3FB27A stroke [EST]) around "$3,000" in the post title, fades in 39.4 s (≈ 0.3 s [EST]) and stays; also a green "tag" highlight. Trigger "$3,000"@#1177 → box ≈ #1180 (Δ +3).

**A15 A-roll captions with script keyword** — "If you want to make *Money* as video editor", "It's super *Simple*": white sans ≈1.5% H cap, script on the key noun/adjective, y≈ 62% H.

**A16 Split-screen recap (cream top / A-roll bottom)** — blur-transition from A-roll at 45.4 s into a split: cream pane (top ≈ 50% H) with "Get really *good*" label and a carousel of 5 portrait cards slides in (46.0-47.5 s, ≈ 1.5 s [EST]); the pane then shows the X profile card (47.5-49.5 s), the label swaps to "Build a premium *brand*"? (not legible), and at 50.0-51.0 s pane fills the frame with "**Service** *your clients*" (black bold + script blue) before blurring into A-roll (51.0 s). Trigger "brand"@#1443 → card ≈ #1425 (Δ −18); "clients."@#1548 → text ≈ #1500 (Δ −48). Not tracked.

**A17 Course banner rise** — purple gradient banner card ("From Beginner Editor to Viral Editing Styles & $2,000/mo in 90 days", presenter photo, "Ultimate Editors 2.0" tag below): tracker t_thumb (#1623-1634) bh 232→313 px (18%→24.5% H; 348→470 px@1080), bw 469→500, 367 ms, bh bez (0,0.3,0,1.1) rmse .062 → named easeOutExpo ≈ [MEAS ≈]; the tag text types "Ultimate" → "Ultimate Editors" → "Ultimate Editors 2.0" 54.6-55.8 s [OBS]. Trigger "learn"@#1630 → start #1623 (Δ −7).

**A18 20-days red ellipse** — hand-drawn red ellipse draws around "20 days" at ≈ 59.3-59.7 s (≈ 0.4 s stroke-dashoffset [OBS tile 59.5 s]); "forever" in script; "in around" small. Trigger "20"@#1778 → ellipse ≈ #1785 (Δ +7).

**A19 Comment sheet + typed ACCESS** — dark "Comments" sheet (avatar, input, blue send) rises ≈ 60.4 s (≈ 0.5 s [EST]); text types "A" → "ACCESS" 61.0-61.5 s; cursor clicks send (62.0 s); comment posts ("you · ACCESS") and the input resets (62.5 s) [OBS]. t_comment.csv is empty (header only) → discarded. Trigger "comment"@#1805 → sheet ≈ #1815 (Δ +10); "ACCESS" ASR "Axis"@#1830 → typed ≈ #1830 (Δ 0).

## 4. Text & typography system
| style | font (conf.) | weight | cap %H | colour | use |
|---|---|---|---|---|---|
| A-roll caption | grotesque (Inter-like, med) | Regular, Bold on key word | ≈1.5 | #FFFFFF | spoken lines |
| Script word | italic high-contrast serif (low-med) | Regular italic | ≈2.0 | #FFFFFF; navy-blue ≈ #2A5FA0 [EST] on cream | This, believe, Ultimate Editors, Paid off, two, Short-form, Money, Simple, forever |
| Hook numeral | grotesque | Bold | ≈5 | #FFFFFF + glow | $3,000 |
| Step title | grotesque | Medium | ≈1.5 | #FFFFFF | under diamond |
| Cream-scene lead | grotesque | Bold | ≈2.2 | #1B1B1F [EST] | "Service your clients" |
| UI micro text | SF-like | Regular | 0.4-0.7 | grey | post cards, toasts |
Rules [INF]: script = names, outcome words and adjectives; bold = money amounts and the keyword of the line ($1,600, **20 days**, **February**); step titles sit centred under the diamond; cream scenes use dark text + navy-blue script.

## 5. Colour, light & material
- Cream ground #EBE7E1 (corner #E6E3DB) [MEAS f200/f400]; paper grid faint.
- A-roll: wall #0E1117 left / #56555C right at f5 [MEAS] (side-lit wall), teal rim on plant, hoodie grey; red/blue accents absent except diamond blue ≈ #2F80FF [EST].
- UI: white cards with soft shadow (≈ 25 px src [EST]), dark glass toasts, green numerals ≈ #3FB27A [EST], Stripe-style purple icon ≈ #635BFF [EST], red ellipse ≈ #E83A3A [EST].
- Glow radii not measured (Q12 gap); corner radii EST: post card ≈ 2.5% W, toast ≈ 4% W.

## 6. Depth & 3D
Mostly flat. Real 3D only in A13 (post card tilt ≈ −8° yaw + scale push) and in the second card wall (perspective ≈ 12° [EST]); blur-depth on card walls and behind the speaker.

## 7. Camera & transitions
| frames | type |
|---|---|
| #141, #240, #311, #472, #750, #1060, #1123, #1279 | hard cuts (diff 62-210) |
| #629-674 | soft cut X profile (46 f burst, peak 61.6) |
| #1174-1272 | continuous 3D camera move on post card (17 sub-threshold diffs) |
| #1356-1391 | blur into split screen (36 f) |
| #1531… | blur out of cream "Service your clients" |
No flashes/whips; no A-roll punch-ins measured.

## 8. Assets used
Recreated: community post cards, X profile page, Stripe toast, comment sheet, course banner, card walls (own course UI). Captured: student avatar and posts (real, study-only), Noise earbud product card. Built: diamond, ellipse.

## 9. Sound ↔ picture
| onset s (frame) | attack ms / centroid Hz | visual | Δ f |
|---|---|---|---|
| 4.3 (#129) | 522 / 2613 | cut #141 (+12 f later) | −12 |
| 8.82 / 9.2 s | 116 / 203 | diamond #241-254 settled (#254 = 8.47 s), "amazing"@#272 | +11 / +22 |
| 12.19 (#366) | 517 / 2837 | card title swap "Editing…" | in event |
| 18.72 (#562) | 12 / 4537 | card field slide-out | in event |
| 25.05 (#751) | 284 / 2343 | cut #750 | +1 (hit) |
| 27.82 (#835) | 41 / 2993 | Stripe toast #833 | +2 |
| 35.97 / 36.32 s | 35 / 435 | card wall (after cut #1060) | +24 / +35 |
| 37.5 (#1125) | 145 / 2409 | cut #1123 | +2 (hit) |
| 45.07 (#1352) | 17 / 3301 | split blur #1356 | −4 |
| 52.52 (#1576) | 406 / 1290 | before banner #1623 | −47 |
| 58.91 / 60.53 / 61.18 s | 134 / 366 / 279 | ellipse, comment sheet, typing | ≈0 |
18 strong onsets in 63.0 s (0.29/s — the sparsest); 2 of 9 cuts have an onset within 100 ms (#750 +1 f, #1123 +2 f; hit rate 0.22, median offset 61 ms); cue medians 571.5 ms long, attack 174 ms, centroid 2436 Hz, peak −2.2 dBFS [MEAS]. Short-attack onsets (≤ 45 ms: 18.72, 27.82, 35.97, 45.07 s) land on element events, long-attack ones precede or overlap transitions [OBS]. Names of sounds not verified [INF]. Music bed likely (rms p10/p50/p90 −31.1/−19.6/−12.9 dB) [EST].

## 10. Editing psychology
| condition | action | reason [INF] |
|---|---|---|
| a person's story | introduce with their real post card on cream | verifiable identity |
| each of 3 steps | A-roll + centred diamond, then a proof artifact (card wall / X page / Stripe toast / post) | speaker narrates, artifact proves |
| income | bank-notification toast with the exact amounts | specific, checkable |
| climax ($3,000) | one slow 3D push on the post, number highlighted in green | the biggest artifact gets the longest, calmest move |
| recap of the recipe | split screen with 3 images in sequence | compresses the lesson |
| CTA | red ellipse on the deadline, comment sheet typing the keyword | urgency + action |
Pacing (state changes per 10 s [EST from §2 + A-lists]): 0-10 s: 11 · 10-20 s: 8 · 20-30 s: 8 · 30-40 s: 8 · 40-50 s: 7 · 50-63 s: 8. Steady ≈ 1 per 1.2 s despite fewer cuts.

## 11. Signature moves (self-contained recipes)
1. Hook lockup: avatar pop (0.37 s, `cubic-bezier(.1,.9,.2,1.1)`, 15% W) + "$3,000" revealed left→right in 0.37 s `cubic-bezier(.5,1.4,.9,1)`.
2. Centred diamond badge: 16.5% W at (50%, 57% H), 0.43 s `cubic-bezier(0,.6,.2,.6)`, ghost "Step N" word behind, title below at y≈ 64%.
3. Card wipes in from the left edge in 0.37 s (`cubic-bezier(0,.9,0,1)`): post card 5%→90% W, bh 1.6%→26.8% H.
4. Bank toast slides in from the left to centre (0.43 s `cubic-bezier(0,.9,0,1)`, 16%→76% W), numeral counts +$727 → +$800.
5. Card wall: 30 cards, slow drift, one dark focus card whose title swaps every ≈ 1.3 s.
6. Slow 3D push on the hero post (tilt ≈ −8°, +45% scale in 0.7 s then +10% over 3 s) + green highlight on the number.
7. Red hand-drawn ellipse on the deadline; comment sheet types the keyword.
8. Silent-ish cuts: 2 of 9 cuts carry an onset ≤ 2 f; element events carry the rest.

## 12. Gaps / uncertain
- Strips viewed: 0/32 (budget); everything from 6 sheets + 8 prior CSVs + events.md; sheet-derived timings are "~"/[EST]. Q6 not met.
- Work CSVs: t_avatar, t_pill, t_believe, t_postcard, t_diamond, t_stripe, t_thumb all cited (13 fits ≤ .12 rmse); t_comment.csv empty → discarded; PNGs (f*.png) moved to work/tr/. t_postcard cx/cy are bbox centres clipped at the frame edge.
- Perspective of A13 / card wall not measured; hex of green box, highlight and Stripe purple are EST; fonts unconfirmed.
- ASR "Axis" → on-screen ACCESS; the 3D push explains events.md's 27 "shots" (only 9 real cuts).
