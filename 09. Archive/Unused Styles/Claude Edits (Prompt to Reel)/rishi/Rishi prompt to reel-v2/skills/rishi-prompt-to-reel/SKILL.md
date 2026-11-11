---
name: "rishi-prompt-to-reel"
description: "Build @rishi.docx Prompt-to-Reel reels (slash command typed in an app UI, then the result) in rishi.docx branding, delivered as two Motion builds: ink (dark) and paper (light)."
---

# rishi.docx Prompt-to-Reel (v1.2)

A 9:16 reel that sells "one prompt → a real result": a /slash-command is typed into a calm app UI, sent, and the generated visual takes over, with a label, a rolling number and a "Comment WORD" end card. Reverse-engineered from 6 reference reels (R01–R06). Full research docs, frames and mockups live in the user's folder `Teaching Claude/Claude Edits/_style_system/` (DESIGN_SYSTEM.md, COMPONENT_LIBRARY.md, LAYOUT_LIBRARY.md, MOTION_LIBRARY.md, VISUAL_REFERENCE_LIBRARY.md, BRAND_SKIN_RISHI_DOCX.md, mockups/rishidocx_prompt-to-reel_frame.html). Read them when the folder is connected; this file is enough on its own.

Brand: @rishi.docx only. Never use for gradnext reels (those use the gradnext design system).

## Workflow (every time)

1. **Input.** Rishi gives a short brief and usually a list of styles to cover. Sound is optional:
   - **Mute reel (common, the default when no SRT is given):** no voiceover, no SRT. The visuals carry everything, like the reference reels. Timing comes from the beat sheet, not from speech.
   - **With SRT / voiceover:** sync each style to its SRT line; captions follow the voice.
   - Talking head vs AI voiceover: he says which. If there is footage but it's unclear, ask.
2. **Styles not listed?** Do NOT pick silently. Show the Style Catalog below (grouped, one line each) and ask which ones he wants (and in what order). Wait for the answer.
3. **Beat sheet.** For each chosen style: slash name, one-line description, the typed prompt, label text, on-screen caption words, the number that animates, breakout yes/no, start/end time. Mute reels: 4–5 s per demo, total = demos × 4.5 s + 3.5 s end card. Show it briefly, then build.
4. **Keyword.** If Rishi gave the CTA keyword, use it. If not, do NOT ask at the start: build with the placeholder WORD, and ask for the keyword only at the very end, after the design is approved; then drop it into the end card (and the optional composer typing of the keyword) in both versions.
5. **Build two versions** in the Motion artifact type: **ink (dark)** and **paper (light)**. Same timing, same content, only the theme tokens change. Name them "<topic> - ink" and "<topic> - paper".
6. **QC** both against the checklist below, fix, then deliver both links with a one-line note. If the keyword is still WORD, ask for it now.

## Mute-reel rules

- The on-screen text does the talking: typed prompt, status line, kinetic caption inside the card (2–5 words written for the screen, not from a transcript), label stack, numbers.
- Give each beat enough read time: caption on screen ≥ 1.2 s; type the prompt at a readable 12–15 chars/s; keep prompts short (≤ 8 words after the slash command).
- No caption band at the bottom (no voice to caption). Keep the in-card caption band only.
- Deliver a soundtrack-friendly SFX stem anyway (key clicks, send pop, reveal whoosh, counter ticks), plus a note that he can lay music under it; the Motion build itself can be silent.

## Reel templates

- **T-A UI Showcase (default, 17–33 s):** per demo (4–5 s): compose screen (type the command ~1 s, autocomplete chip pops) → send (keyboard drops, user bubble flies top-right) → "Animating with /x…" status shimmer (0.4–0.8 s) → output card blur-to-sharp reveal → payoff: kinetic caption + label stack + rolling view count; header counter ticks (1/N → 2/N). Optional full-bleed breakout of the card at most once per 2 demos. Optional: type the CTA keyword in the composer. End card 3–4 s.
- **T-B Effects Reel (talking head, 22–35 s):** hook line 0–2 s; persistent numbered effects list (Notes-style card or two glass columns) with a counter badge "01/NN + name"; one effect per ~1 s on hard cuts, list item highlights as it plays; caption = the /effect name or keyword; a pull-back reveal mid-video; end card or comment-bubble CTA. Follow rishi.docx talking-head rules (green screen only in the hook split, then full-screen graphics).

