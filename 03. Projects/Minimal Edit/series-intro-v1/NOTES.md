# Series intro, Version 1 · build notes

**Current:** with sound: `Intro_V1_captions_Upright_sound.mp4` / `Intro_V1_captions_Italic_sound.mp4` (rebuild: `python build.py <root> upright|italic --sfx --mix=0.86`). Before sound: caption-only pair `Intro_V1_captions_Italic.mp4` / `Intro_V1_captions_Upright.mp4` (no cards, no grid). Rebuild: `python build.py <root> italic|upright` (add `--overlays` to bring back the cards and grid). Before that: draft 3, `Intro_V1_draft3.mp4` (upright Playfair heroes). Draft 2 (italic heroes): `Intro_V1_draft2.mp4`. Draft 1: `Intro_V1_draft1.mp4` (1080×1920, 30 fps, 8.44 s). Editable: `Intro_V1.tsrct`. Rebuild: `.tesseract-work/build.py` on `.tesseract-work/v0_base.tsrct`.
**Brief:** rebuild Rishi's Premiere storyboard (`Premiere Pro/export/Intro Try_2–5.mp4`) in Tesseract, using gradnext colours. No pink.

## How the reference was read
- `Try_5` = raw A-roll. It is V1 source **1.714 → 10.156 s**, one continuous take, no trims (audio cross-correlation 0.92–0.99, constant offset).
- `Try_4` = + card stack: 5 small episode cards fly in and fan across the top (0–1.2 s). The big *Profitability Case* card lands on the right (~2.3 s) and leaves first (~7.0 s), then the small cards go right → left (gone ~8.0 s).
- `Try_3` = + 30-day grid: a yellow card pops in on the left (0.6 s), 30 navy tiles build in (1.1–1.8 s), tile 1 turns white on "1" (~2.2 s), and it all exits on "teaching" (~5.3 s).
- `Try_2` = + rough captions "anatomy of a case" / "day 1/30" (to be redesigned).

## What draft 1 does
- Same layers and timing as above. Cards are your stills (`Downloads/Growth case@1x.png`, `Downloads/Day 01 · Anatomy of a case@1x.png`, which shows *Profitability Case*), alternating Growth / Profitability with the big card on Profitability, as in the reference. Each card has rounded corners, a white frame and a soft shadow, and flies in with a small spin.
- gradnext palette: chrome yellow #FFA601 grid card, rhino navy #2E3558 tiles and chip, white for today's tile.
- Title redesigned (Minimal Editorial text rules, gradnext fonts):
  - *Anatomy* in Besley SemiBold Italic, character by character on the spoken word.
  - "of a case." in Jost, word by word.
  - A navy **DAY 01 / 30** chip with a yellow edge grows on "day", and its words arrive on "day" / "1" / "30".
  - The title holds to the end over a soft navy scrim.
- A-roll: 115 % punch for the first 280 ms (as in the Premiere cut), then 100 % with the +1.2 %/s push.
- Voice: cleaned V1 voice (HPF, 2.5:1 compression, limiter). Programme −13.7 LUFS, −1.4 dBFS peak.
- Everything is moved inside the Instagram Reels safe zone. The reference's big card (top 170 px) and grid (left 38 px) sat outside it, so the stack is ~85 px lower and the grid starts at x 120.

## Open
- The big card says *Profitability Case*. For Day 1 it may want to be *Anatomy of a Case* (send a still or I can build the title natively over the photo).
- Safe-zone audit flags the tail of the "y" in *Anatomy* (x 872, icon column starts at 845 below y 1130). Within the italic overhang; shrink it if you want it strictly inside.
- No SFX yet. Not checked by ear.

## Revision log
| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 1 | 0:00–end | Title lockup (*Anatomy* + DAY 01/30 chip) isn't the Minimal Editorial caption style | Minimal Editorial captions, inspired by the Premiere "anatomy of a case / day 1/30" idea | Chip and lockup removed. Six spoken caption groups: *anatomy* / of a case. → this is / *day 1* / of 30 → of cracking / *consulting cases* → where I am / *teaching* → all consulting / *frameworks* → in / *30 days.* Playfair Bold Italic heroes (char by char, blur), Inter 48 px support (word by word, tight to the hero). One accent: the "1" in chrome yellow. Every hero finishes ≥350 ms before its cut, capped at 570 px so it stays left of the icon column. Safe-zone audit is clean | done |
| 2 | — | Cards and 30-day grid | Not part of this pass | Unchanged | — |
| 3 | all captions | Playfair's heavy italics are too much | Less extreme serif | Heroes switched to upright Playfair Display Bold; same char-by-char reveal, sizes and layout | done |
| 4 | all | Focus on captions only; compare italic vs upright | Two versions, no tile cards or 30-day grid | `build.py` takes `italic`/`upright` and `--overlays`. Both exports drop the cards and grid; captions identical apart from the Playfair face | done |
| 5 | all | No sound design | Sound for the captions | 22 cues from `SFX/` (see `sound_cue_sheet.md`): Hi-Tech Click on the 6 hero words (−17 dBFS), a quiet flick on 14 support words (−27 to −29), Modern-technology pop on the yellow "1" (−21), Swoosh into the first caption (−21). +3 dB for the first 5 s, easing back by 6 s. Whole-mix trim 0.86 | done |

## Sound pass (2026-11-03)
- Mix: **−15.0 LUFS integrated, −2.5 dBTP true peak** (measured on the final export, both versions).
- Placement: an effects-only render shows every cue's peak within ±25 ms of the cue sheet, apart from the first click, whose window overlaps the opening swoosh. Hi-Tech Click levels measure within 1 dB of target.
- Fix found: the Hi-Tech Click `peak_db` estimate carried over from the first edit was ~8 dB off for the 450 ms trim, so clicks played at about −23 dBFS. Recalibrated from the mix measurement (`sfx_peaks.json`).
- Voice unchanged (same cleaned stem, same clock), so lip sync is unchanged from the earlier drafts.
- No music: none supplied.
- **Not verified by ear.** I can't play audio here; levels are set by measurement. Check on a phone with sound on.
