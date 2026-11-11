# Learnings: Rishi's editing style (updated)

> **History (v2.2, 2026-11-11):** fully compiled into `../SKILL.md` and `../reference/`; where each item now lives is in `RULE_AUDIT.md`. Kept for the why, not as a mandatory read.

Written 2026-11-09, after editing `roughcut_v3` ("Claude can edit your videos only once you teach it your taste") through four drafts in Tesseract.
This file comes from one long working session: what Rishi asked for, approved, rejected and corrected. Read it **before** planning any new edit.

> **Where this sits:** we started from "Azma's style" (Paper Stage: white paper stages, coloured floors, ink headlines, K-keys). The final edit is very different. It's a mix of **Minimal Edit Style** (the captions), **Rishi's Editing Style v1.3** (ink/ice cards, split pane, behind-the-head depth, comments-sheet CTA) and a few **Daniel Presley** ideas (name pill, framed screens). Treat this file as the current truth. The older skill folders are reference material to borrow from, not rules.

---

## 1. How Rishi likes to work (process)

### 1.1 The loop that worked
1. **Rough cut + SRT come from Rishi** (`03. Projects/Rishi Style v2/<Video N>/roughcut_vN.mp4`, SRT of the *original* recording). Claude maps the SRT onto the rough cut by matching audio (spectral features; raw waveform matching failed because the rough-cut audio is processed).
2. **Options board first** (local HTML): every frame type × **5 options**, each drawn as a phone-frame mock-up, with Keep / Maybe / No buttons, a notes box, and a "Copy my picks" button that outputs a text summary Rishi pastes back.
3. **Storyboard** (local HTML) of the picked options, frame by frame, *before* building.
4. **Build in Tesseract** (never Remotion, never a Claude artifact).
5. **Feedback rounds** by timestamp → numbered checklist (F1…Fn) → **storyboard first, then build**.
6. **Sound design** is included once the visuals are close (Rishi asked for it together with draft 2).
7. Deliverables: MP4 + editable `.tsrct` + filmstrip + `sound_cue_sheet.md`; on request, **SFX-only MP3** and **voice-only MP3**.

### 1.2 Hard preferences about the process
- **No Claude artifacts. Ever.** Rishi deleted one and said "We never create an artifact." Everything visual is a **local HTML file** he opens in a browser.
- **Visual over text.** Storyboards, plans and questions = HTML pages with drawn frames and real stills, not tables in chat. He also asked for image format once, so save a PNG screenshot next to the HTML.
- **Multiple options to choose from:** at least **5 per frame type**. He mixes them freely ("B as baseline, take a bit of A and C"). Expect mixes; build exactly the mix.
- **Frame-by-frame references when something's ambiguous:** for unclear animation ideas, show ≥5 interpretations as 5-frame strips (0.00 / 0.15 / 0.30 / 0.50 / 0.72 s) and let him pick.
- **Storyboard approval rule:** "If I don't tell you anything explicitly, assume the storyboard was approved." But when he says "storyboard only, don't make changes," stop after the storyboard.
- **Ask, but don't stall.** Questions are welcome; if he says proceed, list your assumptions *inside* the storyboard ("tell me if any is wrong") and keep going.
- **Each draft gets its own folder** (`roughcut_v3_edit`, `_v2`, `_v3`, `_v4`). Never overwrite a previous draft. "Keep that as it is."
- **Timebox investigations.** "If it takes more than 2–3 minutes to decide if it works, drop the idea." Example: the Brave/browser-editor check was dropped.
- **Approval gates for anything structural.** Installing tools, changing browser flags, new infrastructure: give a feasibility report first, wait for explicit approval, and only do the approved phase.
- **Report honestly.** He reads the filmstrips and the video; state what was checked (filmstrips, loudness, effects-only cue check, black frames) and what wasn't (Claude can't listen; levels are measured).

### 1.3 How he gives feedback
- Long voice-transcribed paragraphs with timestamps ("at 8 seconds…", "frame 6, around 16 s"). Split them into numbered items before acting.
- Words he uses: **"smooth"** (most frequent), "snappy" (bad), "pop" (bad), "premium", "subtle", "a little" (means small, not big; over-correcting is a mistake), "decent" (okay, not great).
- He notices **every** visual glitch: half-rendered glyphs, a black bar, an oval gap around the head, a white caption on a white tile, uneven padding inside cards.

---

## 2. What the videos are
- **Format:** 9:16 talking-head reels, 1080×1920, 30 fps, about 30–35 s, Hinglish (Hindi + English), creator speaking to camera with a lav mic, marble-wall background, green jacket.
- **Topic:** AI / Claude workflows for creators ("Claude edits my videos", skills, taste).
- **Structure:** hook (naive belief) → "no, it doesn't work like that" → hoarding skills/repos → thesis (taste / design skill) → proof ("this video was edited by Claude") → contrast with "Claude slop" → "I taught it" → iterations → autonomy → CTA "comment EDIT".
- **CTA:** comment keyword (EDIT) → DM breakdown.

---

## 3. Visual style (what got approved)

