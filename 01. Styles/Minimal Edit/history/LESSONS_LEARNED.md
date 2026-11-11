# Lessons learned — Minimal Editorial edits in Tesseract

> **History (v1.2, 2026-11-11).** Every rule here is compiled into `../SKILL.md` or a `../reference/` doc; see `RULE_AUDIT.md`. Don't read this to run an edit. §10 and two lines marked *(older copy)* were folded in from the archived duplicate so this record is complete. Old paths updated: `edits/` → `03. Projects/Minimal Edit/`, `SFX/` → the pack's `sfx/`.

From the first full edit: *First principles in consulting*, Kashish Malhotra podcast clip (34 s, 9:16 Riverside split screen), 2026-11-01/02. Project: `03. Projects/Minimal Edit/first-principles-kashish/`.
Read this **before** planning the next edit. Rishi's feedback here overrides older defaults in `DESIGN_SYSTEM.md` and `MOTION_LIBRARY.md` wherever they conflict.

---

## 1. Ask these up front (so they aren't discovered mid-edit)

| Ask | Why it mattered this time |
|---|---|
| Which design style? (default: this Minimal Editorial folder) | Rishi said he'd attach a style, but only the video came through |
| Framing for split-screen / multi-cam sources | The source was a Riverside split screen. He chose to keep it, which moved all captions onto the seam |
| **Platform safe zone** (default: Instagram Reels, §4) | Missed in draft 1–2; text reached the frame edge |
| **SFX library**: use the pack's `sfx/` first | Procedural sounds alone were judged "average at best" |
| Music: is there a licensed track? | None was supplied, so no bed. Ask before the sound pass |
| Speaker name / any words to verify | Whisper heard "i will stop" for "they will stop" (confidence 0.61) |

---

## 2. Text animation (Rishi's rules, now core)

**Two text roles, two motions. Never put whole lines on screen at once.**

| Role | Motion | Values that were approved |
|---|---|---|
| **Support / normal text** | **Word by word**, each word on its *spoken* time; rises from below while opacity eases up | rise 22 px → 0 over 420 ms, opacity 0 → 100 over 380 ms, ease-out `cubic-bezier(0.22,1,0.36,1)` |
| **Impact / hero text** | **Character by character, left → right.** Each glyph slides in from the left, **unblurs** and fades up | slide 28 px over 380 ms, blur 10 → 0 over 300 ms, opacity over 240 ms. Stagger = the word's spoken length ÷ glyph count, clamped 12–48 ms |

- He liked the blur, so keep it on impact text.
- The reveal must **finish ≥ 350 ms before the caption cuts**. If the word is spoken right before a scene change, push the scene change later (we moved the graph cut 260 ms so *faltering* could read).
- Drive every word from the word-level transcript. Never invent timings.

## 3. Caption layout

- **On A-roll, impact words are always serif** (Playfair Display Bold Italic), lowercase, including words like *not* (*not comfortable* is one serif phrase). *(older copy)* **Series intro (2026-11-03):** he asked for an upright option, compared both, and **shipped the Bold Italic** in his final (Try_6). Default stays Bold Italic; offer upright only as an alternative. Bold sans impact words are only OK inside full-screen graphic scenes, for contrast.
- When the impact phrase stands alone (e.g. *first principle thinking*): the serif phrase is the hero and the trailing word ("thinking,") goes **above, on the right**, small.
- **Support text is bigger and tight to the hero.** Use about 36 % of hero size (48 px with a 132 px hero), not 25–30 %.
  - Line above: baseline at `hero_y − 0.80 × hero_size − 8`, inset about 7 % of hero width from the hero's **left** edge.
  - Line below: inset about 7 % from the hero's **right** edge, about 58 px under the baseline, or 74 px if the hero ends in a descender (g, j, p, q, y, comma).
- **Split-screen sources:** put captions on the **seam band** (y ≈ 680–1240) over a vertical gradient scrim (transparent → 70 % black → transparent). It's the only band that covers neither face.
- Cap the hero width at **740 px** so italic overhang stays inside the safe zone. Shrink long support lines to fit.

## 4. Instagram Reels safe zone (Rishi's template)

```
x 120 – 960   (840 px wide)
y 250 – 1600
+ keep clear: the icon column x > 845 for y > 1130 (like / comment / share)
```
- Every text, shape and dot must sit inside this, **after** the scene's camera push-in. A 105 % group scale pushes edges outward from the centre, so check at max scale.
- The build script audits every element and prints violations (`check_safe()` in `03. Projects/Minimal Edit/first-principles-kashish/.tesseract-work/build.py`). Reuse it.
- Make an overlay check sheet (template shaded red over ~14 frames) before calling a draft done.
- Also watch out for: wide block stacks and graph end-points drifting into the icon column, long labels touching x = 120, and quote marks hanging outside the margins.

