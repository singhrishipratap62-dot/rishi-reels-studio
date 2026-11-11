# DEPTH_AND_ORBIT — Rishi's Editing Style v1.2

The depth family: graphics that sit **behind**, **around** or **in 3D space with** the speaker. Rishi asked for this as a signature (`[R1.2]`: "orbit animations, things going behind my head"). v1.0/v1.1 filed it under EXPERIMENTAL because most of it appears in only one reference (V01). v1.2 promotes it to **SIGNATURE**: specced, buildable, used deliberately, still rationed (§8).

Evidence tags: `[MEAS]` measured on native frames · `[OBS]` seen · `[EST]` eyeballed · `[INF]` my inference. Source px are 720×1280 (×1.5 for 1080×1920). Frame numbers are V01 native frames at 30 fps. Where a value falls between two measured points it is `[INF]` and the first pilot must tune it.

## 1. Layer stack (z-order, back → front)
1. **Ground**: A-roll (graded) or a graphic ground (blue / cream).
2. **Behind-subject graphics**: outline words, card strips, rings, glows. Visible only around the speaker.
3. **Speaker**: the A-roll subject. For behind-subject effects this layer is a **matte cut-out** (§2).
4. **Foreground graphics**: UI cards, chapter badge, icons, anything that overlaps the speaker.
5. **Captions**: sit in front of the subject by default; the occluded-by-mic variant (§2.1) is a deliberate exception.
6. **Grade / grain / vignette** over everything.

## 2. Behind-the-subject
### 2.1 Captions occluded by the mic boom (V01, the "main depth trick on A-roll") `[OBS]`
White caption words render **behind** the mic boom and the speaker's foreground objects, so the boom cuts across the letters. Works because the camera is locked and the boom is static, so a **fixed mask polygon** (the boom shape) is enough. `[INF]`: a handheld mic and moving hands (Rishi's footage) are NOT static, so this needs a real matte (§9), or must be limited to shots where the foreground object is still.
### 2.2 Outline word behind a face-circle (V01 A23) `[OBS]`
Pale-blue **stroke-only** "100s" sits behind the circled face and orbit cluster. Pure layer order, no matte needed (the face is a card, not footage).
### 2.3 Reel-card strip behind the head (V13, V14, V15) `[OBS]`
A row of ≈ 7-8 portrait cards (≈ 14% W × 22% H) scrolls **above** the head, A-roll defocused 8-10 px `[EST]` behind it; 1 card per 30-45 f leftward, linear. Needs no matte because the strip lives in the empty top band. In MOTION_LIBRARY as `reel-strip-scroll`.
### 2.4 True behind-head graphics (new for Rishi) `[INF]`
Anything that must pass **behind the head or shoulders** (a word, ring or card partly hidden by the speaker) requires the per-frame matte (§9). No reference reel was verified to do this on a moving speaker; treat it as new build, not a copy.

## 3. Orbit ring — "many / community / everyone" (V01 A23) `[MEAS]`
A cluster of thumbnails orbits a circled face. It says **abundance** ("hundreds of tutorials").
| phase | frames (src) | what moves | measured |
|---|---|---|---|
| a. face card → circle | #1012-1020 (267 ms) | card height 1273 → 549 px while corner radius → 50% (squircle → circle) | ease-in (accelerates) `[MEAS]` |
| b. thumbnails fly in | #1020-1035 (15 f) | cards enter from the frame edges toward the ring | `[OBS]`; stagger `[INF]` ≈ 1-2 f |
| c. cluster zoom-out | ~#1020-1046 (867 ms) | cluster bbox height 1234 → 497 px | easeOutCubic ≈ `(0.1,0.3,0.2,0.8)` `[MEAS]` |
| d. ring rotates | #1036-1052 (16 f) | angle 36° → 123° clockwise (≈ 160°/s) | `[MEAS]` |
| e. ring decays | #1052-1084 | ≈ 26°/s, then ≈ 14°/s by #1084 (144.8° → 151.4° over #1070-1084) | `[MEAS]` |
| f. exit | ~1267 ms | whole cluster slides left, centre x 350 → 136 px | ease-in quad `[MEAS]` |
Rules: the ring is **flat 2D** (no tilt); cards **stay upright** while orbiting (counter-rotate each card by −θ) `[OBS]`; each card carries a faint glow in its thumbnail colour (~25 px src) `[OBS]`; outline word behind (§2.2).
Remotion recipe `[INF]`: `θ(t) = θ0 + ω∞·t + (ω0 − ω∞)·τ·(1 − e^(−t/τ))` with ω0 ≈ 160°/s, ω∞ ≈ 14°/s, τ ≈ 0.4 s; card i at angle `θ + i·360/N`, position `(cx + R·cosθi, cy + R·sinθi)`, rotation `−θ`. Fit τ to the three measured angles in the pilot.
Variant: V11 "Nearby Markets": labelled bubbles orbit a circular avatar (white ring ≈ 29% W), slower, with glow `[OBS]`.

## 4. Cylinder carousel — "scroll through many" (V01 A11/A12; V04 flat variant) `[MEAS/EST]`
- Footage shrinks into the centre card with a **cylindrical bend**: #330-365 (35 f).
- Cards travel right → left, ≈ 1 card per 25 f (~0.8 s), continuous.
- Neighbours rotateY ≈ ±25° `[EST]`, strong perspective, centre upright.
- V04 uses a flat 7-card row, side cards smaller/dimmer, rotateY ±20° `[EST]`, no orbit. Use V04's flat version when the content is a list; V01's bend when it is "endless".

