# Button

A text button for digital surfaces — an intentional addition, since the guidelines define colour pairings but no button.

Provide `children` (a short verb phrase, sentence case) and optionally `variant` plus any native button props.

- `primary` — Chrome Yellow `highlight` with `on-highlight` text. One per view: the key action.
- `secondary` — Periwinkle `accent` with `on-accent` text. Supporting actions.
- `ghost` — outlined in `ink`. Tertiary actions; works on both themes.
- Corners `radius-sm`; focus shows a 2px `focus-ring` outline.
- Don't put yellow or periwinkle text on white; don't stack two primaries.
