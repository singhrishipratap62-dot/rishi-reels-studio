# SOUND.md — sound design for Paper Stage (A13, v1.0)
Library: `Azma's style/sfx/<folder>/` (Rishi's 22 files, sorted and renamed 2026-11-08; originals unchanged apart from name).
**Peak** = seconds from file start to its loudest point. To land a sound on an event at time T, start it at T − peak.

## Library
| folder | file | length | peak | character | use for |
|---|---|---|---|---|---|
| click | mouse-click.mp3 | 0.24 s | 0.06 | dry single click | K09 click (default) |
| click | mouse-click-2.mp3 | 0.27 | 0.19 | brighter click | K09 alternate (avoid repeating the same click) |
| click | double-click.mp3 | 0.27 | 0.19 | double click | K09 "open"/select, menu choice |
| click | hitech-click.wav | 1.76 | 0.10 | digital click + tail | K17 UI appearing, K20 year change |
| pop | pop-soft.mp3 | 0.34 | 0.12 | soft round pop | K06 accents, K08 sticker pop, K10 items |
| pop | pop-tech.mp3 | 0.13 | 0.06 | tiny tech pop | K16 candles/coins, K04 big word land (sparingly) |
| whoosh | woosh.mp3 | 1.99 | 0.64 | full whoosh | K06 hero prop slide-in, K15 punch zoom |
| whoosh | swoosh.mp3 | 1.23 | 0.57 | lighter swoosh | K19 lower-third, K18 card, K07 cut-out slide |
| whoosh | flick.mp3 | 0.24 | 0.09 | short flick | K11 leaf flips / reel stops, K10 fast stacks, K20 roll |
| riser | riser.mp3 | 1.71 | 1.52 | build-up | into the hook's big reveal (max once per video) |
| riser | riser-tick.mp3 | 1.93 | 1.21 | riser ending in a tick | K11 counter climbing to its final value |
| riser | charge.mp3 | 2.51 | 0.09 | charge-up hum | K16 chart rising / K11 long growth bed (low) |
| hit | drop.mp3 | 7.73 | 1.58 | bass drop / impact, long tail | the single biggest reveal (hook number or thesis); fade the tail |
| camera | camera-shutter.mp3 | 0.22 | 0.14 | shutter | K15 article snaps in, photo cards |
| camera | camera-click.mp3 | 0.34 | 0.14 | camera click | K08 face sticker first appearance (alt) |
| camera | old-cam.mp3 | 0.86 | 0.15 | vintage camera | K03 mono-beat (on request), old-photo moments |
| camera | flash.mp3 | 1.88 | 0.35 | flash zing | K19 shine sweep, K18 reveal |
| ui | highlighter.mp3 | 0.79 | 0.09 | marker stroke | K15 highlight sweep (one per highlighted line) |
| ui | beep.mp3 | 1.96 | 0.09 | notification beep | K17 notification/alert in a mock-up |
| ui | typewriter.mp3 | 1.90 | 0.09 | key taps | K17 typing in a prompt box, K04 long lead-in typed |
| ui | multi-flicker.mp3 | 1.02 | 0.34 | glitch flicker | K14 glitch frames, screen turning on |
| texture | music-box.wav | 2.00 | 0.14 | soft chime | gentle/nostalgic moment, close; rare |

## What her reels show (audio study, `work/audio/`)
- Exact-file matching against her 15 reels found **no confirmed matches** (her library differs, or it's buried under voice + music). So the trigger map below is from timing analysis, not copied cues.
- Transient onset at graphic entries: full-screen object scenes **40 %**, article/data scenes **42 %**, vs **26 %** at random times (speech). → she puts a light sound on roughly **1 in 4–5 graphic entries**, mostly pops/clicks on object scenes and articles.
- On-A-roll cards (quote card, lower-thirds, timeline): whoosh-like rising sound before **27 %** of entries vs ~6 % elsewhere → whooshes belong to cards sliding over A-roll.
- Exits: no extra transients (27 % ≈ baseline) → **no sound on exits**.
- Greyscale beats: 0 % → silence/voice only (old-cam only if Rishi asks).
- Overall feel: sparse, light, UI-ish; voice always clearly on top.

## Trigger map (per key)
| key | sound | when |
|---|---|---|
| K01, K02 | none | — |
| K03 | old-cam (optional) | at the snap, only if asked |
| K04 | pop-tech, very low | only on the hook's big word |
| K06 | woosh (or swoosh) | hero prop landing; pop-soft on 1–2 accents |
| K07 | swoosh | cut-out slide |
| K08 | pop-soft per sticker (alternate pitch ±2 semitones) | each sticker; camera-click on the first |
| K09 | mouse-click / mouse-click-2 / double-click | every click, never the same file twice in a row |
| K10 | pop-soft or flick per item | each item |
| K11 | flick per flip (thin out to ~4/s max) or riser-tick to the final value | growth |
| K15 | camera-shutter on entry, highlighter per line, woosh on punch zoom | |
| K16 | pop-tech per bar (low), charge bed optional | |
| K17 | hitech-click on appear, typewriter for typing, beep for alerts | |
| K18 | swoosh + flash (low) | card entry |
| K19 | swoosh on slide, flash on shine | |
| K20 | flick or hitech-click per year change | |
| hook reveal | riser → drop (once per video, tail faded by 1.5 s) | biggest number / claim |

## Mixing rules
- Voice on top: SFX peaks around −18 to −24 dB relative to full scale, **≥ 8 dB under the voice**; music bed −20 dB under voice (per plan B7), ducked further under dense SFX.
- Density: sound on ~30–50 % of graphic entries, not all; never more than 3 SFX inside any 1 s; no sound on exits.
- Pitch/volume vary ±10 % on repeats; trim long tails (hitech-click, beep, flash, drop) with 100–300 ms fades.
- Deliver: cue sheet (time · key · file · gain dB · offset) + one SFX stem WAV + mix.
