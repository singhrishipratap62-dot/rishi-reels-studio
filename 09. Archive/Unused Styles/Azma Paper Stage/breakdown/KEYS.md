# KEYS.md — her named keys (A7 style study)

Source: work/keys/INDEX.md (A5), 23 motion strips (A6), 16 full-res type frames (`work/a7/type_sheet_*.jpg`).
Example stills for each key: `breakdown/keys/<key>/` (copied by time range from `keys.tsv`).
Share of runtime (all 15 videos, ~35 min): A-roll ~50 %, fs-object ~19 %, broll ~19 %, fs-data ~7 %, onscreen-pop ~2.5 %, camera ~1 %, half-screen <0.5 %.

## Changes to the §5 scheme (A5 review)
- **hook is a position, not a scene type.** Her first 5 s use the same keys as the body (mostly K04 + K06/K16). Treated in PLACEMENT.md.
- **chapter-ui: none.** She never uses numbered chapter markers.
- **fs-text does not exist on its own.** Text always sits in a scene with a prop (K04 inside K06/K16). Kept only as K04 rules.
- **half-screen: one video only** (v1 podcast clips). Low priority key K21.
- **"camera"** = colour/grade beats on A-roll (K02, K03), not real camera moves. She has no whip-pans or 3D camera moves; every full-screen graphic has a slow constant push/drift instead.
- A5 boundaries were by time range, so ~5–10 % of stills in `work/keys/captions/` are really cutaway frames near edges. Not worth re-sorting; refs come from `breakdown/keys/`.

## Animation types actually used (second axis)
| code | animation | where |
|---|---|---|
| A1 blur-in | element/clip enters blurred (≈12–20 px) and sharpens in 2–4 frames, opacity 0→1 | every fs scene entry, A-roll return, article screenshots |
| A2 ink-reveal | word appears as light-grey "ghost", then darkens to ink as it is spoken (word-by-word, synced to VO) | all headlines, quote cards |
| A3 slide-blur | object slides in from an edge (mostly bottom or left) with motion blur, fast-out/soft-landing, no bounce | props, cut-outs, cards, car lower-thirds |
| A4 stack-in | items enter one after another with ~4–6 frame stagger, each A3 | folder tabs, candles, album sleeves, tyres, face stickers |
| A5 drift | constant slow push-in (scale ≈1.00→1.05 over the scene) or slow pan | every full-screen graphic + article |
| A6 counter-roll | numbers/leaves/reels flip or roll to a final value | calendar leaves, slot machine, timeline years |
| A7 highlight-sweep | blue bar wipes L→R behind a sentence, text turns white | articles |
| A8 grade-snap | A-roll snaps to greyscale (with brief blur), then hard cut back to colour | mono-beat |
| A9 pixel-mosaic | big grey pixel blocks frame or wipe a clip | memes, transitions |
| A10 glitch-cut | 2–4 frames of data-glitch / pixel-corrupt between clips | colour broll, A-roll return |
| A11 cursor-click | pixel-art arrow cursor moves in, clicks (item scales 0.95 and changes colour) | UI mocks, buttons, tabs |
| A12 hard-cut | plain cut, no transition | caption swaps, meme in/out, most cuts between scenes |

There is **no** scale-bounce/overshoot and no draw-on in her style. Motion is soft and fast; the "life" comes from A5 drift + A2 ink-reveal.

## A10 outcome (Rishi)
- Active set for his edits: K01, K02, K04, K06–K11, K15–K20. On request only: K03, K14. Dropped: K05, K12, K13, K21, K22.
- Fonts: Inter (+ Playfair Display accent) instead of Poppins; details in NOTES.md.
- Brand-coloured pieces (K18, K19) get their colours agreed per video.

