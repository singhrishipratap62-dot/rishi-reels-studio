# Checklist

A task list where rows get ticked and struck through one by one.

**Use for:** "AI can now do all of this", steps completed, before/after lists of work.

**Anatomy:** `surface` panel with an `ink` header bar (`label` text) → rows: 44px square checkbox (4px ink border) + task in 44px → done state: filled ink box with paper tick, text in `ink-muted` with a strike line drawing through.

**Motion:** panel and empty rows appear first; each row ticks on its word (box fills instantly, strike draws in 200ms). Optional `Callout` ("AI does the work") on the last row.

**You provide:** the tasks.
