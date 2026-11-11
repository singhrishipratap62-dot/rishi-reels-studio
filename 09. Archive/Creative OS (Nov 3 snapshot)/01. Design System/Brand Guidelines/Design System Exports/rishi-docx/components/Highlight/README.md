# Highlight

The one way to emphasise words: inside real text (articles, posts, docs, screenshots, chat) and on motion-graphic headlines, labels and list rows. Three strengths of the same bar, never a pen circle.

**Use for:** pointing at what matters in a source while it's read out (`ReadAlong`, `PostCard`, `WindowFrame`, `ChatFrame`).

**Anatomy:** a flat bar behind the words, very subtly rounded ends (`radius-highlight`, 6px at 1080), 4–6px padding either side, wrapping cleanly across lines.

| Level | Token | Text colour | When |
|---|---|---|---|
| 1 · Follow | `highlight-follow` | `ink` | The words being read out right now. |
| 2 · Key line | `signal-marker` | `ink` | The sentence that matters. One per frame. |
| 3 · The point | `signal-deep` (solid) | `brand-paper` | The single phrase to remember. Max one per frame. |

**Motion:** sweeps left to right, never fades in. Follow uses Voice (linear, at the speed of speech); Key line and The point use Draw easing, `dur-normal`. For level 3 the text turns paper as the bar passes it. Lines that aren't highlighted drop to `ink-ghost`.

**Rules:** text inside a highlight never turns red. A frame with a level 3 has no other signal moment (no pen mark, no red headline phrase). Step up as the voice lands: Follow → Key line → The point. In motion graphics it is the main emphasis tool: the hook's key word on The point bar, key labels and list rows on Key line. Use it in place of any pen circle.

**You provide:** the exact source text and which phrase gets which level.
