---
name: minimal-editorial-edit
description: Plan and build premium minimal talking-head reel edits (Arthur Brooks style) in the Minimal Editorial design system: transcript, scene plan for approval, Tesseract or Motion build, revisions, sound, QC.
---

# Minimal Editorial — talking-head edit (v1.2)

Turns a talking-head clip into a premium minimal 9:16 reel: cinematic captions plus paintings, B-roll, lines, illustrations, quotes, callouts and graphs, each chosen by what that line does. Calm authority: negative space, one accent, texture everywhere, every visual shows the spoken line.

**This is the only mandatory read**; it holds every current rule (proof: `history/RULE_AUDIT.md`). Open `reference/` docs only on the triggers at the end.

- Design System artifact "Minimal Editorial": https://claude.ai/artifact/NDguL5ottfkuCUcQQKzCoP (`project/README.md`, `tokens.json`, `components/bundle.css`); this file wins on conflict.
- Fixed: caption logic, texture, 10 scene types + A-roll, announce → face / explain → show, one accent. May vary: accent hue, serif partner.
- Projects `03. Projects/Minimal Edit/<edit>/`; exports `04. Exports/Minimal Edit/`; `sfx/` is shared by other styles (never move/rename). Layout, gotchas, brand: `02. Shared Core/`.

## Model gate
Check `MODEL_MODE` in the studio root CLAUDE.md, or what Rishi said this session. If it is `opus-only`, skip this section. Otherwise, steps marked [OPUS] (creative planning, storyboard or options, first look-dev of a new scene type, judging QC failures that need taste) need a check: if you are not running on Opus, stop and ask "Next step is creative (<step>). Switch to Opus with /model opus, or continue on Sonnet?" Steps marked [SONNET] (transcribe, cut, captions, building from an approved plan, applying a listed revision, renders, cleanup) run on whatever model is active; if that is Opus, mention once that Sonnet would be cheaper for this stretch.

