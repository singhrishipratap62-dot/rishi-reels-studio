# VISUAL REFERENCE LIBRARY: Rishi's Editing Style (v1.0)

An **index**, not a gallery. The 15 reference reels are third-party content: frames are for private study only, never to be published or reused in Rishi's edits (`plan.md` hard rules). This pack therefore stores **pointers** (reel, frame, teardown section) instead of copied stills. Extract a frame on demand when you need to look.

## 1. How to look at a reference
- Videos: `a reference to Rishi's editing style/*.mp4` (720×1280, 30 fps); `teardown/index.txt` maps V## to the file. Frame `N` = `N/30` s.
- One full-res frame: `bash engine/measure-scripts/frame.sh <video> <frame#> <out.png> [w:h:x:y crop]` (write to a scratch folder, never into the pack).
- Strips (every frame, 60 per image) and sheets (2 fps) are **not stored** (regenerable, ~250 MB): run `engine/measure-scripts/strips.py` / `sheets.py` on the video when you need to look.
- Measurements per move: `teardown/V##_<slug>/BREAKDOWN.md` §3 (IDs `V##-A##`) and `animations.json`; cross-reel summary: `teardown/SYNTHESIS.md`.
- Evidence quality: V01, V10, V14, V15 are the best measured; V05-V09, V11 are weakest (see `BUILD_PLAN.md` evidence table).

## 2. Where to see each device (best examples first)
Frames are native frame numbers of the reference reel. IDs refer to the teardown catalogues.
| device (pack name) | best reels | where (frames / ID) | note |
|---|---|---|---|
| split pane drop / expand / lift | V14 | enter #333-364, #961-990, #1466-1500; expand #445-472, #1036-1060; lift #1713-1742 (A05, A06, A15) | all six curves measured; also V02 #405-418 (433 ms), V07 #1257-1279, V12 #625-646, V03 #428-458 |
| hero-card settle / card snap | V10, V13 | V10 post card #145-156 (A05), Stripe toast #833-846 (A11); V13 post card #350-385 (A07) | V10 fast (0.37 s) vs V13 slow (1.17 s) |
| grow-from-edge card | V13 | SaaS card #825-885 (A12) | 2.0 s, left edge → centre |
| card → doc morph | V14 | #510-545 (A07) | 1.17 s, no overshoot |
| avatar pop + value reveal | V10 | #15-26 (A01), #37-48 (A02) | hook lockup |
| chapter diamond (centred) | V10 | #241-254 (A07) | 16.5% W at (50%, 57% H) |
| chapter diamond (lower-left) | V04, V06, V08, V09 | V04 #150-172 (A06); V08 #205-225 (A04) | lower-left variant is [EST] timing |
| 1-2-3 tracker | V02 | #10-34 (A01) | line draws 0.8 s |
| counter running at frame 0 | V09, V07 | V09 #0-45 (A01); V07 #0-60 (A01) | values read at 2 fps |
| price strike + arrow + green price | V15 | #67-138 (A02, A03) | + confetti (optional) |
| price pill rise (before spoken) | V09 | #1508-1545 (A16) | rises ≈ 2.4 s before "$299" |
| pixelated hidden price | V12 | #182-288 (A05, A06) | curiosity gap |
| red hand-drawn ellipse | V07, V09, V10, V12, V15 | V15 #250-262 and #1651-1670 (A04, A17); V12 #130-141 (A04) | scarcity words only |
| deadline type beat | V13, V15 | V13 #1592-1698 (A16); V15 #1633-1700 (A17) | text-only ground, calm |
| giant verdict word | V11 | #372-425 (A06) | 72% → 89% W in 1.77 s |
| drum-roll words | V14 | #232-307 (A04) | 0.5 s per word, hard swaps |
| card wall / zoom-out | V12, V05, V13, V15 | V12 #344-475 (A07); V05 grid #310-345 (A06); V13 #900-1019 (A13); V15 tweet wall #304-360 (A05) | outer cards blurred |
| category carousel | V12, V15, V09 | V12 #805-1034 (A11); V15 #809-975 (A11, IG-post frame); V09 #371-668 (A06) | swap every 1.5-1.8 s |
| reel-card strip behind head | V13, V14, V15 | V13 #1109-1119 (A14); V14 #750-960 (A09); V15 #718-800 (A10) | horizontal scroll |
| proof zoom | V13, V11, V01 | V13 job post #1314-1344 (A15); V11 phone #1255-1335 (A14); V01 #92/#93 (A04, 2.00× cut) | 1.8-3.5× |
| typed prompt / UI step | V03, V05 | V03 chat #290-396 (A06); V05 #650-830 (A10) | ≈ 15-20 chars/s [EST] |
| comment-bar CTA | V05-V08, V10, V12, V13, V15 | V15 #1867-1878 (A19); V12 #1600-1665 (A17); V13 #1700-1780 (A17) | bar grows from the right edge |
| literal demonstration (rule performed) | V02, V08, V11 | V02 icon −25% #536-600 (A09); V08 60/30/10 bar #610-760 (A11); V11 garage → showroom #855-945 (A11) | the on-screen change equals the spoken number |
| before / after card | V15 | #990-1096 (A12) | profit digits count |
| footage → card opener (optional) | V01, V04, V05 | V01 #21-77 (A01); V04 #8-70 (A01); V05 #0-28 (A01) | A-roll shrinks into a rounded card |
| defocus bridge | V03, V10, V12, V14 | V03 #390-410 (A07); V12 #1252-1295 (A14) | A-roll blurred under a floating element |

### Experimental (reference only; off by default)
glass/glow panels and holograms V01 (#857-923, A22); orbit ring V01 (#1012-1092, A23); cylinder carousel V01 (#330-422, A11/A12); font-cycle word V01 (#132-143, A06); countdown ring V06 (#103-130, A02); percentage ring V11 (#268-345, A05); 3D post push V10 (#1165-1278, A13); iris wipe V02 (#259-262, A04).

## 3. Reference stats (from the teardowns)
| reel | length | hard cuts | notes |
|---|---|---|---|
| V01 | 47.2 s | 9 | benchmark (Family A look) |
| V02 | 49.7 s | 4 + panes | rules demo |
| V03 | 57.4 s | 7 | AI workflow |
| V04 | 53.4 s | 1 | 6 pillars |
| V05 | 55.7 s | 8 | AI workflow |
| V06 | 69.1 s | 12 | 60-second timer |
| V07 | 48.4 s | 4 | offer |
| V08 | 66.0 s | 5 | design lesson |
| V09 | 56.9 s | 11 | offer + interviews |
| V10 | 63.0 s | 9 | case study |
| V11 | 61.2 s | 10 | tips |
| V12 | 56.4 s | 8 | offer |
| V13 | 60.0 s | 8 | case study |
| V14 | 65.9 s | 4 + 6 pane moves | argument |
| V15 | 64.3 s | 10 | offer |
Median hard-cut spacing ≈ 6.7 s [MEAS from `events.md`, 15 reels]; counts above are hard cuts listed in each reel's `events.md` (pane/blur transitions are not counted).

## 4. Pilot checks that need stills (Phase 5)
When the pilot edit starts, extract (privately) the 3 frames per Family-B reel needed to close the [EST] gaps listed in `SYNTHESIS.md` §8: caption cap-height and y position, green/red pixel samples (V15), and one blur-rise card (sharpness column in `track.py`).
