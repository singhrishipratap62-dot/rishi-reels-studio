# KaraokeText

A sentence shown in full in ghost grey that turns to ink word by word as it's spoken, with a highlighter sweeping across the key phrase.

**Use for:** definitions, rules, key sentences, quotes being read out — whenever the exact wording matters.

**Anatomy:** optional `label` + title (`display`, with a 4px ink rule under it that draws on) → body in `title` size (60px, Medium) in `ink-ghost` → each word turns `ink` on its spoken frame → the key phrase gets a `signal-marker` highlight sweeping left to right while it's said.

**Motion:** title fades ghost → ink (200–300ms). Words flip colour with the voice (linear, ≈120ms). Highlight sweep matches the duration of the phrase.

**Rules:** max ~25 words on screen. One highlighted phrase per sentence. Hide the caption pill while KaraokeText is up — it is the caption.

**You provide:** the sentence and which phrase to highlight.