## Workflow (gates never skipped)
0. **Ask up front** [SONNET]: style (default this pack); split-screen/multi-cam framing; safe zone (default Instagram Reels); SFX library (default `sfx/`); licensed music (none → no bed); speaker name, words to verify. If Rishi says go straight to a draft, use defaults and list them in NOTES.md.
1. **Transcribe + cut** [SONNET]: mlx-whisper turbo word timestamps, edges snapped to silencedetect (−35 dB, 120 ms); save ms JSON + SRT + table; flag confidence < 0.7 as uncertain, never as fact. Cut silences > 200 ms to ~120 ms (60 ms padding each side; raise if attacks clip); hide jumps under a graphic or punch-in; skip trims that jump mid-A-roll. Remove false starts and orphan words ("But"); keep pauses before punchlines. **Series intros: no pause trims, continuous take, ~0.4 s lead before the first word.**
2. **Plan, then STOP** [OPUS]: plan page, one row per beat: time, exact script, core idea (≤ 3 words), function (hook, announce, explain, example, number, quote, emotion, close…), options A/B/C (scene type, visual, motion IDs, assets), "why this", notes box; recommend one. **Never animate before Rishi approves.**
3. **Assets** [SONNET]: source + licence each (Wikimedia public-domain paintings, Pexels, Rishi's photos). Ask for gaps; never substitute an unrelated visual.
4. **Build draft 1** [SONNET] (new scene type look-dev [OPUS]): captions first, then scenes in order; one function per scene type; texture inside the camera group; every rule below from draft 1; audit every build. Call it a draft.
5. **Revise** [SONNET] (taste calls [OPUS]): numbered table (timestamp · problem · expected · fix · status) in NOTES.md; fix all in one pass; archive draft in `Versions/`; re-render; ask "ready for sound design, or more revisions?" **No sound before visual approval.**
6. **Sound** [SONNET]: rules below; deliver `sound_cue_sheet.md`.
7. **QC + export** [SONNET] to `04. Exports/Minimal Edit/`.
8. **Close-out** [SONNET]: after Rishi approves the final export, run `"<studio root>/06. Tools/finalize_reel.sh" "<project folder>"` (deletes only regenerable intermediates after confirming the export exists). Then run the Learning loop.

## Scene selection
Announce/hook/emotion/joke/close → A-roll. Number/trend → Graph. Story/historic/romantic → Painting (specific person → character callout). Felt action → B-roll. One concept → Center illustration. Two things → Side illustration. Real artefact → Object/photo callout. Stages → Line + illustration zigzag. Consequence → line to subject. Chain of abstract terms → Line + text. Quote/thesis → Text-centric. Can't say why a visual beats A-roll → A-roll. Average shot 1.5–3 s; first visual by ~2 s; 40–55 % A-roll; A-roll ≤ 4 s without a framing change; graphics runs ≤ ~8 s; alternate light/dark/blue grounds; one idea per scene; hard cuts to/from A-roll, whips only graphic → graphic; camera follows line heads.

## Look
- 1080×1920, 30 fps. Accent `#0B52F9` (glow `#1A83FB`); paper `#FCFAFB`→`#F2F2F2`; ink `#0D0D0D`, never pure black; graph `#121212`–`#1A1A1A` + noise. White text on footage/dark; on paper `#111111` sans + blue serif. A-roll keeps its grade, bottom darkened.
- Texture on every graphic, moving with its layer; no flat vectors. Tesseract grain 0.8 light / 1.0 dark, size 1.6, vignette 0.18 light / 0.35 dark. B-roll: paper texture, darkened + blurred edges. Paint texture half strength.
- Inter (hero 700–800, support 500) + Playfair Display Bold Italic. Hero 90–130 px (132 proven).

## Captions
- ≤ 5 words per group, one hero (the meaning word), captions on screen throughout (also over graphics); groups hard-cut.
- **A-roll hero always Playfair Display Bold Italic, lowercase**, even *not*. Upright only as an offered alternative. Bold sans heroes only in full-screen graphic scenes.
- **Support 48 px (≈ 36 % of hero), tight:** line above baseline at `hero_y − 0.80 × hero_size − 8`, inset ~7 % of hero width from its left; line below inset ~7 % from its right, ~58 px under the baseline (74 px if the hero ends in g/j/p/q/y/comma). Lone trailing word goes above-right, small.
- Hero centred, y 55–70 %, ≤ 740 px wide; shrink long support lines to fit rather than wrapping past the safe zone. Split-screen: seam band y ≈ 680–1240 over a scrim (transparent → 70 % black → transparent). Graphic-print shirt: block below the print (standing: hero y ≈ 1480–1510).
- Hinglish (Roman only): hero may be Hindi; helper verbs small; never split compound verbs; digits for numbers.

## Safe zone (Instagram Reels)
Everything inside x 120–960, y 250–1600, icon column clear (x > 845 for y > 1130), checked at max push-in scale; graphs inside x 160–840. Audit every build (`check_safe()`) and review a red overlay sheet (~14 frames). Graphics Rishi places himself keep his geometry; captions still obey.

## Motion (driven by word timings; never invented)
- **Support, word by word (M01):** on its spoken time, rise 22 px → 0 over 420 ms, opacity over 380 ms, `cubic-bezier(0.22,1,0.36,1)`. Never a whole line at once, in graphics too.
- **Hero, char by char left → right (M02):** slide 28 px over 380 ms, blur 10 → 0 over 300 ms, opacity 240 ms; stagger = spoken length ÷ glyphs, 12–48 ms. Done ≥ 350 ms before the cut, else move the cut later.
- **A-roll push (M06):** +1.2 %/s linear, every shot; zoom cuts (115–140 %) on top.
- **Builds overlap (M28):** each piece ~900 ms ease-in-out, next every ~520 ms.
- **Highlight box (M25):** scaleX 0 → 100 over ~480 ms ease-in-out, from ~120 ms before the word; text then word by word.
- **Quote marks** first, bracketing the block: open top-left of first line, close bottom-right after last; block slightly above centre.
- Holds: graphs ≥ 0.5 s complete, complex illustrations ≥ 2 s. No shot < 0.5 s; short A-roll beats ≥ 0.5 s readable hero. No linear easing except path speed and M06. Visuals land on trigger words.
- Text never covers faces. Panels and card stacks go behind the subject by default on close and standing framings, never over the face (series-intro verdict; Rishi can ask otherwise): person matte, `reference/TESSERACT_BUILD.md`.

## Sound (dense but quiet; voice peaks ≈ −4 dBFS)
A quiet cue on every text entry, `sfx/` first. Mix peaks (dBFS): impact word **Hi-Tech Click** (450 ms trim, peak on first glyph) −17 · every support word **flick** −27 to −29, ±2 dB, skipped within 110 ms of a bigger cue · line draw and each extension **Highlighter** −19 to −21 · highlight box **Highlighter** −18 · line arrives **Riser + Tick** −19 · graphic → graphic **Swoosh** −16 · cut into graphic **Woosh**/low impact −17 · blocks settle **Pop different** −19 · dots **Modern technology pop** −21/−22 · quote marks **Mouse click different** −22 · grid/UI **multi flicker** −23 · value drop procedural downlifter 1.4 s −20.
- First 5 s +3 dB, back to normal by 6 s. No two cues within ~110 ms.
- Target peaks per cue, not flat gain. **Align each file's peak, not its start**; measure it inside the trimmed window (a reused click peak was ~8 dB off). MP3 → 48 kHz WAV.
- Voice: 75 Hz HPF → 2.5:1 at −24 dBFS (15/180 ms) → makeup → limiter −1.5 dBFS; no NR if pauses < about −55 dB. Music (supplied only): start 18–24 dB under voice, ducked 3–6 dB; if it's inaudible on Rishi's phone, raise it (Consulting settled at 13 dB under, R1.16).
- Measure the **final program** (trims add ~3 dB): −15 LUFS (−16 to −14), true peak ≤ −1 dBTP.
- Verify: effects-only render (cues within ±60 ms; none past the end); voice cross-correlated ≤ 10 ms. Cue sheet: time, sound, peak, reason. You can't listen: say so; Rishi checks on a phone.

## QC + export
H.264 MP4, 1080×1920, 30 fps, AAC 48 kHz, loudness measured on the MP4. Check: captions match audio word for word; rules above; safe-zone audit + overlay; black-frame detection; portrait filmstrip (`--tile-width 270 --tile-height 480`); no micro-clips (< 0.3 s) or stray words; assets licensed; phone watch with sound and muted. Full list: `reference/QUALITY_CONTROL.md`.

## Build
Tesseract (proven) or Claude Motion. Tesseract: one regenerable `build.py` (footage JSON → graphics batch → sound layers) from a clean base `.tsrct` with fonts, footage, audio imported; series get one script with a per-version table. Template: `03. Projects/Minimal Edit/first-principles-kashish/.tesseract-work/build.py`.

## Read only when…
| Trigger | Open (in `reference/`) |
|---|---|
| Before writing/changing a Tesseract `build.py`; engine errors | `TESSERACT_BUILD.md` |
| Designing a scene type's internals | `TEN_SCENE_PRINCIPLES.md` |
| Other motion IDs; Motion/Remotion builds | `MOTION_LIBRARY.md` |
| Unsure which scene fits a beat | `EDITING_PSYCHOLOGY.md` |
| Full colour tokens, textures, components; updating the artifact | `DESIGN_SYSTEM.md` |
| Plan-page template; training a new style | `PRODUCTION_WORKFLOW.md` |
| A cue not listed above | `SOUND_DESIGN.md` |
| Final QC pass | `QUALITY_CONTROL.md` |
| Choosing reference stills | `VISUAL_REFERENCE_LIBRARY.md` |

## Learning loop
During a reel, append Rishi's raw notes to `FEEDBACK_LOG.md` (date, reel, note). When the reel is approved, fold the durable rules into this SKILL.md or the right reference/ doc, delete any rule they reverse, add a line to `history/CHANGELOG.md`, and mark the log entries as folded. Keep SKILL.md under about 1,500 words; move detail to reference/ instead of growing it.

New reference style from Rishi: follow "Evolving the system" in `reference/PRODUCTION_WORKFLOW.md`.
