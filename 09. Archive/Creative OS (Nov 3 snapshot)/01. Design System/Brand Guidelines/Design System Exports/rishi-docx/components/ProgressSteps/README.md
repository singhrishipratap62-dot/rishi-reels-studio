# ProgressSteps

A loading bar with a live percentage, and step dots that fill in sequence.

**Use for:** waiting, installing, processing ("the model is loading"), and showing progress through a multi-step sequence.

**Anatomy:** `surface` panel → status line in 44px Medium → version/percentage row in `caption` → 16px track in `line`, fill in `ink`. Step dots: 28px circles with 4px ink rings joined by `line-strong` connectors; done steps fill ink.

**Motion:** bar fills linearly with the percentage counting in sync; dots fill one per step on the voice.

**You provide:** the status text and the steps.
