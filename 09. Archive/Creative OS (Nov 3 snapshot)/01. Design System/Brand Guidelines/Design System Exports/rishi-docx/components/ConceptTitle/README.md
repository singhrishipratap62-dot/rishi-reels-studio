# ConceptTitle

The title of an explainer plate: a spaced kicker between hairlines, then the name of the idea in Gambetta, with an optional italic second line.

**Use for:** naming a phenomenon, law, mechanism or idea when the reel explains it ("Automation / *Bias*", "Schlep / *Blindness*", "Until / *2020*"). Not for the reel's hook — that's `HookTitle` or `TitleOverFace`.

**Anatomy:** `kicker` (uppercase, tracking 0.22em, `ink-muted`, between two 56px `line-strong` hairlines) → `concept-title` (Gambetta 96–120px, regular) → optional second line in Gambetta italic → one visual below (a `Halftone` object, `UnitDots`, a card) → crop-mark corners at the safe-area corners.

**Motion:** kicker appears with the ground → title words go from `ink-ghost` to `ink` one by one on the voice (Linear, ~120ms each) → the visual eases in after the last word (Smooth, `dur-normal`).

**Rules:** 1–3 words per line, two lines max. Centred (it stands alone). The italic line may be `signal` only if nothing else on the plate is. English only.

**You provide:** the kicker, the title words and the visual.
