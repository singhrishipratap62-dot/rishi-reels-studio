# RisingCaption

Word-by-word captions that rise into a black rounded pill, timed to the reel's SRT, with any number or % in yellow.

## Use it

1. `KMReel.RisingCaption.wordsFromSrt(srt, {"tabbed":"capped"})` splits each cue's time across its words by length, fixing mis-heard words.
2. `phrasesFromWords(words, filmEnd)` groups them into one-line phrases.
3. `mount(stage, phrases)` builds the layer inside a 1080×1920 stage and returns `render(t)`; call it every frame with the time in seconds. It is a pure function of `t`, so it scrubs and exports frame-exact.

The host supplies the 1080×1920 stage (scaled to fit as a whole), tokens.css and the Avenir LT Pro fonts. Nothing else.

## Rules

- **Phrases:** one line, about 20 characters (3–5 words). Break after . ? !, after a comma once a phrase has 2+ words, or at a pause over 0.35s. A sentence-ending word may join a phrase up to 26 characters so it isn't left alone.
- **Words:** each rises `cap-rise` (64px) from below inside the pill's mask and fades in, starting `cap-word-lead` (0.12s) before its SRT time and settling over `cap-word-rise` (0.32s) on `cap-ease`. No bounce.
- **Between phrases:** when the next phrase starts within 0.6s, the old line lifts `cap-exit` (46px) and fades in 0.18s while the pill's width morphs over 0.32s.
- **Pauses:** after a gap over 0.9s the pill fades out `cap-hold` (0.45s) after the last word, scaling to 96%; it returns in 0.28s from 94%.
- **Place:** pill top at `cap-top` (1416px), 112px tall, 42px side padding, 30px corners, centred. Keep motion graphics above y 1330.
- **Colours:** caption-text white on caption-pill; words with digits or % in caption-highlight.
- **Green-screen pass:** the same layer, same timing, over a flat `chroma-key` canvas, nothing else on it.
- Fix transcript errors in the words, never retime them.
