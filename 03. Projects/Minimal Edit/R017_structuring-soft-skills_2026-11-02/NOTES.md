# R017 · "Structuring is just 30–40%" · build notes

**Current revision:** draft 1 (visuals only, no sound design): `R017_Structuring_draft1.mp4` (1080×1920, 30 fps, 37.8 s).
- Source: Reel 017 from `Experimental Podcast/Mock_Case_Automobile_Servicing`, episode 00:38:20.33–00:39:09.30, cut to `assets/source_clip.mov`.
- Editable project: `R017_Structuring.tsrct`. Rebuild everything with `.tesseract-work/build.py` from `.tesseract-work/v0_base.tsrct`.
- Word timings: `transcript/words.json`. Onsets placed on measured speech segments; neither the episode SRT nor whisper.cpp timings were reliable here. Not checked by ear.

## Defaults used (not asked up front; the user asked to go straight to a draft)
- Split screen kept, as in the approved First Principles edit; captions on the seam band over a gradient scrim.
- Instagram Reels safe zone. The build's audit reports every element inside.
- No music. No SFX yet: sound design comes after visual approval (SOUND_DESIGN.md).

## Edit
- Trims: the opening "But yeah,", pauses over 200 ms (down to ~120 ms), and the candidate's overlapping "Yeah" / "I see" / "yeah yeah OK". All trims fall on scene boundaries, under graphics, or on zoom cuts.
- Scenes:
  1. A-roll: *pretty well* → *good thing* → *case solving*.
  2. White text-centric: *composure* → line → COMMUNICATION.
  3. A-roll: *really good.*
  4. Dark graph: STRUCTURING; the bar fills to 30, then 40 % on the spoken numbers; the rest fills white → *softer skills.*
  5. A-roll: *doing well* → *major thing* → *lack in.* → *brainstorming*.
  6. Black line + text: *new ideas* → QUESTIONS → *more relevant*.
  7. A-roll: *a lot of time* → *ideas* → *not work out*.
- Zoom cuts at 107 / 104 / 108 / 112 / 108 / 114 %, plus a +1.2 %/s push on every A-roll segment.

## Checks done
- Key-frame filmstrip (`Previews/draft1_keyframes.png`). Black-frame detection: none.
- Export loudness: −23.7 LUFS integrated, −4.3 dBTP. Not normalised; that happens in the sound pass (target −15 LUFS).

## Open questions / uncertain
- "rest is the softer skills": "rest" is heard by whisper only; the SRT drops it.
- 0:19 ("doing well in the … major thing"): whisper hears "structure"; not captioned.
- The candidate's "OK, fair enough" still overlaps Kashish's "where" at the start of the stages scene (can't separate them).

## Sound pass v1 (2026-11-02)
Current: `R017_Structuring_v1_sound.mp4`. Visuals are unchanged from draft 1.
- **Voice:** `assets/audio/voice_clean_v1.wav`, using the same chain as First Principles (recipe in `assets/audio/RECIPE.md`): 75 Hz high-pass, 2.5:1 compression at −24 dBFS, +13 dB, −1.5 dBFS limiter. No noise reduction needed (pause floor −61.6 dB). It's placed as Audio layers that mirror every footage cut, and the footage's own audio is off.
- **Effects:** 90 cues, all from the SFX library. Full list in `sound_cue_sheet.md`:
  - 20 Hi-Tech Clicks (−17), one on every impact word.
  - 57 flicks (−27 to −29), one per support word, skipped within 110 ms of a bigger cue.
  - 8 Highlighters (−19 to −21): link line, bar outline, the three bar fills, and the spine draw plus its two extensions.
  - 3 Wooshes (−17), one on each cut into a graphic scene.
  - A multi flicker (−23) as the graph grid switches on.
  - A Riser + Tick (−19) as the bar completes.
  - +3 dB on every effect in the first 5 s.
- **Music:** none supplied.
- **Mix:** whole-mix trim 0.92. The export measures −15.3 LUFS integrated, −1.6 dBTP true peak, LRA 3.3 LU.

### Checks
- **Placement:** effects-only render. All 17 cues with no neighbouring cue in a ±150 ms window peak within ±15 ms of the cue sheet. Cues that overlap can't be measured individually; the median deviation across all 90 is 5 ms. No cue falls past the end.
- **Lip sync:** voice cross-correlated against the source at 6 points: +5 ms everywhere (correlation 0.86–0.92).
- **Not checked by ear:** levels are set by measurement, so listen on a phone.

## Music v1 (2026-11-02)
Current: `R017_Structuring_v2_music.mp4`. Visuals and effects are unchanged from v1 sound.
- **Brief:** the user picked "compose an original bed" and asked for "John Harris-style" music. I read that as Johnny Harris (the documentary explainer YouTuber) and confirmed nothing further; check this.
- **Track:** `assets/audio/music_bed_v1.wav`, composed by `.tesseract-work/music.py`. Original, no third-party audio. Recipe in `assets/audio/RECIPE.md`; spectrogram in `Previews/music_bed_v1_spectrum.png`.

| Edit time | Section | Music |
|---|---|---|
| 0:00–0:06.6 | praise | warm pad + soft 8th-note pluck arpeggio |
| 0:06.6 | white scene | arp moves to 16ths |
| 0:12.2–0:14.5 | graph | sub + ticking hats enter; riser builds into the **30% reveal (0:14.5)**, with a low hit on it |
| 0:18.2–0:26.5 | A-roll | hats and sub drop out, so it breathes |
| 0:26.5–0:33.0 | stages | sub + hats return, arp brightest |
| 0:36.4 → end | close | resolves to F major and fades with the picture |

- **Mix:** the bed is about 19 dB under the voice (≈ −34 LUFS in the mix) and pre-ducked up to −5 dB whenever Kashish speaks. Program: −15.3 LUFS integrated, −1.7 dBTP, LRA 3.2 LU.
- **Not checked by ear:** I can't listen here. The structure is checked on the spectrogram and the levels by measurement.
