# EchoBackdrop

A UI card on a giant, dimmed, blurred copy of itself, so a product screen never floats on an empty ground.

**Use for:** app and web UI, agent runs, chat windows and dashboards shown on their own — especially when the card is small relative to the frame.

**Anatomy:** `brand-ink` ground → the echo: the same card at ≈220% scale, 6px blur, 25–30% opacity, offset up so its larger text sits behind the card → the card itself (`WindowFrame` or a plain UI card), 900px wide, `radius-lg`, `shadow-float` → highlight or `signal-marker` on the one line that matters.

**Motion:** echo and card arrive together (Smooth, `dur-normal`). The echo pushes slowly (1.0 → 1.06 over the hold, Cinematic) while the card stays perfectly still — depth without floating. Cut, don't cross-fade, to the next screen.

**Rules:** the echo is always the same content as the card, never a different image. Ink ground only (on paper the echo turns into grey mush). Max one card per echo.

**You provide:** the screenshot or recreated UI.
