# rishi.docx skin for Prompt-to-Reel (v1.1)
This skin REPLACES the reference (Claude-look) tokens in DESIGN_SYSTEM.md for all @rishi.docx output. Source: rishi.docx design system artifact (tokens.css, Taste.md). Structure, layouts, motion and rhythm from the reference stay.

## Token swap
| Reference token | rishi.docx token | ink mode | paper mode |
|---|---|---|---|
| bg.app #1A1A16 | --bg | #141414 | #f4f1ea |
| surface.input #21211C | --surface | #1f1e1c | #e9e4d8 |
| surface.raised #3C3C40 | raised (step of surface) | #2b2a27 | #dcd6c8 |
| output card | card | #1b1a18 + 2px #f4f1ea14 border | #fffdf8 + soft shadow |
| text.primary | --ink | #f4f1ea | #141414 |
| text.secondary | --ink-muted | #a29e95 | #5f5c56 |
| accent.terracotta #D4704C | --signal | #e2432a | #e2432a |
| keyword selection box (blue) / yellow | **The point bar**: solid signal, paper text, 8px radius | same | same |
| Claude asterisk | rishi.docx mark: 22px signal square + "rishi .docx" wordmark | | |
| "Chat / Code" toggle | brand wordmark centred (no product imitation) | | |
| "with Claude Code" | "with one prompt" (or "with Claude", only when Claude is the real tool shown) | | |

## Fonts
- Big numbers, hooks, CTA word: **Bricolage Grotesque 700–800**.
- UI text, captions, labels, slash commands: **General Sans 400/500/600**.
- Label sub-line: **Gambetta italic 400** in signal, ~58px — the only serif on screen. (Open: Rishi dislikes Gambetta punchline words in talking-head reels; if he rejects it here too, swap to General Sans 500 in ink-muted.)
- Floor size 32px at 1080 wide.

## Rules inherited from rishi.docx Taste.md
- Touch of red on every frame; red only once per element.
- No red pen circles, stamps, diagonal exits, text over graphics.
- Every zoom anchored at x = 540; card symmetric about centre.
- Safe zones: text between y 250 and y 1500; right 160px clear.
- Captions (VO reels): General Sans Semibold 46px, words rise 38px, 60ms stagger, bottom at y ≈ 1490 — outside the app card when the card is full-height.

## Modes
- **ink** (default for app-showcase reels: matches reference mood).
- **paper** (for explainer-heavy or "calm" reels; also for light explainer cards inside ink reels).
- Mockups: mockups/rishidocx_prompt-to-reel_ink.png, _paper.png, source _frame.html (body class ink|paper).