## Style Catalog (everything seen in the references)

Keep names as slash commands. Source in brackets.

**A. Explainer / animation styles (output-card content)**
- /full-visual: full-screen 3D animated explainer of how a thing works (laptop battery wear, PS5 games on PC, touchscreen layers) [R01]
- /stat-chart: big number + line chart, annualised value climbing ("$4.1B") [R06]
- /paper-desk: paper notes and a chart pinned on a green cutting mat, hand-annotated ("THE HOOK") [R06]
- /headline: newspaper front page ("The Morrow Ledger") with highlighted lines [R06]
- /ink-wash: Chinese ink-wash landscape with red sun, title card mood [R06]
- /teardown: exploded 3D product view with numbered part labels (keycaps / switches / plate) [R06]
- /map-route: 3D clay-white city map with a blue route drawing between points [R06]
- /phone-ui: product app screens on a phone mockup with floating stat chips [R06 grid]
- /timeline: "From a garage to 31 countries" vertical milestone timeline [R06 grid]
- /editor-ui: dark editing-app UI with sliders and a timeline [R06 grid]

**B. Talking-head transformations (one clip, one prompt)**
- /over-the-shoulder: proof cards (view counts) appear behind the speaker [R05]
- /glass-graph: liquid-glass bar chart that counts up over the footage [R05]
- /freeze-frame: freeze, cut-out with white sticker outline, tilted name tag ("Brody / FOUNDER") [R05]
- /tier-list: S-to-F coloured tier list, items drop in (also "ai tier list", /ranking-list) [R03, R04, R05]
- /text-behind: giant word or number ("20K") behind the speaker [R05]
- /color-grade: flat footage → cinematic grade, BEFORE/AFTER tags and wipe [R05]
- /behind-the-person: content grid / profile page behind the speaker [R04]
- /split-screen: speaker plus a reference post ("Find a viral carousel → this button") [R04]
- /explainer: light card "Steal what works": another niche → your niche, with arrow, speaker below [R04]
- /trial-reels: three reel variants side by side with different hooks [R04]
- /storytelling: speaker with stacked story cards (timer, comments, "I made this carousel") [R04]

