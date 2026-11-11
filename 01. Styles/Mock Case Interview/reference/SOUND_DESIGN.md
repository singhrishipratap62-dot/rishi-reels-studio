# SOUND_DESIGN — mock case motion graphics
Rules = `01. Styles/Minimal Edit/reference/SOUND_DESIGN.md` (sound only, never its visuals) via `01. Styles/Consulting Case/reference/SOUND_DESIGN.md`. Library: `../sfx48/` (48 kHz WAV + `info.json` with each file's peak time). Built by `../engine/sfx_mg.py` from the board's `events_*.json`. [M21] Read from SKILL.md at step 9 (SFX) or when a sound/level is questioned.

## Principle
Lots of sound, each one quiet. Every graphic that enters gets a sound; captions are silent. Align the sound's **peak** to the visual event. Within 110 ms the louder cue wins.

## Trigger map (style level = peak in a −15 LUFS program)
| Board event (renderer tag) | Sound | Level |
|---|---|---|
| Chapter change (`chapter`) | Swoosh + Mouse click different (+0.19 s, tab) | −16 / −22 |
| Beat visual clears (`clear`) | Swoosh | −19 |
| Root question box (`hero`) | Hi-Tech Click (trim 450 ms) | −17 |
| Big number / count-up (`count`) | Hi-Tech Click | −17 |
| Result chip, quote card, Tie / Recommended tags (`result`) | Hi-Tech Click | −17 |
| Icon (`icon`) | Highlighter | −20 |
| Bar / strike-through grow (`bar`) | Highlighter | −19 |
| Chip, pill, card, table cell, tick row (`pop`) | Pop different | −19 |
| Small label (`label`) | Modern technology pop | −22 |
| Plain text (`text`) | Modern technology pop | −21 |

## Level offset (important)
The timeline voice is untreated (4 Nov case: −28.9 LUFS). The stem is placed `voice_lufs − (−15)` dB lower (−13.9 dB) so the SFX-to-voice balance matches the style. If the program is later normalised, the balance holds. First case: 131 cues, stem peak −29.9 dBFS.

## Delivery
SFX stem `MG_sfx.wav` on its own audio track (A3) via `overwrite_clip`; cue sheet `MG_sfx_cues.md`. Ask Rishi to listen on his phone; move the whole stem in 2 dB steps if needed.
