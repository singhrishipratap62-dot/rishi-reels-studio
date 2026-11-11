# Talking-head layout (green screen)

How motion graphics are laid out when Rishi is on camera. Added October 2026 from the "AI and patience" reel (Reel 5).

## When to use it

Two kinds of reel come in with an SRT. Check the brief before laying anything out:

| The brief says… | Layout |
|---|---|
| **"Talking head"** (Rishi on camera; the SRT is his own recorded voice) | **This page.** Split screen with a green-screen panel he keys his video into, alternating with full-graphic and full-green beats. |
| Nothing about talking head, or **"AI voiceover"** / ElevenLabs / faceless | The standard full-frame layout from *Formats and safe zones*, *Motion* and *Taste rules*. **No green screen anywhere.** |

If the brief doesn't say, assume AI voiceover (no green screen).

Everything else in the system still holds in talking-head reels: colours, fonts, the pen, the highlights, *Taste rules*, the hook rules, the SFX stem and the checklist.

## The green key

- Colour: **`#00B140`** (broadcast chroma green), flat, full-bleed, no texture, grain, gradient or shadow. It's a production key, not a brand colour, and it's the only exception to the three-colour rule.
- Nothing of the design (text, shapes, tints, glows, shadows) may sit on the green, except a full-green beat's plate (below) and the captions in full-green beats. Anything drawn on the green gets keyed out or tints his video.
- The green panel is one solid layer above the graphics. Moving that layer *is* the transition between layouts.

## The three frames

| Frame | Graphics | Green | Captions |
|---|---|---|---|
| **Split** (the default) | Top half, y 0–960, on paper or ink | Bottom half, y 960–1920 | **In the graphics half**, centred, bottom edge at y ≈ 936 (just above the seam). Dark on paper, light on ink. Never on the green. |
| **Full graphic** | Whole frame, as in a normal reel | Off screen (slid down) | Normal band, y 1395–1490, dark on paper, light on ink |
| **Full green** (Rishi full frame) | One paper plate at the top only, y ≈ 236–700 (a name card, a checklist, a short stat), with a hairline border and a red 10px edge | Whole frame | Normal band, y 1395–1490, `brand-paper` text with a soft shadow (`0 2px 14px rgba(0,0,0,.45)`) so it reads over his video |

### Split-frame bands (graphics half)

- y 0–220: keep clear (Instagram's top bar).
- y 226 to ~450: headline / kicker band (Bricolage; 96–98px for 2-line hooks so it fits).
- y ~470–835: the graphic. Shapes, nodes, charts and tabs all end above y ≈ 840.
- y ~845–936: **caption band in split** (one or two lines of 46px General Sans Semibold).
- y 960: the seam. Nothing crosses it.
- Right edge: keep text and key shapes left of x 940.

Elements sit higher than in a full-frame reel: shrink or re-flow the graphic to fit the ~370px graphic band rather than letting it reach the captions or the seam.

## Rhythm: keep it changing

- **Open in split at frame 0.** The first frame is already split: hook headline and hook visual in the top half, green below. No intro slide before it.
- **Alternate frames by idea**, never by a fixed pattern. A good mix for 60–75s is about 5 split, 4 full graphic, 2 full green, plus the end card. Never more than two scenes in a row in the same frame.
- **Full graphic** for the big beats: the main number or chart, the punchline / concept phrase, the end card.
- **Full green** for personal or list beats: "my name is Rishi", the follow ask, a quick checklist while he talks.
- **Nothing static for more than ~3 seconds.** Every frame has something building, counting, sweeping or pushing; a hold gets a slow centred push (1.0 → 1.03–1.05).

## Transitions between frames

All of them are moves of the green panel (Smooth / `ease-in-out`, ~0.45–0.5s, starting on the scene's first cue):

- Split → full graphic: green slides **down** off the bottom.
- Full graphic → split: green slides **up** from the bottom to y 960.
- Split / full graphic → full green: green slides **up** to y 0.
- Full green → full graphic: green slides **down**, revealing the graphic.
- Split → split: hard cut on the word (green stays at 960).

The captions switch place and colour on the same frame the green finishes moving.

## End card

Full graphic, paper, crop marks allowed: the green slides down to reveal it. Profile photo if one is supplied, else typographic `@rishi.docx`.

## Deliverables (same as other reels)

The silent motion-graphic film (green included, his video keyed in later in his editor), the SFX stem from 0:00 with its cue sheet, and swooshes on every green-panel move.