## 5. Graphic-scene details he corrected

- **Quote marks bracket the text.** The opening mark hugs the first line top-left, and the closing mark comes after the last line, bottom-right. Keep the block slightly above centre. Floating marks read as separate elements.
- **Sequential builds never pause.** Stacked elements (blocks, bars) overlap: each rises over about 900 ms with ease-in-out, and the next starts about 520 ms later. A visible gap between pieces reads as a stutter.
- **Highlight box grows from nothing.** scaleX 0 → 100 over about 480 ms with ease-in-out, starting about 120 ms before the word. Its text then arrives word by word. With a fast ease-out, a 220 ms grow looked like it "started midway".
- **A-roll always has a very slow push-in:** about +1.2 % scale per second, linear, on every A-roll shot (punch-in zoom cuts stack on top).
- **Texture:** engine grain at `amount 0.25` was invisible. Use 0.8 on light grounds and 1.0 on dark, size 1.6, plus a vignette.
- Give short A-roll beats at least 0.5 s of readable impact text. Avoid micro-shots under 0.5 s.

---

## 6. Sound design (his notes, now core)

**Principle: lots of sound, each one quiet.** Every text entry gets a sound. The denser a layer, the lower its level, so the whole thing has "essence and depth" without feeling busy. v1 (27 sparse procedural cues) was too thin; v2 (103 cues, mostly from his library) was the direction.

| Event | Sound (from `sfx/`) | Peak in mix (voice peaks ≈ −4 dBFS) |
|---|---|---|
| Impact word reveal | **Hi-Tech Click** (trim to 450 ms) | −17 dBFS |
| Every support word | **flick**, ±2 dB variation, skipped within 110 ms of a bigger cue | −27 to −29 |
| A line drawing / extending (incl. each extension) | **Highlighter** | −19 to −21 |
| Highlight box opening | **Highlighter** | −18 |
| Line reaching its destination | **Riser + Tick** (land the tick on arrival) | −19 |
| Graphic → graphic transition | **Swoosh** | −16 |
| Cut into a graphic scene | **Woosh** or a low impact | −17 |
| Blocks settling | **Pop different** | −19 |
| Small dots / markers | **Modern technology pop** | −21 / −22 |
| Quote marks appear | **Mouse click different** | −22 |
| Grid / UI switching on | **multi flicker** | −23 |
| Value dropping | downlifter (procedural, 1.4 s) | −20 |

- **The first 5 s get +3 dB on every effect**, easing back to normal by 6 s, for a livelier hook.
- Set levels as **target peaks in the mix**, not flat gains. The library files are hot (~0 dBFS) and the procedural ones sit at −12.
- **Align each sound's peak, not its file start**, to the visual event (measure each file's peak time). Convert MP3s to WAV before import.
- *(older copy)* **Measure each library file's peak inside the trimmed window, in the mix.** In the series-intro edit (2026-11-03), the Hi-Tech Click `peak_db` (−9.6) carried over from the first edit was ~8 dB off for the 450 ms trim, so clicks played at about −23 instead of −15. Calibrate from an effects-only render.
- **Voice chain that worked** (clean Riverside audio): 75 Hz high-pass → 2.5:1 compression at −24 dBFS → makeup gain → limiter at −1.5 dBFS. No noise reduction needed (noise floor in pauses −59 dB).
- **Measure the final mix, not the voice stem.** Trimming pauses made the program 3 dB louder than the stem measured. Target −15 LUFS and true peak ≤ −1 dBTP (we hit −15.2 / −3.5).
- **Verify:** render an effects-only copy and check each cue sounds within ±60 ms of the cue sheet. Cross-correlate the voice against the source for lip sync (we got ±5 ms). Drop any cue past the video's end.
- Always deliver `sound_cue_sheet.md` (time · sound · level · reason).
- Claude can't listen in this environment, so always say levels are set by measurement and ask Rishi to check on a phone.

---

## 7. Workflow that worked

1. **Transcript:** `mlx-whisper` (cached `mlx-community/whisper-turbo`) with word timestamps, then snap word edges to `silencedetect` (−35 dB, 120 ms) boundaries. Save ms JSON + SRT + table, and flag words with confidence < 0.7.
2. **Plan, then stop** (beat table, recommended option per beat). Wait for approval.
3. **Build as one regenerable script** (`build.py`): footage JSON (stage 1) + native graphics action batch (stage 2) + sound layers. Always rebuild from a clean base `.tsrct` (fonts + footage + audio already imported). Archive every draft in `Versions/` and keep a revision table in `NOTES.md`.
4. **Pause trims:** cut silences > 200 ms down to ~120 ms (60 ms padding each side). Hide each jump under a graphic or a punch-in, and skip trims that would cause a visible jump mid-A-roll.
5. **Review:** portrait filmstrips (`--tile-width 270 --tile-height 480`), black-frame detection, safe-zone overlay, then the sound checks above.
6. **Gates:** plan → visuals (revise until approved) → sound → QC.

