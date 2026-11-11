# gradnext motion explainer: building the video in Tesseract

Read this before building any reel from a script and voiceover. It is the approved production standard, distilled from the user's review rounds on R003 (McKinsey hourly rates, November 2026). The raw notes and what changed each round are in `FEEDBACK_LOG.md`. When this file and the "Visual cue rules" in `SKILL.md` disagree, this file wins.

Scope: use the gradnext design system and this skill only. Never borrow another editing style's look. The one exception is sound design: it follows Minimal Edit Style's `SOUND_DESIGN.md` and SFX library (user instruction, Nov 2026).

## 1. Inputs and setup

- Each reel folder (`Video Projects/IG gradnext 0NN/`) has a script `.docx` and an ElevenLabs `.mp3`. **The audio is the source of truth.** The script may not match the recording, and its feedback note may change a line, so always transcribe.
- Transcribe with `whisper-cli -ng -l en -ml 1 -sow -ojf` (word offsets; `-ng` because Metal is blocked in the sandbox). Every timing (captions, word reveals, scene changes) keys off these word offsets.
- Re-verify every on-screen figure from a primary source and keep the arithmetic in `.tesseract-work/NOTES.md`. The figures doc linked in a script may not be shared with this account.
- Project root: `Video Projects/IG gradnext 0NN/R0NN_topic_YYYY-MM-DD/` containing `R0NN.tsrct`, `Previews/`, `Versions/` and `.tesseract-work/`. Final render goes to the workspace `exports/`.
- Start from `templates/build_reel.py` and `templates/rebuild.sh`. Keep the helpers (`text(... words=...)`, `motion()`, `blur_fx()`, `row()`, `chip()`, `cue()`) and rewrite only the scene content. The project is regenerated from scratch on every change, so it always matches the script.

## 2. Look

- **Background:** the supplied loop `assets/gradnext-background-loop-9-16.mp4` (5 s, soft periwinkle glows and a fine dot grid), tiled as back-to-back Video layers behind everything. Do not hand-build a gradient background; a static gradient was "very bland", and my drifting-glow version was rejected in favour of this loop.
- **No topic tag.** A small-caps tag in the top-left corner ("CONSULTING FEES") reads as AI-generated design. Header = gradnext wordmark only, top right at about y 300, inside the 4:5 crop.
- **Type:** Avenir LT Pro Heavy for headlines and Black for hero numbers (tracking −40 to −55), Medium for labels and support text, and one Besley Italic phrase per scene in rhino-500. Social tracking is tight, but keep it balanced: on big statements, reduce letter spacing a little and tighten line spacing to roughly 0.95–1.05× (premium, not cramped). Check that lines never collide.
- **Colour:** rhino text, navy bars, periwinkle as the single highlight per scene, periwinkle-100 plates. Never periwinkle text on white.
- **Corners:** chips, plates and cards are rectangular with a very subtle radius (6 on chips, 8 on bars, about 12 on cards). Pill shapes were rejected as "too curved".
- **Bars:** a horizontal navy gradient from rhino to rhino-600, measured across the full chart width, so a longer bar reaches a richer blue. One persistent chart whose bars change length and order; never cut to a new chart.
- **Highlighter** (hero number, closing line): a bold periwinkle block at about 0.9–0.95 alpha over the **bottom 30–35%** of the glyphs. It runs from the first character to the last key character, then fades out over the tail (for example towards the "+"). It grows left to right with an ease in-out. The first version (about 0.6 alpha) was "good, but make it bolder".

## 3. Motion vocabulary (everything enters with motion; nothing just appears)

