# Tesseract build — pipeline and engine gotchas (v1.2)

Read this **before writing or changing a `build.py`** for a Minimal Editorial edit in Tesseract. Compiled (wording kept, paths updated) from `../history/LESSONS_LEARNED.md` §4–5, §7–8 and §10 (series intro, from the older copy), plus the R017 project NOTES. The house rules (look, motion, sound levels) are in `../SKILL.md`. Cross-style engine quirks also belong in `02. Shared Core/GOTCHAS.md`.

Reference implementations:
- `03. Projects/Minimal Edit/first-principles-kashish/.tesseract-work/build.py` (single reel; `check_safe()` safe-zone audit at line ~174).
- `03. Projects/Minimal Edit/series-intro-versions/.tesseract-work/build.py` (one script per series with a per-version table).

## Pipeline that worked (LESSONS §7)
1. **Transcript:** `mlx-whisper` (cached `mlx-community/whisper-turbo`) with word timestamps, then snap word edges to `silencedetect` (−35 dB, 120 ms) boundaries. Save ms JSON + SRT + table, and flag words with confidence < 0.7. (R017: neither the episode SRT nor whisper.cpp timings were reliable; onsets were placed on measured speech segments.)
2. **Plan, then stop** (beat table, recommended option per beat). Wait for approval.
3. **Build as one regenerable script** (`build.py`): footage JSON (stage 1) + native graphics action batch (stage 2) + sound layers. Always rebuild from a clean base `.tsrct` (fonts + footage + audio already imported). Archive every draft in `Versions/` and keep a revision table in `NOTES.md`.
4. **Pause trims:** cut silences > 200 ms down to ~120 ms (60 ms padding each side). Hide each jump under a graphic or a punch-in, and skip trims that would cause a visible jump mid-A-roll. (Series intros: no pause trims, see `../SKILL.md`.)
5. **Review:** portrait filmstrips (`--tile-width 270 --tile-height 480`), black-frame detection, safe-zone overlay (template shaded red over ~14 frames), then the sound checks.
6. **Gates:** plan → visuals (revise until approved) → sound → QC.
7. **Series:** build one script per series with a per-version table (span, caption grammar by transcript index, hero y). Then all versions rebuild consistently from one approved recipe `[R1.2]`.

## Engine gotchas (CLI 0.4.0) — each one cost a rebuild (LESSONS §8)

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
| Grain `amount 0.25` is invisible | 0.8 light / 1.0 dark, size 1.6, plus a vignette (0.18 light / 0.35 dark) |
| A 105 % group scale (camera push-in) pushes edges outward from the centre | Audit the safe zone at max scale |

## Graphics behind the subject (LESSONS §10, series intro) `[R1.2]`
- Tesseract `personMatte` gave an empty matte here. Make a local MediaPipe matte video (selfie_multiclass), import it as footage, mirror the A-roll's transform keys, and use it as a `lumaInverted` track matte. A layer consumed as a matte doesn't render on its own.
- Shared matte tool: `02. Shared Core/engine/matte/matte.py`.

## Sound layers
- Convert library MP3s to 48 kHz WAV before import; measure each file's peak time and level **inside the trimmed window** (a stored `sfx_peaks.json` from another edit can be ~8 dB off).
- Procedural accents (e.g. the 1.4 s downlifter) come from `tesseract_sound.py` in the tesseract-video skill's scripts.
- Voice is placed as Audio layers that mirror every footage cut; the footage's own audio is off.
