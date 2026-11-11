# UnitDots

Counting with dots: one circle per year, person or item, with the endpoints in signal and a bracket naming the span.

**Use for:** "the first time in 34 years", "1 in 20 people", "12 releases in 18 months" — spans of time and ratios that feel abstract as a single number.

**Anatomy:** optional `kicker` + `ConceptTitle`/`headline` → rows of 30px hollow `ink` circles (3px stroke) on the grid, up to 18 per row → the units that matter filled `ink`, the two endpoints (or the one exception) filled `signal` → a bracket above the span (hairline with end ticks) carrying a tab-style count (`34 YEARS`) → axis labels at the ends in `label`/`ink-muted`.

**Motion:** dots pop in left to right, 12–24ms apart, scale 0 → 1 (Settle) → the bracket draws out from its centre (Draw, `dur-quick`) → its count eases in. For ratios, the highlighted dots fill on the word after the grid lands.

**Rules:** max ~60 dots on a frame; beyond that use a `StatReveal`. Every dot is one real unit — never round the count for looks. Source line if the data isn't common knowledge.

**You provide:** the count, which units are highlighted, the span label and the axis labels.
