# Kashish Malhotra reel

The house style for Kashish Malhotra's talking-head reels: flat motion graphics on white, and captions that rise into a black pill one word at a time, timed to the voice. Use it for every reel, cut and overlay pass.

## Content fundamentals

- Captions say exactly what was spoken, in order. Fix mis-heard words from the transcript (for example "tabbed purse" → "capped purse"); never reword or retime.
- One line at a time, about 20 characters (3–5 words). Sentences break at . ? !, clauses at a comma once a phrase has two words, and any pause over 0.35s starts a new line.
- Numbers stay as spoken: "27 crore", "39%", "₹9.3 lakh". Any word holding a digit or % shows in yellow.
- No emoji, no exclamation marks added, sentence case as spoken.

## Visual foundations

- **Colour:** `ground` white canvas, `ink` black for every line, icon and outline, `accent` #FED300 for the one key value in a frame. Captions: `caption-text` white on `caption-pill` #0A0A0A, highlights in `caption-highlight`. The caption-only overlay pass sits on `chroma-key` #00FF00 and nothing else.
- **Type:** Avenir LT Pro, the `caption` family. Captions are `caption-word`: Heavy 58px on a 1080×1920 canvas, letter spacing −1.5%, word gap 0.26em. Graphic labels are `label-kick`, small uppercase Heavy.
- **Layout:** 1080×1920. The caption pill sits from y 1416 to 1528 (`cap-top`, `cap-height`), centred, clear of the bottom 18% app UI. Motion graphics stay between y 230 and 1330.
- **Shape:** the pill is 112px tall with 30px corners (`cap-radius`) and 42px side padding (`cap-pad-x`). It grows to fit each phrase, up to `cap-max-line` 880px, then the font shrinks to fit.

## Motion

Every caption move uses `cap-ease`, a cubic ease-in-out: no bounce, elastic or overshoot.

1. Each word rises `cap-rise` (64px) from below, masked by the pill, and fades in. It starts `cap-word-lead` (0.12s) before its SRT time and settles over `cap-word-rise` (0.32s).
2. When the next phrase starts within 0.6s, the old line lifts `cap-exit` (46px) and fades in `cap-line-swap` (0.18s), while the pill's width changes to fit the new phrase over `cap-pill-morph` (0.32s).
3. After a pause over 0.9s, the pill fades out `cap-hold` (0.45s) after the last word, scaling to 96% over `cap-pill-out`. It returns over `cap-pill-in` (0.28s), scaling from 94%.

The **RisingCaption** component does all of this from an SRT: see its guidelines.

## Green-screen pass

For editing, render the same captions with the same timing on a flat `chroma-key` canvas, with no other element. Its pixels match the main pass apart from the antialiased edge of the pill.
