# DataTable

A real table — pricing, benchmarks, comparisons — where the row being discussed inverts to ink and everything else drops to ghost.

**Use for:** model pricing, benchmark scores, salary bands, before/after numbers across several items.

**Anatomy:** `kicker` + `headline` question ("Who's cheapest?") → header row in `label` uppercase, `ink-muted`, on a 4px `ink` rule → rows in `body`-ish 38px, tabular figures, numbers right-aligned, 2px `line` dividers → focus row: `brand-ink` fill, paper text → caption source line below.

**Motion:** table eases in at full ink (150ms) → on the first spoken item, every row but the focus row fades to `ink-ghost` (200ms) → focus row inverts → moving focus cross-fades (150ms). Optional push-in toward the focus row.

**Rules:** max 7 rows and 4 columns on screen; crop the rest. Rupees for Indian audiences (convert and say so in the source line). One focus row at a time. Never re-order a real table to make a point.

**You provide:** the table data, the focus order and the source.
