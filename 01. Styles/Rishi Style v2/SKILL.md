---
name: rishi-v2
description: "Edit Rishi's 9:16 Hinglish talking-head reels in the Rishi v2 style: smooth premium-minimal graphics around the face (chat cards, split pane, behind-the-head cards, PiP, comments sheet), serif-hero romanised captions, dense-quiet sound. Process: SRT intake → HTML options board → HTML storyboard → Tesseract build → numbered feedback → sound → QC."
---

# Rishi v2: talking-head edit skill (v2.2)

GradNext reels: Rishi to camera (lav mic, marble wall, green jacket), ≈30–35 s, Hinglish, AI/Claude topics, comment-keyword CTA. **Only mandatory read**; open reference/ docs only when the table says so. Studio rules: `02. Shared Core/STUDIO.md`, `GOTCHAS.md`, `BRAND.md`. Rishi's notes on this video beat this file, which beats reference/.

## Model gate
Check `MODEL_MODE` in the studio root CLAUDE.md, or what Rishi said this session. If it is `opus-only`, skip this section. Otherwise, steps marked [OPUS] (creative planning, storyboard or options, first look-dev of a new scene type, judging QC failures that need taste) need a check: if you are not running on Opus, stop and ask "Next step is creative (<step>). Switch to Opus with /model opus, or continue on Sonnet?" Steps marked [SONNET] (transcribe, cut, captions, building from an approved plan, applying a listed revision, renders, cleanup) run on whatever model is active; if that is Opus, mention once that Sonnet would be cheaper for this stretch.

## Workflow
`<studio>` holds `.studio-root`; paths below are pack-relative; each reel gets `<studio>/03. Projects/Rishi Style v2/<Video N>/`.
0. **Intake [SONNET].** Raw or rough cut, plus the original's SRT (Hindi, mixed English). Ask only for what's missing: CTA keyword, brands (real logos into `assets/logos/<brand>/`), photos, accent. No SRT: ask before choosing a transcription route. Raw: cut dead silence and unclear sound yourself (silencedetect, cut on a quiet frame); keep pauses carrying a joke or beat, and say which. `srt_remap` (note chunks across cuts); the SRT is a draft, so flag meaning-changing mishearings ("slow" was "slop"). `roman_map.json` → `roman_captions`; flag inferred words near cuts. `face_track`; matte if behind-head is likely.
1. **Options board [OPUS], then STOP.** `templates/options_board.html` → `<Video N>/storyboard/<name>_v1/index.html`. Per frame type (hook, reaction, list, thesis, proof, contrast, explanation, iteration, CTA; captions if open): ≥5 phone-frame options on real stills, **plus every option he liked before, Keeps first, even past 5**; Keep/Maybe/No, notes, one "my pick"; motion as looping tiles. Wait for his "Copy my picks". He mixes ("B plus bits of A and C"): build exactly the mix, restated as an F-list.
2. **Storyboard [OPUS].** `templates/storyboard.html` → `storyboard/<name>_vN/`: per beat before still, drawn after frame, timings, F-tags; assumptions box on top (incl. accent). Unclear motion: ≥5 interpretations as 5-frame strips (0/0.15/0.30/0.50/0.72 s). Label mock-ups as sketches where the build differs. Silence means approved; "storyboard only" means stop.
3. **Build [SONNET]** (first look-dev of a new scene type: [OPUS]). New `<Video N>/<name>_edit_vN/` via `mkdir` (no `-p`); never touch earlier drafts. Captions, then scenes in order, A-roll motion, sound. Filmstrip (270×480) each changed beat; fix; re-check glyphs, gaps, bars.
4. **Feedback.** Notes become a numbered F-list with timestamps [SONNET]; non-trivial changes go to the storyboard first [OPUS]; next draft in a new folder [SONNET]. Small bugs found while building: fix and mention.
5. **Sound [SONNET]** with the visuals; effects-only check every draft.
6. **QC + delivery [SONNET]** (taste calls: [OPUS]). Draft folder: `<name>_draftN.mp4`, `.tsrct`, `Previews/Filmstrip-draftN.jpg`, `sound_cue_sheet.md`; SFX-only and voice-only MP3s on request. Report changes, checks, what wasn't checked (Claude can't listen), open items, timestamps.
7. **Close-out [SONNET].** After Rishi approves the final export, run `"<studio root>/06. Tools/finalize_reel.sh" "<project folder>"` (deletes only regenerable intermediates after confirming the export exists). Then the learning loop.

