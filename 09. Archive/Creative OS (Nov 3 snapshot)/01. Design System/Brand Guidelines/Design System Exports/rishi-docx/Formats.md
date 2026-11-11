# Formats and safe zones

All sizes are in pixels at native resolution. Design at these sizes; all type sizes in the tokens assume a 1080px-wide canvas.

## Reels and motion graphics — 1080×1920 (9:16)

Instagram's interface covers parts of the frame. Keep text and anything important inside the safe area:

| Edge | Keep clear | Token | Why |
|---|---|---|---|
| Top | 250px | `safe-top` | Username, follow button, audio row |
| Bottom | 420px | `safe-bottom` | Caption text, progress bar |
| Right | 160px | `safe-right` | Like / comment / share / audio column |
| Left | 64px | `space-5` | Side margin |

That leaves a text-safe area of roughly 856 × 1250px. Backgrounds, grids and footage can (and should) run full-bleed; only text, numbers and key shapes stay inside.

If a reel is ever boosted as an ad, Meta's ad guidance is stricter (roughly 14% top, 35% bottom). Design key text for the centre of the frame and you're covered either way.

**Test it:** before finalising, check one frame with Instagram's UI on top (or a safe-zone overlay in your editor). Instagram changes its interface; these numbers are a working standard, not a guarantee.

## Captions

Burned-in captions on every reel (`Captions`). Updated October 2026:
- In English, 3–6 words per chunk, changing with the voice.
- General Sans Semibold 46px on a 1080 canvas, no pill: `ink` text on paper grounds, `brand-paper` text on ink grounds.
- Each word rises in from below (≈38px, ~0.3s, staggered ~60ms).
- Centred horizontally, bottom edge at y ≈ 1490, just above `safe-bottom`. The band y 1395–1490 is reserved: scene text and graphics end above y 1390.
- Someone else speaking (clip, quote): Gambetta italic, same size, so the viewer hears it's another voice.

## Talking-head reels on green screen

For reels where the brief says **talking head**: 50/50 split (graphics y 0–960, green `#00B140` y 960–1920), captions in the graphics half just above the seam, plus full-graphic and full-green frames. Full rules in *Talking-head layout*. AI-voiceover reels never use a green screen.

## The split hook

Top 60% (y 0–1150) visual, bottom 40% you; title over the seam. See `SplitHook` and *Pacing and structure*.

## Landscape footage

Centre it full width, letterboxed on `bg`, captions below the footage instead of over it.

## B-roll and footage framings (reference set 2)

| Framing | Size on a 1080×1920 canvas | Use |
|---|---|---|
| **Square card** | 1:1 at 1000×1000, centred at y ≈ 860, on `brand-ink`; caption pill below it at y ≈ 1440 | Short b-roll inserts (1–2s) in a face-led reel: space, labs, places. Calm and premium, and the caption never fights the image. |
| **Paper mat** | Full frame inset by 24px on all sides, `bg` showing as a mat, 2px `line` hairline at the image edge | Cinematic or archival footage in story reels — reads as a printed photograph, not a stock clip. |
| **Echo backdrop** | Card at 900px wide, echo at 220% scale behind it | App and web UI that would otherwise sit on an empty ground (`EchoBackdrop`). |
| **Phone** | Phone outline 760px wide, centred | Articles, blog posts and Wikipedia pages being read along (`ReadAlong` inside it). |

## Title over the face

In face-led reels, the hook can sit over the top of the talking-head frame instead of a split (`TitleOverFace`): title baseline between y 300 and y 560, inside `safe-top`, over a soft `scrim` band so it reads on any background. Frame yourself a little lower than usual (eyes at ≈ 42% of height) so the title doesn't touch your head.

## Graphics over talking-head footage

When a graphic sits over you on camera:
- **Full-screen card**: a `bg` frame (paper or ink) slides up and covers the footage completely. Best for diagrams, charts and big numbers.
- **Upper card**: a `bg` card covering the top ~55% of the frame, footage visible below. Good for a quick stat or quote while you keep talking. Keep the card inside `safe-top` for its text.
- **Lower third**: name/title labels, sitting above `safe-bottom`.

Don't place small floating text directly on footage without a ground behind it. Busy backgrounds kill readability.

## Reel covers — 1080×1920, seen as 3:4

The full cover shows in the Reels tab, but the profile grid crops it to 3:4 (1080×1440), keeping the middle — it cuts about 240px from the top and bottom. Put the hook text in the vertical centre (between y ≈ 300 and y ≈ 1600) so it survives both views.

Covers use: paper or ink ground, hook in `display`/`display-xl`, one Gambetta italic phrase in signal, optional pen mark, wordmark small. Readable at thumbnail size (~120px wide on a phone): if the hook isn't readable that small, it has too many words.

## Carousels — 1080×1350 (4:5)

The profile grid crops 4:5 slightly to 3:4 (about 34px off each side), so keep the side margin at `space-5` (64px) or more.

Slide structure:
- **Slide 1:** the hook, `display` size, one italic signal phrase.
- **Middle slides:** one idea each — `headline` + one visual (diagram, number, chart) + `body` line at most.
- **Last slide:** the takeaway or CTA, plus wordmark.
- A small `label` page counter (`02 / 07`) top-left on every slide after the first; wordmark bottom-left.
- Alternate paper and ink theme only at deliberate turns in the argument, not every slide.