---

## 8. Tesseract gotchas (CLI 0.4.0) — each one cost a rebuild

| Gotcha | Do this |
|---|---|
| Children created with `insertIndex: append` end up **below** the scene's background rect, so shapes vanished (text oddly still showed) | Create the background first, then every child with `{"type":"prepend"}` |
| Keyframe `layerTime` is **relative to the owning layer's activeRange start** (child-local), not the parent clock | Start each element's layer at its reveal time and key from 0 |
| Video-layer keyframes run on the **source clock** (inputOffsetMs included) | Key a Video's scale at `s0 … s1` source ms |
| Point text **wraps** once wider than about 900 px ("FIRST PRINCIPLE" broke onto two lines) | Cap the width (≤ 740–840 px). Use anchor x = 0 |
| `positionY` keys alone are rejected ("paired spatial position path") | Use `setFxPositionKeyframes` with both X and Y tracks |
| Two keys at the same time on one track (different ids) are rejected | One key per time per property |
| Negative activeRange duration breaks the batch | Skip glyphs/words whose start falls past their parent's end |
| Glow effect fields are `glowRadius / glowIntensity / glowThreshold` | Check the schema for effect field names |
| Preview PNGs have **alpha**; sampling RGB alone misreads opacity | Read the alpha channel |
| There's no action to create Audio layers | Add Audio layers via editable JSON + `project commit`. A Video layer with `volume` omitted is silent, so the voice never doubles |
| Fonts aren't discovered from the system | Download from `github.com/google/fonts` (OFL) and `import-font`. Styles: `Inter / ExtraBold`, `Playfair Display / Bold Italic` |
| Video `cornerRadius` is a **fraction of the half-side**, not px (6 or 60 → pill) | Use ~0.12 for card corners. White border = `stroke` effect (inside, 6 px) + `dropShadow` effect on the Video layer |
| A child layer's activeRange longer than its group's remaining window is rejected ("start_time must fit") | Child duration = group end − group start |
| Per-glyph and per-word layers are fine at this scale | ~1,300 actions, export ≈ 6 s for 33 s at 1080×1920 |

---

## 9. My mistakes this session (don't repeat)

1. Shipped draft 1 with whole-line text pops. Default to word-by-word support and char-by-char impact text from the first draft.
2. Used sans impact words on A-roll. Serif is the default for caption heroes.
3. Support text was too small and floated away from the hero. Start at 48 px, tight.
4. Ignored the platform safe zone until Rishi raised it. Audit from draft 1.
5. Quote marks were placed as separate elements, not bracketing the text.
6. Blocks popped on separate words with dead time between. Overlap builds.
7. Highlight box grow was too fast to read as "from zero".
8. Sound was sparse and quiet, and ignored the supplied SFX folder. Check `sfx/` first and give every text entry a quiet cue.
9. Stated a transcript word ("they") as fact without listening. Flag it as uncertain instead.
10. Measured loudness on the voice stem instead of the trimmed program.

---

## 10. Series intro (30 Days of Consulting Prep), learnings from Rishi's final (2026-11-03) *(older copy)*
Project: `03. Projects/Minimal Edit/series-intro-versions/`. His final (Premiere `Intro Try_6.mp4`) = our caption + sound export + his own overlays.
- **Captions and sound shipped unchanged.** The Minimal Editorial caption set (§2–3) plus the dense-quiet cue map (§6) is the approved package for talking-head intros.
- **Graphics go behind the subject.** He wants panels (the 30-day grid) occluded by his body. On close or standing framings, the card stack also has to go behind him so it never covers the face.
- Tesseract `personMatte` gave an empty matte here. Make a local MediaPipe matte video (selfie_multiclass), import it as footage, mirror the A-roll's transform keys, and use it as a `lumaInverted` track matte. A layer consumed as a matte doesn't render on its own.
- **Intros keep the take continuous.** No pause trims; ~0.4 s lead before the first word.
- **His overlay geometry wins over the safe-zone template** for graphics he places himself (cards at top 170 px, grid at x 38). Captions still obey §4.
- **Watch the shirt print.** Graphic tees put text exactly where captions sit; move the caption block below it per framing (standing shots: hero y ≈ 1480–1510).
- Build one script per series with a per-version table (span, caption grammar by transcript index, hero y). Then all versions rebuild consistently from one approved recipe.

