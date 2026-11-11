# Motion Library — v1.1

> v1.1: M01, M02, M06 and M25 revised and M28 added from Rishi's notes on the first Tesseract edit (`[R1.1]`, see `../history/LESSONS_LEARNED.md`). The v1.1 values are approved; they replace the estimates.
> v1.2 (2026-11-11): reference doc; `../SKILL.md` holds the compiled rules. Lines aligned with it are marked `[v1.2]`.

All durations at 30 fps. Most values are `[EST]` from 1 fps and 6 fps frame strips (`../references/contact_sheets/E_final_1fps.jpg`, `F_anim_strips_6fps.jpg`) — sub-frame precision isn't possible from these samples, so tune by eye. Default easing: `cubic-bezier(0.22, 1, 0.36, 1)` (easeOutQuint-like) for entrances, `cubic-bezier(0.65, 0, 0.35, 1)` for camera moves `[INF]`. Nothing in this style moves linearly except line-draw speed along a path and the constant A-roll push (M06) `[v1.2]`.

| ID | Name | Initial → Final | Duration / delay | Use | Evidence |
|---|---|---|---|---|---|
| M01 | `word-rise-support` (v1.1) | per word: opacity 0, y +22 px → 1, 0 | opacity 380 ms, rise 420 ms, ease-out; each word starts on its spoken time | **all** support/normal text, in captions and in graphic scenes | `[R1.1]` (was y +6 px, 3–4 f) |
| M02 | `hero-char-reveal` (v1.1) | per glyph, left → right: x −28 px, blur 10 px, opacity 0 → 0, 0, 1 | slide 380 ms, blur 300 ms, fade 240 ms; stagger = spoken length ÷ glyphs (12–48 ms); finish ≥ 350 ms before the cut | **all** impact/hero text | `[R1.1]` (was whole-word blur-in 5–10 f) |
| M03 | `ghost-to-white` | hero word at 35 % grey/blurred → solid white | 6–8 f, word-timed | 2nd hero word in a pair ("this **show**"). `[v1.2]` Not a default: all hero text uses M02; use M03 only if Rishi asks | `[OBS final 23.7 s]` |
| M04 | `caption-hard-out` | visible → gone | 0 f (cut) | caption group change | `[OBS]` |
| M05 | `aroll-zoom-cut` | crop 100 % → 115–140 % | instant cut | create cuts inside A-roll | `[OBS final 31/35/39 s]` |
| M06 | `aroll-slow-push` | scale +1.2 % per second, linear (zoom cuts stack on top) | every A-roll shot, whole shot | **always on** A-roll (v1.1); stronger push optional on hook/emotional holds | `[R1.1]`; `[OBS plan "Opening zoom-out" tut 13:36; "slow zoom out" revision #5]` |
| M07 | `focus-pull-reveal` | blur 20 px, opacity .6 → 0, 1 | 5–6 f | paintings, B-roll entry | `[OBS final 10.5 s]` |
| M08 | `camera-slide-in` | x +15–25 %, blur → 0 | 8–12 f | painting reveal (as taught) | `[TX 02:37]`, `[EST]` |
| M09 | `ken-burns` | scale 1.00 → 1.08, slight pan | whole shot (2–4 s) | paintings, B-roll, illustrations | `[OBS]` |
| M10 | `whip-transition` | horizontal motion-blur streak, 30–60 px blur | 4–6 f | graphic → graphic (painting→painting, line scene out) | `[OBS final 11.5 s, 47.8 s]` |
| M11 | `line-draw` | stroke-dashoffset 100 % → 0 | 18–30 f per segment, ease-in-out | Line+Text, Line+Illustration | `[OBS final 50–53 s]` |
| M12 | `line-interrupt` | line stops at text bbox − padding, resumes after | gap = text width + ~40 px | Line+Text | `[TX 03:01]` |
| M13 | `camera-track-line` | camera keeps line head ~40 % from frame edge | continuous, slight lag (6–8 f) | Line scenes, graphs | `[TX 03:25, 06:05]` |
| M14 | `zigzag-pan` | camera pans vertically, objects reveal alternately L/R | 0.8–1.2 s per stage | Line+Illustration B | `[OBS tut 03:38]` |
| M15 | `marker-dot-pop` | scale 0 → 1.2 → 1, glow | 6–8 f | white dot on line; blue ball | `[OBS tut 03:32]` |
| M16 | `graph-axes-draw` | axes length 0 → full | 8–10 f | graph start | `[OBS final 1 s]` |
| M17 | `graph-step-climb` | ball advances one step per spoken trigger word | per word | "up and up and up" | `[TX 13:36, OBS final 2–4 s]` |
| M18 | `graph-hold-then-cut` | final state held | ≥ 15 f after last label | graph exit | `[TX revision #2]` |
| M19 | `paint-in-figure` | texture mask reveal: speckles → full painted figure | 10–20 f | painted figures, center illus. | `[OBS final 19 s]` `[EST]` |
| M20 | `stacked-text-build` | lines add below/beside hero one by one; words inside each line still follow M01/M02 `[v1.2]` | per spoken phrase | center illustrations | `[OBS final 19–22 s]` |
| M21 | `orbit-text` | words travel on a circle/arc around subject | 3–5 s per revolution, words fade at back | center/side illustration | `[TX 05:18, OBS final 43–46 s]` |
| M22 | `spiral-draw-zoom-out` | spiral stroke draws, camera zooms out 1.3 → 1.0 | draw 20–30 f; zoom over the full hold | concept shapes | `[OBS final 25–27 s; revision #5]` |
| M23 | `photo-drop` | y −30 px, rotate ±4°, opacity 0 → settle with shadow | 8–10 f | object/photo callouts; stacking | `[OBS final 32–34 s]` `[EST]` |
| M24 | `rough-reveal` | torn/noisy alpha mask wipes in | 8–12 f | object callouts | `[TX 05:41]` |
| M25 | `highlight-box-wipe` | blue box scaleX 0 → 1 from its left edge, then its text word by word (M01) | **480 ms ease-in-out, starting ~120 ms before the word** (v1.1; a 5–6 f grow looked like it started midway) | single-word / short-phrase emphasis | `[R1.1]`, `[OBS final 18 s, R1 0:08]` |
| M26 | `quote-marks-first` | marks fade in, then text writes (support M01, hero M02 `[v1.2]`); marks bracket the block (open top-left of first line, close bottom-right after last line) | marks 4 f, text word-timed | text-centric | `[OBS final 48 s]` |
| M27 | `glow-pulse` | glow radius ±10 %, slow | 1.5–2 s loop | orbs, icons on dark | `[OBS R1 0:20, R6 0:58]` |
| M28 | `overlap-build` (v1.1) | each piece y +90 px, opacity 0 → settled | 900 ms ease-in-out per piece, next piece starts every ~520 ms: no dead time between pieces | stacked blocks, bars, steps, any multi-part build | `[R1.1]` |

**Sequencing pattern inside a graphic scene** `[INF from OBS]`
1. Background (already present at cut) → 2. structural element (line/axes/figure) → 3. marker → 4. text synced to words → 5. camera move continues → 6. hold ≥ 0.5 s → 7. hard cut to A-roll *or* whip to next graphic.

**Implementation notes (Remotion)**: `interpolate` + `Easing.bezier`; `spring({damping: 200})` for pops; SVG `pathLength` for M11; CSS `filter: blur()` for M02/M07; a parent `<AbsoluteFill style={{transform}}>` as `CameraRig`; texture layers as PNG/WebM overlays with `mix-blend-mode: multiply/overlay` inside the moving group.
