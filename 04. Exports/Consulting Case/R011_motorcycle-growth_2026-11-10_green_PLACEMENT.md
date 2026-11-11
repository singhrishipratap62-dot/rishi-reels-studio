# R011 — how to rebuild the final from the green + raw exports

Files (all **1080x1920**, 29.97 fps):
- `R011_motorcycle-growth_2026-11-10.mp4` — the posted reel (1.2x speed + music), 4771 frames, 2:39.
- `R011_motorcycle-growth_2026-11-10_1x.mp4` — the same reel at 1x (reference for the green/raw rebuild).
- `R011_motorcycle-growth_2026-11-10_green.mp4` — graphics only, 1x. Pure green **#00FF00** wherever the video shows.
- `R011_motorcycle-growth_2026-11-10_raw.mp4` — your trimmed cut (your Premiere Sequence 01 edit + 0.3 s tail), 1x, uncropped, scaled to 1080x1920.

`_green` and `_raw` have the same length and frame count as `_1x` (5726 frames) and are frame-for-frame in sync.

## Setup (Premiere or any editor)
1. Sequence 1080x1920, 29.97 fps.
2. V1: `_raw.mp4` (three copies, cut at the scene times below). V2: `_green.mp4` with Ultra Key (key colour #00FF00). Audio: `_1x.mp4` (voice + SFX mix).
3. Both start at 00:00:00:00. Do not slip either track.
4. To match the posted reel: nest, speed 120 % (keep pitch), add the music bed (`assets/music/Background music.mp3` from 0:15, ~13 dB under the voice).

## Raw clip placement per scene
Position = centre of the clip in sequence pixels (Premiere's Motion › Position). Anchor at the clip centre (default).

| Scene | Time (seq, 1x) | Frames | Scale | Position (x, y) | What the green area is |
|---|---|---|---|---|---|
| S1 hook | 0:00.000 – 0:03.570 | 0 – 106 | **100.00 %** | **540.0, 1290.0** | bottom of frame, y 750–1920 (white hook panel covers the top) |
| S2 punch-in | 0:03.570 – 0:05.672 | 107 – 169 | **129.96 %** | **569.2, 701.8** | full frame (the final eases 143 % → 130 % over S2) |
| S3 board + end card | 0:05.672 – end | 170 – 5725 | **79.41 %** | **552.9, 1263.0** | rounded card x 136–946, y 858–1766, radius 28 px |

Cuts land exactly on frames 107 and 170, the same hard cuts as the final. In S3 the raw clip is bigger than the card; the green layer's board/background covers everything outside the card once keyed.

Equivalent crops of the 1080x1920 raw (if you prefer Crop over Scale): S1 1080x1170 from (0, 420) → at (0, 750) · S2 831x1477 from (102, 420) → full frame · S3 1020x1144 from (15, 450) → 810x908 at (136, 858).
