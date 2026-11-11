# Motion references, set 2

A second set of five reels Rishi chose (14 October 2026), studied frame by frame (338 of 453 extracted frames viewed; the rest were near-blank transition frames too small to matter). Same rule as set 1: **only motion, pacing, layout and graphic language are taken. Colours and fonts never are** — every reference colour below is translated into paper, ink and signal.

## What this set adds, in one paragraph

Set 1 taught *fast, voice-synced, framed*. Set 2 adds **editorial explainer craft**: a face-led reel where the cutaways are small, beautifully finished "explainer plates" — a serif concept title, a labelled diagram, a dot-built chart, a portrait card — each built in two or three steps on the voice. Real documents are *read along with* (a highlight bar walks down the lines as they're said, everything else dims). Big numbers count up with a tiny unit line under them. Things are named with small boxed tags that have a coloured tab. And it's all held together by restraint: plain grounds, crop-mark corners, lots of air.

## The five reels

**F — AI model launch explainer (split hook + documents).** Opens split: top half a plain white panel with the company mark and a serif-italic line ("…has finally"), bottom half the presenter. Then full-bleed cinematic stills with one huge white word per name. The middle is real material — the launch tweet, a benchmark chart, a pricing table, a phone showing the blog post — each *read along*: a solid highlight box walks across the exact words as they're spoken, the rest of the text dims to ~35%, and in charts every bar except the one being talked about fades. App windows sit on a giant, dimmed, blurred copy of themselves (an "echo" backdrop) so the frame is never empty. Small dark caption pills, 1–3 words, ~73% down.

**G — Science explainer (face-led, illustrated plates).** Talking head ~55% of runtime, with jump-cut punch-ins every few sentences. A persistent serif title sits over the top of the face for the first seconds ("…explained in under 2 minutes"). Cutaways are editorial plates: cream ground, tiny spaced uppercase kicker ("PHYSICS NOBEL · LAUREATES EACH YEAR"), serif headline, engraved-style illustration, and a **dot timeline** — one circle per year, a bracket reading "34 YEARS" spanning the gap. Navy diagram plates name every object with a **tab label** (white boxed uppercase tag, coloured tab on its left, hairline leader to the object). Huge condensed numerals with a serif unit ("65 billion") and a tiny spaced subline ("EVERY SECOND"). A globe rotates to a location and drops a pin. Serif headlines fade from ghost to solid word by word. Real b-roll goes in a **square card on a black ground** with the caption under it.

**H — Brand/history story (cinematic word-per-beat).** Graded, slightly desaturated footage inside a thin paper mat (like a printed photo). One word per beat, big, centred, condensed, white — "Something" / "Ridiculous" — with one word in the accent colour filling the width. Mixed type within a line: plain sans + script/italic ("In INDIAN *History*", "1,000 ₹ *Dinner*"). Flat-lay object collages that slide as a whole. Objects floating on black (coins, cards) drift slowly.

**I — Tech crime story (documentary + data motion).** Split hook (cinematic still on top, presenter below) with a three-tier title: light "one of the" / heavy "Worst Cyberattacks" / light right-aligned "in history". News article and Wikipedia page in a phone, headline read along with an inverted highlight. A name reveal inside a monitor frame ("Andres" → "Andres Freund", company line types in). Black-ground data graphics: a **radar sweep** with node icons on rings, binary trailing along spokes, and a live readout ("CPU 2.3%" with a sparkline drifting past a dashed "expected" line); a radial burst around a padlock with a red tag ("HIDDEN BACKDOOR") and a **digit-scramble counter** ("LINUX MACHINES 8,394,138"). A terminal tilted in perspective scrolling upward. Rain of numbers as a closing texture.

**J — Founder story (editorial pastel explainer — the closest match).** Paper ground with faint grain, crop-mark corners on every plate, a tiny spaced kicker between hairlines ("— THE PHENOMENON —"), serif title with an italic second line ("Schlep / *Blindness*"). Halftone-shaded objects (a sphere, a rocket nozzle with dimension lines, a launch photo turned halftone). UI cards with soft shadows: a tree of rows branching from one node, rows getting ticked; a padlocked slider ("PRIVATE LAUNCHES · NOT ALLOWED"); a stat card with a dot field and a line. **Portrait cards** — photo in a paper card over a halftone circle, serif name under it, small highlighted role tag. **Dot-matrix map** of India that zooms to a pin with a highlighted **coordinate tag** ("SRIHARIKOTA · 13.72°N 80.23°E"), a logo tile and a polaroid photo pinned beside it. A year written large in serif over a tick ruler with a marker ("UNTIL 2020").

## What all five share (new to us)

1. **Read-along on real sources.** Never show a whole document and hope people read it. A highlight walks the exact words being spoken; the rest dims.
2. **Focus by dimming.** In charts, tables and lists, the thing being discussed stays full ink; everything else drops to ghost. No arrows needed.
3. **Name things with tags, not captions.** Small boxed uppercase labels with a hairline leader name every object in a diagram, a map, a photo.
4. **Count with dots.** Quantities and spans of time are drawn as rows of dots (one per year, one per person), with a bracket naming the span.
5. **The explainer plate.** Kicker → serif concept title → one illustration or card → caption pill. Built in 2–3 steps, held 2–4s.
6. **Faces carry more of the reel.** In face-led explainers the presenter is 40–60% of runtime, kept lively with punch-in jump cuts and a title over the face for the opening seconds.
7. **Echo, mat and card framing.** UI over a dimmed echo of itself; footage in a paper mat; b-roll in a square card on ink. Never raw, never unframed.
8. **Restraint holds it together.** Two type voices (sans + serif), one accent, plain grounds, crop marks.

## What we adopt, and how it's translated

| Seen | In rishi.docx |
|---|---|
| Highlight walking across tweet/article text | `ReadAlong` — `brand-ink` bar (paper text) or `signal-marker` swipe; rest in `ink-ghost` |
| Window on a blurred enlarged copy | `EchoBackdrop` |
| Boxed tags with a coloured tab | `TabLabel` — signal tab, paper box, ink text |
| Dot timeline with "34 YEARS" bracket | `UnitDots` |
| Serif concept titles with italic second line | `ConceptTitle` (third approved use of Gambetta, see README) |
| Portrait in a card over a halftone circle | `PortraitCard` |
| Dot map zooming to a pin + coordinate tag | `DotMap` |
| Radar sweep + live readout + sparkline | `RadarSweep` |
| One big word per beat over footage | `BeatWord` |
| Pricing/benchmark table with row focus | `DataTable` |
| Persistent title over the face for the first seconds | `TitleOverFace` |
| Digit-scramble counter, focus-by-dimming, globe-to-pin, tilted terminal, punch-ins | *Motion* and *Pacing* sections |

## What we don't take

- **Pastel blush gradients, navy grounds, mint mats, yellow serif titles, lime accents.** Translated to paper/ink/signal. Grounds stay flat.
- **Condensed and script fonts.** "Condensed" big words become General Sans Semibold at tight tracking; "script" accents become Gambetta italic.
- **Monospace micro-labels.** Kept as General Sans uppercase, tracking 0.16–0.24em (two-font rule).
- **Cinematic AI stills as decoration.** Only when the image *is* the story, and inside a frame.
- **Floating/drifting objects and rain-of-numbers textures.** Our stillness rule stands: things land and stop. One exception — slow push-in on a held image.
- **Sub-32px text.** The references use tiny captions and tags; ours never go below 32px on a 1080 canvas.
