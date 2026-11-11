# FollowCard

The end-of-reel follow card: profile photo with a pen ring, name, handle, one line on what the account is, and a Follow button that gets tapped and turns into Following.

**Use for:** the last 2–3 seconds of a reel when the CTA is "follow". Not on every reel — only when the CTA type is follow (see the reel framework's CTA mix).

**Anatomy:** `label` "FOLLOW" → profile photo (the `Profile` asset `rishi-avatar.webp`), 360px circle → pen ring around it in `signal`, drawn on → name "Rishi" in `display` → handle "@rishi.docx" in `body` Medium, `ink-muted` → one line in `title` with one `accent-italic` signal phrase → Follow button (ink fill, paper text, 420×120, square) → pen arrow pointing at the button.

**Motion (about 4s in a reel):** photo scales up from 92% and fades in (Enter) → ring draws around it (250ms) → name, handle and line rise in, staggered → button and arrow arrive → the button is pressed (scales to 94% and back) → it swaps to "Following" on a `surface` ground with an ink border and a small ink tick. Holds, then the reel ends.

**Rules:**
- Two pen marks only: the ring and the arrow. The tick inside "Following" is part of the button, in ink, not a pen mark.
- The circle crop is allowed here because it is literally Instagram's avatar shape (UI), like the chat bubbles.
- Keep everything inside the reel safe area; on a 1080×1920 frame, centre the block vertically between `safe-top` and `safe-bottom`.
- The middle line is editable per reel ("AI, explained without the hype" is an example) — it should promise what the next reels give, and can tie to a concrete next reel ("Tomorrow: …").

**You provide:** the one-line promise for this reel (optional). Photo, name and handle are fixed.
