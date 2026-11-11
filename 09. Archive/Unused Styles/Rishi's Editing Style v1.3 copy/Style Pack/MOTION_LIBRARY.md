# MOTION_LIBRARY — Rishi's Editing Style v1.0

Named, reusable moves for Remotion at 30 fps. Curves are measured cubic-beziers from the reference reels where the fit passed the quality gate (rmse ≤ .05) [MEAS]; anything else is marked ≈ or [EST]. "f" = frames at 30 fps.

## Grammar (applies to everything)
1. **Entrances = fast-start ease-out, ≤ 3% overshoot.** House curve: `EASE_OUT = bezier(0.1, 0.9, 0, 1)` [MEAS V09 rmse .01, V10 .017-.035, V12 .021]. Heavier hero variant: `EASE_HERO = bezier(0.1, 1.4, 0, 0.9)` [MEAS V12 .019, V13 .015-.037, V04 .03-.04].
2. **Two duration tiers.** Secondary elements (toast, avatar, pill, badge, small card): 11-14 f (0.35-0.45 s). Hero card / the reel's key artifact: 30-45 f (1.0-1.5 s); up to 60 f when a card grows across the frame.
3. **Pane moves = ease-in-out / ease-in** (they are camera-like, not object-like).
4. **Springs only on small objects** (icons, pills, swatches, avatars): peak ≤ 1.25× final.
5. **Timing to speech:** start −10…+10 f around the trigger word; numbers/prices may lead by 20-70 f. Never start after the word has finished.
6. **Exits** are faster and quieter than entrances: fade/blur-out 6-10 f, or the scene is replaced by a cut/pane.
7. No motion blur, no shake, no whips, no flashes [OBS: none in any reel].

## Remotion helpers
```tsx
import {Easing, interpolate, useCurrentFrame} from 'remotion';
export const EASE_OUT   = Easing.bezier(0.1, 0.9, 0, 1);
export const EASE_HERO  = Easing.bezier(0.1, 1.4, 0, 0.9);
export const EASE_SNAP  = Easing.bezier(0, 0.9, 0, 1);
export const PANE_IN    = Easing.bezier(0.7, 0.1, 0.4, 0.9);
export const PANE_EXP   = Easing.bezier(0.7, 0, 0.7, 0.8);
export const PANE_OUT   = Easing.bezier(0.6, 0.1, 0.4, 0.9);
export const MORPH      = Easing.bezier(0.2, 1.4, 0.6, 0.9);
export const SPRINGPOP  = Easing.bezier(0.2, 1.4, 0.2, 1.1);
// t: 0→1 progress of a move that starts at `start` and lasts `dur` frames
export const prog = (f: number, start: number, dur: number, ease = EASE_OUT) =>
  interpolate(f, [start, start + dur], [0, 1], {easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
```

