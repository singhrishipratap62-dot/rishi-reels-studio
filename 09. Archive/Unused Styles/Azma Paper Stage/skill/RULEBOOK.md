# RULEBOOK.md — Paper Stage rules (v1.0)
Sources: breakdown/PLACEMENT.md (A8), NOTES.md (A9), A10 review. Canvas 1080×1920.

## 1. Rhythm and density
| | target |
|---|---|
| graphics share of runtime | **40–45 %** (her refs ~50 % incl. memes, which Rishi dropped) |
| graphic length | 1.5–3.5 s (median 2 s); 6–12 s only for article reads, lists, counters |
| A-roll between graphics | 2–4 s typical, **never > 8 s** in the body |
| first graphic | **≤ 2 s** (cut away after the first words of the hook) |
| hook (first ~8 s) | most graphic-dense part: ≥ 60 % covered, a cut every 1–1.5 s |
| outro (last 10–20 s) | ≤ 1 graphic, then plain A-roll to the end |
| repeats | the same key at most twice in a row; alternate full-screen and on-A-roll |

## 2. Structure
1. **Hook:** 0.5–1 s A-roll with caption → the hook claim full-screen (K04 big word = the key number/name, inside K06/K11/K16).
2. **Intro line** (who he is / what this is): plain A-roll.
3. **Body:** cell of ~6–8 s = fact graphic (2–4 s) → A-roll (K02 return) 2–4 s → next graphic.
4. **Close:** one K06 that restates the thesis literally, optional K18 quote card with the key line, then A-roll.

## 3. Trigger map (SRT line → key)
| the line has… | use |
|---|---|
| number, money, %, date, stat | K04 with the number as big word, in K06 / K11 (growth) / K16 (trend) |
| a person named first time | K08 face-sticker (or K07 if it's Rishi), name in K04 |
| a product/brand he keeps talking about | K19 lower-third over A-roll, else K06 with the product as hero prop |
| "according to / reported / announced / said" | K15 article, highlight = the exact sentence |
| a list of 2–6 items | K10 stack-in, one item per spoken word (K09 cursor if they're UI items) |
| an AI tool, app or website | K17 mock-up of that product's UI (+ K09 cursor) |
| years / chronology | K20 timeline-rail (on A-roll or white) |
| a metaphor / "imagine…" | literal illustration in K06 (+ K07 Rishi cut-out) |
| the thesis / a quotable line | K18 quote card (usually last 20 s) |
| opinion, bridge, reaction, joke, intro, closing question | **plain A-roll** |
Rule of thumb: no number, name, quote, list, product or picture-able metaphor → A-roll.

## 4. Timing against speech
- Cut **in** on the trigger word (or 2–3 frames before); cut **out** on the first word of the next sentence.
- Words inside graphics follow the VO (A2 ink-reveal): each word turns ink when spoken.
- Exits are hard cuts. Entries use blur-in or slide-blur. The A-roll comes back with K02.
- Captions only while Rishi is on screen; graphics carry their own text.

## 5. Captions (K01, Rishi variant)
Inter Regular 40–44 px, white, faint shadow, lowercase as spoken with punctuation, 1–4 words / ≤ 20 chars, one line, hard swap per phrase. Position: centred, top of text at `chin_y + 0.02` from `face.json`, clamped to 0.50–0.80 of frame height; keep clear of graphics/cards (if K18/K19 is on screen, move caption above the card or hide it).

## 6. Fonts
Inter (Light lead-ins and ghosts, Regular captions/body, Medium–SemiBold big words, Bold/Black labels); Inter Tight Black (names, caps display; Black Italic for "shout" lines); Playfair Display italic for one accent word, max one per scene. Patrick Hand only as handwriting inside notebook props; Helvetica/Arial only for scribble notes.

## 7. Palette (approved)
ink #1E1E1E · lead #6E6E6E · ghost #CFCFCF · paper #FFFFFF / #F6F4FA · mint #8ED9BF · teal #3FA884 · deep-green #1E5B47 · gold #E6C873→#F7EDCC · yellow-floor #E9C95A→#F4E3A1 · red #D23C4C→#5C1A24 · highlight-blue #1F5FD6 · card-teal #2C6A5E→#A7D8C8 · pill-dark #2E2E2E@70 %. Brand pieces (K18, K19): colour asked per video.

## 8. Motion defaults
- Entry: 4–6 frames, blur 16→0 px, opacity 0→1, ease cubic-bezier(0.2,0.8,0.2,1). Slides add 40–120 px travel + motion blur. No bounce, no overshoot.
- Drift: every full-screen scene scales 1.00→1.05 linearly over its length (or a 30–60 px pan).
- Ink-reveal: ghost #CFCFCF → ink over 6 frames, triggered at the word's start time.
- Stagger: 4–6 frames between stacked items.
- Living elements: face stickers wiggle (±2–4°, 3–6 px bob, 1.5–2.5 s loop, random phase).

## 9. Look rules
- Full-screen scenes: white paper, one floor plane, **one** hero prop + max 2–3 small accents, soft grey contact shadow, headline in the empty third.
- Pixel-art touches (cursor, coins, small squares, clouds) are the signature texture; use 1–2 per scene, not everywhere.
- People cut-outs greyscale (Rishi's own cut-out may keep one colour accent).
- Text never covers the face on A-roll.

## 10. QC before render
□ graphic share 40–45 % · □ no A-roll stretch > 8 s · □ first graphic ≤ 2 s · □ every number/name/quote in the script has a visual or a reason not to · □ every big word inks on its spoken word (±2 frames) · □ captions under chin, never over a card · □ only Inter/Playfair (+ exceptions) · □ K18/K19 colours approved · □ articles are real, highlighted sentence = spoken sentence · □ ends on A-roll · □ SFX per SOUND.md, none on exits.
