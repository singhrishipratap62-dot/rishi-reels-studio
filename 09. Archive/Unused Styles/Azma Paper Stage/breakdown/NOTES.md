# NOTES.md — breakdown notes per key (A9, updated with Rishi's A10 review)

> **A10 rule:** her look is the reference, but builds use Rishi's fonts and his choices below. Where a key has an **A10** line, that line wins over the A9 notes.

All sizes for a **1080×1920** canvas (her files are 720×1280; multiply her pixels by 1.5). Colours are sampled by eye from stills: treat as starting values and confirm in A10/A11. Timings at 24 fps unless noted.

## Global tokens
**Fonts (A10 — Rishi's system, replaces her Poppins)**
- **Inter** does almost everything: Light (lead-ins, ghost words), Regular (captions, card text), Medium/SemiBold (big headline words), Bold/Black (labels, names). Inter Tight for tight display lines.
- **Playfair Display** is the accent font: occasional key word in a headline (K04), usually italic. Use sparingly.
- Name display ("HAMILTON"): Inter Tight Black caps by default (Rishi unsure; Playfair as alternative). Confirm per video if it matters.
- Heavy italic ("BEST THING EVER"): **Inter Tight Black Italic**.
- Handwriting inside notebook/journal props: **Patrick Hand** (prop texture only).
- Annotation scribble ("Good Hook"): **Helvetica** (fallback Arial) instead of a handwritten font.
- Rishi's stated preference: mostly two fonts (Inter + Playfair); Patrick Hand and Helvetica only in those two special cases.
- Size and weight ratios from A9 stay the same; only the family changes (Inter runs slightly wider than Poppins, so drop sizes ~5 % if lines overflow).

**Palette** (A10: all approved as picked; brand-coloured elements K18/K19 are chosen per video with Rishi)
| token | hex (approx) | use |
|---|---|---|
| ink | #1E1E1E | big headline words |
| lead | #6E6E6E | small lead-in line |
| ghost | #CFCFCF | word not yet spoken |
| paper | #FFFFFF (sometimes #F6F4FA lavender) | backgrounds |
| mint | #8ED9BF | labels, water floors, tags |
| teal | #3FA884 | rails, accents, green candles top |
| deep-green | #1E5B47 | green candles bottom, headline variant |
| gold | #E6C873 → #F7EDCC | gold tags, coins, beams |
| yellow-floor | #E9C95A → #F4E3A1 | floor plane |
| red | #D23C4C → #5C1A24 | red candles, product base cards, alert labels |
| highlight-blue | #1F5FD6 (text white) | article highlights, accent words |
| card-teal | #2C6A5E → #A7D8C8 at ~85 % | quote card |
| pill-dark | #2E2E2E at ~70 % | timeline year pill |

**Textures / motifs:** pixel-art (8-bit) props, pixel arrow cursor, pixel coin emojis, pixel flower pin (on cards, pills), green pennant/arrow icons beside names, 6×5 dotted grid, faint grid paper, soft grey contact shadows under every prop, B&W grade on all memes and on people cut-outs (except her red hair).

**Motion defaults:** entries 4–6 frames with blur 16→0 px and a soft ease-out (≈ cubic-bezier(0.2,0.8,0.2,1)); exits are hard cuts. Every full-screen scene drifts (scale 1.00→1.05 linear over the scene, or 30–60 px pan). No overshoot or bounce.

## K01 caption-whisper
- Inter Regular **38–44 px**, white #FFFFFF, faint shadow (0 1 6 rgba(0,0,0,.25)), lowercase as spoken incl. punctuation ("but after 2022,").
- Centre x, baseline at **~15 % from top (y ≈ 280 px)**, above her head. One line, 1–4 words / ≤ 20 characters.
- Phrase swaps are hard cuts on phrase boundaries (≈ 0.5–1.2 s each); no pop, no colour emphasis words.
- **A10:** in Rishi's videos the caption sits **near or just below his chin** (track the face; keep it clear of the mouth), not above the head. Only on A-roll where he is visible.

## K02 focus-return
- First 2–3 frames of A-roll after a cutaway: gaussian blur ~20 px → 0 with a slight scale 1.04 → 1.00. Caption appears sharp straight away.
- After colour b-roll she sometimes uses 2–4 frames of glitch (K14) instead.

## K03 mono-beat
- Cut to A-roll fully desaturated, blur 12 → 0 over 3 frames, slight punch-in (1.08×). Holds 1–2.5 s, then a hard cut back to colour (often a different framing).
- Optional centred word, Inter Regular ~80 px white, soft glow; or orange (#F08A24) handwritten 2-word annotation.
- **A10:** add a subtle frame wiggle driven by a **nose tracker** (small position/rotation follow, a few px). Rare: **only when Rishi asks for it.**

## K04 ink-headline
- **Lead-in:** Inter Light **40–50 px**, #6E6E6E, sits directly above the big line, left edge aligned with it.
- **Big word(s):** Inter Medium **140–180 px**, ink, tracking −2 %, line height 0.9. 1–3 words per line, max 2 lines.
- **Ghost word:** the upcoming word shows in #CFCFCF Inter Light at full size, then turns ink when spoken (~6 frames).
- Ratio lead : big ≈ 1 : 3.5. Placement: upper third (y 8–35 %), left-aligned at x ≈ 60 px *or* right-aligned at x ≈ 1020 px (opposite side of the prop); centred only for labels over a centred prop.
- Colour variants for the key word: highlight-blue, deep-green, red, mint.
- **A10:** Inter for lead-in and big word; sometimes one accent word in **Playfair Display** (italic).

## K05 gold-tag
- Rectangle ~ 50–60 % of width, height ≈ 1.4× text, vertical gradient gold #E6C873 (bottom) → #F7EDCC (top), thin darker top edge; no radius.
- Lead-in above it (Inter Light 44 px, #444). Word inside: Inter Medium ~110 px, highlight-blue (or black / green).
- Enters by a left→right wipe (5 frames), then the word ink-reveals.
- **A10:** pending. Rishi wasn't sure what this is; explained in chat (the gold label behind a key word, e.g. v7 "Mark did something **Very** interesting"). Use only if he confirms.

## K06 paper-stage
- White void; one perspective floor plane covering the lower 25–45 % (yellow, mint "water" with reflection, teal, dark red felt, black road, beige ramp).
- One hero prop 55–80 % of width, centred or bottom-right, soft grey contact shadow; 3D render or pixel-art. Max 1 hero + 2–3 small accents (coins, stickers, pixel squares, clouds).
- Headline (K04) in the empty upper third. Prop enters with A3 from bottom/side or A1 blur-in; scene drifts A5. Length 2–5 s.

## K07 avatar-cutout
- Her photo cut-out, greyscale with red hair kept, or a flat cartoon avatar of her (red curly hair). Stands on the floor plane at ~40–60 % of frame height, often holding a prop/sign. Thin white sticker edge optional.
- Enters slide-up from below (A3, 6 frames) or is already there with A1.

## K08 face-sticker
- Real face cut-out ~250–350 px, greyscale or colour, outlined with a 6–10 px gold or mint polygon border; on stick-figure, bobblehead, pixel or illustrated body. Accessory: pixel "deal with it" shades.
- Groups: totem stack, row of 7, or network with thin gold connector lines growing between stickers; mint name pills (Inter SemiBold caps 36 px).
- Stickers pop in one by one (A4, 4-frame stagger).
- **A10:** stickers must feel alive: each head **wiggles subtly** (rotation ±2–4°, bob 3–6 px, 1.5–2.5 s loop, random phase per sticker) so it reads as character animation, not a still image.

## K09 cursor-click
- Pixel arrow cursor (white/cream fill, black pixel outline), ~90–120 px. Glides in on a curve (8–10 frames), click = item scales to 0.95 and changes to mint/green, small pixel sparkle.
- **A10:** keep the cursor **pixelated with personality**, filled with a **gradient** (blue gradient, or white→grey). Rishi likes this detail a lot.

## K10 stack-in
- Same-size items (folder tabs, album sleeves with vinyl sliding out, tyre cards, carousel cards) enter one per spoken item from bottom or left, 4–6 frame stagger, each pushes the stack up/sideways. Labels Inter Regular on each item; caption line at bottom (Inter Light + Regular, white on dark base or ink on white).
- **A10:** keep the animation; labels/caption in Rishi's fonts (Inter, Playfair accent) instead of hers.

## K11 counter-build
- The number is shown by physical growth synced to the VO: calendar leaves flip (~3 per second), cash stack rises in layers, slot reels spin 0.7 s and land one by one, towers rise on a map. Final value appears as K04 big word ("$65 Billion").
- **A10:** growth must be **smooth and synced to the VO**; keep her colours.

## K12 mono-meme
- Clip fully desaturated, contrast +10 %, full-bleed (crop to 9:16), slow push. Length 1–2 s, hard cut in/out.
- Optional caption: Inter Bold CAPS **80–110 px** white with soft shadow, centred at y ≈ 50 % (single word) or stacked 2–3 lines left/right in the lower third; one word in a line may be bolder/larger. Fades in over 3 frames at cut + 2 frames.
- Format "X BE LIKE:" top-left in two lines.
- **A10: DROPPED.** Rishi doesn't use meme cutaways.

## K13 mosaic-meme
- Same as K12 plus bands of large grey pixel blocks (≈ 90 px squares, greys #555–#BBB) top and bottom, or a full pixel-block wipe in/out (4–6 frames).
- **A10: DROPPED.**

## K14 colour-broll
- Real footage in colour, 0.7–1.5 s per shot, no text, cut on beat; between shots 2–4 frames of glitch (RGB split, data overlay, pixel corrupt). Product footage can use a split-mirror wipe.
- **A10:** only **when Rishi asks** for b-roll; default is no b-roll.

## K15 article-highlight
- Screenshot full width (light or dark theme), starts blurred 20 px → sharp (6 frames) while drifting up/in (scale 1.0→1.08 or slow scroll). Headline/source visible at the top.
- Highlight: highlight-blue bar, height = line height + 4 px, wipes L→R across the read sentence at reading speed (~0.4 s per line), text inside turns white. Optional dark vignette.
- Embedded extras: a small photo, tweet, or her A-roll inset at the top.
- **A10:** sequence = enter with Gaussian blur → slow push + highlight → for the most important words, a short **sharp push/zoom** (≈ 8–10 frames, scale +15–25 %, strong ease-in-out) onto them, then hold.

## K16 chart-build
- Pixel candlesticks (red #D23C4C→#5C1A24, green #3FA884→#1E5B47, 6×6 px light pixel pattern inside), ~110 px wide, enter from the left one by one (4-frame stagger) with blur; pixel coin emojis (with small red/green arrows) pop on tips. K04 headline right-aligned top. Whole chart pans slowly left.
- **A10:** use only when the point needs a chart; treat it as the aesthetic reference (pixel pattern, coins, ink headline) for any data visual.

## K17 ui-mock
- Clean flat UI (rounded 28 px window, 1 px light border, mint gradient panels with fine dot texture, simple line icons). On white or lavender #F6F4FA. Teal swirl or pixel decorations in corners. Cursor clicks per K09.
- **A10:** used often: whenever he talks about a specific AI tool, website or app, build a clean mock-up of **that** product's UI in this style.

## K18 quote-card
- Over A-roll, card width ~72 % (≈ 780 px), centred, top at y ≈ 64 %, radius ~32 px, vertical gradient card-teal (dark top → light bottom) at ~85 % opacity.
- Tab label on the top-left edge: mint #8ED9BF pill, Inter Medium 40 px dark-green text (source name, e.g. "Anthropic" or "Part 2"), with the pixel-flower pin overlapping its left end.
- Quote: Inter Regular ~42 px white, centred, 3 lines max; words ink-reveal ghost (white 35 %) → white 100 % with the VO.
- Card enters with A1 (blur + fade, 5 frames) and stays until cut. End-card variant: "Part 2" tab + title + "COMING SOON".
- **A10:** behind the card, darken his lower half: blur + black gradient from the bottom (≈ 0 → 70 % black over the lower 50 %). **Card colour is asked before building**; recommend the brand's own colour (e.g. Anthropic → its orange) instead of teal.

## K19 object-lowerthird
- Over A-roll in the lower third (y 60–80 %): red gradient rounded base plate (radius 24 px) wipes in from left; cut-out product slides in from left with motion blur (6 frames), a white light sweep passes across it (~10 frames); mint name pill (Inter Bold caps 36 px) pops above. Optional small white description text (Inter Regular 32 px) on the left.
- **A10:** keep the motion; **colours are agreed with Rishi per video** before building.

## K20 timeline-rail
- Teal #49B79A vertical rail with tick marks at the left edge (x ≈ 40 px, full height), dark translucent pill (pill-dark, radius 6 px) with white Inter Regular ~60 px year and the pixel flower at its left, at y ≈ 25 %.
- When the year changes, the new year rolls in (A6) and the old one slides down and fades. Stays on through several captions.
- **A10:** works on A-roll or on a **white full-screen** version (no speaker); choose in planning. No b-roll beside it.

## K21 podcast-split
- Frame split horizontally at 50 %: other clip top, her clip bottom. Guest clip may carry a yellow (#F2D45C) caption pill with black text.
- **A10: DROPPED.**

## K22 today-card
- Paper-stage with her cut-out holding a yellow sign ("AND TODAY"), a red gradient card "Today's Story" sliding in with thin corner lines, or a series title card (gold tag "Part 02" + pixel letters + face stickers). 1–2 s, right after the intro sentence.
- **A10: DROPPED.**
