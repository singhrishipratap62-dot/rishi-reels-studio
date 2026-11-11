# SOUND DESIGN — Daniel Priestley Editing Style (v1.0)

Claude cannot hear. Everything here is **measured**, and the meaning of each measurement is **inferred**. Rishi must listen and correct (see §5).

## 1. What was measured and how
- 4 intros (first 60 s) of R01, R18, R22, R24 — the densest edit sections.
- **Stem separation failed** (Demucs model download blocked/hash mismatch in sandbox), so analysis is on the **full mix** (skill fallback). Tools: librosa HPSS percussive onsets, ffmpeg ebur128 / silencedetect / astats. Script: `tools/style_audio.py`; raw output `.work/audio/*.json`.

## 2. Results
| Metric | R01 | R18 | R22 | R24 | Read [INF] |
|---|---|---|---|---|---|
| Integrated loudness (whole video) | −15.7 LUFS | −16.9 | −17.1 | −26.6 | Most sit ≈ −16/−17 LUFS (R24 is an outlier upload) |
| Loudness range (LRA) | 2.5 LU | 2.0 | 2.2 | 5.9 | Very compressed, broadcast-steady voice |
| True peak | +0.1 dBFS | −1.9 | −3.9 | −3.1 | R01 clips; ceiling not consistent |
| Silences < −45 dB ≥ 0.25 s (60 s intro) | 0 | 0 | 1 | 0 | **A bed never drops out** — continuous music/ambience under voice |
| RMS floor (p10) vs median (p50) | −35.8 / −20.7 dB | −35.3 / −21.3 | −32.1 / −20.6 | −44.3 / −28.7 | Bed ≈ **14–16 dB under** speech |
| Strong percussive onsets / s | 0.55 | 0.27 | 0.32 | 0.38 | Low — not an SFX-heavy edit |
| Visual cuts hit by an onset within ±100 ms | 0/11 | 0/13 | 0/13 | 1/19 | **Cuts are not punctuated with whooshes/hits** |
| Typical onset character (median) | 580 ms long, attack 232 ms, centroid 2.1 kHz | 592 / 119 / 2.3 k | 598 / 308 / 2.0 k | 563 / 168 / 2.1 k | Soft swells/whoosh-like, mid-bright; slow attack (not clicks) |
| Name-sting window level vs video | ±0 dB (R01) | — | — | +3.7 dB (R24) | Possible sting swell in R24; unverified |

## 3. Cue groups (for matching once a library exists)
`assets/sfx` was **empty** at build time — no file matching was possible. Rows below are the targets to match against later.
| Visual event | Cue group | Target character | Level | Timing | Status |
|---|---|---|---|---|---|
| Everything | Music bed | Continuous, unobtrusive; under voice | ≈ −14 to −16 dB below dialogue | Never drops out; no sudden stops | measured (presence) / unverified (genre) |
| Name sting M01 | Soft swell/whoosh | ~0.6 s, attack 150–300 ms, centroid ~2 kHz | ≤ dialogue level | Peak on band sweep | unverified |
| Chapter arc wipe M02 | Soft whoosh | same family | well under dialogue | on wipe | unverified (no onset alignment measured) |
| Chip/pill pops M05 | Light tick/pop (optional) | short, bright | quiet | on each chip | unverified — not detected |
| Hard cuts | **none** | — | — | — | measured (≈0 hit rate) |

## 4. Rules for the edit skill
1. Voice first: dialogue normalised, steady (LRA ≈ 2–3 LU). Deliver at workspace spec **−14 LUFS** (Rishi's export spec overrides the refs' −16/−17). [R1.0 via CLAUDE.md]
2. One continuous music bed ≈ 15 dB under voice; duck nothing abruptly. [MEAS]
3. Do **not** add whooshes/hits on ordinary cuts. [MEAS]
4. Optional soft swell on the name sting and chapter wipes only, after visuals are approved. [INF]
5. Sound only after visuals are approved (skill gate).

## 5. Listening step (Rishi)
Listen on a phone to R01 00:55–01:05 (name sting), R24 00:44–00:50 (sting + arc wipe), R16 05:57–06:01 (pill pops), any 30 s of A-roll (music bed genre/level). Log corrections in LESSONS_LEARNED as `[R1.x]`.