## Working rules
- Precedence: Rishi's notes on this video > his past verdicts (this file) > pack tokens (reference/) > source books when drawing options: Minimal Edit → Rishi v1.3 → Daniel Presley → Paper Stage (the last three are in `09. Archive/Unused Styles/`).
- Never a Claude artifact or Remotion. Reviews are local HTML plus a PNG (headless Chromium); `node --check` page scripts. Chat: paths, what to look at, what to decide.
- Don't stall: assumptions go in the storyboard. Timebox side quests to 2–3 min. Installs, flags, infrastructure: feasibility report, approval, then that phase only.
- "Smooth" is the goal; "snappy" and "pop" are defects; "decent" means okay; "a little" ≈ 30 px, not 120. Mishearings: Enter/Inter, sea/C, deep/D, ice + green/ice + grain, wallpaper/warm paper.
- He spots every glitch (half glyphs, bars, gaps, uneven padding). Name accidental textures he likes.

## Look
- Face is the spine: hook, verdict, payoff and CTA on the face; graphics around it or carrying it. One idea per screen, ≤2 moving focal points. Real logos, filenames, past drafts, his clip; his face sticker (`assets/people/rishi/`) as every avatar.
- Colours: ice `#EAF0F8`, ink `#0B1224`, text `#0B1730`, muted `#4A5878`/`#9AA8C7`, dark card `#121C38`, green `#2FD08A` only for "sent ✓", Claude `#D97757` only via its logo. White cards `#FFFFFF → #E4E6EA` plus vignette, never blue-tinted.
- Accent: Rishi names one per video; default `accent.duo` (`#3E7BFA` UI, `#FFD68A` emphasis). Ground per video (mesh is his favourite); coarse grain behind cards; never a blurred own frame.
- Inter for UI, support and all digits; Playfair Display Bold Italic for heroes, never digits. Draw ✓ ↑ ● as shapes.
- Tile corners ≈8 px, cards 14–36 px. Organic shapes, never circles. Labels above lines and dots. Graphics over A-roll sit low, blurring only the bottom half; face sharp. Split pane: full hair line just below it, no black bar.

- **IG safe zone** (captions, key text): x 120–960, y 250–1600; keep the right icon column clear below y 1130; hero ≤ 740 px wide. Audit at the maximum scale of any push-in.

## Captions
- Romanised Hinglish exactly as spoken ("aisa kuch nahi hota hai"): no Devanagari, translation or grammar fixes; English lowercase; punctuation marks pauses; never split compound verbs ("samjha paoge").
- ≤5 words per group, ≤ ~22 characters per line, centred; hero is the meaning word.
- A-roll: hero Playfair Bold Italic lowercase 132 px white, baseline y 1420, ≤740 px wide; support Inter Medium 48 px, white 85 %, lower line at hero baseline + 0.55 × support size; bottom gradient 0 → 45 % black over the bottom 40 %; never a blue hero. Support rises word by word; hero builds letter by letter, done ≥0.35 s before the group ends; groups leave softly (C-out).
- Modes: light ground (ink, top of the white area); split (pane top, hero 100 px); PiP (one Playfair line between card and PiP); wall (one black word in the tile below the face); CTA (one white word above "Comments"). Highlighter underline for one verdict word per section.
- Never white on white, blue on light, or over a card. Repeated phrase with one new word: keep the support, swap the hero. Mode boundaries slightly before word starts. Match roman_map keys by NFD.

## Motion
- Eases: E1 (0.22,1,0.36,1) entrances, ES (0.45,0.05,0.2,1) big moves, EX (0.55,0,0.75,0.4) exits. Linear only for drifts; no overshoot.
- Every card R01 line → rectangle: scaleY 3 → 100 %, rise 40 px, blur 18 → 0, ≈0.65 s ES, shadow grows. Exit R02: slide, blur, fade, 0.42–0.6 s; the next element enters from the side the old one left toward.
- Big moves 0.8–1.45 s with motion blur peaking mid-move; entrances 0.5–0.7 s; word rise 26 px, stagger 0.20 → 0.08 s. Outros are calm moves (parallax), not the intro reversed.
- First graphic by ~0.7 s; graphics ≈45–55 % of runtime, ≤ ~8 s bare A-roll. Cut on the trigger word; return to the face after the line ends; no blank white beat > ~1 s; hide jump cuts in a zoom; hold end states ≥0.5 s; A-roll push +1.2 %/s.

