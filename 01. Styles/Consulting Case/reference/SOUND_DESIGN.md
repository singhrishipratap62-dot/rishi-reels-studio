# SOUND_DESIGN (v1.5)
Reference only: SKILL.md wins on any conflict.
**[R1.10] supersedes v1.0 "voice only".** Rishi wants SFX. Use the sound rules of `01. Styles/Minimal Edit/reference/SOUND_DESIGN.md` (sound only, never its visuals) with the library in `01. Styles/Minimal Edit/sfx/`. Built by `engine/sfx.py`.

## Principle
Lots of sound, each one quiet. Every element that enters the board gets a sound. Captions are silent [R1.12]. Peaks are aligned to the visual event (measured peak time per file in `sfx48/info.json`).

## Trigger map (board grammar → Minimal Edit sounds)
| Visual event | Sound | Target peak |
|---|---|---|
| Opening blur-in resolves (~0.55 s) | Woosh | −17 (+3 opening lift) |
| Cut S2 → S3 (into board) | Woosh | −17 |
| Client question box appears | Hi-Tech Click (trim 450 ms) | −17 |
| Phase switch (board clears, question moves up) | Swoosh | −16 |
| Big count-up number (M05) | Hi-Tech Click | −17 |
| Icon draw-on (M04) | Highlighter | −20 |
| Bar / years bar segment / range fill / highlight strip (M06) | Highlighter, at each segment start | −19 |
| Q/A pills, fact values, placeholders, ✗, results "= ₹X" | Pop different | −19 |
| Floor / ceiling / answer marker lands (M09) | Riser + Tick (tick on landing) | −19 |
| Reference (grey) marker, labels, chips, other text | Modern technology pop | −21 / −22 |
| Tab activates / greys out (M10) | Mouse click different | −22 |
| Unit grid (M07) | multi flicker | −23 |
| Board → end card | Swoosh | −16 |
| Caption words / hook word darkening | **nothing** [R1.12] | — |
| S1 → S2 punch-in cut | nothing | — |

Rules: within 110 ms the louder cue wins. +3 dB on every cue in the first 5 s, easing to 0 by 6 s.

## Voice + program
75 Hz HPF → 2.5:1 compression at −24 dB (15/180 ms) + 4 dB makeup → limiter −1.5 dBFS → voice to −15 LUFS → mix SFX stem → program trimmed to **−15 LUFS, true peak ≤ −1 dBTP**. R006: −15.1 LUFS, TP −1.0, LRA 2.9.

## Music bed [R1.15]
Rishi supplies the track in `05. Asset Library/music/`. Added after the 1.2x speed-up (music itself not sped), starting past the track's quiet intro (R006: 0:15). Level calibrated to **13 dB under the voice** while speaking [R1.16; 21 dB was inaudible], light sidechain duck (threshold 0.1, ratio 2, 60/450 ms), 1 s fade-in, 2 s fade-out. Program −15 LUFS, true peak ≤ −1 dBTP via 4x-oversampled limiter. R006: −15.1 LUFS, TP −1.4, LRA 2.4.

## Limiting + ducking notes [E1.14, E1.18, E1.19]
AAC adds ~0.3–0.5 dB of true peak: without music, limit the mix at −1.6 dBFS. With the music bed, sample-peak limiting at 48 kHz still left +0.1 dBTP, so limit at 4x oversampling (aresample 192k → alimiter −2.0 dB → 48k). The cut has almost no pauses, so a voice-keyed duck is either always on or useless: set the bed level against the voice under speech (GAP, now 13 dB per R1.16; E1.19's 21 dB is superseded) and keep the duck light (threshold 0.1, ratio 2).

## Deliver
`sound_cue_sheet.md` (time · sound · peak · reason) in the project folder. Rishi listens on a phone; measurements aren't a listening check.
