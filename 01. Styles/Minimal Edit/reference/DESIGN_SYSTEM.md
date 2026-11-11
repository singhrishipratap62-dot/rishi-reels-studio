# Minimal Editorial — Design System v1.1

> v1.1 (2026-11-02) adds Rishi's corrections from the first Tesseract edit. Tag: `[R1.1]` = a rule Rishi set directly (it outranks `[EST]`/`[INF]`). Full context: `../history/LESSONS_LEARNED.md`.
> **v1.2 (2026-11-11):** this is a reference doc. `../SKILL.md` is the mandatory read and holds the compiled current rules; lines changed to match it are marked `[v1.2]`. Tag `[R1.2]` = a Rishi rule from the series-intro edit (2026-11-03).

Source of truth for the "premium minimal talking-head" style taught in Joseph's tutorial *How to Edit VIRAL Talking Head Videos Using ONLY Claude* (reference creator: Arthur Brooks reels). Built from the tutorial (video + transcript) plus 7 reference reels supplied alongside it (R1–R7).

**Evidence tags used everywhere in this system**
- `[OBS]` seen directly in frames (timestamp given)
- `[TX]` stated in the tutorial transcript
- `[EST]` measured/estimated by me from frames or pixels — treat as starting values
- `[INF]` my interpretation; not shown or stated

---

## 1. Philosophy

1. **Calm authority.** Few elements, lots of negative space, one accent colour. The look should feel like a printed essay that moves. `[TX 01:09–01:34, INF]`
2. **The speaker's face is a scene type, not filler.** A-roll is chosen on purpose: whenever a new idea/category is *announced*, we see the speaker; whenever it's *explained*, we see it. `[TX 14:15]`
3. **Every visual literally illustrates the line being spoken.** No decorative B-roll. If you can't find something that shows the idea, stay on A-roll with captions. `[TX 02:15, INF]`
4. **Texture makes it premium.** Paper grain, paint, cloth and noise sit on almost every graphic so nothing looks like flat vector/AI output. `[TX, OBS throughout]`
5. **One consistent kit across many scene types.** Ten scene categories, one shared palette, type pair, texture set and edge treatment. `[TX 04:54]`

## 2. Canvas

| Item | Value | Tag |
|---|---|---|
| Ratio | 9:16 vertical | `[OBS]` all reels 720×1280 |
| Production size | 1080×1920, 30 fps | `[OBS]` final export "MP4 · 1080×1920 · 0:57" at 17:00 |
| Safe zone | **Instagram Reels template:** everything inside x 120–960, y 250–1600, and keep the icon column clear (x > 845 below y 1130). Check positions *after* scene push-ins; audit every build | `[R1.1]` |
| Side margin | ~~~6–8 % of width~~ superseded: the safe zone above sets the margins (x ≥ 120 px ≈ 11 %) | `[v1.2]` |

## 3. Colour

| Token | Hex | Use | Tag |
|---|---|---|---|
| `accent.blue` | **#0B52F9** (range #0855FA–#1B51F9) | full-bleed blue backgrounds, painted illustrations, serif emphasis words, lines | `[EST]` pixel medians R4 0:17, R6 0:17, R4 0:11 |
| `accent.blue.light` | #1A83FB / #216FEB | glows, orbs, gradient halos, highlights on dark | `[EST]` R6 0:41, R3 0:12 |
| `accent.blue.legacy` | #0D6BD9 | older/cooler variant (R2) — avoid mixing with main blue in one video | `[EST]` R2 0:04 |
| `paper.white` | #FCFAFB → #F2F2F2 with grain | light backgrounds | `[EST]` R4 0:28 |
| `ink.black` | #0D0D0D | dark backgrounds (never pure #000 once textured) | `[EST]` R2 0:04 |
| `graph.dark` | #121212–#1A1A1A + noise | graph scenes | `[OBS]` 05:40, final 0:01 |
| `text.on-dark` | #FFFFFF | captions on A-roll/B-roll/dark | `[OBS]` |
| `text.on-light` | #111111 sans; `accent.blue` serif emphasis | white paper scenes | `[OBS]` 05:08 "same job" |
| `grid.line` | white @ ~10–20 % opacity, slight glow | graphs | `[OBS]` 05:42 |
| `highlight.box` | `accent.blue` fill, white text | single-word callouts ("decline", "42 years") | `[OBS]` R1 0:08, final 0:18 |

Rules: one accent hue per video `[INF]`; blue is never used for body text on blue; A-roll footage keeps its natural grade, darkened at the bottom (vignette/gradient) so white captions read `[OBS final 0:00]`.

## 4. Typography

| Role | Reference font | Character that matters | Tag |
|---|---|---|---|
| Primary | **Inter** (Bold/ExtraBold for hero; Regular/Medium for support) | neutral grotesk, tight, high x-height | `[TX 01:32]` |
| Secondary | **Playfair Display Italic** (Bold Italic for hero) | high-contrast didone italic, editorial | `[TX 01:32]` |
| Observed alternates | a condensed high-contrast serif roman (R4/R5 "worked", "suffering", "project") | same role as Playfair | `[OBS]` |

