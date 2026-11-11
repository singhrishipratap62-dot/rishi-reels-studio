# ReadAlong

A real post, article or document read along with the voice: a highlight walks across the exact words being spoken while everything else dims.

**Use for:** quoting a tweet, launch post, news article, blog, Wikipedia page or court filing — any real text you're reading from on camera.

**Anatomy:** the real source, recreated or screenshotted, in its frame (`PostCard`, `WindowFrame`, or a phone outline 760px wide) → the spoken phrase gets the Follow highlight (`highlight-follow`, ink text, rounded ends); the sentence that matters steps up to Key line (`signal-marker`), and at most one phrase to The point (`signal-deep` with paper text) → every other line, the avatar and the metadata drop to `ink-ghost`.

**Motion:** source eases in at full ink (150ms) → the rest dims (200ms) → the bar grows across each phrase with Linear easing at the speed of the voice → jumps to the next phrase. Highlights from the same sentence stay on; they clear together (100ms) when the sentence ends. A slow push-in (1.0 → 1.05) toward the active line is allowed.

**Rules:** highlight only what is said, word for word, so viewers can check it. One highlighted sentence at a time. Keep the real source readable at rest — the highlight points, it doesn't replace. Always show who posted and when (that's the source line).

**You provide:** the source (screenshot or text), the phrases to highlight in order, and the post/article metadata.
