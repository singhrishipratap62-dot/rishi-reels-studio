# ImageGenerate

A square pixel mosaic that churns in ink and grey, then resolves cell by cell into a photo, or turns one photo into the next through the mosaic. Rebuilt in plain canvas from the idea behind the open-source `img-fx` "Image generation" loader (MIT, Libraries.dev): no WebGL, no three.js, no React.

**Use for:** photos of people, mainly. The moment a person is named in the voiceover and their photo arrives (`PortraitCard`, `MediaFrame`), a big person image in the frame, or a then/now swap from one photo to another. Works for any image, but a screenshot of an article should usually just cut in with `MediaFrame`: use this for faces and pictures, not for text you need to read.

**Anatomy:** `bg` ground with square cells (28 to 30px on a 480px photo, 14px on a 210px one) in ink and grey, about one in five cells empty so paper shows through; **one cell flashes `signal` red** (that is the frame's single red moment, so keep other red off the photo); the photo is cover-cropped with the focus kept high (`focusY` 0.2) so faces stay in.

**Stages (p from 0 to 1):** 0 to 0.25 the old photo (if swapping) breaks into cells, 0.25 to 0.45 pure churn, 0.45 to 0.9 cells resolve into big pixels of the photo, then sharpen to the real image, 1 = full photo. Cells resolve in a drifting diagonal order, never all at once.

**Timing:** generate in about 3s, swap in about 3.2s, hold 1.6s. On a reel, take 1.5 to 2s for a quick generate so the voice isn't waiting; the photo must be fully sharp before the line about that person ends. Churn flickers at 10 fps on purpose, so it reads as pixels, not a blur.

**Use it:** `components/lib/rishi-imgfx.js` exposes `RishiImageFX`.
- `RishiImageFX.render(canvas, {to, from, p, size, cell, focusY, theme: "auto" | "paper" | "ink", radius}, t)` draws one exact frame (`to` and `from` are loaded `Image`s, `t` in seconds drives the flicker). Use this for rendered video: `p` from the timeline, `t = frame / fps`.
- `RishiImageFX.mount(canvas, {images: [urls], size, cell})` loops generate, hold, swap on its own.
- `RishiImageFX.load(url)` returns a promise for an image. Images must be same-origin or CORS-enabled.

**Rules:**
- Square corners; round only if the photo sits in rounded UI (`radius`).
- Keep to the palette: cells are ink, grey and paper, one red cell. No colour cells, no gradient sweep, no glow.
- No text on top of the photo while it resolves.
- One person per effect. For two people, run two frames side by side, in step.
- Never use on a face that has already been on screen for more than a couple of seconds; it is an entrance, not a decoration.

**Not used on purpose:** the original's `sweep-gradient` preset (a gradient), and its colour-from-the-photo mode, because both break "no gradients, three colours".

**You provide:** the photo (and the next one for a swap), and when the voice names the person.