**Hierarchy (estimates from 1080×1920):**

| Level | Size | Weight | Tracking | Tag |
|---|---|---|---|---|
| Hero word (1–2 words) | 90–130 px | Inter 700–800 (graphic scenes only) or Playfair Bold Italic (always on A-roll; upright only as an offered alternative `[R1.2]`) | −2 % to −4 % | `[EST]`, `[v1.2]` |
| Support words | **48 px (≈ 36 % of hero)**, tight to the hero | Inter 500 | 0 | `[R1.1]` (was 26–36 px — read as too small and floating) |
| Quote / text-centric line | 40–60 px | Inter 600 + serif accent | −1 % | `[EST]` |
| Line height (stacked) | 0.85–1.0 for hero; support sits tucked within ~0.2 em of hero | — | `[EST]` |

Tutorial's Figma breakdown notes on one caption: "Multiple sans light small text", "Singular or double bold sans text", "Distance of the light sans text is 75 % of the big bold text" `[OBS 08:54 — wording read from a small frame; meaning of "75 %" uncertain]`.

**Placement logic** `[TX 01:32–01:54]`
1. Chunk the script into lines of ≤ 5 words.
2. Pick the 1–2 most important words → hero (bold sans **or** bold serif italic), centred.
3. Put the remaining words small in the free space *above* (lead-in) and/or *below/right* (tail), often left- or right-aligned to the hero's edge, not centred.
4. Asymmetric but balanced: support text hugs a corner of the hero.
5. ~~Serif italic = emotion/abstract/emphasis words; sans bold = concrete nouns/numbers~~ `[INF from R1–R7 usage]`. **Superseded in v1.1:** A-roll caption heroes are **always serif** (Playfair Display Bold Italic, lowercase), even words like *not*, *industry*, *first principle*. Bold sans heroes are only for full-screen graphic scenes, where they give contrast `[R1.1]`. Series intro: Rishi compared an upright serif and shipped the Bold Italic, so Bold Italic stays the default; offer upright only as an alternative `[R1.2]`.
6. **Tight placement** `[R1.1]`. The line above has its baseline at `hero_y − 0.80 × hero_size − 8` and is inset about 7 % of hero width from the hero's left edge. The line below is inset about 7 % from the hero's right edge, about 58 px under the baseline (74 px if the hero ends in a descender).
7. When the hero stands alone with one trailing word ("*first principle* … thinking"), the trailing word goes **above, on the right**, small `[R1.1]`.
8. Cap the hero at **740 px** wide so the italic overhang stays inside the safe zone; shrink long support lines to fit `[R1.1]`.

## 5. Texture library

See §5 in TEN_SCENE_PRINCIPLES for per-scene use. Summary:

| Texture | Look | Where | Intensity | Tag |
|---|---|---|---|---|
| Light paper | fine grain + faint fibres | over B-roll, paintings, white bgs | low (5–12 % overlay) | `[TX 02:15]` |
| Rough paper | visible mottling, speckles | white & blue text-centric bgs, center illustrations | medium | `[OBS 04:04–04:08]` |
| Paint | brush/canvas texture | paintings | low–medium; must **move with the image** | `[TX 17:00 revision #3]` |
| Rough painted noisy | dry-brush, speckled blue fill, ragged edges | character silhouettes, center illustrations | high on the subject only | `[OBS 04:26 "Rough, painted, noisy"]` |
| Rough cloth | woven/fabric fibres + diagonal light | character profiles, half-circles | medium | `[OBS 04:48]` |
| Noise | fine luminance noise | dark & graph bgs | low | `[OBS 05:40]` |
| Edge darkening | vignette, stronger at bottom | B-roll, paintings, A-roll bottom | medium | `[TX 02:15]` |
| Edge blur | soft blur ring outside focal subject | B-roll | low–medium | `[TX 02:15]` |
| Dot/halftone grid | faint dot pattern on white | white illustration bgs | very low | `[OBS final 0:19–0:37]` |
| Glow/halo | soft blue radial behind subject | center illustrations, orbs | medium | `[OBS R6 0:58, final 0:19]` |

Rule: textures are static relative to their layer — if a layer moves/zooms, its texture moves with it. `[TX revision #3]`

Engine note (Tesseract grain effect): `amount 0.25` was invisible. Use **0.8 on light grounds, 1.0 on dark**, size 1.6, plus a vignette (0.18 light / 0.35 dark) `[R1.1, measured]`.

## 6. Layout

