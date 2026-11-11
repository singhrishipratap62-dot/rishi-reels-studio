# DESIGN_SYSTEM — Consulting case reel edit (v1.5)
Reference only: SKILL.md wins on any conflict. Lines marked SUPERSEDED are kept for context.
Evidence tags: [OBS] seen (ref+time) · [EST] measured/estimated · [INF] interpretation · [R1.x] Rishi rule (wins).

## Philosophy
A consultant whiteboard that builds itself while Rishi talks. Calm, clean, product-UI look (white cards, lavender, navy text). The board carries the logic, the caption carries the words, the face carries trust. Nothing decorative moves; only information appears. [INF]

## Canvas
1080x1920, 29.97 fps (30000/1001), H.264 ~17-19 Mb/s, AAC 48 kHz stereo. [OBS R1,R2]
Runtime ~1:41-1:44 of speech; video ends when speech ends + end card (no black tail) [R1.0].

## Background [R1.17]
Board scene (S3/S4): the reference loop `05. Asset Library/videos/gradnext-background-loop-9-16.mp4` (1080x1920, 5 s, lavender glows + dot grid), looped behind a transparent board layer. The CSS gradient below is only a fallback.

## Colour tokens [EST, PIL medians on R1 0:48, 1:41]
- bg gradient: top-left #FDFDFD (near white) → top-right #E6E9FD → bottom-left #CFD7FD → bottom-right #DBE0FC. Soft lavender wash, strongest bottom-left; faint lavender dot grid (~36 px pitch) visible in the upper bg.
- board card: #FFFFFF, radius ~32 px, very soft shadow.
- caption text: #2C3552 (navy). Ghost (incoming) word: same navy at ~35-45% opacity.
- board ink/text: #2B2F3A-#373B3A (near-black navy). Small labels: grey #8A8FA0, uppercase, letter-spaced.
- accent: #5670FC (bars, active tab dot, fills). Light accent fills/pills: ~#E3E6FD / #EEF0FE. Dark bar segment: #2C3552.
- face-card glow: lavender (#C9CEFB-ish) blur ~60-80 px around the face card.
- highlight under key numbers: pale yellow/peach marker strip (e.g. ₹400 answer). [OBS R1 1:28]

## Type [R1.0 Avenir Next]
- Captions: Avenir Next Demi Bold, ~52 px (cap height ~40 px), navy, one line, centred, max 4 words / 680 px (x 200–880) [R1.5]. [EST]
- Board headline numbers: Avenir Next Medium/Demi, 60-90 px (₹80, ₹100, 400 km). [EST]
- Board question box: Demi ~30 px inside rounded outline box. Tree rows: Medium ~22-26 px. Labels: Regular/Medium ~18-20 px uppercase tracking +6%.
- Hook question: Avenir Next Demi ~40 px, 3 lines, left-aligned.
- Header (hook panel + board card, not the end card) [R1.17]: "Solving real consultant cases" Regular ~18 px grey + pill "Part NN" (accent text on light-accent pill) top-left; "gradnext" Demi ~26 px navy top-right.

## Layout (main scene) [EST R1 0:48]
- Board card: x 38–1041 (≈1003 w), y 141–705 (≈564 h) → a 16:9 card. Inner padding ~32 px. Header row at y≈172.
- Caption line: baseline band y≈782–821 (centre ≈ y 800).
- Face card: x 136–945 (≈810 w), y ≈858–1766 (≈908 h), radius ~28 px, lavender glow. Face cropped from the raw: head + shoulders, eyes at ~33% of card height.
- Safe zone: Reels UI covers bottom ~300 px and right icon column; face card bottom (1766) sits under the UI band — acceptable because it's face/shirt, not text. All TEXT stays within y 140–830. [INF]

## Layout (hook scene) [EST R1 0:01]
- Top white panel full-width y 0–750: header row, case photo (rounded, ~45% width, left), question text right, MBB logo strip centred below (McKinsey, BCG, Bain) [R1.0 always all three].
- Bottom y 750–1920: raw camera full-bleed (no card, no glow). Hook caption: CENTRED inside the white panel at y≈625, M01 rise-in [R1.4, R1.14]. (SUPERSEDED [OBS]: reference caption sat top-left ~y 800, x≈160, over the wall.)
- Hook question: shown in full from frame 0 in light grey; each word turns dark ink as spoken [R1.6]. Opening blur-in on the panel only (y 0–750), σ 12 → 0 ease-out, done by 0.8 s (max 1 s), never the face [R1.11].
- MBB strip: real logos `05. Asset Library/stickers/mbb_logos_trim.png` (`mbb_logos.png` = untrimmed), never typeset wordmarks [R1.8].

## Board grammar (the core) [OBS R1,R2]
Two phases on one persistent card.
1. FACTS phase (setup + clarifying questions):
   - Right column: issue tree. Root = rounded outline box with the client question ("How do we price this?" / "What toll should we charge?"). Under it a small uppercase label "CLARIFYING QUESTIONS", then rows: Q pill (light-accent fill) → A pill (white, accent outline). One row per question asked, ADDED and kept. Also collects facts (Refill today ₹80, Device cost ₹100 to make, R&D ₹50 cr …).
   - Left column: the current beat's visual, replaced beat by beat: photo tile, big number, line-drawn icon (bottle, plug device, store, clock), unit grid (squares), years progress bar, "? ? cr" placeholder box, comparison "A vs B", stacked bar.
   - Before the root box exists, beats use the full card (client intro: photo + label + big number).
2. SOLVE phase ("So how do we price it? I'd price it in N ways"):
   - Board clears. Top: client question box stays (small, centred). Row of method tabs (Cost method · Alternatives · Value) — grey dots, active = accent/navy dot + bold.
   - Bottom: horizontal ₹ number line spanning the card. Markers drop in as they are found: floor (₹290 / ₹1,000), alternatives, ceiling (₹640 / ₹1,400), answer (₹400 / ₹1,100) with highlight strip.
   - Middle: working for the active method: equation chips ("R&D ₹50 cr ÷ 10 lakh units a year × 5 years = ₹100 a unit"), stacked bars (cost + trade margin), unit grids (8 refills), "= ₹594 a year" result, comparison boxes (₹80 ≈ ₹640 · 8x more expensive).
3. END: board replaced by end card: "Solving real consultant cases", pill "Part NN", then pill button "Follow for Part NN+1" (pops in on "Follow"). NO "gradnext" and no header on the end card; the header fades out as it arrives [R1.9, R1.17]. Face card + caption stay. (SUPERSEDED [OBS]: references had a centred "gradnext" on the end card.)

## Number line / working area [E1.6, E1.7]
Values closer than ~5 % of the axis (₹1,000 vs ₹1,500 on a ₹20k axis) collide: reference marker (grey) below the axis, floor/ceiling on tier 1, answer on tier 2. MID working rows above y≈375 in card coords, axis at y 508. A big ✗ over a number hides it: use a strike-through line + small ✗ beside it.
Market-sizing variant (R008): Demand/Supply tabs + Cities/Villages tables + 0–400 cr count bar, from existing beats.js classes. Growth variant (R011): sales bar with today / increments / target segments.

## Core / optional
- CORE: three-zone layout; persistent board; word-synced builds; one-line word-by-word caption; hook top-panel + full-bleed face; one punch-in; facts→solve phases; ₹ number line with floor/ceiling/answer; end card with part number.
- OPTIONAL: which left-column visual per beat (icon vs photo vs grid); number count-up; highlight strip.
- Low evidence (2 refs): exact font sizes, glow radius, shadow, dot-grid pitch.