## 5. Hologram icon in the hands (V01 A22) `[MEAS/OBS]`
Diamond (45° square) with **cyan `#6FD3FF` stroke + bloom**, translucent fill, containing a 3D object (brain, galaxy) and a white label. Scale/fade in over #857-871 (467 ms), ease-in `(0.6,0.1,0.8,1.1)` `[MEAS]`; slight float; tracked between the hands, tilt rotateX ≈ 20° `[EST]`; exit fade + blur 333 ms. Triggers 8 f before the spoken word. `[INF]` Needs hand tracking or hand-keyed positions; see §9.

## 6. Real 3D moves (V10, V11) — use at most once
- **3D post push** (V10 A13): a post card tilts ≈ −8° yaw (`[EST]` angle) while scale-pushing. Continuous camera move, not a cut.
- **Card wall in perspective** (V10): ≈ 12° `[EST]`.
- **Pseudo-3D unfold** (V05): cube → column → grid, ≈ 15° tilt `[EST]`.

## 7. Depth by blur and light (CORE, already in the pack)
`defocus-bridge` (A-roll blurs 0 → 10 px under a floating element, 12-20 f in/out), blur on far/outer cards, soft shadows, `reel-strip` parallax. These are the everyday depth tools; the moves above are the occasional signature.

## 8. Rules of use (premium minimal) `[INF]` — tune in the first real edit
| rule | reason |
|---|---|
| At most **one** orbit / carousel / hologram / 3D move per reel; at most **two** depth-family moves in total (reel-strip counts as everyday) | "One primary motion at a time"; rationed motion keeps the premium feel and makes each one mean something |
| Use only for **abundance, community, many-of-X, an abstract idea made physical** | Each reference ties the move to a spoken idea (hundreds of tutorials; knowledge + hard work). A move with no spoken job is decoration |
| Stay inside the safe zone (y 250-1500, right icon column clear) including card glow | IG UI |
| Never behind or across captions unless it is the deliberate §2.1 occlusion | Legibility |
| Start the move on or before the word (−10…+10 f) | Proof-lands-on-the-word rule |
| Keep the speaker's face unobstructed (matte or placement) | Face is the spine |
| Hard-cut in and out of the scene; the ring itself exits by sliding off | V01 pattern |

## 9. Build requirements and open decisions (need Rishi)
The Remotion side (rings, 3D transforms, strips) needs nothing new. **True behind-subject graphics need a per-frame person matte**, and this workspace has none: `rembg`, OpenCV and MediaPipe are not installed, and nothing is to be installed without Rishi's approval. Options:
| option | cost | works for |
|---|---|---|
| A. Segmentation model run once per clip (e.g. a video matting model), output a matte video Remotion composites | install + model download (hundreds of MB), minutes of compute per reel | moving speaker, handheld mic, hands; the full §2.4 |
| B. Static mask polygon for fixed foreground objects (mic boom on a tripod) | none | §2.1 only, locked camera |
| C. Placement only: keep graphics in empty areas (top band, sides), no occlusion | none | §2.3 strip, rings around a face card |
**Decision `[R1.2]` (Rishi, 2026-11-06): option A.** Status: **working, verified on Vid 1** (2026-11-06). Model `engine/matte/models/rvm_mobilenetv3_fp32.torchscript` (Robust Video Matting, 15,501,891 bytes, sha256 `f01e0c93…c5a1`, PeterL1n/RobustVideoMatting v1.0.0 release) + `engine/matte/matte.py`, using the existing venv's torch on MPS; no packages installed. Run by Rishi in his own terminal (the permission classifier blocks the assistant from loading a downloaded TorchScript file; rerun it the same way for new reels).
Test: Vid 1, 3 s at 720×1280, `--ds 0.375` → 90 frames in 4.8 s (**≈ 18.6 fps**; a 40 s reel ≈ 1 min at 720p; expect roughly half the speed at 1080×1920). Checked by eye on 3 frames (source / matte / composite over magenta): clean hair edge, both hands and the mic held whole, the dark chair behind the head correctly excluded, no visible flicker between the 3 frames.
Known flaws `[OBS]`: (1) faint speckle holes in the matte where the mic's grey fur is semi-transparent; (2) slightly soft edge where the hand leaves the frame on the right; (3) a thin dark fringe left of the head (chair headrest). **Not yet checked:** temporal stability over a full clip (only 3 frames viewed), 1080×1920 quality, other lighting.
Production recipe `[INF]`: run at `--w 1080 --h 1920 --ds 0.25`; in Remotion draw behind-subject graphics, then the A-roll with this matte as an alpha mask; add a 1-2 px feather and a small hole-fill (close) on the matte before use to remove the mic speckle. Fall back to C for any shot where the matte fails.
Also open: hand tracking for §5 (manual keyframes per reel is the cheap fallback).

## 10. Evidence strength
| item | source | strength |
|---|---|---|
| orbit ring | V01 (A23), V11 bubbles | one reel measured; bubble variant `[OBS]` |
| cylinder carousel | V01 (A11/A12), V04 flat | angles `[EST]` |
| hologram icon | V01 (A22) | timing `[MEAS]`, angles `[EST]` |
| occluded captions | V01 | `[OBS]` only |
| 3D post push / wall perspective | V10 | angles `[EST]` |
| reel-strip behind head | V13-V15 | `[OBS]`, three reels |
V01 is the best-measured reel in the set, but nothing here has been rebuilt and compared yet. Expect the pilot to correct several values.
