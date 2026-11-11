# R006 — revision round 1 (Rishi notes, 2026-11-05)
Scope: **final export only**. `_green.mp4` and `_raw.mp4` stay as delivered (R1.3).

| # | Where | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 1 | S1 hook 0:00–0:03.9 | Caption left-aligned | Centred; keep the word rise-in animation | `#cap` centred in S1 | ✅ done |
| 2 | Whole reel | Too many words per caption line; risk of Reels UI danger zone | Fewer words per line | Max 4 words, max width 680 px (x 200–880) | ✅ done |
| 3 | S1 hook | Caption sits over the video | Put the caption in the white panel (space is there) | S1 caption at y≈640 inside the white panel | ✅ done |
| 4 | S1 hook | Hook panel is static | Question text already shown; each word gets darker as it is spoken | Question starts light grey; each word turns ink on its spoken onset (~120 ms) | ✅ done |
| 5 | S1 MBB strip | Typeset wordmarks | Real McKinsey / BCG / Bain logos, same layout | 05. Asset Library/stickers/mbb_logos_trim.png (Rishi's strip, whitespace trimmed, multiply blend) | ✅ done |
| 6 | 0:00–0:01 | Hook just appears | Starts Gaussian-blurred at 0:00, unblurs by ~0:01 | ffmpeg gblur, σ 40 → 0 over 1.0 s, ease-out | ✅ done |
| 7 | Hook + board header | "gradnext" top-right | Remove | Header brand removed | ✅ done |
| 8 | Hook + board header | "Solving real consultant cases · Part 41" top-left | Remove | Header row removed | ✅ done |
| 9 | End card | "gradnext" on the end card | Remove | End card = "Solving real consultant cases" · "Part 41" · "Follow for Part 42" | ✅ done |
| 10 | Whole reel | Voice only, no SFX | Sound design from the Minimal Edit SOUND_DESIGN (sound only, no visuals) using `01. Styles/Minimal Edit/sfx/` | Cue sheet generated from board events + caption words; levels per the Minimal Edit hierarchy; voice chain + −15 LUFS | ✅ done |

Status column is updated as each fix is verified in the re-render.

## Round 1b (Rishi notes after viewing)
| # | Where | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 11 | 0:00–0:03 | Blur lasted ~3 s and covered the whole frame (bug: vertical blur never cleared) | Blur only the white panel, subtle, gone within 1 s | Panel-only gblur σ 12 → 0 over 0.8 s, both axes, filter off after | ✅ done |
| 12 | Whole reel | A sound on every caption word | SFX only on animations, none on captions | Per-word flicks removed (captions + hook word darkening) | ✅ done |
| 13 | 0:03.87–0:06.01 (S2) | Punch-in is static | Start ~110% zoomed, ease back to 100% (as in the references) | Per-frame scale, cubic in-out, 110% → 100% over 64 frames | ✅ done |
| 14 | 0:00–0:03.9 (S1) | Hook caption a little too high | Slightly lower, still in the white panel | y 590 → 625 | ✅ done |
| 15 | 0:03.87–0:06.01 (S2) | Zoom-out looked wobbly/odd | Simple, smooth, buttery | Sub-pixel affine zoom, centred, sine in-out (was whole-pixel ffmpeg scale) | ✅ done |

## Round 2 (Rishi, 2026-11-05)
| # | Where | Request | Fix | Status |
|---|---|---|---|---|
| 16 | Whole reel | Speed up 1.2x | Picture setpts/1.2 → 29.97 CFR; voice+SFX atempo 1.2 (pitch kept). 2:41 → 2:14. 1x kept as `_1x.mp4` | ✅ done |
| 17 | Whole reel | Add background music at optimum level | `05. Asset Library/music/Background music.mp3` from 0:15, ~21 dB under voice, light duck, 1 s in / 2 s out; program −15.2 LUFS, TP −1.2 | ✅ done |
| 18 | Whole reel | Music too low, inaudible | Music raised 8 dB: 13 dB under the voice (was 21). −15.1 LUFS, TP −1.4 | ✅ done |

## Round 3 (Rishi, 2026-11-05)
| # | Where | Request | Fix | Status |
|---|---|---|---|---|
| 19 | Board scene | Background doesn't look good | Reference loop `05. Asset Library/videos/gradnext-background-loop-9-16.mp4` behind a transparent board layer | ✅ done |
| 20 | Hook + board | Bring back "Solving real consultant cases · Part 41" (left) and "gradnext" (right); not on the end card | Header restored; fades out at the end card; hook contents shifted down | ✅ done |