## Scenes
Beat-to-scene defaults (S1–S9) live in reference/EDITING_PSYCHOLOGY and SCENE_LIBRARY. Hook result card: his own clip graded warmer with a serif word (confirm per video). Reaction beats carry no words. CTA: sheet and keyboard held to the last frame, keyword typed in CAPITALS, then a DM notification ("rishi sent you a file") slides left → right mid-screen above the caption. Lists swap inside the PiP card once a PiP is up. Also approved: reel-timer ring.
Rejected unless asked: Paper Stage look, pops, snappy sheets, sudden orbit words, strike-then-replace, chapter marker, window zoom-through, generic AI mock-ups (except as "slop").

## Depth and matte
1–3 behind-head moments per reel, never a visible gap. New matte per cut: `"<studio>/06. Tools/venv-style/bin/python" -I "<studio>/02. Shared Core/engine/matte/matte.py" cut.mp4 matte.mp4` (match size/fps); check polarity on one frame. The matte mirrors the A-roll transform JS; graphics use `trackMatte lumaInverted`; switch to a non-matted copy before the face moves. Words behind only if readable; fan, deck and giant-word values in DEPTH_AND_MATTE §5.

## Sound
Dense but quiet (`assets/sfx/`, ≈170 cues per 33 s): hero `hitech` −17 dBFS; support `flick` −27…−30; swooshes full length, 0.25 s fade-in, peak at the move's midpoint, −17…−21; pops −20…−24; ticks −19…−20. First 5 s +3 dB. Voice (pre-mastered): 75 Hz HPF, −1.5 dB, own Audio layer; A-roll video silent. Final ≈ −15.5 LUFS (−16…−14), true peak ≤ −1 dBTP, measured on the MP4. No music without a licensed track.

## QC (every delivery)
Safe-zone audit at the maximum scale of any push-in; new draft folder; F-items done; caption rules and whole glyphs; every card R01, nothing snappy; split, behind-head and PiP clean; `fx_check.py` 100 % cues within ±60 ms; loudness on the MP4; ffprobe 1080×1920, 30 fps, duration matches the cut; `blackdetect` 0; filmstrip in `Previews/`. Every export, check renders too, is 1080p: never `--resolution 720p`.

## Engine
Python: `<studio>/06. Tools/venv-style/bin/python`. Tools: `srt_remap`, `roman_captions`, `face_track`, `fx_check` (`--mp3` for the MP3s). Copy `build_template.py` + `lib.py` (draft 4) into `.tesseract-work/`; edit CONFIG and scenes. It predates v2.1: add soft caption exits, the tight lower support line and R01+/R02+/R03+ yourself.
Tesseract musts: rebuild from clean `base.tsrct`; `mapping.input.start` equals `inputRange.start`; animate a Group around a Video; every blur `layerSize: [1080, 1920]`; one `setFxPropertyKeyframes` call per property; `t-(-0.05)`, never `t--0.05`; unique mask ids. If Rishi edits in a GUI, edit his `.tsrct` in place.

## Read only when…
All in reference/ unless noted.

| Trigger | Open |
|---|---|
| Options board, storyboard | REVIEW_FORMATS, SCENE_LIBRARY, MOTION_LIBRARY, DESIGN_SYSTEM, EDITING_PSYCHOLOGY (+ CAPTION_SYSTEM if captions are open) |
| Building a scene; a note names a motion | MOTION_LIBRARY, SCENE_LIBRARY, DESIGN_SYSTEM |
| Building captions | CAPTION_SYSTEM |
| Behind-the-head graphic | DEPTH_AND_MATTE |
| Running intake tools or a build; a layer misrenders | engine/README.md (commands), TESSERACT_NOTES |
| Sound pass | SOUND_DESIGN |
| Delivery | QUALITY_CONTROL |
| Reference frames | VISUAL_REFERENCE_LIBRARY |
| Stage detail | PRODUCTION_WORKFLOW |
| Why a rule exists | history/ |

## Learning loop
During a reel, append Rishi's raw notes to `FEEDBACK_LOG.md` (date, reel, note). When the reel is approved, fold the durable rules into this SKILL.md or the right reference/ doc, delete any rule they reverse, add a line to `history/CHANGELOG.md`, and mark the log entries as folded. Keep SKILL.md under about 1,500 words; move detail to reference/ instead of growing it.
