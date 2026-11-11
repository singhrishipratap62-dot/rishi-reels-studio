# BarChart

A simple bar chart that grows on the grid, with one bar highlighted in signal.

**Use for:** comparing 2–6 amounts — growth over years, before vs after, one company vs others.

**Anatomy:** `label` title → bars in `ink` on a 4px `ink` baseline, value labels in `body` Medium above each bar → x-axis labels in `caption`/`ink-muted` → source line. The bar that makes the point is `signal`; all others `ink`.

**Motion:** grid first, then baseline, then bars grow from the baseline (700ms, Enter easing, staggered 80ms), values follow. Optional pen circle on the key bar instead of colouring it.

**Rules:** square bars (`radius-0`), no gridline clutter beyond the background grid, no 3D, no legends — label directly. Max 6 bars.

**You provide:** the values, labels, which bar is the point, and the source.
