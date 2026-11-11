# Component Library v1.0
Tokens: see [[DESIGN_SYSTEM]]. Ref IDs: see [[VISUAL_REFERENCE_LIBRARY]].

### C01 iOS Status Bar — A
"9:41", signal/wifi/battery, white, 34 px from top. Sells "real phone". Refs R01,R05. C. Mistake: real time/notifications.

### C02 App Header — A
Left: round "=" menu button (72 px, surface.raised). Centre: segmented pill "Chat | **Code**" (active segment `#3C3C40`, bold). Right: **progress counter** "0/3 → 3/3" in round chip, increments each demo; R04/R06 use a new-chat icon + speaker avatar thumbnail instead. Refs R01,R04,R05,R06. C.

### C03 Greeting — A (optional)
Terracotta asterisk + "Evening, <Name>" centred at ~22% height, serif. Refs R04,R06. C. Appears on empty states only.

### C04 Autocomplete Chip — A
Rounded rect, `surface.accent-tint`, 1 px accent border at 25%; asterisk icon tile; **/command** in terracotta 500 + one-line description in secondary grey ("Full-screen animated explainer"). Sits above composer. Refs R01,R05,R06. C.

### C05 Composer — A
Rounded rect (`surface.input`), optional attached clip thumbnail (R04,R05,R06), typed text: slash part terracotta, rest primary; blinking caret; bottom row "+", sliders icon, mic, **terracotta square send button** with ↑. Refs all A. C.

### C06 iOS Keyboard — A
Dark keyboard, predictive bar showing quoted word, key-pop magnifier on pressed key. Present only while typing (~1 s). C.

### C07 User Bubble + Status line — A
After send: tiny right-aligned bubble (orange /cmd + text, or clip thumbnail + /cmd). Status: "✳ Animating with /x…" / "Editing with /x…" in grey with shimmer. C.

### C08 Output Card — A (hero)
81% width, ~1.65:1 tall, radius 36, centred, top ≈ 9% of height. Contains the generated visual. Bottom overlay: **Label stack** (C09) + optional **View pill** (C10). Refs R01,R05,R06. C.

### C09 Label Stack
Line 1 bold sans "<topic> explainer" / "liquid glass chart"; Line 2 italic serif "with Claude Code" / "with one prompt". Centred, lower 15% of card, on dark gradient scrim. C.

### C10 View Counter Pill
Pill outline 1.5 px white 25%, ▷ icon, rolling number (tabular, 800), "views" in grey. Number rolls up with motion-blurred digits. Refs R01. C.

### C11 Reply Bar — A
Bottom: "+ Reply to Claude…" pill + mic + circular ↑. Always visible when keyboard hidden. C.

### C12 Kinetic Caption (word-at-a-time)
2 lines, centred near top of content; past words 45% opacity, current word white bold with blue selection box + handles (A) — or B: single bold word at chest height, white with soft shadow; keyword yellow + larger. C.

### C13 Effects List Overlay — B
Persistent panel. R02: two glass columns (01–08 / 09–16), mono numbers grey, names white, **current item yellow/bold**. R03: Apple-Notes-style white card "Effects to try 01/24", checkbox list of /slash names, current one ticks. Placed upper-right / upper corners, ~30% width. C.

### C14 Effect Counter Badge — B
Top-left pill: red/orange square badge "01/24" + effect name ("Glass widgets"). C (R03).

### C15 Glass Widget Cards
Frosted cards with big numbers ("38 effects one clip", "Rendering 4K 31%", "Top reels 197K"), profile card with avatar. R03, R05 (liquid glass chart). C.

### C16 Sticker Cut-out
Subject frozen, thick white outline, slight lift/shadow, name tag ("Brody / FOUNDER") in rounded pill with tilt. R05, R02(doodle). C.

### C17 Text-Behind-Subject
Giant number/word ("20K", "VIDEO EFFECTS", "RIGHT NOW") masked behind the person. R05, R03. C.

### C18 Tier List
S/A/B/C/D/F coloured squares (rainbow) on dark glass, items drop in. R03,R04,R05. C.

### C19 CTA End Card (all refs)
bg.app-deep; terracotta asterisk (A, R01) ; **"Comment “WORD”"** — WORD terracotta (R01: WORD 2.2× size with giant curly quotes) or white with terracotta pill subline "for every style's prompt" / "and I'll send you all 6"; below: grid (3×2 / 3×3) or fanned carousel of output thumbnails with view counts. Last 3–4 s. C.

### C20 Proof Grid / Fan
Thumbnails of outputs: fanned perspective row (R01) or 3-col grid with labels under (R04, R06). C.
