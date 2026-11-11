# ThinkingOrb

A dotted sphere that shows "the AI is doing something". Nine states, each a different verb. Rebuilt from the open-source `thinking-orbs` (MIT, Libraries.dev) as a self-contained canvas script: no React, no install.

**Use for:** the beat where an AI is working, searching, checking or waiting, in place of a spinner or loading dots. It is the only thing in the system that is allowed to turn on its own axis (see Rules).

**States and when to say them:**

| State | Looks like | Use when the voice says |
|---|---|---|
| `working` | dots on tilted orbits | "it's working on it", generic thinking |
| `searching` | a scan line sweeps a dotted globe | "it searched / looked it up / browsed" |
| `solving` | bands scramble, then click back | "it solved / cracked / figured out" |
| `listening` | a wave rolls through rings | "you speak, it listens", voice input |
| `connecting` | a constellation wires itself | "it connected tools, sources, agents" |
| `weaving` | three strands plait | "it combined / merged ideas" |
| `composing` | an undulating sash | "it wrote / drafted / generated" |
| `breathing` | a ring slowly morphing | idle, waiting for the next prompt |
| `shaping` | circle, triangle, square | "it shaped / structured / planned" |

**Colour:** ink dots on paper, paper dots on the ink theme (the theme is read from the nearest `data-theme`). Pass `color: "signal"` only when the orb is the frame's single red moment. Red then needs a bigger mark: use `dotSize` 2.2 at size 20, or size 64 at scale 1.5 or more. Never any other tint.

**Sizes:** two tuned designs, `64` (hero, avatar) and `20` (inline). They are not a scale of each other. Reels need big marks, so always enlarge with `scale`: hero 64 at scale 3 to 5 (about 190 to 320px on a 1080 canvas), inline 20 at scale 2 (40px) next to 32px text. Nothing renders below 32px visible.

**Anatomy:** a 64 or 20 orb in a transparent canvas, no card, no ring, no glow. Optional label beside it in `label` style (`Searching 14 sources`), the key words on `signal-marker`.

**Use it:** load `components/lib/rishi-orb.js`, then either `<canvas data-orb="searching" data-size="64" data-scale="4" data-color="signal">` or `RishiOrb.mount(canvas, {state, size, scale, theme: "auto" | "paper" | "ink", color, speed, dotSize, dots})`. For rendered video frames call `RishiOrb.draw(canvas, opts, tSeconds)` with `t = frame / fps`, so every frame is deterministic and seekable.

**Motion:** it enters with a fade and a 90% to 100% scale over `dur-normal` on `ease-smooth`, runs continuously while the idea is on screen, and leaves with a fade. One orb per frame (two only in a split-screen comparison). Never freezes on the OS reduce-motion setting (it is a video tool).

**Rules:**
- Replaces any spinner, ellipsis or loading bar. Never next to one.
- Don't stack it on busy footage; give it paper, ink or a `surface` well.
- Exception to the no-rotation rule of `Halftone`: the orb turns because that is how it reads as "thinking". Nothing else rotates.
- Don't change dot counts or speed beyond `speed` 0.6 to 1.6; the presets are hand-tuned.
- Credit: engine is thinking-orbs 0.3.2 (MIT). Keep the licence note at the top of `rishi-orb.js`.

**You provide:** the state, and optionally a label.
