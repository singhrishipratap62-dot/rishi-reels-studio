# LOOKBOOK.md — how each key looks and is built (v1.0)
Canvas 1080×1920; timings at 30 fps (her refs 24 fps, same durations in seconds). Fonts/palette tokens from RULEBOOK §6–7. Refs: `refs/<key>/` (stills `v<vid>_t<sec>.jpg`, motion strips `strip_*.jpg` = 12 frames left→right, top→bottom).
Each section: **Look** · **Build** (layers + keyframes) · **Params** (what changes per use).

## K01 caption-whisper (A-roll)
**Look:** small lowercase white caption under the chin, one short phrase at a time.
**Build:** text layer Inter Regular 42 px #FFF, shadow 0 1 6 rgba(0,0,0,.25), centre x, top y = (chin_y+0.02)×1920 from face.json (interpolate between samples, smooth with 0.3 s lag, clamp 960–1536). Swap phrase with a hard cut at the phrase's first word. Group 1–4 words by natural phrase.
**Params:** phrase grouping; y override when a card is on screen.

## K02 focus-return (A-roll)
**Look:** A-roll comes back soft and snaps sharp.
**Build:** on the first 3 frames of an A-roll clip after a graphic: blur 20→0 px, scale 1.04→1.00, ease-out. Caption sharp from frame 1.
**Params:** none.

