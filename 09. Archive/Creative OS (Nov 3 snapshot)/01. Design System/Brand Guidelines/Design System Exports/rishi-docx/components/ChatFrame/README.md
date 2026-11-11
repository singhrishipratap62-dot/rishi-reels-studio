# ChatFrame

A recreated chat with an AI, shown as UI, with the key phrase highlighted.

**Use for:** showing what a chatbot or AI model actually said in a story.

**Anatomy:** `surface` panel with `radius-lg` → user bubble in `ink` (paper text), right-aligned → AI bubble in `bg`, left-aligned, with a small `label` speaker name → key phrase with a `signal-marker` highlighter swipe → `caption` source line ("Recreated from [source]").

**Motion:** bubbles rise in one by one; the AI reply can type on word by word. Highlighter swipes across the key phrase last.

**Rules:** only quote what the source actually reports. Mark it as recreated, not a real screenshot. Rounded corners here only, because it's UI.

**You provide:** the exact messages (from the source) and the source.
