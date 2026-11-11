# Depth and matte: graphics behind the head

> Rishi loves "things going behind my head" `[RES]`, used sparingly (1–3 moments per reel). It must look real: **no visible gap or oval around the head** `[R]`.

## 1. Make the person matte
- **Tool:** `02. Shared Core/engine/matte/matte.py` (Robust Video Matting). Run: `"<studio root>/06. Tools/venv-style/bin/python" -I "<studio root>/02. Shared Core/engine/matte/matte.py" IN.mp4 OUT_matte.mp4 [--w 1080 --h 1920 --fps 30 --ds 0.25]` (`--ds` ≈0.25 for 1080×1920, 0.375–0.5 for 720×1280; the usage line inside matte.py still shows the old `<DIFF Acc>` path). Output: a white-person-on-black MP4 the same length and frame rate as the rough cut (roughcut_v3: 720×1280, 1002 frames, ≈33 s to compute).
- Check one frame against the footage (side by side) for polarity and alignment before using it.
- Tesseract's built-in `personMatte` gave an empty matte in an earlier edit. Use the RVM video. `[ME]`
- Make a new matte for every new rough cut. Never reuse one across different cuts.

## 2. Wire it in Tesseract
1. Import it: `tsrct project import-video --file matte.mp4 --asset-id matte`.
2. Add a root **Video** layer for the matte (no volume), sized `fit: cover` with `sourceRect` 1080×1920.
3. Give it **exactly the same transform JS as the A-roll** (scale, position, punch-ins, B&W tracking, split shift, cut-hiding zoom). In the engine, `aroll_motion(L)` is applied to both.
4. On the graphic (group or image) put `"trackMatte": {"layer": <matte id>, "mode": "lumaInverted"}`. The graphic shows only outside the person.
5. A layer consumed as a matte doesn't render. One matte layer can serve several graphics.

## 3. Rules of use
- Put the card high (y 250–710) so the head covers only its lower-middle; keep labels at the left and ticks at the right so they stay readable around the hair.
- Only while the A-roll it mirrors is visible and unmoved. When the face shrinks into UI (S2), the matte no longer matches, so hand the element to a non-matted copy once it's clear of the head (opening logo: `logoA` → `logoB`).
- Combine with a cut-hiding zoom: the matte follows automatically because it shares the transform JS.

## 4. Failure modes seen
| Symptom | Cause | Fix |
|---|---|---|
| Oval gap around the head in a mock-up | drawn radial mask in the storyboard | say mock-ups are sketches; the build uses the real matte |
| Graphic hidden where no head is visible | matte static while the visible face moved (shrink/PiP) | switch to a non-matted copy before the face moves |
| Graphic cut by the head at the wrong place | matte transform not mirrored | apply the same JS to the matte layer |

## 5. Behind-the-head layouts Rishi tuned `[R]`
- **Fan (R39):** screens appear together, then split. Tops ≈ y 180 (not ≈70: "getting a lot out of the frame … bring it down a little notch"), spread ±255 px / ±12°, rise 0.7 s + split 1.1 s (vid5).
- **Deck (R29):** rotation anchored on the bottom-centre; fan in from wide to a still-visible fan, never fully collapsed.
- **Giant word (R41):** baseline ≈ y 445 at 360 px, rise ≤0.7 s, or the head hides the middle letter and the word never lands (vid5).
- **Arc (R40):** top just above the hair; labels above the dots.
- Words/orbits behind the head only when the framing leaves room to read them (D28).
