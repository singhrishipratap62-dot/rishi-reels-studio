# roughcut_v3 — Storyboard (for approval before build)

**Format:** 1080×1920 · 30 fps · 33.5 s · Paper Stage style (skill palette, Inter + Playfair Display)
**Your decisions folded in:** Claude orange #D97757 for the brand pieces · output in shot 2 is a mockup for now · a short black-and-white beat (0.9 s) · version rail for "iterations" · line 9 becomes two screens, a drowsy one and then an animated skill-folder one.

**Build tool:** Tesseract (tesseract-video), locally on the laptop, from `roughcut_v3.mp4` with its own audio. No Claude artifact.
**Logos and UIs:** product screens are clean recreations in the Paper Stage UI style, with "Claude" in plain Inter. If you want the real Claude / GitHub marks on screen, drop the PNG/SVG files in `Video Projects/` and I'll use them; otherwise I'll keep text-only labels.

**Captions (K01):** on every A-roll shot. Inter Regular 42 px, white, faint shadow, lowercase, 1–4 words, hard swap per phrase. They sit under the chin at y ≈ 1270 px (chin_y 0.644), are hidden under the CTA card, and don't appear on full-screen graphics.
**A-roll return (K02):** after every full-screen graphic, the first 3 frames go blur 20 → 0 and scale 1.04 → 1.00.
**Drift:** every full-screen scene scales 1.00 → 1.05 over its length. Entries are blur-ins (4–6 frames, blur 16 → 0). Exits are hard cuts.

---

### Shot 1 · 0.00–0.55 · A-roll
**Says:** "Claude में video डाल…"
**Screen:** Rishi, caption "claude में video डाल".