- **Word reveal (the default for all text):** each word slides up about 30–50 px out of a gaussian blur (14–22 px) while fading in, with an ease in-out over about 0.42 s. Use a text animator with a word-based range selector whose `start` is driven by a JS sum of eased per-word progress (see `text(..., words=[times])`). This applies to headline lines, labels, sub-lines, card text, the takeaway and the closing card.
- **Captions:** the same word reveal, timed to the spoken word offsets (0.28 s per word, smaller blur). Captions are the only on-screen event without a sound.
- **Headlines:** line by line (the second line about 160 ms after the first). They exit upward with blur and an ease-in before the next scene's lines enter.
- **Hero number:** drops from above, top to bottom, out of a heavy blur (about 40 px), counting up from a little below the target to the target (for example $940 to $1,000) and then locking. The "+" or unit arrives separately when the narrator says it, followed by the highlighter.
- **Bars:** grow with ease in-out `cubic-bezier(0.4, 0, 0.2, 1)`: a brisk start and a long soft settle. Values count up on the same curve and ride the bar end. Row labels reveal word by word as their bars start.
- **Colour change on a bar:** never a flat swap. A soft-edged periwinkle gradient wipe travels **right to left** with an ease in-out over about 0.9 s. It is clipped to the bar by a duplicate matte rect (an alpha track matte consumes its matte layer, so the matte must be a separate copy). It recedes right to left when the highlight leaves.
- **Re-sorts:** a gentle spring (about 0.7 s). Collapsing rows fade and blur out.
- **Cards and callouts:** slide in horizontally out of a blur (about 0.75 s), then the main figure reveals word by word, then the working line word by word.
- **Scene transitions** must feel continuous: the outgoing group lifts and blurs out (about 0.5 s, ease-in) while the next headline is already entering. No hard swaps.
- **Closing card:** "Follow for more" plus *consulting insights* revealed word by word with the spoken words. Then the half-height highlighter under *consulting insights* fades at its end, and the wordmark rises in out of a blur.

## 4. Sound design (Minimal Edit Style rules and library)

Principle: lots of sound, each one quiet. **Every on-screen event gets a sound except captions.** Align each file's measured **peak**, not its start, to the visual event. Set levels per cue as target peak dBFS, measuring each file's peak time and level once (`sfx-library.json`).

| Event | Sound | Target peak |
|---|---|---|
| Scene transition | Swoosh | −16 |
| Card slide-in, re-sort | Woosh | −17 / −18 |
| Hero line or hero word (headline line 1, hero number, key figure, takeaway, closing) | Hi-Tech Click, trimmed to 450 ms | −17 |
| Highlighter wipe, bar colour wipe | Highlighter | −18 / −19 |
| Bar growing (a line drawing) | Highlighter | −20 |
| Long bar landing (total) | Riser + Tick, tick on arrival | −19 |
| Chip or caveat plate | Pop different | −19 |
| Wordmark landing | Modern technology pop | −21 |
| Every support word, count-up step | flick, varied ±2 dB | −27 to −29 |

- Add +3 dB to all effects in the first 5 s, easing back to normal by 6 s.
- Drop any cue within 110 ms of a louder one (one family per moment).
- Convert the library MP3s to 48 kHz stereo WAV before importing. Write `sound_cue_sheet.md` with every build.

## 5. Tesseract gotchas (each one cost a revision)

- **Audio layer mapping:** `playback.mapping.input` must equal the layer's `inputRange` on the parent clock (`{start: t, duration: d}`), not `{start: 0}`. With `start: 0`, any cue not at time 0 is silent. The voiceover masked this in v1 and v2: every SFX was missing until it was fixed. After each export, check that the tail after the voice is not silent.
- A **zero-width rounded rect still draws a hairline.** Keep bars, mattes and highlighters at opacity 0 (hold keys) until they grow.
- Re-sort keyframes need a hold key at the move time; otherwise the row drifts for the whole interval.
- Fade values out the moment a bar starts collapsing (return '' when the phase target is 0); count-downs on collapsing rows look messy.
- Layer-blur effects make export slow (about 7–9 min for a 47 s reel). Use `--start-ms/--duration-ms` segment exports for checks.
- Tesseract's own mix lands near −18 LUFS. Deliver a two-pass `loudnorm` copy (I=−14, TP=−1.5) to `exports/`, with the video stream copied, and keep the editable mix unchanged.
- The `tsrct` binary lives in `~/Library/Application Support/Tesseract/bin/`, which the sandbox blocks, so run `tsrct` commands outside the sandbox.

## 6. Review before showing the user

1. Overview filmstrip (16 frames) plus full-resolution crops of the hook, a chart frame, any colour wipe mid-change, the callout and the closing card.
2. Check line collisions, slivers and hairlines, chip text fit, the loop seam (sample ±50 ms around each 5 s boundary), and the 4:5 crop for the hook and wordmark.
3. Export, then confirm the effects are audible (volumedetect on the tail after the voice). Measure LUFS and true peak and deliver the normalised copy.
4. Say plainly that you could not listen to the mix; ask the user to check it on a phone.
