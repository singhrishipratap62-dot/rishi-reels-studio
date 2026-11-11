# R018 · Mental maths shortcuts · build notes

**Current revision:** v2 (revised visuals + sound): `R018_MentalMaths_v2_sound.mp4` (1080×1920, 30 fps, 79.0 s, −15.0 LUFS).
Earlier: draft 1 (visuals only), kept in `Versions/`.
- Source: `Minimal Edit Style/Mental Maths/IMG_4176.MOV` (90.7 s, 4K 60 fps HEVC), converted to `assets/source_clip.mov` (1080×1920, 30 fps).
- Editable project: `R018_MentalMaths.tsrct`. Rebuild everything with `.tesseract-work/build.py` from `.tesseract-work/v0_audio.tsrct` (footage, fonts, cleaned voice, SFX library), then `project commit` editable.json + `project apply` edits.json.
- Word timings: `transcript/words.json` (+ `words_table.md`, `transcript.srt`), from whisper.cpp base with DTW alignment, snapped to silencedetect boundaries. Not checked by ear.

## ⚠ Check by ear first
1. **0:37 · trick 3:** whisper hears "49 times 18 becomes **fifteen** times 18, which is 900". Only **50** × 18 = 900, so the graphic shows **50 × 18**. If Kashish actually said "fifteen", that line needs a re-record or a pickup.
2. **0:40 · "Number 4":** one whisper pass heard "Therefore" here. It's captioned "Number 4,".
3. Word onsets in the second half may run 0.1–0.3 s late (DTW drift), so caption reveals there may lag the voice slightly.

## Choices made (the user asked to go straight to draft 1, with no music)
- Single-speaker vertical, so captions sit at 56 % height over a soft lower scrim (white shirt). Instagram Reels safe zone; the audit reports every element inside, after push-ins.
- Structure: **announce → face, explain → show.** Each trick's name is on A-roll with a serif hero, and its working is a full graphic scene.

## Edit
- 29 trims: the 2.7 s head, and every pause > 200 ms cut to ~120 ms. Each trim is a zoom cut (100/108/103/111/105/113 %, anchored on the eye line) or sits under a graphic. +1.2 %/s push on all A-roll.
- Scenes (edit time):
  1. 0:10–0:16 **01 Flip** (white): 16% of 50 lakh = 50% of 16 lakh. The blue 16 travels across the rows, then *8 lakh* lands in a highlight box.
  2. 0:21–0:28 **02 Fraction anchors** (dark table): 1/8 → 12.5%, 1/6 → 16.7%, 1/7 → about 14.3%.
  3. 0:34–0:40 **03 Round, then correct** (black spine): 49 × 18 → 50 × 18 → = 900 − 18 → *= 882*.
  4. 0:43–0:50 **04 Split** (white): 15% of 640 branches to 10% = 64 and 5% = 32, which merge into *96*.
  5. 0:53–1:02 **05 Rule of 72** (dark graph): 72 ÷ growth rate; a 12 % curve doubles at *6 years*.
  6. 1:09–1:12 **Thesis** (white quote): "that's what sounds like *confidence* in a case interview."
- A-roll captions on the hook, each trick's name, the 120/840 example, and the close/CTA.

## Checks done
- Two review filmstrips (`Previews/draft1_strip_a.png`, `_b.png`). Fixed after review: the opening quote overlapped "that's", and the "12% a year" label sat on the curve.
- Safe-zone audit: all inside. Black-frame detection: none. ffprobe: 1080×1920, 30 fps, 78.97 s.
- Loudness of the export: −23.4 LUFS integrated, −0.9 dBFS peak. Not normalised yet; that's for the sound pass (target −15 LUFS, TP ≤ −1).

## Revisions (draft 1 → v2)
| # | Time | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 1 | all A-roll | captions + dark scrim too high | down at the mic | hero baseline 1080 → 1440, caption block centred at x 482 (clears the Reels icon column), hero ≤ 660 px; scrim now 1150 → frame bottom | done |
| 2 | 0:00–0:03 | no hook, motion not snappy | sudden zooms, premium but engaging | snap punches on the meaning words (14 of them, ~110 ms in, 1 % settle), wider zoom-cut alternation, text motion ~30 % faster, graphic scenes snap in 106 → 100 %, opening riser into "16%", 3-second timer ring | done |
| 3 | numbers | no highlighter | marker on 16%, 50 lakh, 3 seconds… | blue marker swipe behind 9 A-roll phrases + every key number in the graphics; dark scenes: blue band, white type; the swipe follows the glyph reveal | done |
| 4 | throughout | more animation | more moments | five shortcut dots, ghost numerals 01–05 behind each "Number N", "≈ 1/7" callback tag, answers land with an overshoot pop, bookmark icon on "Save this" | done |
| 5 | — | no sound | full sound design | see below | done |

## Sound pass v1 (with v2 visuals)
- **Voice:** `assets/audio/voice_clean_v1.wav` (recipe as R017: 75 Hz HPF, 2.5:1 at −24 dBFS, +13 dB, −1.5 dBFS limiter; pause floor −63.5 dB, no NR). Audio layers mirror every cut; footage audio is off.
- **Effects:** 198 cues from `Minimal Edit Style/sfx` (WAV copies in `assets/audio/library/`); full list in `sound_cue_sheet.md`. A Hi-Tech Click on every impact reveal, a flick on every support word, Highlighter on every marker swipe and line draw, a soft Woosh on each snap zoom and each cut into a graphic, Swoosh on the ghost numerals, pops on the dots, tag and bookmark, Riser + Tick on the timer ring and on each answer (8 lakh, 882, 96, 6 years), a multi flicker as the table and graph switch on, clicks on the quote marks. Moments with only captions: the opening Riser into "16%", a riser into "confidence", a low drop under "Save this". +3 dB on effects in the first 5 s. No music.
- **Mix:** whole-mix trim ×1.1. Export: −15.0 LUFS integrated, −3.9 dBTP true peak, LRA 2.5 LU.
- **Placement:** effects-only render. Highlighter ±1 ms, Woosh 0 ms, most flicks 2 ms, Hi-Tech Click −16 ms (at 48 kHz). The outliers are cues whose window catches a neighbouring long tail. Riser + Tick is a run of equal ticks, so its "peak" can't be measured. No cue past the end.
- **Lip sync:** voice cross-correlated at 5 speech points: 0 / −10 ms (corr 0.66–1.0).
- **Not checked by ear:** levels are set by measurement; listen on a phone.

## Next
- Notes from the phone listen and watch. On approval: final export to `exports/` (−14 LUFS IG spec in CLAUDE.md vs −15 in this system; confirm which).