### Shot 2 · 0.55–2.87 (2.3 s) · K17 chat mock + K09 cursor · full screen
**Says:** "…के ये prompt डाल दोगे तो ऐसा कुछ बन जाएगा।"
**Ground:** lavender paper #F6F4FA with a soft grey contact shadow under the window.
**Hero:** a rounded chat window (radius 28, 1 px #E3E7E5 border, subtle mint dot texture) with the header "Claude" in plain Inter and an empty input bar.
- **0.55** ("video"): a file chip "roughcut.mp4" (small film-strip icon) slides into the input from below with blur.
- **0.85–1.45** ("prompt"): the prompt types in letter by letter: *"edit this like a pro ✨"*.
- **1.45–1.70** ("दोगे तो"): the gradient pixel cursor (blue #5B8CFF → #1F5FD6, 16×22 grid) glides in an arc to the Send button and clicks (2-frame dip). The button turns mint and 3 pixel sparkles burst.
- **1.77–2.87** ("ऐसा कुछ बन जाएगा"): **MOCKUP output** blurs in above the input. It's a polished 9:16 reel card with a gradient frame, a big title "WOW." and a play button, and a small "mockup" tag in the corner. *(You'll tell me later what goes here.)*

### Shot 3 · 2.87–3.25 · A-roll (K02 return)
**Says:** "ऐसा कुछ…"
**Caption:** "ऐसा कुछ".

### Shot 4 · 3.25–4.15 (0.9 s) · K03 mono-beat · A-roll
**Says:** "…नहीं होता है।"
**Screen:** snaps to black and white (blur 12 → 0 over 3 frames, scale 1.08). The frame follows the nose from face.json with a tiny wiggle. One word in the centre, Inter Regular 80 px white with a soft glow: **"nope."** (or no word, your call). Hard cut back to colour.

### Shot 5 · 4.15–5.93 · A-roll
**Says:** "This doesn't work like that. आप दुनिया भर…"
**Captions:** "this doesn't work" → "like that." → "आप दुनिया भर".

### Shot 6 · 5.93–8.10 (2.2 s) · K10 stack-in · full screen
**Says:** "…की skills इकट्ठा कर लो, GitHub repos इकट्ठा कर लो।"
**Ground:** white paper with a mint floor (lower 30 %).
**Headline (K04, top-left):** grey lead-in "collect all the" (Inter Light 44). The big word (Inter Medium 160) starts as ghost grey.
- **5.93** ("skills"): the big word **"skills"** inks. Paper skill files with folded corners (e.g. *video-editor.md, caption-pro.md, motion-kit.md, viral-hooks.md, color-grade.md*) drop onto the floor one every 0.2 s and pile up.
- **6.75** ("GitHub repos"): the big word swaps to **"repos"** and inks. Repo cards (a generic book icon, a made-up name, a "★ 12.4k"-style count) stack on top of the pile, so it gets comically tall.
- Pixel accents: 2 small squares and a coin-style star.
**Hard cut** at 8.10.

### Shot 7 · 8.10–9.15 · A-roll (K02)
**Says:** "जब तक आप Claude को अपना…"
**Captions:** "जब तक" → "आप claude को अपना".

### Shot 8 · 9.15–10.75 (1.6 s) · K06 paper-stage · full screen
**Says:** "…taste या design skill नहीं समझा पाओगे,"
**Ground:** white, with a yellow floor (#E9C95A → #F4E3A1) in perspective.
**Hero prop:** a paint palette with a fat brush resting on it, drawn in code, slightly pixel-edged, with a soft shadow. It slides up with blur.
**Headline (K04, top-right):** lead-in "until you teach it your".
- **9.15:** **"taste"** inks in Playfair Display italic (the one accent word).
- **9.51–9.79:** **"& design skill"** inks in Inter Medium.
**Accents:** 2 pixel squares and a tiny pixel sparkle.

### Shot 9 · 10.75–13.39 · A-roll (K02)
**Says:** "वो आपके लिए कुछ घंटा अच्छा edit नहीं करने वाला है। And ये पूरी video भी…"
**Captions:** phrase by phrase.

### Shot 10 · 13.39–14.71 (1.3 s) · K19 object lower-third · on A-roll
**Says:** "…end-to-end Claude से edited है।"
**Screen:**
- A rounded base plate in the orange gradient (#D97757 → a darker shade) wipes in from the left at y ≈ 72–84 %.
- A drawn clapperboard slides in on the plate with motion blur, and a white shine band sweeps across.
- At **13.73** a pill pops above it: **"EDITED BY CLAUDE"** (Inter Bold caps 36, plain text, no logo).
- The caption stays above the plate.

### Shot 11 · 14.71–16.11 · A-roll
**Says:** "Why does this look better than all…"
**Captions:** "why does this" → "look better" → "than all".

### Shot 12 · 16.11–17.45 (1.3 s) · K06 paper-stage · full screen
**Says:** "…the Claude slop which you see out there?"
**Ground:** white, with a dark-red felt floor.
**Hero:** a messy pile of **identical generic "AI slop" cards**. Each has a purple-to-pink gradient, a 🚀, "10X YOUR LIFE" and stock sparkles, and they boil slightly so they feel cheap and samey.
**Headline (K04, top-left):** lead-in "than all the", big "Claude **slop**".
- **16.43:** "slop" inks in red #D23C4C.

### Shot 13 · 17.45–18.78 · A-roll (K02)
**Says:** "Because मैंने उसको समझाया। पहली बार में…"
**Captions:** phrase by phrase.

### Shot 14a · 18.78–19.98 (1.2 s) · "drowsy" screen · full screen
**Says:** "…आपको उसको मेहनत से समझाना है"
**Ground:** greyish paper, slightly desaturated.
**Hero:** the same chat window as Shot 2, but **tired**:
- dimmed colours and a header dot that slowly blinks;
- a little sleepy face with "z z z" drifting up;
- a progress bar stuck at 12 % and jittering back and forth;
- a blurry, grey, broken-looking output card with a crooked thumbnail;
- a tag "no skill loaded".
**Motion:** the slow, droopy kind. The window sags 6 px, as if it's nodding off.

### Shot 14b · 19.98–21.70 (1.7 s) · animated skill-folder screen · full screen
**Says:** "कि क्या करना है, कैसे करना है और एक बार वो समझ गया,"
**Ground:** bright white with a mint floor.
**Hero:** the same window, wide awake, with a folder **paper-stage-edit/** opening inside it. Your real skill files cascade in, staggered: SKILL.md, RULEBOOK.md, LOOKBOOK.md, SOUND.md, LESSONS.md.
- **19.98** ("क्या करना है"): the cursor clicks **RULEBOOK.md**, which goes mint with a tick and a side label **"what to do"**.
- **20.54** ("कैसे करना है"): the cursor clicks **LOOKBOOK.md**, which goes mint with a tick and the label **"how to do it"**.
- **21.28** ("समझ गया"): the progress bar fills to 100 % with a green check and pixel sparkles burst.

### Shot 15 · 21.70–22.27 · A-roll (K02)
**Says:** "…गया। कुछ…"
**Caption:** "कुछ".

### Shot 16 · 22.27–23.47 (1.2 s) · K20 version rail · on A-roll
**Says:** "…iterations के बाद it will get…"
**Screen:** a thin teal ruler (#49B79A, ticks every 24 px) down the left edge, with a dark pill (#2E2E2E at 70 %) at y ≈ 25 % and a pixel flower on its left. The label rolls up as he speaks:
- **22.27** "v1";
- **22.67** "v2";
- **23.09** "v3" (true: this is roughcut v3).

The caption stays under the chin.

### Shot 17 · 23.47–29.10 · A-roll
**Says:** "…so better that it can do the whole thing autonomously without your intervention. And if you want to learn how I did this,"
**Captions:** phrase by phrase. This is the longest plain stretch, 5.6 s (the limit is 8).

### Shot 18 · 29.10–31.06 (2.0 s) · K18 CTA card · on A-roll
**Says:** "comment "edit" and I will send you a step-by-step…"
**Screen:**
- His lower half blurs and darkens (gradient 0 → 70 %).
- An orange card (780 px wide, radius 32, #D97757 gradient) blurs in at y ≈ 64 %.
- A tab pill **"comment"** with a pixel flower sits on top. Inside: **"EDIT"** in big type that lights up at 29.48, and under it "for the step-by-step breakdown". Each word goes from 35 % to 100 % opacity as he says it.
- Captions are hidden while the card is up.

### Shot 19 · 31.06–33.50 · A-roll to the end
**Says:** "…breakdown of how you can achieve these kind of results."
**Captions** to the end. No graphics: it ends on plain A-roll.

---

## Checks
| | value | target |
|---|---|---|
| graphic share | 15.7 s = **47 %** | 40–45 % (2 % over, because of the black-and-white beat and the two-screen line 9) |
| first graphic | 0.55 s | ≤ 2 s ✓ |
| hook coverage 0–8 s | **66 %** | ≥ 60 % ✓ |
| longest A-roll | 5.6 s | ≤ 8 s ✓ |
| ends on A-roll | yes | ✓ |

## Notes
- **Audio:** the rough cut's own voice track is kept as-is. Sound effects come later, at the Sound step.
- **Before the full render:** a design sheet (one still per graphic shot) for your approval, per the skill.
- **Assets:** none needed from you. Everything is drawn in code, and the skill filenames are your real ones.