## The keys
| key | scene type | animation | what it is | frequency | A10 status |
|---|---|---|---|---|---|
| K01 caption-whisper | captions | A12 | tiny lowercase white caption, 1–4 words, top-centre, swaps per phrase | all A-roll | keep (caption below chin) |
| K02 focus-return | camera | A1 (+A10 sometimes) | A-roll comes back from a cutaway blurred → sharp in ~3 frames at 24 fps | after most cutaways | keep |
| K03 mono-beat | camera | A8 | A-roll goes greyscale for a sarcastic/reaction beat; caption hidden or one centred word ("Congratulations", "Great decision"); sometimes orange handwritten scribble ("Good Hook") | ~1 per video | on request only |
| K04 ink-headline | (text system) | A2 | small Poppins Light grey lead-in line + big Poppins Medium word(s) in ink; next word shows as ghost first | in nearly every fs scene | keep (+Playfair accent) |
| K05 gold-tag | (text system) | A3 wipe + A2 | key word set on a cream→gold gradient label under a light lead-in; word coloured (blue / black / green) | ~2 per video | DROPPED |
| K06 paper-stage | fs-object | A1/A3 + A5 | white void + one coloured "floor" plane (yellow, mint water, teal, dark-red felt, black road) + one hero prop (3D render or pixel-art), soft grey drop shadow | core look, 4–8 per video | keep |
| K07 avatar-cutout | fs-object | A3 | her own cut-out, greyscale with red hair kept, or a cartoon avatar of her, placed in a paper-stage | ~2 per video | keep |
| K08 face-sticker | fs-object | A4 | real person's face cut out, thick outline (gold/green polygon), on stick-figure / bobblehead / pixel body, pixel "deal with it" shades; groups as totems or network graphs with name tags | people stories | keep (+head wiggle) |
| K09 cursor-click | fs-object / fs-data | A11 | pixel arrow cursor clicks icons, menu items, buttons, tabs | ~1 per video | keep (gradient pixel cursor) |
| K10 stack-in | fs-object | A4 | folder tabs / album sleeves / cards / tyre cards enter one by one, one per item spoken | lists | keep (Rishi fonts) |
| K11 counter-build | fs-object | A6 + A4 | number grows physically: calendar leaves flipping 1…12, cash stack rising, slot reels, brick towers on a map | money / time stats | keep (smooth, synced) |
| K12 mono-meme | broll-text | A12 (+ A5) | B&W meme/film clip full-screen, ~1.5 s; optional bold white caps caption (often Hinglish), "X BE LIKE:" | 4–10 per video | DROPPED |
| K13 mosaic-meme | broll-text | A9 | B&W meme with grey pixel-block bands top/bottom or pixel wipe | ~1–2 per video | DROPPED |
| K14 colour-broll | broll-text | A12 / A10 | real colour footage (product, race, anime), 0.7–1.5 s cuts, no text | topic-dependent (cars, F1, anime) | on request only |
| K15 article-highlight | fs-data | A1 + A5 + A7 | article/news screenshot (light or dark), blur→sharp, slow push/scroll, blue highlight sweeps the quoted sentence | 1–4 per video | keep (+sharp zoom on key words) |
| K16 chart-build | fs-data | A4 + A2 | pixel candlesticks / bars build one by one with pixel coin emojis + K04 headline | money videos | when needed |
| K17 ui-mock | fs-data | A3 + A11 | clean UI mock-ups (post menu, chat box, Notes window, phone wallet, Instagram) on white/lavender, mint accents | tech videos | keep, frequent |
| K18 quote-card | onscreen-pop | A1 + A2 | translucent teal-gradient rounded card over A-roll lower half, mint tab label + pixel flower pin, quote ink-reveals in white; also the series end-card ("Part 2 … COMING SOON") | 0–1 per video, near the end | keep (bg darken, brand colour asked) |
| K19 object-lowerthird | onscreen-pop | A3 + shine | cut-out product (car, trading card) slides in over A-roll lower third on a red-gradient rounded base with mint name pill; light sweep across | product videos | keep (colours asked) |
| K20 timeline-rail | onscreen-pop | A6 | teal vertical ruler at left edge, dark translucent year pill with pixel flower that rolls to new years as the story moves | chronology videos | keep (A-roll or white) |
| K21 podcast-split | half-screen | A12 | other person's clip top half, hers bottom; yellow caption pill on guest | rare (v1) | DROPPED |
| K22 today-card | fs-object | A3 | the "and today…" topic card right after the intro: her cut-out holding a sign, red gradient card "Today's Story", or "Part 02" title card | 1 per video at ~10–18 s | DROPPED |
