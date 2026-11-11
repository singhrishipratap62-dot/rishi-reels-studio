# Motion

The feel: **smooth, deliberate and in sync with the voice.** Every element eases in and eases out: nothing starts at full speed or stops dead. Things glide into place, then sit perfectly still. Scenes still cut hard. Nothing bounces, wobbles, spins or floats; the only overshoot allowed is a tiny settle on small accents. (Updated October 2026. These curves and timings override any older timings in component notes.)

## Motion styles

The curves and speeds are saved as tokens (`easing` and `duration`), so every graphic uses the same set and the whole system can be retuned in one place. Pick the style by **what the element is**:

| Style | Curve token | Speed token | Use for |
|---|---|---|---|
| Soft | `ease-soft` | `dur-normal` (big titles: `dur-relaxed`) | Text arriving: hook words, headlines, labels, quotes, numbers. |
| Smooth | `ease-smooth` | `dur-normal` (full frames: `dur-relaxed`) | Cards, frames, windows, diagram nodes, chart bars; anything relocating. |
| Settle | `ease-settle` | `dur-quick` | Small accents only: tags, ticks, pins, icons, role chips. Tiny overshoot, then rest. |
| Draw | `ease-draw` | `dur-normal` | Lines, leaders, connectors, rules, pen marks, highlight sweeps. |
| Cinematic | `ease-cinematic` | `dur-slow` or `dur-camera` | Camera push and pan, map zooms, reveal moments. |
| Exit | `ease-exit` | `dur-quick` | Anything leaving inside a scene. |
| Crisp | `ease-snap` | `dur-quick` | Rare: a deliberate hit on a beat. Not a default. |
| Voice | `ease-linear` | matched to speech | Typing, karaoke, read-along bars, counters' last digits, radar sweep, slow push-ins. |

**Speed tiers:** `dur-instant` 120ms · `dur-quick` 240ms · `dur-normal` 400ms · `dur-relaxed` 600ms · `dur-slow` 900ms · `dur-camera` 1600ms. To make a whole reel calmer or punchier, move every element one tier up or down together; don't retune elements one by one.

Overshoot (`ease-settle`) never goes on text, cards or frames. No motion blur except on a very fast word slide-in in a hook title.

## Durations by element

| What | Style · speed |
|---|---|
| Text, card, node arriving | Soft or Smooth · `dur-normal` |
| Big title, full frame, window | Soft or Smooth · `dur-relaxed` |
| Tag, tick, pin, icon | Settle · `dur-quick` |
| Ghost → ink (word lighting up) | Voice · `dur-instant` per word |
| Stagger between items in a group | 80–120ms |
| Line / leader / connector drawing | Draw · `dur-quick` to `dur-normal` |
| Highlight bar extending | Draw · `dur-quick`, or Voice matched to speech |
| Pen mark (underline, circle, arrow) | Draw · `dur-normal` |
| Typing | Voice · 25–40ms per character, or matched to the voice |
| Number count-up | `ease-soft` · `dur-slow` |
| Chart bars growing | Smooth · `dur-relaxed`, staggered 80ms |
| Camera push/pan on a graphic | Cinematic · `dur-camera` |
| Exit inside a scene | Exit · `dur-quick` |
| Scene change | Hard cut (0ms) |

## Sync to the voice

- **Arrival on the word.** Because elements now ease in, start the move 2–3 frames before the word so it *lands* as the word is spoken. Never seconds before.
- **Karaoke text.** When a sentence is shown in full, show it in `ink-ghost` first; each word turns `ink` as it's spoken, and key phrases get a `signal-marker` highlight sweeping left to right as they're said (see `KaraokeText`).
- **Holds follow the voice.** Spoken text can leave as soon as it's been said and the next beat starts. Text the viewer must *read* without it being spoken (a quote, a stat source, a list) holds at least 1.2s + 0.25s per word.

## Build orders

- **Graphic:** ground → frame (window, card, hairline box) → structure (axes, nodes, empty rows) → content arriving with the voice → annotation (tag, highlight, pen) last.
- **Annotation tag (`Callout`):** leader line draws from the target (Draw, `dur-quick`) → tag bar extends (Settle, `dur-quick`) → text types in (≈200ms). Exit in reverse, faster.
- **Diagram:** nodes appear one per sentence; connectors draw as the relation is named.
- **List / checklist:** rows appear empty first, then fill or tick one by one on the voice.
- **Split hook:** both halves visible at frame 0; title words arrive ≈100ms apart; release to full-screen with a hard cut or a 2-frame flash.

