# RadarSweep

A radar of rings and nodes with a rotating sweep and a live readout: something running, scanning or being watched.

**Use for:** security stories, an agent monitoring systems, a model scanning thousands of files, "it was there the whole time and nobody noticed".

**Anatomy:** `brand-ink` ground → 4 hairline rings (paper at 20%) → dashed spokes to 4–6 node tiles (72px paper squares with an `IconSet`-style glyph), the node in question in `signal` → padlock or icon at the centre → sweep wedge (a soft paper wedge, the one allowed gradient here) → a `TabLabel` title above (`SSH CONNECTIONS`) → readout below: small label chip + big tabular number (`CPU 2.1%`) + a `signal` delta (`+0.5 ms`), optional sparkline crossing a dashed "expected" line.

**Motion:** rings draw out from the centre (300ms, 60ms stagger) → nodes settle on → sweep rotates continuously (one turn per 2.4s, Linear) → readout ticks every 400ms. The odd node turns `signal` on the word that reveals it. This is the one looping motion in the system.

**Rules:** the numbers in the readout must come from the story (a reported figure), labelled as illustrative if not. One signal node at a time.

**You provide:** the node names, the readout label and values, and which node is the anomaly.
