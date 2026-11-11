# Timeline

A spine that draws across the frame with dated stops landing in order.

**Use for:** anything that happened over time — a story's sequence of events, how a technology evolved, a court case's progress.

**Anatomy:** 4px `ink` spine → square stops (24px), the current/key one in `signal` → date in `body` Medium, short label in `caption`/`ink-muted` below.

**Motion:** spine draws across (Smooth easing), stops land as the spine reaches them, 300ms apart.

**Rules:** 3–5 stops per frame; for longer histories, scroll the spine horizontally. Use "Today" or the actual date for the present.

**You provide:** the dates and a 1–3 word label for each.