- Single focal point per frame; ≥ 50 % negative space on graphic scenes `[EST]`.
- Center illustration: subject occupies lower ~55 %, "bleeds" up into the upper-middle; text fills top third `[TX 04:30]`.
- Side layouts: subject on one side (≈ 45–55 % width), text block on the other `[TX 05:18]`.
- A-roll captions: hero word around y 55–70 % (chest/mic area), never at the very bottom `[EST from R1, R7, final]`. Exceptions `[v1.2]`: split-screen → seam band (below); a graphic-print shirt → move the caption block below the print per framing (standing shots: hero y ≈ 1480–1510) `[R1.2]`.
- Text-centric: text block slightly above centre; quote marks bracket the text: the opening mark hugs the first line top-left, the closing mark sits after the last line, bottom-right `[R1.1, v1.2]` (was "close top-right of block" `[OBS 04:08]`).
- Graphs: dark card, thin grid, label text top area `[OBS]`. Keep the whole graph inside x 160–840 `[R1.1]`.
- **Graphics Rishi places himself** (e.g. series-intro cards at top 170 px, grid at x 38) keep his geometry over the safe-zone template; captions still obey the safe zone. Panels such as a 30-day grid go **behind the subject** (person matte); on close or standing framings card stacks also go behind him so they never cover the face `[R1.2]`.
- **Split-screen / two-person sources** (e.g. Riverside): if kept as is, put captions on the **seam band** (y ≈ 680–1240) over a vertical gradient scrim (transparent → 70 % black → transparent). It's the only band that covers neither face `[R1.1]`.

## 7. Scene categories

A-roll + captions, plus the ten principles (details in TEN_SCENE_PRINCIPLES.md):

| # | Category | Background family |
|---|---|---|
| 0 | A-roll + cinematic captions | footage |
| 1 | Cinematic caption design (applies everywhere) | — |
| 2 | B-roll + cinematic text | footage (treated) |
| 3 | Painting + text | painting (treated) |
| 4 | Line + text | black or white paper |
| 5 | Line + illustration (3 variants) | black or white paper |
| 6 | Text-centric | white or blue rough paper |
| 7 | Center illustration + text | white paper (also blue/dark) |
| 8 | Side illustration + text | white/blue paper |
| 9 | Object + text callout | white paper |
| 10 | Graphs & statistics | dark textured + grid |

## 8. Component library (build once, reuse)

| Component | Props |
|---|---|
| `CinematicCaption` | words[], heroIdx[], heroFont(sans/serif), layout(above/below/left/right), revealMode |
| `PaperBg` | tone(white/blue/black), roughness, grain, dots |
| `TreatedMedia` | src, paperTex, vignette, edgeBlur, paintTex, kenBurns |
| `AccentLine` | path(svg), width, drawDuration, dot(bool), cameraFollow |
| `MarkerDot` | colour(white/blue), glow |
| `PaintedFigure` | src(cutout), fill(accent), texture(rough/cloth), halo |
| `QuoteMarks` | size, colour |
| `GraphCard` | grid, axes, series[], ball, labels, cameraFollow |
| `HighlightBox` | text, colour |
| `OrbitText` | items[], radius, speed |
| `PhotoCallout` | src, tilt, shadow, stack |
| `CameraRig` | pan/zoom keyframes for the whole scene |
| `WhipTransition` | direction, blur |

## 9. Editing rules (core)

1. A-roll on announcements, visuals on explanations. `[TX 14:15]`
2. One idea → one scene. Change scene when the idea changes, not on a timer. `[INF]`
3. Average shot ≈ 1.5–3 s (reference reels measured 1.52–3.14 s; tutorial final ≈ 2.3 s). `[EST]`
4. Visual beats sync to the exact spoken word (ball steps on each "up"; hero word lands on its syllable). `[TX 13:36]`
5. Every graphic carries text that reinforces the line (cinematic caption logic). `[TX 02:37]`
6. Hard cut in/out of A-roll; whip/slide transitions between consecutive graphic scenes. `[OBS 6 fps strips]`
7. Give illustrations time to read (≥ ~2 s once complete). `[TX revision #5]`
8. Remove micro-clips (< ~0.3 s) and stray words like a lone "But". `[TX revision #4]` Also no shots under 0.5 s, and short A-roll beats get ≥ 0.5 s of readable impact text `[R1.1, v1.2]`.
9. Captions on every second of the video, including over graphics where the line isn't already written. `[OBS]`

## 10. Consistency checklist (quick)
Same blue · same type pair · texture on every graphic · no flat vectors · ≤ 5 words on screen per beat · one hero per frame · motion eased, never linear · A-roll used intentionally.

## 11. Core vs optional vs experimental

- **Core:** colour tokens, type pair, caption placement logic, texture on every graphic, A-roll/visual alternation, 10 categories.
- **Core (added v1.1):**
  - Support text reveals word by word; impact text reveals character by character, left to right.
  - A-roll heroes are serif.
  - Support text is 48 px and tight to the hero.
  - Everything sits inside the Instagram safe zone.
  - Constant subtle A-roll push-in.
  - Dense-but-quiet sound on every text entry (see SOUND_DESIGN v1.1).
- **Optional variations:** blue vs white vs black base per scene, serif-roman alternate, highlight box, orbit text, glow orbs.
- **Experimental (seen in R1–R7, not taught):** glowing 3D-ish icons (R1 scales, R5 brain), document/paper-sheet inserts (R3, R6 "PANAS"), 2×2 matrices (R6), B-roll in a small floating card (R5 0:58), A-roll split with a second camera inset (R7 0:15).