## Library
| name | element / use | frames (ms) | easing | properties from → to | evidence |
|---|---|---|---|---|---|
| **pane-drop** | split pane enters from top | 30 f (1000); range 14-39 | `PANE_IN` | pane bottom y 0 → 922; A-roll translateY 0 → +922 (or crop) | [MEAS] V14 ×3 rmse ≤ .012; V15 1.17 s; V02 433 ms (fast variant) |
| **pane-expand** | pane grows to near full before a doc/full scene | 26 f (850) | `PANE_EXP` | boundary 922 → 1786 (93% H) | [MEAS] V14 ×2 |
| **pane-lift** | pane exits upward | 29 f (970) | `PANE_OUT` | boundary 922 → 20; A-roll returns; A-roll sharpens at the end | [MEAS] V14 |
| **card-snap** | secondary card/toast wipes in from the left edge | 11-13 f (370-430) | `EASE_SNAP` | width 5% → 76-90% W (clip from left), x left-anchored; opacity 0 → 1 in 4 f | [MEAS] V10 A05/A11 |
| **slide-in card** | product/feature card slides in | 10-14 f (330-470) | `bezier(.5,.9,.4,1)` | x −60 → 0 px, opacity 0 → 1 | [MEAS] V15 A09/A14 rmse .013-.014 |
| **hero-settle** | hero card rises and settles | 30-45 f (1000-1500) | `EASE_HERO` | scale 0.86 → 1, y +50 → 0, blur 8 → 0 [EST], opacity 0 → 1 (8 f) | [MEAS] V12 A12/A15, V13 A07 |
| **grow-from-edge** | card grows from the left edge to centre | 60 f (2000) | `bezier(.2,1.4,0,.9)` | width 5% → 67% W, cx 16% → 50% W | [MEAS] V13 A12 |
| **card→doc morph** | card reshapes into a document/panel | 35 f (1170) | `MORPH` | W +23%, H −32%, y −42 px | [MEAS] V14 A07 rmse .007-.01 |
| **badge-pop** | chapter diamond appears | 13 f (433) | `bezier(0,.6,.2,.6)` | size 0 → 178 px (centred) / 0 → 120 px (lower-left); title wipes in next 12 f | [MEAS] V10 A07 rmse .019; lower-left [EST] |
| **avatar-pop** | avatar circle + name label | 11 f (370) | `bezier(.1,.9,.2,1.1)` | scale 0 → 1 | [MEAS] V10 A01 rmse .021 |
| **value-reveal** | "$3,000"-style lockup revealed left → right | 11 f (370) | `bezier(.5,1.4,.9,1)` | clip 0 → 100% | [MEAS] V10 A02 rmse .014 |
| **price-pill-rise** | price pill rises ahead of the spoken price | 37 f (1230) | `EASE_OUT` | y +59 src px (≈ +90 px) → 0 | [MEAS] V09 A16 rmse .01 |
| **ring-pop** | big circular element pops | 27 f (900) | `bezier(0,1.4,0,.9)` | diameter 0 → 22% W | [MEAS] V06 A02 rmse .023 |
| **counter-run** | numerals count up/down | 30-60 f; price steps 15 f each | ease-out (≈ easeOutExpo) | value start → final; final turns green | [OBS] values at 2 fps; curve [EST] |
| **comment-bar-grow** | CTA bar grows from right + keyword types | bar 35-65 f; typing ≈ 8 f/char | `bezier(.2,1.4,0,1)` ≈ | width 16% → 94% W, cx 91% → 50% W (right edge → centred) | [MEAS ≈] V06 A20, V12 A17 |
| **comment-sheet-rise** | comments sheet rises | 11 f (370) | `bezier(.7,.6,.6,1)` ≈ | cy 65% → 73% H | [MEAS] V15 A21 cy rmse .048 |
| **caption-word-in** | newest caption word enters | 6-10 f | `bezier(.2,0,0,.9)` | opacity .25 → 1 (+ blur 4 → 0 [EST]) | [MEAS] V01 only (16 f); Family B "fade" [EST] — tune in pilot |
| **italic-wipe** | Playfair italic word reveals left → right | 10-25 f | `bezier(.7,.6,.2,.9)` ≈ | clip 0 → 100% | [MEAS ≈] V13 A06 |
| **blur-rise** | generic card/banner entrance | 15-45 f | `EASE_OUT` | blur 10 → 0 px, y +40-60 → 0, opacity 0 → 1 | [EST] 9 reels |
| **defocus-bridge** | A-roll blurs behind a floating element | 12-20 f in, 12-20 f out | ease-out | A-roll blur 0 → 10 px [EST] | [OBS] 6 reels |
| **red-ellipse** | hand-drawn loop around a word | 11-15 f | linear stroke draw | stroke-dashoffset 1 → 0, 10px `signal.red` | [OBS] [EST timing] |
| **strike + arrow** | old price struck, arrow to the new one | 8 f + 11 f, then new price pop 14 f | linear; pop `bezier(.7,0,.2,1.1)` ≈ | strike draw; arrow draw; new price scale .9 → 1 (≈ 3% overshoot), green | [OBS] V15; pop [MEAS ≈] |
| **wall-build** | 12-60 cards fill a grid | 30-40 f | ease-out per card | delay 1.2 f × (row + col); scale .8 → 1, blur 6 → 0 | [EST] V05 |
| **wall-zoom-out** | reveal more cards | ≈ 30 f | ease-in-out | scale 1 → 0.4 | [OBS] V12 |
| **carousel-step** | category card swap | step every 45-54 f, dissolve 12 f | ease-in-out | blur-dissolve to next card | [MEAS ≈] V12 A11 |
| **reel-strip-scroll** | thumbnails behind the head | continuous | linear | 1 card per 30-45 f leftward | [OBS] V13-V15 |
| **proof-zoom** | zoom into the key detail | 26-80 f | ease-in-out (linear for slow pushes) | scale 1 → 1.8-3.5 toward the detail | [MEAS] V01 2.0× (cut), V11 1.8× in 2.7 s; others [EST] |
| **hold-push** | anything held > 3 s | duration of the hold | linear | scale 1.0 → 1.04 | [INF] (keeps "nothing static") |
| **drum-roll words** | single white words on the full blue ground (Inter SemiBold ≈ 64px, last word Playfair Italic ≈ 80px) | 15 f per word | hard cut | last word italic | [OBS] V14 |
| **giant-word open** | verdict word | 53 f (1770) | `bezier(.2,.9,.6,.6)` | width 72% → 89% W (letter-spacing open) | [MEAS] V11 A06 rmse .042 |
| **spring-pop** (small objects only) | icon, pill, swatch | 14-20 f | `SPRINGPOP` ≈ | scale .4 → 1, peak ≤ 1.25× | [MEAS] V01 A24 (18.9%), V02 peak 1.24× |
| **footage→card** (optional opener) | A-roll shrinks into a rounded card on the blue or light ground | 28-62 f | `bezier(.2,.4,0,1)` | scale 1 → 0.48-0.63, radius 0 → 4% W | [MEAS] V01, V04 ≈ |

## Experimental (off by default; only if Rishi asks)
Font-cycle word (2 f per font), orbit ring (163°/s decaying), cylinder carousel, hologram icons, glass glow panels, flicker title, gradient type-on, 3D post push (rotateY −8°), countdown ring, iris wipe (3 f), particle burst. Sources: V01, V02, V04, V06, V10.
