# Series intro (30 Days of Consulting Prep) · build notes

**Current:** draft 1, comparison reel `SeriesIntro_comparison_draft1.mp4` (1080×1920, 30 fps, 34.27 s). Editable: `SeriesIntro_comparison.tsrct`.
Rebuild: `.tesseract-work/build.py` (stage 1 footage + voice JSON, stage 2 graphics batch) on top of `.tesseract-work/v0_base.tsrct`.

## Layout of the reel
| Edit time | Segment |
|---|---|
| 0.00–1.00 | Slate · Version 1 |
| 1.00–9.14 | V1 (seated) |
| 9.14–10.14 | Slate · Version 2 |
| 10.14–19.72 | V2 (at the whiteboard) |
| 19.72–20.72 | Slate · Version 3 |
| 20.72–25.42 | V3 (sticky-note open, short) |
| 25.42–26.42 | Slate · Version 4 |
| 26.42–34.27 | V4 (whiteboard pan) |

## What's in draft 1 (the recommended picks)
- Beat 1: the A-roll blurred and darkened (blur 38, brightness −45) as a plate. 5 BTS video cards fly in and fan-stack in the top band (rounded corners, 6 px white stroke, drop shadow). Serif *anatomy* reveals char by char, with "of a case." below.
- Beat 2: hard cut to sharp A-roll at 108 %. Caption "this is" / *day 1* / "of 30", over a 30-dot strip where dot 1 fills pink on "1".
- Beat 3: series line as a serif caption (*consulting cases* / *case interviews*).
- Beat 4: sticky-note wall on white paper (V1, V2, V4). The support line arrives word by word, then the pink serif hero; the 6 notes pop in with overlapping timing.
- Beat 5: A-roll at 110 %, *30 days.* with the dots filling 1→30 in a wave.
- On top of the plan: +1.2 %/s push on all A-roll; grain + vignette on graphic scenes; a 160 ms dip to black at each version's end.
- Voice: per version, 75 Hz HPF → 2.5:1 compression → gain to about −16 LUFS → limiter, so all four sit at the same loudness. Programme: −13.4 LUFS integrated, −1.3 dBFS peak (not final-mixed; the sound pass comes after you pick).

## Deviations from the plan
- V4: no pause between "frameworks" and "in", so the wall holds through "in" and cuts to A-roll on "30". Otherwise *frameworks* couldn't read.
- BTS card 3: swapped C0299 (mostly a bag in frame) for VID_20260924_185957952. Cards are IMG_4118, IMG_4116, VID_…185957, VID_…190010, IMG_4111.
- Accent pink #EE4FA5 was picked by eye to match the sticky notes, not pixel-sampled.

## Known issues / open
- Case-type notes are **placeholders** (Guesstimates, Profitability, Market Entry, M&A, Pricing, Market Sizing). Waiting on the real list.
- The "V1–V4" corner tags and the slates are comparison-only. Remove them for the final.
- Safe-zone audit: 1 flag, the italic overhang of the last glyph of *consulting cases* in V1 (x 846 vs 845 limit at y 1330). It's 1 px; tighten if needed.
- Captions on V2–V4 sit over the "DIMENSION C-137" shirt print, so the small "of 30" support word is busier to read there.
- V3 starts speaking on frame 0; the attack of "Anatomy" may be clipped. Not checked by ear.
- No SFX yet (by design: sound comes after visual approval).
- Tesseract note: Video `cornerRadius` is a fraction of the half-side (0.12 ≈ 13 px on a card), not pixels. 6+ made pills.

## Revision log
| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
