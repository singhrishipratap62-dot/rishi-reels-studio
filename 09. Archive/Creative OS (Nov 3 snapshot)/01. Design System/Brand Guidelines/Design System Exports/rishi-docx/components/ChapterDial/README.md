# ChapterDial

A section marker: a big number on a dotted arc, with the next numbers waiting on the arc, and the chapter title beside it.

**Use for:** the start of each chapter in a list-style reel ("3 ways", "4 mistakes"). Shows where we are and how many are left.

**Anatomy:** dotted `line-strong` arc entering from the left edge, a small ink dot at the active position → current number in `chapter-number` (200px) → previous/next numbers in `ink-ghost` along the arc → title in `title` Semibold + one-line `caption` subtitle.

**Motion:** arc rotates into place (≈14°, Smooth, `dur-normal`) → number fades ghost → ink → title eases in (Soft) 100ms later. On screen ≈1–1.5s, then hard cut to the chapter's content.

**You provide:** chapter number, title, one-line subtitle.