### 3.1 Overall feel
- **Premium minimal, smooth, calm.** One idea per screen. Long, soft ease-in-out curves. Never snappy, never a "pop".
- "Even if the animation stays a little longer on the screen, keep it smooth."
- The **face is the spine**: return to the face between graphics, and use the face *inside* graphics (shrinking into a chat, PiP, a tile in a wall).
- **Real things beat stand-ins:** real Claude / GitHub / Instagram logos, real skill filenames, his own clip inside mock-ups, his own face sticker as the comment avatar.

### 3.2 Palette
| Token | Hex | Use |
|---|---|---|
| ice ground | `#EAF0F8` | light graphic grounds (chat, split pane) |
| ink | `#0B1224` / text `#0B1730` | dark text on light, dark cards |
| accent blue | `#3E7BFA` | ticks, progress, send button, glow |
| card white → grey | `#FFFFFF → #E4E6EA` + soft radial vignette | **all white cards** (no blue tint in white areas) |
| muted | `#4A5878` (on light), `#9AA8C7` (on dark) | support text |
| green | `#2FD08A` | "sent ✓" state only |
| Claude orange | `#D97757` | only via the real logo |
- Grain on grounds (Tesseract grain amount 0.6–1.0). White/grey gradients on white elements must stay grey-scale.

### 3.3 Typography
- **Inter** (Light/Regular/Medium/SemiBold/Bold) + **Playfair Display Bold Italic** for hero words.
- Text in UI mock-ups: Inter. Big statements / captions: Playfair hero + Inter support.

### 3.4 Motion language (approved defaults)
- **Card reveal ("line → rectangle"):** a thin horizontal line opens from its centre into the full card (scaleY 3 → 100), unblurring (≈18 px → 0) and rising ≈40 px, about 0.65–0.7 s, smooth in-out. **No fade-pops, no scale-pops.** Use it for every card.
- **Exits:** slide (left or up) + blur + fade, about 0.5–0.6 s.
- **Word-by-word reveals** for lists inside cards (rise 26 px + fade, about 0.12–0.15 s stagger), like the design-skill.md lines.
- **Big moves** (shrinks, zoom-outs, PiP transitions): 0.8–1.45 s, smooth ease-in-out. No "pause, then snap".
- **Subtle life:** slow logo rotation (±6° over 3 s), gently drifting gradients, a slow orbit that starts fast and settles.
- **Corners:** subtle. Large rounded corners on tiles looked "weird"; ≈8 px on tiles, ≈14–36 px on cards.

### 3.5 Scenes that Rishi approved (the reusable library)
1. **Hook "shrink into chat":** the face slowly shrinks into a Claude chat card as the video attachment; the prompt types; a yellow highlighter swipes the prompt; send is pressed; the result card opens (line → rectangle) showing **his own clip, graded warmer, with a serif word**.
2. **Opening twin slide-out:** the Claude logo (on a **white disc with shadow**) and a framed card of his video slide **diagonally out from behind his head** (body matte) to the upper-left and upper-right, **not too high**.
3. **Black & white beat with nose-tracked camera** on the "no / doesn't work like that" line, starting the instant the hook returns to the face.
4. **Split pane (ice) swiping down from the top:** face in the lower half with the **full hair line visible just below the pane**; captions at the top of the white area; content below them, clear of the pane edge. Skill cards (white, small GitHub mark, even padding) arrive one by one, then dark repo cards glide in from the right.
5. **Doc + illustration in the split:** `design-skill.md` card (left of centre) + an **organic painted blue blob** (not a circle; "a circle has no personality") with **many orbiting words** (palette, practice, rhythm, sound design, pacing, texture, timing, typography).
6. **Behind-the-head card:** a timeline card (lanes with gradient bars, Claude name pill) behind the head via the person matte. A subtle eased zoom-in hides the jump cut.
7. **Wall zoom-out:** the face becomes the 2nd tile from the top of a wall of white "slop" tiles (Inter Bold, grey gradient text, slowly moving gradient). Starts exactly on the trigger word, zooms out slowly, holds.
8. **Picture-in-picture:** the face moves into a rounded, glowing PiP with the headspace cropped; **one card stays** above it while its **contents swap** (old rows slide left + blur, new rows rise word by word, evenly spaced with dividers). Return to full screen only **after** the line finishes.
9. **Comments-sheet CTA:** the face moves up, blurred and dimmed; a dark Instagram-style sheet + **full keyboard** rises smoothly; his **face sticker** is the avatar; EDIT types with key pop-ups (also shown in the suggestion bar); a soft tap dot on send; the button turns **green with a tick**. The sheet stays **until the very last moment** of the video.

### 3.6 Rejected or disliked (don't repeat)
- Paper Stage look as the main language (coloured floors, ink headlines everywhere): drifted away from it.
- "nope." text on the B&W beat: removed.
- Fade-pop / scale-pop entrances; snappy keyboard; sudden orbit words.
- White captions on white backgrounds; blue captions over the wall.
- A blank white beat of more than ~1 s between graphics.
- A separate behind-head scene for "iterations": keep the PiP layout and swap the card contents instead.
- The face cut off too low in the split (or a black bar): find the middle ground.
- Big rounded corners on tiles; circles instead of organic shapes.
- Over-correcting: when he says "a little higher," move a little (≈30 px), not 120 px.

