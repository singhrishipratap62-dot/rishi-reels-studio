# Series intro, all four versions (rebuilt from Try_6) · notes

**Current:** `Intro_V1.mp4` … `Intro_V4.mp4` (+ matching `.tsrct`). 1080×1920, 30 fps. Archived as `Versions/Intro_V*_r1.mp4`.
Rebuild one version: `.tesseract-work/build.py <root> <1-4> --mix=<trim>` on `.tesseract-work/base_v<n>.tsrct`. Trims used: V1 0.86, V2 0.821, V3 0.815, V4 0.821.

## What Try_6 taught (Rishi's final V1)
Try_6 is our italic caption + sound export (audio correlation 0.996), composited in Premiere with his card stack and a lemon-yellow 30-day grid **behind** him. So:
1. **Captions:** keep the Minimal Editorial set exactly: Playfair Bold *Italic* hero char by char with blur, Inter 48 px support word by word, chrome-yellow "1". He chose italic over upright for the final.
2. **Sound:** keep the caption cue map: Hi-Tech Click per hero, flick per support word, pop on "1", swoosh on the first caption, +3 dB opening, −15 LUFS.
3. **Cards:** his stack and positions (big card top ~170 px, i.e. outside the Reels top margin, accepted). Small cards fan in over 0–1.2 s, the big card lands on "day", the big card leaves first, then the small cards right → left, gone ~0.5 s before the end.
4. **Grid:** lemon #FDD649 card, #191C35 tiles, tile 1 white on "1", at x 38–455 / y 845–1275, **behind the subject**. It exits on "teaching".
5. **Cut:** one continuous take, no pause trims, ~0.4 s lead before "Anatomy".

## Applied to each version
| | Source span | Length | Captions (hero in *italics*) | Notes |
|---|---|---|---|---|
| V1 | 1.714–10.156 s | 8.44 s | *anatomy* · *day 1* · *consulting cases* · *teaching* · *frameworks* · *30 days.* | Matches Try_6 frame for frame, incl. the 115 % opening punch. Grid behind him; cards as overlay (his face sits below them) |
| V2 | 1.280–11.195 s | 9.92 s | *anatomy* · *day 1* · *case interviews* · *teaching* · *every case type* · *30 days.* | Standing, closer framing: cards **and** grid behind him so the face stays clear. Captions at y 1480, under the shirt print |
| V3 | 0–4.434 s | 4.43 s | *anatomy* · *day 1* · *consulting cases.* | No promise line, so the grid exits 0.5 s before the end. Speech starts on frame 0, so the cards open over the sticky-note close-up |
| V4 | 0.535–8.480 s | 7.95 s | *anatomy* · *day 1* · *case interviews* · *teaching* · *frameworks* · *30 days.* | Cards and grid behind him; captions at y 1510 (he walks closer near the end). *frameworks* holds until "30" so it can finish revealing (no pause before "in") |

## How "behind the subject" works
Tesseract's built-in `personMatte` returned an empty matte on this machine (no segmentation model). So a person matte is made locally with MediaPipe selfie-multiclass (`assets/mattes/matte_v*.mp4`, same clock and framing as the A-roll, push-in mirrored). It's used as a **lumaInverted track matte** on the grid group, and on the card images in V2–V4. Edges are slightly feathered; check hair and fast hand moves (V2's opening whip is the hardest case).

## Checks
- Loudness, final exports: V1 −15.0 LUFS / −2.5 dBTP; V2 −15.0 / −2.8; V3 −14.9 / −3.0; V4 −15.0 / −2.5.
- SFX placement (effects-only renders): every cue within ±60 ms, except the first click in V1 (78 ms) and V3 (68 ms), whose window overlaps the opening swoosh.
- Caption safe-zone audit is clean for all four; no black frames; filmstrips in `Previews/`.
- **Not verified by ear.**

## Open
- In V4's last two seconds he steps closer, and the shirt print still brushes the top of "all types of" / *30 days.*
- The big card still says *Profitability Case* in every version (as in Try_6).

## Revision log
| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