## K03 mono-beat (A-roll, on request only)
**Look:** A-roll snaps to black-and-white for a dry beat, frame wiggles following the nose.
**Build:** saturate 0, blur 12→0 over 3 frames, scale 1.08; position follows `nose` from face.json (offset = (nose − nose₀)×0.3, 4-frame lag) + tiny noise wiggle (±4 px, 1.2 s). Optional one word centred Inter Regular 80 px white with soft glow, or a Helvetica orange (#F08A24) 2-word note. Hard cut back to colour after 1–2.5 s.
**Params:** word; duration.

## K04 ink-headline (text system, inside full-screen scenes)
**Look:** small grey lead-in line above one or two big words; the next word waits as a pale ghost and darkens when spoken.
**Build:** lead-in Inter Light 44 px #6E6E6E; big line Inter Medium 150–170 px #1E1E1E, tracking −2 %, line height 0.9, max 2 lines × 1–3 words; lead:big ≈ 1:3.5. Each word starts as ghost #CFCFCF (Inter Light) ~0.3 s before it's spoken and inks over 6 frames at its timestamp. Place in the empty third: left-aligned x=72 or right-aligned x=1008 (opposite the prop), y 8–35 %. Optional one accent word in Playfair Display italic, or in highlight-blue / deep-green / red.
**Params:** words + timestamps; side; accent word.
**Ref:** `refs/K04-ink-headline/strip_candlestick-text_v2_1s.jpg` (frames 3–12 show the ghost→ink sequence).

## K06 paper-stage (full-screen object scene) — the core look
**Look:** white void, one coloured floor plane in perspective, one hero prop with a soft shadow, headline in the empty space.
**Build:** layers back→front: paper #FFF → floor plane (skewed quad covering lower 25–45 %: yellow-floor gradient, mint "water" with a 30 % mirrored reflection, teal, dark-red felt, black road, or beige ramp) → contact shadow (ellipse #000 18 %, blur 24) → hero prop (55–80 % width, PNG cut-out or code-drawn pixel art) → 2–3 accents (pixel coins, squares, clouds, stickers) → K04 text. Prop enters slide-blur from bottom or side (6 frames, 80–120 px, blur 16→0) or blur-in; accents pop in staggered 4 frames. Whole group drifts scale 1.00→1.05 over the scene.
**Params:** floor colour; prop; accents; text side.

## K07 avatar-cutout (inside K06)
**Look:** Rishi's own cut-out (greyscale, one colour accent allowed) or a cartoon avatar standing on the floor, often holding a prop or sign.
**Build:** PNG cut-out height 40–60 % of frame, 4 px white sticker edge optional, slides up from below 6 frames. Add a slow ±1.5° sway so it isn't dead.
**Params:** photo (ask Rishi), prop in hand.

## K08 face-sticker (people)
**Look:** real faces cut out with a thick outline on simple bodies (stick figure, bobblehead, pixel body), alive with small head wiggles; groups as totems, rows or networks with name pills.
**Build:** face PNG ~300 px, greyscale or colour, polygon outline 8 px gold #E6C873 or mint #8ED9BF; body drawn in code. Head wiggle: rotate ±3° + y bob 4 px, sine 1.5–2.5 s, random phase per sticker. Entry: pop-in staggered 4 frames (scale 0.9→1 with blur, no overshoot). Network: gold 2 px lines draw between stickers over 8 frames. Name pill mint, Inter Bold caps 36 px #10372A. Optional pixel "deal with it" shades.
**Params:** faces (photos needed), layout (row/totem/network), names.

## K09 cursor-click (UI)
**Look:** a chunky pixel-art arrow cursor with character, filled with a gradient (blue gradient or white→grey), clicking things.
**Build:** cursor drawn on a 16×22 pixel grid scaled to ~110 px (crisp, image-rendering pixelated), 1-px black outline, fill linear-gradient (#5B8CFF→#1F5FD6 or #FFFFFF→#BDBDBD). Path: ease-in-out curve 8–10 frames to target, 2-frame dip (scale 0.9) on click; target scales 0.95→1 and turns mint/green; 3–4 pixel sparkle squares burst.
**Params:** targets + click times (on the spoken word).

## K10 stack-in (lists)
**Look:** same-size items (folder tabs, album sleeves, cards, tyre cards) enter one per spoken item and stack.
**Build:** item i enters slide-blur from bottom or left at its word time, pushing the stack 24–40 px; labels Inter Regular/Medium (Playfair italic accent allowed); caption line at bottom (Inter Light lead-in + Inter Medium). Drift over the scene.
**Params:** items + times; item style.

## K11 counter-build (numbers that grow)
**Look:** the number is shown by something growing smoothly in sync with the VO — calendar leaves flipping, cash stack rising, slot reels landing, towers on a map — then the final value as a big word.
**Build:** growth eased (ease-in-out) from the number's first mention to its final spoken value; leaves flip ~3/s; stack adds layers every 3–4 frames; reels spin 0.7 s and land one by one 6 frames apart. Final value K04 big word. Keep the ref colours (mint/teal cash, gold, red, green).
**Params:** start/end value, object, sync points.

## K14 colour-broll (on request only)
**Look:** real colour footage, 0.7–1.5 s cuts, no text, 2–4 glitch frames between shots (RGB split + pixel blocks).
**Params:** clips from Rishi.

## K15 article-highlight
**Look:** real article screenshot blurs in, slowly pushes in while a blue highlight sweeps the quoted sentence; on the most important words a short sharp zoom punches in.
**Build:** screenshot full-width (light or dark), blur 20→0 over 6 frames; slow push scale 1.00→1.08 (or scroll up 60–120 px) linear; highlight rect #1F5FD6, height = line height + 4 px, wipes L→R at ~0.4 s per line synced to her reading, text above turns white. **Punch:** at the key phrase, 8–10 frame zoom to ×1.25–1.4 centred on the phrase (ease in-out cubic), hold to scene end. Optional source logo/headline at top, small photo or tweet inset.
**Params:** screenshot, sentence bbox, punch phrase.

## K16 chart-build (only when a chart is needed)
**Look:** pixel candlesticks/bars build one by one with pixel coin emojis, headline right-aligned.
**Build:** bars 110 px wide, red #D23C4C→#5C1A24 or green #3FA884→#1E5B47 gradients with a 6×6 px lighter pixel pattern, wick 6 px; enter from left staggered 4 frames with blur; coins (pixel, with small up/down arrow) pop on tips; group pans left 40 px over the scene. K04 right-aligned at top.
**Params:** data series (real numbers only), up/down colours.

## K17 ui-mock (tools, apps, websites — frequent)
**Look:** a clean recreation of the product he's talking about (chat box, menu, dashboard, phone screen), flat, rounded, light.
**Build:** window radius 28 px, 1 px #E3E7E5 border, soft shadow; panels with subtle mint gradient + fine dot texture; Inter UI text; product's real logo/colour where known. On white or lavender #F6F4FA. Enters slide-blur from bottom; menus/rows reveal staggered; K09 cursor drives interactions. Drift.
**Params:** product, screens/states, what gets clicked.

## K18 quote-card (on A-roll)
**Look:** translucent rounded card on Rishi's lower half; behind it his lower half darkens and blurs; tab label + pixel flower pin; quote words light up as spoken.
**Build:** backdrop: lower 50 % of A-roll gets blur 10 px masked by a vertical gradient + black gradient 0→70 % from the bottom. Card 780×(auto) px, radius 32, top at 64 % height, vertical gradient in the **brand colour** (ask; e.g. Anthropic orange) dark→light at 85 %; tab pill (lighter brand tint) with Inter Medium 40 px label + pixel flower overlapping its left end. Quote Inter Regular 42 px centred white, words 35 %→100 % opacity on their timestamps. Entry blur-in 5 frames; caption hidden while the card is up. End-card variant: tab "Part 2" + title + "COMING SOON".
**Params:** brand colour, label, quote.

## K19 object-lowerthird (on A-roll)
**Look:** product cut-out slides over the lower third on a rounded base plate, name pill pops above, a light sweep crosses it.
**Build:** base plate radius 24, gradient in the **agreed colour** (her ref: red #D23C4C→#5C1A24), wipes in from left 6 frames; product slides from left with motion blur 6 frames; white shine band (skewed, 40 % opacity) sweeps across in 10 frames; name pill Inter Bold caps 36 px pops 4 frames later; optional Inter Regular 32 px descriptor at left. y 60–80 %; caption moves above.
**Params:** product PNG, colour, name.

## K20 timeline-rail (on A-roll or white)
**Look:** thin teal ruler down the left edge with a dark year pill that rolls to the next year as the story moves.
**Build:** rail x=40, full height, teal #49B79A 6 px with tick marks every 24 px; pill #2E2E2E@70 % radius 6 with Inter Regular 60 px white year + pixel flower at left, y≈25 %. Year change: new year rolls up from below (6 frames), old fades down. White variant: same rail + pill on paper with K04 text beside it.
**Params:** years + times; background (A-roll / white).
