# Tesseract notes (CLI 0.4.0)

> Every item here cost at least one rebuild on roughcut_v3. The engine already handles them; read this before changing it.

## Pipeline
`create` → `import-video` (aroll, matte) → `import-font` (each TTF) → `import-asset` (logos, avatar, sfx) → copy to `base.tsrct` → `checkout` → `editable.orig.json` → **build script** writes `editable.json` + `edits.json` → copy base over the project → `commit` → `apply` → `filmstrip` / `preview` → `export` (**default 1080p, never 720p**).
Always rebuild from the clean `base.tsrct`; never stack commits on an old project.

## Gotchas
| Problem | Fix |
|---|---|
| Groups/clips that start later never render ("never visible on the project timeline") | `playback.mapping.input.start` is on the **parent** clock: it must equal `inputRange.start` |
| Rect drawn in the wrong place | `rect.position` is the local **top-left**; use `[0,0]` and position with the transform |
| Keyframes on a nested Video clip ignored or clamped | **wrap the clip in a Group** and animate the Group |
| Blur clips text to a baseline strip, or a group blur does nothing | every gaussianBlur needs `layerSize: [1080, 1920]` (and `repeatEdgePixels: false`) |
| Shape fill alpha ignored | set `fills[0].opacity` (0..1), not the colour alpha |
| `source.cropRect` didn't crop | use a punched framing (scale 118 %, y = 1920 − 960×1.18) + a mask |
| Mask point `cornerRadius` ignored | draw rounded rects with **cubic Bézier corners** (`rrect()` in the template) |
| ✓ ↑ ● missing in Inter (latin subset) | draw ticks, arrows and dots as shapes |
| Behind-the-head | matte Video layer + `trackMatte {mode: lumaInverted}`; mirror the A-roll transform JS |
| Video layer embedded audio | omit `volume` on picture copies; a separate Voice Audio layer carries sound |
| Text typing / changing labels | `setFxPropertyKeyframes` on `textContent` with hold easing |
| JS animators | `layerTimeJsCode` reads the layer-local `input.time.seconds`; root video = project time |
| One key per time per property | duplicate times are rejected |
| Effect-param animation | `setFxLayerEffectParamAnimator` with a JS animator (blur reveals, saturation) |
| A second `setFxPropertyKeyframes` call on the same property replaces the first (rise then `exit_` lost the fade-in; vid5) | one call per property: combine into `rise_exit` / `reveal_exit` style helpers |
| `apply` fails on JS like `t--0.05` | wrap negative offsets: `t-(-0.05)` |
| Mask ids collide | mask ids must be unique across the whole document |

## Review commands
```sh
tsrct filmstrip --project p.tsrct --timestamps-ms 1000,2000,… --tile-width 270 --tile-height 480 --items-per-row 4 --output check.png
tsrct preview --project p.tsrct --time 3.25 --output f.png          # single frame / glyph checks (crop with magick)
tsrct filmstrip --project p.tsrct --fx-solo main:<id> …            # isolate a layer when something is missing
ffmpeg -i out.mp4 -af ebur128=peak=true -f null -                    # loudness
ffmpeg -i out.mp4 -vf blackdetect=d=0.1:pix_th=0.05 -an -f null -    # black frames
```

## Browser editor (parked)
- The official `tesseract-editor` skill + `tesseract-0.4.0-web.zip` can open, edit and save the same `.tsrct`.
- Saving in place needs the File System Access API: Brave has it off by default (flag `brave://flags/#file-system-access-api`), Chrome has it on.
- If Rishi ever edits in a GUI, stop regenerating from the script and edit the saved project in place.
