# SliderControl

A slider whose handle travels to a value while the number counts with it.

**Use for:** "how much?", trade-offs, settings, how strictly, how much — any quantity on a scale.

**Anatomy:** question in 40px Medium → value in 80px Semibold, top right → 8px track in `line-strong`, filled part in `ink` → 56px handle, `signal` fill with ink ring → axis labels in `caption` → optional `Callout` under the handle.

**Motion:** handle travels with Smooth easing over ≈1.2s while the number counts in sync → callout eases in when it lands.

**You provide:** the question, the range, and the value.
