# Sound design: Rishi v2

> Minimal-style "lots of sound, each one quiet" `[ME]`, approved with Rishi's note: make swooshes **longer and smoother** `[R]`. Code: the cue system in `engine/build_template.py` (`cue()`, `audio_layers()`). Library: `assets/sfx/` (trimmed WAVs + `sfx_meta.json`).

## 1. Voice
- The rough-cut audio was already mastered (≈ −13.9 LUFS, TP −7.7). Only a 75 Hz high-pass + −1.5 dB → `voice.wav`, imported as its own Audio layer. The A-roll video layer stays silent (no doubled voice).
- If a future rough cut is raw: 75 Hz HPF → 2.5:1 compression at −24 dBFS → makeup → limiter −1.5 dBFS `[ME]`.

## 2. Cue map
| Event | Sound (`assets/sfx/`) | Target peak in mix |
|---|---|---|
| Caption hero (first letter) | `hitech` | −17 dBFS |
| Each support / caption word, list row, doc line | `flick` (±1 dB variation; skipped within 110 ms of a bigger cue) | −27 to −30 |
| Big transitions (pane drop/lift, wall zoom, sheet rise/drop, card swaps, PiP in/out) | `swoosh_long` / `woosh_long` (full length, 0.25 s fade-in), **peak on the move's midpoint** | −17 to −21 |
| Card settles | `pop` | −20 to −24 |
| Ticks | `techpop` (`hitech` for key ticks) | −19 to −20 |
| Highlighter swipe, line → rect openings, progress fill | `highlighter` | −20 to −23 |
| Progress hits 100 % | `risertick` | −20 |
| B&W snap, wall settle, doc morph | `flicker` | −21 to −24 |
| Send / key presses | `click` | −20 to −24 |
| Prompt typing | `typing` | −25 |
- **First 5 s +3 dB** on every effect, easing back to normal by 6 s.
- Align each file's **peak** (from `sfx_meta.json`) to the visual event; the gain is computed from the measured peak.
- ≈170 cues in 33 s is normal for this style.

## 3. Mix targets
- Final program ≈ −15.5 LUFS (window −16 to −14), true peak ≤ −1 dBTP (reached −7.2).
- Measure the final MP4, not the stems.

## 4. Checks and deliverables
- **Effects-only render** with the voice muted (`engine/tools/fx_check.py`): every cue-sheet time must have energy within ±60 ms.
- Deliver `sound_cue_sheet.md` (time · sound · peak · reason).
- On request: `<name>_sfx_only.mp3` + `<name>_voice_only.mp3` (`fx_check.py --mp3`), 320 kbps, aligned to 0:00.
- Claude can't listen. Say levels are set by measurement and ask Rishi to check on a phone.
- No music bed so far; ask for a licensed track before adding one (≈20 dB under the voice if used).