---

## 4. Captions (most important)
Source: **Minimal Edit Style**, tuned by Rishi.

- **Romanised Hinglish, exactly as spoken** ("aisa kuch nahi hota hai"). No Devanagari, no translation, no paraphrase.
- **Hero word:** Playfair Display Bold Italic, lowercase, ≈132 px, white on the A-roll, ≤740 px wide.
- **Support words:** Inter Medium ≈48 px, white at ~85 %, **centred** above and below the hero (centre-aligned everything).
- **≤ ~22 characters per line**, ≤5 words per caption group. Don't overdo the text.
- **Reveal:** support words rise word by word on their spoken time; the hero builds letter by letter (slide + fade + light blur).
- **Placement:** below the chin, over a soft bottom gradient (0 → 45 % black over the bottom 40 %). **No blue hero colour** (he removed it) but kept the gradient.
- **Context-specific caption modes:**
  - On light graphic grounds (chat, split pane): dark ink, at the **top of the white area**, never touching cards.
  - PiP section: **one line of Playfair** between the card and the PiP.
  - Slop wall: **one word at a time**, pure black Playfair, inside the tile below the face, auto-fit.
  - CTA: **one word at a time**, Playfair, white, just above "Comments".
- **Glitch to avoid:** a blur effect on text layers clipped glyphs to a baseline strip ("bottom 3 % appears first"). In Tesseract, every blur needs `layerSize: [1080, 1920]`.

---

## 5. Sound design (approved approach)
- From **Minimal Edit Style `sfx/`**: dense but quiet, every text entry gets a sound.
  - Hi-Tech Click on hero words (≈ −17 dBFS), flick on support words (−27 to −30), highlighter on swipes/progress, pops on cards, tech-pop on ticks, key clicks on the keyboard, risertick when progress hits 100 %.
  - **Swooshes/wooshes: full length, with fade-in, peak on the move's midpoint** ("make the swoosh smoother and longer").
- First 5 s +3 dB. Final mix ≈ −15.5 LUFS, true peak ≤ −1 dBTP (achieved −7.2).
- Voice: the rough-cut audio is already mastered (≈ −13.9 LUFS), so only a 75 Hz high-pass and −1.5 dB.
- Always verify with an **effects-only render** (all cues within ±60 ms) and hand over `sound_cue_sheet.md`. Offer **SFX-only** and **voice-only** MP3s.

---

## 6. Assets and folders
- Logos: `assets/logos/<brand>/` (claude, anthropic, github, instagram; SVG + 1024 px PNG + README). Download real logos when needed and store them there for reuse.
- People: `assets/people/rishi/rishi-face-sticker.png` (avatar / face sticker).
- Person matte for "behind the head": (old path `Rishi's Editing Style/pilot/vid1/build/matte.mp4`, RVM, frame-aligned to roughcut_v3; the tool now lives at `02. Shared Core/engine/matte/matte.py`). Make a new matte for new footage.
- Storyboards: `03. Projects/Rishi Style v2/<Video N>/storyboard/<edit>_vN/index.html` (+ stills, + PNG).
- Edits: `03. Projects/Rishi Style v2/<Video N>/<edit>_edit_vN/` with `build*.py`, `.tsrct`, MP4, Previews, cue sheet, NOTES.

---

## 7. Tesseract (CLI 0.4.0) lessons that cost rebuilds
- Group/Video `playback.mapping.input` is on the **parent clock**: `input.start` must equal `inputRange.start`.
- Rect `rect.position` is the local top-left.
- **Keyframes on a nested Video clip don't work reliably:** wrap the clip in a Group and animate the Group.
- **Blur:** always set `layerSize`, or text and groups clip or show no blur.
- Shape fill opacity is 0..1 (colour alpha is ignored).
- `source.cropRect` didn't crop: use a punched framing (scale + position) plus a mask.
- Mask `cornerRadius` on path points is ignored: draw rounded rects with **cubic Bézier corners**.
- Track matte: `lumaInverted` with the matte Video mirroring the A-roll transform JS.
- Inter latin subset lacks ✓ ↑ ● glyphs, so draw them as shapes.
- Build everything from one regenerable script (`buildN.py` → editable.json + edits.json + cue sheet), always from a clean `base.tsrct` with assets pre-imported.
- If Rishi ever edits in a GUI, stop regenerating from scratch and edit the saved `.tsrct` in place (see the feasibility notes).

---

## 8. Open items / to decide later
- The Paper Stage skill (now `09. Archive/Unused Styles/Azma Paper Stage/skill/`) and its plan still describe the old Motion-artifact workflow. To be replaced by this updated style.
- Browser editor (official `tesseract-editor`): parked. It would need Brave's File System Access flag or Chrome.
- The result card in the hook was a mock-up early on; now it's his graded clip. Confirm per video what the "result" should show.