**C. Video effects (fast, ~1 s each)**
- /headline-wall, /zoom-through-cut, /vertigo, /green-screen, /phone-mockup, /digital-zoom (REC frame + zoom readout), /paper-cut (ransom-letter text), /ui-world (UI panels in 3D around speaker), /orbit (cards orbit the speaker), /frame-break (subject breaks out of a frame), /doodle-boil (hand-drawn outline jitter), /sticky-text (number tag stuck to a sticker), /before-after (light-leak wipe), /pull-back-reveal (pull back into an editor timeline), /depth-scatter (word scattered in depth), /comment-bubble (comment box types the keyword) [R02]
- /glass-widgets (frosted stat cards), /locked-on (focus brackets track the face), /glitter-spotlight, /backdrop-word (huge word behind), /rabbit-hole (nested frames zooming in), /claude-ui (clip shown inside a chat app), /shadow-puppet (shapes cast on the wall), /shortcut-rain (keycaps falling), /the-bill (receipt itemising the edits), /reject-stamp, /giant-captions, /dot-reveal (dot-matrix halftone reveal), /profile-wall (Instagram profile grid with a count), /red-collage (red bold "ONE CLIP / 24 EFFECTS / ZERO APPS" collage), /phone-fan (fanned phones), /moody (dark grade), /countdown (flip clock), /pullback (zoom out to the phone in Instagram), /ascii (clip turned into ASCII) [R03; a few of its 24 effects weren't legible]

**D. Structure devices (use in every reel)**
- compose-screen typing, autocomplete chip, send + status shimmer, header progress counter, label stack, rolling view-count pill, proof grid / fanned carousel, "Comment WORD" end card.

Taste conflicts (ask before using): /reject-stamp (rishi.docx bans stamps; offer the word on a solid red bar instead), anything that tilts or exits diagonally, any red pen circle.

## rishi.docx skin (overrides the reference look)

| Token | ink (dark) | paper (light) |
|---|---|---|
| bg | #141414 | #f4f1ea |
| surface (inputs, bubbles) | #1f1e1c | #e9e4d8 |
| raised (keys, chips) | #2b2a27 | #dcd6c8 |
| output card | #1b1a18 + 2px #f4f1ea14 border | #fffdf8 + soft shadow |
| inner panel | #262522 | #e9e4d8 |
| text | #f4f1ea | #141414 |
| muted text | #a29e95 | #5f5c56 |
| signal (only accent) | #e2432a | #e2432a |

- Brand mark: 22px signal square + "rishi .docx" wordmark centred in the header. No Claude asterisk, no "Chat | Code" toggle. Reply bar: "Ask rishi.docx…" with a round signal send button. Below it, chips of the reel's slash commands, the current one outlined in signal.
- Fonts: Bricolage Grotesque 700–800 for big numbers, hooks, CTA word. General Sans 400/500/600 for UI, captions, labels, slash commands. Gambetta italic 400 in signal only for the label sub-line ("with one prompt"), about 58 px; if Rishi rejects it, use General Sans 500 muted. Nothing under 32 px.
- Key word emphasis: solid signal bar behind the word, paper text, 8 px radius ("The point" bar). Not-yet-revealed words at 40% opacity.
- Shapes: UI elements rounded (28 px cards, pills 999). Brand graphics inside cards stay square and editorial.

## Layout (1080×1920, 30 fps)

- Status bar "9:41" top 34 px; header y 96–180 (menu button, wordmark, counter "n/N"); user bubble top-right y ~212.
- Output card: x 102–978 (81% width), y 400–1500, radius 28. Inside: caption band at top (y +70), content panel y +250 to +720, label stack (sans 52 px / Gambetta italic 58 px) ~y +780, view pill at the bottom.
- Reply bar y ~1540; command chips ~1690 (chrome only, no key text below y 1500).
- Voiced reels only: VO captions follow rishi.docx caption rules and must not collide with the card; mute reels have no VO captions.
- Text never sits over a graphic. Everything symmetric about x = 540; zooms anchor on centre.
- End card: bg, brand mark, "Comment" (General Sans 600), WORD in Bricolage 800 signal ≥120 px, sub-line on a signal pill ("for every style's prompt"), proof grid 3×2 or 3×3 of every output shown, with labels.
- Talking-head reels (T-B): rishi.docx rules (green screen only in the hook split, captions in the graphics half, nothing static more than ~3 s).

## Motion

- Typing 12–15 chars/s with key pop, caret blink; autocomplete chip rises 8 px in 200 ms.
- Send: button press scale 0.92, keyboard slides down, bubble flies up (300–400 ms).
- Reveal: card blur → sharp + scale 0.96 → 1 (400–700 ms). Breakout: radius → 0, full bleed, 400 ms each way.
- Captions word by word (rise 38 px, 60 ms stagger); the signal bar sweeps behind the key word (on the voice if voiced, on the beat if mute).
- Numbers roll like an odometer with motion blur (1.5–2.5 s, ease-out).
- Exits: lift-and-fade (rise 60–100 px, ~0.6 s). No spins, page curls, diagonal exits.
- Rhythm: a visual change every ~1 s; one demo per 4–5 s (T-A) or one effect per ~1 s (T-B). Nothing static over 2 s except the end card.
- SFX stem (separate; ~8 dB under voice when voiced): key clicks on typing, soft pop on send, whoosh on reveal, tick on counters, riser into the biggest reveal.

## QC checklist (both versions)

1. First frame is a command being typed or a numbered list, never a logo or title card.
2. Only signal red as accent; red in every frame.
3. Every demo labelled (slash name + label stack).
4. A number moves in every demo.
5. Counter ticks n/N; chips match the chosen styles.
6. No text over graphics; nothing in the IG safe zones (top 250, bottom 420, right 160).
7. No stamps, red circles, tilted pairs or diagonal exits.
8. Fonts: Bricolage numbers/hooks, General Sans UI, Gambetta only in the sub-line.
9. Mute reel: every caption readable (≥ 1.2 s on screen) without sound.
10. End card "Comment WORD" + proof grid, held ≥ 2.5 s; keyword confirmed (not the WORD placeholder) before final delivery.
11. Ink and paper versions are identical apart from theme.