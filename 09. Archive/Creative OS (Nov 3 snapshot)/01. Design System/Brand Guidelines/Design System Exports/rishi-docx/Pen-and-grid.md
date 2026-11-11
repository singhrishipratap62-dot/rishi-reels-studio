# Pen and grid

The graphic language of rishi.docx: precise **structure** that organises the explanation, and a human **pen** in signal red that points at what matters.

## Structure

- **No background grid.** Frames are plain paper or ink. The 6-column grid is for alignment only and is never drawn. (Changed October 2026.)
- **Guide lines inside charts and diagrams only**: faint `line` colour, `stroke-hair` (2px), as value guides behind bars or a light pitch behind a diagram's nodes. They end at the chart's edge; they never fill the frame.
- **Rules**: `line-strong` or `ink`, `stroke-rule` (4px). Divide sections, underline a section label, form chart axes and timeline spines.
- **Numbered labels**: `label` style — `01`, `02`, `03` — on diagram steps, slides and list items. Optionally with a short tag: `01 · INPUT`.
- **Corner ticks**: short L-shaped marks at the corners of a diagram or image area, like crop marks. **Rare** (end card, one framed plate at most), and never touching text or another graphic.
- **Construction lines**: dashed `line` lines showing alignment or measurement (e.g. dimension lines on a chart). Use sparingly, for the "explained precisely" feel.

- **Technical ornaments**: small corner ticks on frames, crop marks around tags, a crosshair or a small four-point star in empty corners, dotted guide lines. Ink or `line-strong`, tiny, never more than 2–3 per frame. They make a frame feel precise and made-by-hand rather than templated.
- **Hairline frames**: real media (footage, screenshots) sits inside a `stroke-hair` frame with corner ticks and a small uppercase `label` at the top-left (`MediaFrame`).

## Annotation

Annotation is how the voice points. It belongs to both layers: the structure is the frame, the emphasis is pen.

- **Callout tag**: a hairline leader from the exact target to a small tag — `signal-marker` bar with ink text in `label` style, tiny crop marks at its corners. It names the thing ("this sounds robotic", "sweet spot"). See `Callout`.
- **Highlight**: see *Highlights* below. Swept left to right across words as they're said.
- **Magnifier**: a hairline box on the detail, connected by a hairline to an enlarged inset (`MagnifyInset`). Not a red circle.
- **Object emphasis**: a `signal-marker` tint wash sweeping in behind the object, plus a solid-bar label beside it. For an unknown or mystery: the marching dotted square (round red dots travelling around a square edge).
- **Selection**: one item in a set gets a `signal` 4px outline (`BentoGrid`), the others stay muted.

- **Tab label**: a small paper box with a hairline border, uppercase `label` text in ink, and a 10px `signal` tab on its left edge; a hairline leader to the object it names (`TabLabel`). For naming things in diagrams, maps and photos (`THE SUN`, `SOUTH POLE`, `AGNIKUL LAUNCHPAD`). Unlike a Callout, it names, it doesn't comment — so several can sit on one frame (up to 4).
- **Coordinate tag**: a tab label holding a fact in the format `PLACE · 13.72°N 80.23°E` or `DATE · 30 MAY 2024`, on a `signal-marker` fill. Precision as decoration.
- **Read-along highlight**: on real text (posts, articles, docs), the Follow highlight tracks the words being spoken (`ReadAlong`). Everything else on the frame goes `ink-ghost`.
- **Focus by dimming**: in a chart, table or list, the item being discussed stays full ink and the rest go `ink-ghost`. Often better than a pen mark — it adds nothing to the frame.

Max two annotations visible at once; remove the previous one when the next arrives. (Tab labels don't count towards this — they're names, not emphasis.)

## Dots and measures (reference set 2)

- **Unit dots**: count with dots — one 16px hollow ink circle per year, person or item, in aligned rows; the ones that matter filled `ink`, the endpoints filled `signal`. A bracket above the span carries a tab-style count ("34 YEARS"). See `UnitDots`.
- **Dot fields**: maps and large shapes drawn as a dot matrix (10–12px dots, 20px pitch) instead of solid fills. The region in focus goes full ink; the rest `ink-ghost` (`DotMap`).
- **Dimension lines**: on objects and diagrams, hairline measure lines with arrowheads and a small label (`A`, `Ø 1.2 M`) — the technical-drawing feel. Max one pair per object.
- **Tick ruler**: a hairline ruler with year ticks under a big serif year, a small ink triangle marking the moment ("UNTIL 2020").

## The pen

All pen marks: `signal`, `stroke-pen` (10px), round caps and joins, slightly irregular (hand-drawn, not geometric — a circle that doesn't quite close, an underline with a small lift at the end).

| Mark | Meaning |
|---|---|
| **Underline** | This phrase is the point |
| **Arrow** | This leads to that / look here |
| **Strike-through** | Wrong, myth, what people think |
| **Tick** | Right, what actually works |
| **Bracket** | These belong together |
| **Highlight** (three levels, see *Highlights*) | Any emphasis inside real text: articles, posts, docs, screenshots |

Rules:
- **One or two pen marks per frame, max.** The pen only means something if it's rare.
- The pen counts as the frame's signal moment — if there's a pen mark, the headline doesn't also get a red italic phrase in the same frame (unless the mark is on that phrase).
- Pen marks always animate on after their target, as one stroke.
- Never write words "by hand" — the pen marks, it doesn't write text.

## Highlights

Emphasis on words is **always a highlight, never a pen circle**: in real text (articles, posts, docs, screenshots, chat) and in motion-graphic headlines, labels and list rows too. **Pen circles are retired completely**, including on objects, numbers and nodes (October 2026): use a tint wash, focus-by-dimming or the marching dotted square instead.

**One shape.** A flat bar behind the words with very subtly rounded ends (`radius-highlight`, 6px at 1080), a little padding either side (4–6px), wrapping cleanly across lines. It sweeps left to right (Draw easing, or Voice/linear when it follows speech) and never fades in.

**Three levels, used in this order:**

| Level | Token | Text | Use for |
|---|---|---|---|
| 1 · Follow | `highlight-follow` | ink | Tracking the words being read out. |
| 2 · Key line | `signal-marker` | ink | The sentence that matters. One per frame. |
| 3 · The point | `signal-deep` solid | paper | The one phrase the viewer should remember. Max one per frame, and only after a level 1 or 2 has set it up. |

**Rules:**
- The text inside a highlight never turns red; the red sits behind it.
- A frame with a level 3 has no other signal moment (no pen mark, no red headline phrase).
- Levels can step up on the same line as the voice lands: Follow → Key line → The point.
- Lines that aren't highlighted drop to `ink-ghost` while a highlight is active.

## Combining them

A typical diagram frame: the label arrives → numbered nodes and connectors build on it → the key node gets a red-tint wash and its label a highlight bar (no circle). The structure says "this is how it works", the pen says "this is the part that matters to you".
