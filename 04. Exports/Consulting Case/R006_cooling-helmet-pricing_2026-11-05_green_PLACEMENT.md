# R006 — how to rebuild the final from the green + raw exports

Files (all 29.97 fps, same length, same audio, frame-for-frame in sync):
- `R006_cooling-helmet-pricing_2026-11-05.mp4` — the finished reel (reference).
- `R006_cooling-helmet-pricing_2026-11-05_green.mp4` — graphics only, 1080x1920. Pure green **#00FF00** wherever the video shows.
- `R006_cooling-helmet-pricing_2026-11-05_raw.mp4` — your trimmed cut, 2160x3840, uncropped.

## Setup (Premiere or any editor)
1. Sequence 1080x1920, 29.97 fps.
2. V1: `_raw.mp4` (three copies, cut at the scene times below). V2: `_green.mp4` with Ultra Key (key colour #00FF00). Audio from either file.
3. Both start at 00:00:00:00. Do not slip either track.

## Raw clip placement per scene
Position = centre of the clip in sequence pixels (Premiere's Motion › Position). Anchor at the clip centre (default).

| Scene | Time (seq) | Frames | Scale | Position (x, y) | What the green area is |
|---|---|---|---|---|---|
| S1 hook | 0:00.000 – 0:03.870 | 0 – 115 | **50.00 %** | **540.0, 1440.0** | bottom of frame, y 750–1920 (white hook panel covers the top) |
| S2 punch-in | 0:03.870 – 0:06.006 | 116 – 179 | **64.98 %** | **540.0, 1033.2** | full frame |
| S3 board + end card | 0:06.006 – end | 180 – end | **49.09 %** | **541.0, 1469.2** | rounded card x 136–946, y 858–1766, radius 28 px |

Cuts land exactly on frames 116 and 180, the same hard cuts as the final. In S3 the raw clip is bigger than the card; the green layer's white/lavender background covers everything outside the card once keyed.

Equivalent crops of the 2160x3840 raw (if you prefer Crop over Scale): S1 2160x2340 from (0, 540) → 1080x1170 at (0, 750) · S2 1662x2954 from (249, 330) → full frame · S3 1650x1850 from (255, 675) → 810x908 at (136, 858).