## Transitions

- **Between scenes:** hard cut on a word. Default.
- **Talking head → graphic:** hard cut. The graphic's first element should already be arriving in its first frame.
- **Reveal moments (before → after, "look what happened"):** a 2-frame white or signal flash cut, or a hairline scan-line wipe across the image (300–500ms).
- **Within a graphic:** content cross-fades or eases in; the frame stays put.
- **Camera:** slow push-in (1.0 → 1.08 over the hold) on static screenshots and footage frames so nothing is perfectly frozen. Every push and scale is anchored on the exact centre of what is being zoomed; never let a zoom drift left or right.
- **Objects leaving:** lift-and-fade (rise 60–100px straight up, `ease-smooth`, fading out), or shrink slightly in place and fade. Never a diagonal fly-off, a tumble or a shaky exit; that reads as AI-made motion.
- **Big verdicts** (arrested, banned, confirmed): no rubber stamps. Show the idea literally (jail bars dropping) and put the word on a solid highlight bar.
- **Dates:** a calendar page flips through the days to the date (≈0.35s per flip, max 3 flips a second).

## Patterns from reference set 2

| Pattern | How it moves |
|---|---|
| **Read-along** (`ReadAlong`) | Document arrives at full ink (Smooth, `dur-normal`), then everything except the current line drops to `ink-ghost` (200ms). The highlight bar grows across each spoken phrase with Linear easing at the speed of the voice, then jumps to the next phrase. Spoken lines stay highlighted until the sentence ends, then the whole highlight clears in 100ms. |
| **Focus by dimming** | In charts, tables and lists: the discussed item stays `ink`, everything else fades to `ink-ghost` (Smooth, `dur-quick`). Swap focus with a `dur-quick` cross-fade. Never animate the item itself. |
| **Ghost-to-ink title** | Serif or sans title words start `ink-ghost` and turn `ink` one by one on the voice (Voice, `dur-instant` per word). |
| **Tab label** (`TabLabel`) | Leader draws from the object (Draw, `dur-quick`) → box scales from its tab edge 0 → 100% width (Settle, `dur-quick`) → text appears (no typing; it's a name). Stagger multiple labels 120ms. |
| **Unit dots** (`UnitDots`) | Dots settle in left to right, 12ms apart (a 34-dot row lands in ~0.4s). Then the span bracket draws outward from its centre (Draw, `dur-quick`) and its label settles in. |
| **Digit-scramble counter** | For big counts from technical sources: digits cycle randomly for 400–600ms and lock left to right, 40ms apart. Use it for "machines hit", "rows leaked" — not for money or people (those use the smooth count-up in `StatReveal`). |
| **Radar sweep** (`RadarSweep`) | Rings draw out from the centre (Draw, `dur-normal`, staggered 80ms) → nodes settle on → the sweep wedge rotates continuously (one turn per 2.4s, Linear) → the readout ticks every 400ms. The only looping motion we allow, because it's showing something live. |
| **Globe / map to pin** (`DotMap`) | Dot field fades in → camera pushes into the region (Cinematic, `dur-camera`) → pin drops (Settle, `dur-quick`) with a 1-ring pulse once → coordinate tag extends → photo or logo card arrives beside it (Smooth). |
| **Echo backdrop** (`EchoBackdrop`) | Echo and card arrive together. The echo pushes slowly (1.0 → 1.06) while the card stays still — depth without floating. |
| **Beat word** (`BeatWord`) | Each word hard-cuts in on its syllable, no fade. Footage under it keeps its own push-in. |
| **Tilted terminal** | A terminal or code block rotated in perspective (≈ -12° X, 8° Z) scrolls upward at a steady speed (Linear) while new lines type at the bottom. For "it was running, quietly" moments only. |
| **Punch-in jump cut** | On talking-head cuts, alternate between two framings: wide (1.0) and tight (1.15–1.25, centred on the eyes). Cut on a word. Never zoom smoothly on the face. |

## Stillness

After an element lands, it doesn't move. No idle floating, pulsing or looping (except a blinking text cursor while typing, a loading spinner when the story is about waiting, or a `RadarSweep` showing something live). Held images and echo backdrops may carry a slow push-in; that's camera, not the element moving.

## Sound (not analysed in references)

Keep it subtle: a soft tick as tags and ticks settle, a light key sound on typing, a short whoosh only on flash reveals. Voice always on top. For full SFX stems (highlighter on highlights, old-camera click on calendar flips, riser + drop on the biggest reveal), see *Taste rules*.
