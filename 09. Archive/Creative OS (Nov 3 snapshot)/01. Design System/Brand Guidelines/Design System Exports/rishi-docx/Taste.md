# Taste rules

What Rishi has approved and rejected in review. **Read this before you design any motion graphic, and check every frame against it before you hand anything over.** These rules come from real feedback (October 2026, the "OpenAI recorder" reel) and override anything softer elsewhere in this system.

## Never do these

| Don't | Do instead |
|---|---|
| **Red pen circles**, on anything: words, numbers, objects, devices, map pins, question marks, list rows. | Highlight the word or label (Key line or The point bar). For an object, sweep a red-tint wash (`signal-marker`) behind it and set a solid-bar label beside it ("A small device"). For an unknown or a mystery, use the **marching dotted square** (below). |
| **Rubber stamps** ("ARRESTED", "CONFIRMED", "FAKE") slammed on with a shake. | A literal visual of the idea (jail bars dropping over the date) plus the word on a solid `signal-deep` highlight bar. |
| **Diagonal, rotating, shaky exits**: an object flying off on a slant or tumbling out of frame. This reads as AI-made motion. | **Lift-and-fade**: the object rises 60–100px straight up (`ease-smooth`, ~0.6s) and fades out on the way. Or it shrinks slightly in place and fades. |
| **Text over graphics.** No line of text may sit on top of a drawing, map, chart, building, badge or device, even for a moment, even half-faded. | Give text its own clear area: headline band at the top (y 250 to ~520), caption band at the bottom (see *Captions* below), and graphics between. If space runs out, move the graphic, never overlap. |
| **Crop marks / corner ticks on every frame.** | Rare: the end card, or one framed plate where they add something. When they appear, nothing (text or graphic) may touch them. |
| **Zooms and pushes that drift off-centre.** | Every scale and camera push is anchored to the exact centre of the thing being zoomed (or the frame centre, 540 px on 1080). Build windows and cards symmetric about x = 540 so a push stays centred. |
| **Text-only frames, black and white only.** | Every frame carries a touch of red: a highlight bar, a tint wash, a red-tint ring. Not a red fill everywhere, but never a frame of pure ink on paper. |
| **Literal "light beam" from one thing onto another** to show analysis or scanning. | Dotted probe lines from the source to specific points on the object, each point pinging once with a small red dot as it is "read", with a tint wash behind the object. |
| **Tilted pairs.** Two things being compared at different angles, or an equals sign that sits off their midline. | Comparisons are symmetric: same size, same baseline, mirrored about x = 540, the `=` / `vs` exactly on the shared midline. |
| **One lonely line of fake code** to mean "encryption" or "data". | Three or four lines of code that slide in opposite directions, underlined with a red pen stroke and labelled (`ENCRYPTED`). |

## Things that land well (repeat these)

- **Marching dotted square.** A box around a mystery (a question mark, an unknown person) turns into round red dots that travel around the square's edge. Rishi's favourite device for "we don't know".
- **Dot maps that twinkle.** Map dots breathe softly at slightly different phases (opacity 45–100%, ~0.5 Hz), then a red pin drops on the place and the place name gets a highlight.
- **Calendar flips.** A date never just appears: the tear-off page flips through the days before it (6 → 7 → 8 → 9), each flip about 0.35s apart (never more than 3 per second).
- **Glitch blip on a photo.** A portrait or ID photo "blips" twice: it jumps 8px sideways while a red-tint copy shows offset for ~0.15s. Use for "this is the person".
- **Propagating waves with a red outer ring.** Sound or talk shown as ovals rippling outward from the source; the outermost oval sits still in a light red tint with four tick marks at its compass points.
- **Things building on the voice**: timelines drawing, radar sweeps, networks lighting node by node, a bar filling across two days, a vault wheel spinning before the door opens.
- **Containers sized with breathing room.** Something inside a container (a card inside a vault, a screen inside a phone) sits at about 85% of the space, never filling it edge to edge.

## The hook

The first 3 seconds must be the most scroll-stopping frame of the reel:
- Headline in Bricolage Grotesque ExtraBold (800), 104–120px, 2 short lines.
- The key word on **The point** bar (solid `signal-deep`, paper text) sweeping on as it is spoken.
- A strong visual already on screen at frame 0, with its own clear area: the hook text and the hook drawing never overlap.

## Fonts, every time

- **Headlines, hooks, big numbers: Bricolage Grotesque** (700–800). Never General Sans for a headline.
- **Everything small** (labels, kickers, captions, UI text): General Sans.
- **Gambetta**: the "concept" or punchline phrase only ("a brain.", "a spy movie"), often in signal red at 120px+.

## Captions (motion graphics with voiceover)

- Always on, in **English** (a faithful rendering of a Hinglish voiceover), 3–6 words per chunk, changing on the voice.
- **Animation:** each word rises in from below (about 38px, ~0.3s, ease-out), staggered ~60ms per word. The chunk fades quickly at its end.
- **Colour:** dark text on light grounds, light text on dark grounds. No pill, no box. If the ground under the captions changes mid-scene (a letterbox bar slides in), the caption colour flips with it.
- **Place:** General Sans Semibold 46px, centred, bottom edge at y ≈ 1490 (just above `safe-bottom`). The band y 1395–1490 is reserved for captions: every scene's own text and graphics end above y 1390.
- **Talking-head reels, split frames:** the captions sit in the graphics half, bottom edge at y ≈ 936 (just above the green screen), never on the green where Rishi is speaking. Graphics move up to make room. In full-green frames they go back to the normal band in light text with a soft shadow. See *Talking-head layout*.

## Sound effects

Built as a separate SFX stem that starts at 0:00 with the voiceover, sitting about 8 dB under the voice. Map sounds to motion, sparingly: highlighter sound on every highlight sweep, swooshes on dives and lifts, pops and soft clicks on things appearing, typewriter on typing and code, an old-camera click on calendar flips, a camera shutter on photo blips, a riser into the single biggest reveal and a low drop on its landing.

## Before you hand it over: check every scene

1. Does any text touch a graphic, or any graphic touch the caption band?
2. Is there a red circle anywhere? Replace it.
3. Is there a stamp, a diagonal exit, or a tilted comparison? Replace it.
4. Are crop marks on this frame, and do they need to be?
5. Does every zoom anchor on the centre?
6. Is there a touch of red (highlight, tint, ring) in the frame?
7. Headline in Bricolage?
8. Talking-head reel only: does it open in split, stay off the green, keep split captions in the graphics half, and change frame often enough that nothing is static for more than ~3s?
