# Sound Design — v1.1

**Evidence level: medium.** v1.0 was inferred from the tutorial ("clicks for text, highlighters for graphs, whooshes for transitions", 74 SFX in a 57 s edit `[TX 17:46, OBS 17:48]`). v1.1 adds Rishi's direct notes on the first Tesseract edit `[R1.1]`. A sparse 27-cue mix was "average at best"; a dense 103-cue mix built mostly from his library was the direction. Levels are still set by measurement and need checking on a phone.

## Principle `[R1.1]`
**Lots of sound, each one quiet.** Every piece of text that enters gets a sound. The denser a layer, the quieter it is, so the mix has "essence and depth" without feeling like a lot. Impact text gets its own distinct sound.

## Source order
1. **Rishi's library: this pack's `sfx/` folder** (check it first) `[v1.2 path]`. Convert MP3s to 48 kHz WAV before importing, and measure each file's peak time and level.
2. Procedural accents (Tesseract `tesseract_sound.py`) to fill gaps, e.g. the long downlifter.
3. Music: only a licensed track the user supplies. Ask before the sound pass.

## Hierarchy (loudest → quietest)
1. **Voice.** About −15 LUFS integrated for the final program, peaks around −4 dBFS in the mix.
2. Transitions (Swoosh / Woosh / low impact): **−16 to −17 dBFS** peak.
3. Impact-word clicks (Hi-Tech Click): **−17**.
4. Line draws, highlighter, riser tick, block pops: **−18 to −21**.
5. Small markers, quote-mark click, UI flicker: **−21 to −23**.
6. Per-word ticks under support text (flick): **−27 to −29**, varied ±2 dB so they never sound mechanical.
7. Music bed (if supplied): about 18–24 dB under the voice, ducked 3–6 dB under dense speech.

Set **target peak levels in the mix** per cue rather than one flat gain: the library files sit near 0 dBFS, the procedural ones at −12.

**Opening lift:** add **+3 dB** to every effect in the first 5 s, easing back to normal by 6 s, for a livelier hook `[R1.1]`.

## Trigger map (v1.1)

| Visual event | Sound (library name) | Timing | Level |
|---|---|---|---|
| Impact/hero text (char reveal, M02) | **Hi-Tech Click** (trim to 450 ms) | peak on the first glyph | −17 |
| Every support word (M01) | **flick** | peak ~40 ms after the word starts rising; skip if within 110 ms of a bigger cue | −27 to −29 |
| A line drawing, **and every time it extends** | **Highlighter** | at each segment start | −19 to −21 |
| Highlight box wipe (M25) | **Highlighter** | box start | −18 |
| Line arriving at its destination | **Riser + Tick** | land the tick on arrival | −19 |
| Graphic → graphic transition | **Swoosh** | peak on the cut | −16 |
| Cut into a graphic scene | **Woosh**, or a low impact | peak on the cut | −17 |
| Blocks / pieces settling (M28) | **Pop different** | each piece settles | −19 |
| Marker dots, leader lines | **Modern technology pop** | on the pop | −21 to −22 |
| Quote marks appear (M26) | **Mouse click different** | marks in | −22 |
| Grid / UI switching on | **multi flicker** | as it appears | −23 |
| A value dropping (graph fall) | procedural downlifter, 1.4 s | start of the drop | −20 |
| A-roll ↔ graphic hard cut back to the face | usually nothing; the impact click covers it | — | — |

Unused in v1.1 but available: Camera Click, Camera shutter, old cam, Flash, Typewriter, charge, beep, drop (very bassy, 7.7 s), Riser, Music Box, Double-click, Mouse CLick.

## Rules
- **Align the sound's peak, not its file start**, to the visual event. Measure each file's peak once and store it.
- `[R1.2]` **Measure each library file's peak inside the trimmed window, in the mix.** In the series-intro edit (2026-11-03) the Hi-Tech Click `peak_db` (−9.6) carried over from the first edit was ~8 dB off for the 450 ms trim, so clicks played at about −23 instead of −15. Calibrate from an effects-only render.
- One family per moment: don't stack two cues within ~110 ms. The bigger cue wins.
- Sound confirms motion: nothing moves, nothing sounds. But in this style almost everything moves, so the mix is dense.
- **Voice chain that worked** on clean Riverside audio: 75 Hz high-pass → 2.5:1 compression at −24 dBFS (15/180 ms) → makeup gain → limiter at −1.5 dBFS. Skip noise reduction when pauses sit below about −55 dB.
- **Measure the final program, not the voice stem.** Pause trims raise integrated loudness by about 3 dB. Target −15 LUFS (−16 to −14) and true peak ≤ −1 dBTP.

## Verification (every sound pass)
1. Render an **effects-only copy** (voice muted) and check every cue sounds within ±60 ms of its cue-sheet time. Drop cues past the video's end.
2. **Cross-correlate the processed voice against the source** for lip sync (aim ≤ 10 ms; we got ±5 ms).
3. Measure integrated LUFS, true peak and LRA on the final MP4.
4. Deliver `sound_cue_sheet.md` (time · sound · peak level · reason) with the edit.
5. Ask Rishi to listen on a phone. Measurements aren't a listening check.
