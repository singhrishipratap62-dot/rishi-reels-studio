# PromptBox

A recreated AI prompt box that types out what someone asked, with the key words highlighted.

**Use for:** showing the exact prompt behind a result — "all I typed was this".

**Anatomy:** floating card (`#fffdf8` on paper, `surface` on ink), 24px radius, `shadow-float` → square icon plate in `signal-marker` with a line icon → prompt text in 48px, key words on `signal-marker` → round send button, `ink-ghost` while typing, `ink` when done.

**Motion:** card eases in (200ms) → text types at 30–40ms per character with a blinking cursor → send button fills → optional cut to the result.

**Rules:** this is UI, so rounded corners are allowed. Use the real prompt (shorten honestly if needed). Not branded as any specific product unless it's the real product being discussed.

**After send:** the reply can start with a `ThinkingOrb` (20, scale 2) in the card before the answer types in.

**You provide:** the prompt text and the words to highlight.
