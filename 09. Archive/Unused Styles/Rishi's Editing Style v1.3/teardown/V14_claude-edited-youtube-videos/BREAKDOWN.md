# V14 teardown — "My last five YouTube videos were edited by Claude: is video editing dead?" (video engineering vs development)
720x1280 @30fps, 1976 frames (#0-#1975, 65.9 s). Coordinates x%/y% and px in 1080x1920 (= src x1.5). Frame #N = N/30 s. ms = (end_f − start_f)·1000/30. Q3 fit gate, Q5 sheet timings "~", Q10 no sound named as fact, Q18 on-screen text over ASR.

## 1. Overview
- Hook: "My last five YouTube videos have been completely edited by Claude. They all cost less, took less time and got better viewer engagement. So does this mean that video editing is officially dead?" (0-10 s). Argument: editing = software (two phases: "video engineering" = branding + full plan, "video development" = turning the plan into an edit); the creator's 8 years of experience made Claude's edits good; by 2027 editors get paid to train and guide AI. Offer: free tutorial "master AI video editing in 30 days"; CTA: comment "Guide". [OBS]
- Structure: HOOK #0-231 (0-7.7 s) → QUESTION #232-307 (7.7-10.3 s) → PHASE 1 #308-740 (10.3-24.7 s) → SKILL #741-960 (24.7-32 s) → PHASE 2 #961-1172 (32-39.1 s) → EXPERIENCE #1173-1465 (39.1-48.8 s) → FUTURE #1466-1742 (48.9-58 s) → CTA #1743-1975 (58-65.9 s). [OBS]
- Runtime share [EST from the measured pane timings + cut list]: A-roll full frame (with small overlays) ≈ 34 s (52%); split screen (blue pane top, A-roll bottom) ≈ 15.5 s (23.5%); full-frame blue graphic/text scenes ≈ 16.4 s (24.5%). No cream ground.
- Shots: only 4 hard cuts (#232, #308, #741, #1173; diffs 85-126); the other scene changes are the measured pane slides (6 of them: enter ×3, expand ×2, exit ×1) → 5 shot changes by cut + 6 pane moves in 65.9 s; avg hard-cut shot 13.17 s; a new visual state ≈ every 2.3 s [EST].
- Distinct animations catalogued: 17 in the catalogue (V14-A01…A17); animations.json lists 20 entries because the 6 measured pane moves are split per move (enter ×3, expand ×2, exit ×1); 8 curve sets [MEAS] (6 pane moves from split.txt + doc morph with 3 props + 1 ≈).
- Look: dark A-roll (wall #040D18 / #152233, black tee #14171D [MEAS f10]) — the darkest reel so far; saturated blue ground #4279BD → #205AA4 (mean (59,133,209) [MEAS f270]); white UI cards; Claude orange asterisk tile; white sans with script words; no red ellipse, no cream.

## 2. Beat-by-beat timeline
| frames | time | words | screen layers back→front | anim | camera | onset (MEAS) | WHY |
|---|---|---|---|---|---|---|---|
| 0-231 | 0.00-7.70 | My last five YouTube videos have been completely edited by Claude. They all cost less, took less time, got better engagement | A-roll; a row of UI cards (mind-map "Alex", profile/name list) slides left at the top behind the head (0-3.5 s); caption "My last *Five* YouTube videos have been completely edited by **Claude**"; white tile with orange asterisk (Claude) at lower-centre (2.5-3.5 s); then icon tiles "$" (3.9 s), hourglass (5.4 s), chart (6.9 s) appear one by one under captions "They all **cost** *less*", "they took *less time* to edit", "And even got **better** viewer *Engagement*" | A01,A02,A03 | static | 1.02, 1.65, 1.81, 2.9, 4.53, 4.69, 6.55 s | the claim is shocking; icons list its 3 benefits |
| 232-307 | 7.73-10.23 | So does this mean that video editing is officially dead? | hard cut (diff 97) → full blue: single centred words swap every ≈ 0.5 s: "So does" / "that" / "editing" / "is" / "officially" / "*dead?*" (script, 9.8 s) | A04 | cut | — | the question as a drum-roll of single words |
| 308-740 | 10.27-24.67 | Here's the truth. Editing a video is a lot like building software. Two phases: video engineering … a full plan | hard cut (diff 100): A-roll "Here's the *Truth*" (10.5 s), defocus; pane slides in from the top (11.1-12.1 s, A05); caption "Editing a video is like *building* software" (top pane); two white cards "Video Engineering" / "Video Development" (14.0-15.0 s); pane expands to cover almost the whole frame (14.8-15.7 s, A06); one card "Video Engineering" (orange glow base) 15.5-16.7 s → morphs to a wide doc "Full video script" (17.0-17.5 s, A07) with a vertical connector and two rows "✦ Use a one-object animation" [thumbnail] / "✦ Use a two-object animation" [dark thumbnail] (20-24 s, A08) | A05,A06,A07,A08 | pane + expand | 10.01, 13.14, 14.09, 14.81, 19.97, 21.57, 23.15 s | the abstract "engineering" is shown as a planning document |
| 741-960 | 24.70-32.00 | This is a skill video editors build by watching and learning thousands of pieces of content and a deep understanding of how good edits are put together | hard cut (diff 126): A-roll defocused→sharp (24.5-25 s); a strip of reel cards ("Learn Something", "Book/Habit" brain poster, hourglass "Animations" cards, portrait reels) at the top behind the head, scrolling left ≈ 1 card per 1.5 s (25.0-31.5 s); captions "This is a *skill*", "that video editors *build*", "By watching and learning **thousands** of pieces of *Content*", "And a *deep* understanding", "Of how **good** edits are put *Together*" | A09,A02 | static | 26.49, 29.0, 31.6 s | the card strip = "thousands of pieces of content" |
| 961-1172 | 32.00-39.10 | The second phase, let's call it video development … take that full video plan and turn it into a polished edit using your software and skills | "The second **phase**" (A-roll defocus 32.0 s); pane slides in from the top (32.0-33.0 s, A05) with a "Video Development" card (white, orange footprints glow); pane expands (34.6-35.4 s, A06), card blurs out; doc "Full video script" re-appears with the 2 rows (36-37.5 s); a portrait card ("$2,000/MO" presenter) rises (37.5-38.5 s); Pr and Ae icons stack above (38.5 s) | A05,A06,A08,A10 | pane + expand | — (no onsets 32.9-39.1 s except 31.6 s) | repeats the doc so the plan → edit link is visual |
| 1173-1465 | 39.10-48.83 | Now when I trained Claude to edit those YouTube videos, I still had to use my eight years of editing experience… If I didn't, I would have gotten something more like this | hard cut (diff 85): A-roll; captions "Now when I trained **Claude** to edit those YouTube videos"; carousel strip lower (41.5-46.5 s: video card, white page card, blue "Video" card with ‹ › buttons); big "**8 years**" (≈ 4.6% H cap, 42.5 s) + "My 8 years of editing *Experience*"; "To get it to look this *Good*"; "If I didn't, I would have gotten…"; "Something more like *This*" + a white "You find out about a recession…" card (bad-edit sample, 46.5-47.5 s) | A11,A12 | static | 43.93, 47.18, 48.83 s | experience as the differentiator, shown with a failed-edit sample |
| 1466-1712 | 48.88-57.07 | Video editing is changing, and in 2027 you're no longer gonna get paid to turn raw boring videos into pretty ones. You're gonna get paid to train and guide AI on how it can edit content that can perform well | A-roll "Video editing is *Changing*" (48.0-49.5 s, defocus); pane slides from the top (48.9-50.0 s, A05); raw presenter card ("raw, boring") → arrow → white card "pretty ones" (60-30-10 rule thumbnail) (50.5-53 s, A13); Claude tile + "You're going to get paid *to train AI on how to edit*" (53.5-57 s, A14); pane retracts upward (57.1-58.1 s, A15) | A05,A13,A14,A15 | pane | 53.89, 54.45, 56.26, 57.0 s | the future of the job as an image transformation |
| 1743-1975 | 58.10-65.90 | So if you're a video editor that's never even touched AI, here's a full tutorial on how you can master AI video editing in 30 days. Comment down the word guide | A-roll defocus→sharp (58.1 s); captions "That can actually perform *Well*", "So if you're a video **editor** that's **never** even touched *AI*"; YouTube card "$4,000/mo — How I Would Learn AI Video Editing if I Could Start Over! (30 Day Plan)" rises (60.5 s, A16); "In just **30**"; comment bar types "guide", cursor click (65.0-65.5 s, A17) | A16,A17 | — | 60.0, 61.67, 63.44, 64.9, 65.25 s | tutorial + CTA |

## 3. Animation catalogue
Format: element · trigger (word@frame → start, Δ) · frames/ms · from→to · easing (rmse) · exit · rebuild. Pane curves come from work/split.txt (per-frame boundary y of the pane's lower edge, src px), fitted via ease_fit.py; the doc morph and others from track.py (work/tr/).

**V14-A01 Hook caption + top card strip** — white sans ≈1.5% H cap with script ("Five", bold "Claude"), centred at y≈ 62-66% H; behind the head at the top (y≈ 0-22% H) a row of UI windows (mind-map "Alex" pill, name/profile lists, a presenter card) slides left ≈ 0.7 s per card for 0-3.5 s then leaves [OBS]; same UI as V06/V07 mind-maps (re-used footage of the creator's earlier graphics). Trigger "five"@#11 → "Five" ≈ #14 (Δ +3).

**A02 Caption system (sans + script + bold)** — as V06-V13: script on nouns/qualifiers (Five, "Engagement", "dead?", "Truth", "building", "skill", "Content", "deep", "Together", "Experience", "This", "Changing", "Well", "AI", "Guide"); bold on verbs and numbers (**cost**, **better**, **Claude**, **8 years**, **never**, **thousands**, **good**); y≈ 62-66% H in A-roll scenes, y≈ 52% H (centre) in full-blue scenes, top (y≈ 11% H) in the pane. Word-by-word fade ≈ 5 f [EST].

**A03 Benefit icon tiles ($, hourglass, chart)** — white rounded-square tiles (≈ 10% W, blue glyph) in a row at (x 50%, y 77% H) appearing one by one: Claude asterisk tile (2.5 s), "$" (3.9 s, #116 "cost"), hourglass (5.4 s, #155 "time"), chart (6.9 s, #208 "engagement" start; the chart tile is grey until the word lands) [OBS]. Tracker g3_hourglass (#160-195): bw 79→158 px (11%→21.9% W incl. neighbour), 1167 ms, rmse .12-.157 → family only [EST]; g1/g2 trackers: no change ≥ 15% (tile pops within the tracked ref) → discarded. Triggers: "cost"@#116 → "$" ≈ #118 (Δ +2); "time"@#155 → hourglass ≈ #160 (Δ +5); "engagement."@#213 → chart ≈ #208 (Δ −5). Onsets 4.53, 4.69 s (#136/#141), 6.55 s (#197). Rebuild: scale .5→1.07→1 `cubic-bezier(.3,1.4,0,1.1) 1.1s`.

**A04 Single-word swaps on full blue** — hard cut #232 (diff 97) to blue; six centred words "So does" / "that" / "editing" / "is" / "officially" / "*dead?*" each held ≈ 0.5 s with a hard swap (no animation) [OBS tiles 7.5-10.0 s]; word ≈ 2.4% H cap white sans, "dead?" in script at ≈ 3.5% H cap. Trigger "dead?"@#296 → word at #296 (Δ 0). Exit: hard cut #308 (diff 100) back to A-roll. Same as V01-A14 single-word swap on a coloured ground.

**A05 Split-pane slide-in (measured ×3)** — a blue pane (≈ 48-49% H) slides down from the top edge over the A-roll; the A-roll below is pushed/cropped to the lower half. Boundary-y curves from split.txt: #333-364 y 8→620 px (0.6%→48.4% H; 931 px@1080) over 31 f (1033 ms), bez (0.7,0.1,0.4,0.9) rmse .011 (easeInOutQuad .045) [MEAS]; #961-990 y 33→632 (2.6%→49.4%) over 29 f (967 ms), bez (0.5,0.2,0.3,0.9) rmse .009 [MEAS]; #1466-1500 y 0→608 (0%→47.5%) over 34 f (1133 ms), bez (0.8,0,0.5,0.8) rmse .012 (easeInSine .078) [MEAS]. All three are ease-in-out / ease-in shaped with no overshoot; durations 0.97-1.13 s (V02 433 ms, V03 1000 ms, V07 1.3-1.5 s). Triggers: "software."@#374 → start #333 (Δ −41); "second"@#951 → start #961 (Δ +10); "changing,"@#1450 → start #1466 (Δ +16). Onsets: none within ±100 ms of the starts (nearest 10.01 s (#300) is 33 f before #333). Rebuild: top pane `height` 0→48.4% `cubic-bezier(.7,.1,.4,.9) 1.03s`; A-roll bottom `translateY` in sync.

**A06 Pane expand to near-full frame (measured ×2)** — the pane's lower edge continues down from half height to ≈ 93%: #445-472 y 642→1195 px (50.2%→93.4% H) over 27 f (900 ms), bez (0.7,0,0.7,0.8) rmse .009 (easeInQuad .051 / easeInSine .054) → accelerating [MEAS]; #1036-1060 y 649→1195 (50.7%→93.4%) over 24 f (800 ms), bez (0.8,0.2,0.5,0.6) rmse .010 (easeInSine .043) [MEAS]. Triggers: "engineering,"@#488 → start #445 (Δ −43); "plan"@#1069 → start #1036 (Δ −33): the expansion precedes the word by ≈ 1.1-1.4 s. After the expand the scene is effectively full-frame blue (≈ 7% H strip of A-roll left) until the hard cut back. Rebuild: pane height 50%→93% `cubic-bezier(.8,.1,.6,.7) .85s` (ease-in).

**A07 Doc morph: "Video Engineering" card → "Full video script" panel** — white card with an orange glow at its base and title "Video Engineering" morphs (blur/crossfade ≈ 0.4 s at 16.7-17.0 s [OBS]) into a wide white document panel (≈ 76% W × 14% H; header "Full video script" with orange dot, ≈ 8 lines of tiny text): tracker g4_doc (#510-545, region 60-660 × 300-760, ref blue): bw 443→545 px (61.5%→75.7% W; 818→1018 px@1080), bh 265→179 px (20.7%→14% H), cy 432→390 (−42 px), 1167 ms, all three bez ≈ (0.2,1.4,0.6,0.9) with rmse .012 / .007 / .011 → bezier [MEAS], peak/final 1.00 (no overshoot). Trigger "plan"@#608 → start #510 (Δ −98: the doc precedes "plan" by 3.3 s; its text "My last five YouTube videos… Here's the truth… building software… two phases" is the script itself). Rebuild: width/height/translateY `cubic-bezier(.2,1.4,.6,.9) 1.17s`; text crossfade 0.4 s.

**A08 Plan tree: connector + rows + thumbnails** — a thin vertical white line grows down from the doc (18.0-19.5 s, ≈ 1.5 s [EST]); two rows appear below with a sparkle bullet: "✦ Use a one-object animation" + a white thumbnail (19.7 s, ≈ 0.4 s) then "✦ Use a two-object animation" + a dark thumbnail (21.8 s); they settle ≈ 0.5 s after appearing [OBS tiles 19.5-22.5 s]. Re-used at 36-39 s. Trigger "plan"@#608 → rows ≈ #590-650 (Δ −18..+42). Rebuild: SVG line `scaleY 0→1 1.5s`; rows `translateY(10px→0) opacity 0→1 .4s`.

**A09 Reel-card strip behind the speaker (top)** — ≈ 8 portrait cards (≈ 14% W × 22% H: "Learn Something" poster, brain "Book/Habit" poster, hourglass "Animations" gold card, portrait stills, white "What is good Editing" page) in a row at y≈ 0-22% H behind the head, sliding left ≈ 1 card per 1.5 s (25.0-31.5 s); hard-edged at the top, blurred at the left/right ends; fades out at 32.0 s. Same device as V13-A14 reel wall (but here a horizontal strip). Trigger "skill"@#752 → strip visible at #750 (Δ −2). Onsets 26.49, 29.0 s.

**A10 Presenter card + Pr/Ae icons** — dark vertical card (≈ 28% W × 42% H; presenter in a studio chair, "$2,000/MO" in orange, black frame, radius ≈ 5% W) rises from below at 37.5-38.3 s (blurred at first, ≈ 0.6 s [OBS]); Pr and Ae icon squares (blue-purple, white labels) stack above it at 38.5 s (≈ 0.3 s each); they hint at "using your software and skills". Trigger "software"@#1137 → card ≈ #1125 (Δ −12); "skills."@#1158 → icons ≈ #1155 (Δ −3).

**A11 Experience scene on A-roll** — hard cut #1173 (diff 85); captions "Now when I trained **Claude**", "to edit those YouTube videos"; lower carousel strip (≈ 14% H, y≈ 76% H; 41.5-46.5 s): card row of ≈ 6 cards (presenter video, white page, blue "Video" card) with ‹ › buttons and a mouse cursor, sliding left ≈ 1 card per 1.0 s and blurring at the sides [OBS]; "8 years" (white bold, ≈ 4.6% H cap, centre y≈ 53% H, 42.3-44 s) then "My **8 years** of editing *Experience*" small below it. Trigger "eight"@#1263 → big text ≈ #1270 (Δ +7); "years"@#1273. Onset 43.93 s (#1318; attack 12 ms).

**A12 Bad-edit sample card** — at 46.5-47.5 s a small white card with tiny text ("You find out about a recession… [source]") sits at lower-centre (≈ 40% W × 8% H), appearing blurred then sharp (≈ 0.4 s [OBS]) under "Something more like *This*" — an intentionally dull card = what Claude would produce without the creator's guidance. Trigger "something"@#1391 → card ≈ #1395 (Δ +4). Onset 47.18 s (#1415, attack 563 ms, centroid 4313 Hz).

**A13 Raw → pretty transformation (pane)** — in the top pane: a dark vertical presenter card ("raw, boring" caption under it; ≈ 14% W × 22% H) appears at the left (50.3 s), a thin arrow draws right (51.0 s ≈ 0.4 s), a white card with a navy video thumbnail ("60-30-10 rule", slider, colour dots; caption "*pretty* ones") rises/blur-sharpens at the right (51.5 s ≈ 0.5 s). Tracker g8_pane9 (#1525-1590): union bw 200→573 px (27.8%→79.6% W), 2167 ms, easeOutQuad ≈ rmse .064 / cx .113 → ≈ [MEAS] but staged growth, so it is not one curve. Trigger "train"@#1633 later; "2027,"@#1473 → card at #1510 (Δ +37); the arrow is drawn at ≈ #1530.

**A14 Claude tile + "paid to train AI"** — white rounded square with orange asterisk (≈ 12% W; centre y≈ 49% H of the pane) pops at 53.3 s with a small script caption above ("You're going to get *paid*") and "to train AI on how to *edit*" below (white, script "edit"); tracker g9_claude2 (#1600-1655): rmse .49 → [EST] (caption build changes the bbox). Trigger "train"@#1633 → tile at #1600 (Δ −33); "guide"@#1648 (mis-ASR; on-screen "edit"). Onsets 53.89, 54.45 s (#1617/#1634 ≈ caption build).

**A15 Pane exit upward (measured)** — #1713-1742 the boundary retracts: y 620→16 px (48.4%→1.3% H) over 29 f (967 ms), bez (0.6,0.1,0.4,0.9) rmse .012 (easeInOutQuad .018, easeInOutSine .032) → bezier [MEAS], no overshoot; A-roll below grows back to full frame (blur sharpening 57.5-58.1 s). Trigger "perform"@#1730 → start #1713 (Δ −17). Onset 57.0 s (#1710, attack 493 ms) sits at the start. The only pane exit in the reel (all other panes end with hard cuts). Rebuild: pane height 48%→0 `cubic-bezier(.6,.1,.4,.9) .97s`.

**A16 YouTube tutorial card** — card ("$4,000/mo" in orange above a thumbnail with Claude asterisk tile + play button + presenter face; title "How I Would Learn AI Video Editing if I Could Start Over! (30 Day Plan)", channel line) rises at lower-centre (≈ 52% W × 15% H, y≈ 79-86% H) at 60.4 s: tracker g6_yt (#1815-1860): rmse .12-.40 (hands/gesture pollute the region) → [EST]; Trigger "tutorial"@#1834 → card visible from ≈ #1815 (Δ −19). Exit: fades at 63.5 s as the comment bar enters. Rebuild: translateY(40px→0) + blur 6px→0 `ease-out .5s`.

**A17 CTA comment bar (typed "guide")** — hard-edged dark pill with avatar left, blue send circle right at y≈ 74% H, appears 63.6 s (while "In just 30" caption); tracker g7_comment (#1930-1975): bw 61→557 px (8.5%→77% W), cx 672→524, rmse .15-.29 (family only; typing text changes the bbox) → [EST]; "Add a comment…" → "guid|" → "guide" typed 64.5-65.0 s, cursor clicks send at 65.2-65.5 s; caption "Comment down the word *Guide*" (script "Guide"). Trigger "Comment"@#1927 → bar ≈ #1905 (Δ −22); "guide,"@#1949 → typing ≈ #1935-1950 (Δ −14..+1). Onsets 64.9 s (#1947, attack 12 ms), 65.25 s (#1957, attack 52 ms).

## 4. Text & typography system
| style | font (conf.) | weight | cap %H | colour | use |
|---|---|---|---|---|---|
| A-roll caption | grotesque (Inter-like, med) | Regular, Bold on key word | ≈1.5 | #FFFFFF | spoken lines |
| Script word | italic high-contrast serif (low-med) | Regular italic | ≈2.0 (≈ 3.5 for "dead?") | #FFFFFF | Five, Engagement, dead?, Truth, building, skill, Content, deep, Together, Experience, This, Changing, Well, AI, edit, Guide |
| Big numeral | grotesque | Bold | ≈4.6 | #FFFFFF | "8 years" |
| Pane caption | grotesque + script | Regular + italic | ≈1.2 | #FFFFFF | "Editing a video is like *building* software" (top, y≈ 3-7% H) |
| UI micro text | SF-like | Regular | 0.4-0.7 | grey / dark | doc, rows, tutorial card |
Rules [INF]: single words on full-blue scenes are the biggest type (the drum-roll), numbers are bold and large (8 years), script marks the abstract/emotional word; captions in panes sit at the top of the pane, on A-roll at y≈ 62-66% H.

## 5. Colour, light & material
- A-roll: wall #040D18 (left) / #152233 (right), tee #14171D [MEAS f10]; at f1650 dark #071117 [MEAS]; the darkest and lowest-key grade of the series; blue rim/edge light minimal.
- Blue ground: #4279BD (top corner) → #205AA4 (bottom); frame mean (59,133,209) [MEAS f270]; at f700/f1650 top corner #427ABB [MEAS]; rays + grid [OBS].
- UI: white cards (#D3E7E8 doc interior tint at f700 [MEAS]) with soft shadow; orange Claude asterisk ≈ #D97757 [EST]; orange glow under "Video Engineering" ≈ #F5A623 [EST]; blue tile glyphs ≈ #2F80FF [EST]; "$4,000/mo" orange ≈ #F5A623 [EST]. Glow radii not measured (Q12 gap); corner radii EST: tiles ≈ 18% W of tile, doc ≈ 2% W, cards ≈ 4% W.

## 6. Depth & 3D
Flat; depth by defocused A-roll (≈ 8-10 px [EST]) behind overlays and the pane push (A-roll cropped to the lower half). No perspective, no orbit. The pane's A-roll shifts down with the boundary (parallax-free).

## 7. Camera & transitions
| frames | type |
|---|---|
| #232, #308, #741, #1173 | hard cuts (diff 85-126) |
| #333-364, #961-990, #1466-1500 | pane slide-in 0.97-1.13 s [MEAS] |
| #445-472, #1036-1060 | pane expand 0.8-0.9 s, ease-in [MEAS] |
| #1713-1742 | pane exit upward 0.97 s [MEAS] |
| #1244, #1273-1285, #1312-1329 | carousel/label moves (low bursts) |
No whips, flashes, shakes or A-roll zooms.

## 8. Assets used
Re-used earlier graphics (mind-map "Alex" UI), recreated: doc "Full video script", plan tree + thumbnails, tutorial card, icon tiles, comment bar, pane cards. Captured/stock: reel strip cards (own and others), "$2,000/MO" presenter card. Orange Claude asterisk is the product mark (UI reference only).

## 9. Sound ↔ picture
| onset s (frame) | attack ms / centroid Hz | visual | Δ f |
|---|---|---|---|
| 1.02 / 1.65 / 1.81 s | 284 / 180 / 17 | caption "Five YouTube videos"; strip leaving | in event |
| 2.9 (#87) | 17 / 2348 | Claude tile (≈ #75-90), "Claude."@#89 | ≈0 |
| 4.53 / 4.69 s | 192 / 29 | "$" tile #118 → onsets precede by ≈ −17 f | −17 / −12 |
| 6.55 (#197) | 134 / 2025 | chart tile (#208) | −11 |
| 10.01 (#300) | 52 / 3151 | cut #308 (−8 f) | −8 |
| 13.14 / 14.09 / 14.81 s | 226 / 41 / 134 | cards (#420-440) / pane expand starts #445 | −2..+1 |
| 19.97 / 21.57 / 23.15 s | 163 / 35 / 470 | plan rows | in event |
| 24.2 (#726) | 186 / 2199 | cut #741 (+15 f later) | −15 |
| 26.49 / 29.0 / 31.6 s | 383 / 313 / 192 | strip moves | in event |
| 43.93 (#1318) | 12 / 2047 | "8 years" big text | in event |
| 47.18 (#1415) | 563 / 4313 | bad-edit card | +24 |
| 48.83 (#1465) | 261 / 2313 | pane enter #1466 | −1 (hit) |
| 53.89 / 54.45 s | 238 / 337 | Claude tile caption | in event |
| 57.0 (#1710) | 493 / 1957 | pane exit start #1713 | +3 |
| 64.9 / 65.25 s | 12 / 52 | comment typing / click | in event |
30 strong onsets in 65.9 s (0.46/s); 0 of 4 hard cuts have an onset within 100 ms (hit rate 0.0; nearest −8 f before #308 and −15 f before #741). Of the 6 measured pane moves, 3 have an onset within 3 f of their start: expand #445 ↔ 14.81 s (#444, −1 f), enter #1466 ↔ 48.83 s (#1465, −1 f), exit #1713 ↔ 57.0 s (#1710, −3 f); the other three (#333, #961, #1036) have none within 100 ms [MEAS]. Cue medians 575 ms long, attack 189 ms, centroid 2325 Hz, peak −3.6 dBFS. Sound is attached to pane moves rather than cuts here [OBS]. Music bed likely (rms p10/p50/p90 −30.6/−19.7/−13.2 dB) [EST]. Sound types not verified [INF].

## 10. Editing psychology
| condition | action | reason [INF] |
|---|---|---|
| a provocative question | full-blue single-word drum-roll, hard cut in/out | the question gets its own beat, no face |
| abstract two-phase model | pane + two white cards, expand to near-full, morph one card into a document | the model becomes an artefact the viewer can read |
| "thousands of pieces of content" | strip of reel cards scrolling behind the speaker | quantity without leaving the face |
| the creator's experience matters | big "8 years" + failed-edit sample card | authority + counter-example |
| the future of the job | raw → arrow → pretty transformation + Claude tile "paid to train AI" | the new job role as an image |
| CTA | tutorial card ($4,000/mo) + comment bar types "guide" | proof + action |
Pacing (state changes per 10 s [EST from §2 + A-lists + the measured pane moves]): 0-10 s: 14 · 10-20 s: 9 · 20-30 s: 6 · 30-40 s: 8 · 40-50 s: 8 · 50-60 s: 7 · 60-65.9 s: 5. Longest static A-roll stretch 24.7-31.6 s with only the strip + captions.

## 11. Signature moves (self-contained recipes)
1. Pane slide-in from the top: 0 → 48% H in 1.03 s `cubic-bezier(.7,.1,.4,.9)` (ease-in-out), A-roll pushed to the lower half; used 3×.
2. Pane expand to 93% H in 0.85 s `cubic-bezier(.8,.1,.6,.7)` (accelerating, ease-in) before a doc scene.
3. Card → document morph in 1.17 s `cubic-bezier(.2,1.4,.6,.9)`: width +23%, height −32%, centre up 42 px, no overshoot.
4. Pane exit: boundary 48% → 1% in 0.97 s `cubic-bezier(.6,.1,.4,.9)`, A-roll sharpens at the end.
5. Single-word drum-roll on full blue (0.5 s per word, hard swaps), last word in script.
6. Plan tree: connector grows ≈ 1.5 s, two rows with thumbnails appear 2 s apart.
7. Benefit icon tiles ($, hourglass, chart) popping one per spoken benefit (+2..+5 f).
8. Reel-card strip scrolling horizontally behind the head (1 card / 1.5 s).

## 12. Gaps / uncertain
- Strips viewed: 0/33 (budget); the prior split.txt covers 6 pane moves frame-by-frame (cited); the rest from 6 sheets + CSVs. Sheet-derived timings are "~"/[EST]. Q6 not met.
- Work files: split.py, split.txt (6 ranges) cited; wordtimes.txt (one line of words) used as a cross-check; 9 new tracks run: usable g4_doc (3 props bezier); partially g8_pane9 (≈); discarded g1, g2 (no change ≥ 15%), g3 (EST), g5 (staged), g6, g7, g9 (EST). Checklist item 3 (≥ 8 clean curves) met via the 6 pane curves + g4_doc (3 props) = 9 [MEAS] curves.
- The pane's A-roll translation not tracked separately (assumed in sync with the boundary). The "Alex" top-strip cards (0-3.5 s) are re-used from an earlier graphic; their motion not measured. Fonts unconfirmed; glow radii EST. ASR mislabels "guide" at #1648 (on-screen "edit").
