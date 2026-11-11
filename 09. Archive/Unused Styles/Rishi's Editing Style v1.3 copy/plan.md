# PLAN: Rishi's Editing Style (reverse-engineering 15 reference reels)

Working folder (the ONLY place to write): `Rishi's Editing Style copy/`
Never write to, move, or delete anything in the original `Rishi's Editing Style` folder or anywhere outside this copy.
Read-only use of `../tools/` (python venv `tools/venv-style`, whisper models) is allowed. Install nothing.

## READ THIS FIRST (every new session)
1. Read this whole file, then `PROGRESS.md` (create it if missing) to see what is already done.
2. Check which model you are running as (it is in your system prompt).
3. Do ONLY the phases tagged for your model, in order, and only phases whose earlier phases are ticked below.
4. When you reach a STOP GATE, stop, print the banner given there, and wait. Do not continue into the next model's phases, even if you could.
5. Token budget is tight (Rishi is near the usage limit). One reel at a time, no parallel sub-agents, no re-reading files already written, never `cat` whole CSVs.

## Context
A previous Claude Code session started a measured, frame-by-frame teardown of 15 reference reels (720x1280, 30 fps).
Its scratchpad was copied here:

```
REF="./teardown-workspace/main-session/scratchpad/reel-teardowns"
BIN="./teardown-workspace/main-session/scratchpad/measure-scripts"
PY="/Users/rishi/Documents/Teaching Claude/DIff Acc/tools/venv-style/bin/python" -I
```

Folders were renamed (2026-11-06): `V##` is now `V##_topic-slug` (e.g. `V02_3-editing-mistakes-beginner-to-pro`); the videos live in `reference-reels/` with the same names. The plan still says `V##` as shorthand. No dash-prefixed folder remains, so the `./` prefix is now optional.
`$REF/BRIEF.md` is the spec for each teardown (12-section `BREAKDOWN.md` + `animations.json`, evidence tags
`[MEAS]/[OBS]/[EST]/[INF]`, measure 8-12 animations per reel with `track.py` + `ease_fit.py`).
`$REF/V01/BREAKDOWN.md` and `animations.json` are DONE and are the quality + format benchmark. Do not redo V01.

CURRENT STATUS (updated 2026-11-06 by Sonnet, end of Phase 1):
- ALL Sonnet work is done: Phase 0, Phase 1 (V01-V15 each have `BREAKDOWN.md` + `animations.json`), the optional Opus quality check
  (`$REF/QUALITY_NOTES.md`) and its cheap "now" fixes for V01/V02 (see the last block of `$REF/PROGRESS.md`).
- Phase 2 DONE 2026-11-06 (Opus): `$REF/SYNTHESIS.md` written.
- Phase 3 DONE 2026-11-06 (Opus): Stage 0 answers in `Style Pack/DECISIONS.md` [R1.0]. Key: Family B editing style leads; rishi.docx = light taste only (colours + General Sans; Playfair Italic serif); paper + ink grounds; red + money green; reference UI cards; 46px captions; 9:16; real footage; Remotion; sound later; CTA per reel. Phase 4.1-4.2 DONE 2026-11-06 (Opus): Style Pack/SKILL.md, DESIGN_SYSTEM, SCENE_PRINCIPLES, MOTION_LIBRARY, EDITING_PSYCHOLOGY written. Phase 4.3 DONE 2026-11-06 (Sonnet): README, CHANGELOG, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, PRODUCTION_WORKFLOW, SOUND_DESIGN, LESSONS_LEARNED written. NEXT: Phase 5.1 (Opus/Fable: edit plan for Vid 1.mp4, STOP for Rishi's approval). Open before the first render: fonts General Sans + Playfair Display are not in assets/fonts/; sfx folder empty; auto-editor not found on PATH.
- Helper scripts added in `$BIN`: `fitall.py` (fits every track CSV, prints rmse gate), `mkjson.py` (writes animations.json).
- Per-reel `work/` folders hold CSVs; `work/tr/` holds tracks added in Phase 1 (and `discarded/` ones). Reel folders are `V##_slug`.

### Evidence quality per reel (use this to weight Phase 2; CORE claims must rest on the better-measured reels)
| reel | clean [MEAS] curves | strips viewed | note |
|---|---|---|---|
| V01 | 14 | most | benchmark, 25 json entries |
| V10 | 7 sets (13 fits ≤ .12 rmse) | 0 | best-measured of V02-V15 |
| V14 | 9 (6 pane curves from split.txt + doc morph) | 0 | pane device fully measured |
| V15 | 9 sets (5 bezier-grade) | 0 | highest cut↔onset hit rate (3/10) |
| V04, V12, V13 | 5-6 sets | 0-2 | usable |
| V02 | 10 (some noisy) | 7/25 | strips partly viewed after fixes |
| V03 | 11 | 0 | sheets only |
| V05, V06, V07, V08, V09, V11 | 3-6 sets | 0-2 | tracking on blue/cream grounds was noisy; many entries are [OBS]/[EST] |
All V03-V15 timings read from 2 fps sheets are tagged "~"/[EST]; native-frame strips were NOT viewed for most reels (Q6 unmet).
Hard facts safe to rely on: cut lists + diffs (events.md), audio onset stats (audio.json), hexes tagged [MEAS], measured bezier sets
marked rmse ≤ .05, word→frame trigger offsets (words.json).

### Read order for a new Opus/Fable session (token-light)
1. This file. 2. `$REF/PROGRESS.md` (15 lines: key findings per reel + open items). 3. `$REF/QUALITY_NOTES.md` (evidence rules Q1-Q21).
4. For Phase 2: all 15 `animations.json` (small), then ONLY §1 Overview, §10 Editing psychology, §11 Signature moves, §12 Gaps of each
   BREAKDOWN (use `grep -n "^## 1\.\|^## 10\.\|^## 11\.\|^## 12\."` to slice). Do not read §3 catalogues in full unless resolving a conflict.

---

## PHASE 0: Setup  [SONNET]
- [x] 0.1 Read `$REF/BRIEF.md`, `$REF/V01/BREAKDOWN.md`, `$REF/V01/animations.json`.
- [x] 0.2 Each `$REF/V##/src.mp4` is a symlink into the ORIGINAL folder. Re-point every symlink to the matching file inside this
        copy's `reference-reels/` folder (match by the SaveClip filename the old link names). Verify every
        target exists. Never copy or modify the videos.
- [x] 0.3 Update the `REF=` path inside `BRIEF.md` to the copy's `$REF` path.
- [x] 0.4 Create `$REF/PROGRESS.md` (one line per finished reel: reel, date, #animations, 3 key findings).

## PHASE 1: Reel teardowns V02-V15  [SONNET]
One reel at a time, in order. For each reel: read each strip once (glance at static ones), run `track.py` + `ease_fit.py` on 8-12
animations, write `BREAKDOWN.md` section by section, then `animations.json`, then append a line to `PROGRESS.md`.
Format and depth must match V01.

- [x] V02  - [x] V03   (batch A)
- [x] V04  - [x] V05   (batch B)
- [x] V06  - [x] V07   (batch C)
- [x] V08  - [x] V09   (batch D)
- [x] V10  - [x] V11   (batch E)
- [x] V12  - [x] V13   (batch F)
- [x] V14  - [x] V15   (batch G)

### Batch rule
After every 2 reels (one batch) STOP and tell Rishi: what is done, what remains, and "check /usage before continuing".
Continue only when Rishi says go. If a reel is unfinished when you stop, write exactly where you stopped in `PROGRESS.md`.

### Optional quality check (after batch A)  [OPUS or FABLE, short]
- [x] Rishi may open a new session on Opus/Fable to read ONLY V01 and V02 `BREAKDOWN.md` and judge whether they meet the
      "10x better than a normal reverse-engineering" bar, then list corrections. Corrections go in `$REF/QUALITY_NOTES.md`;
      Sonnet applies them to later reels. Skip this if usage is tight.

---

## STOP GATE 1: end of all Sonnet work
When every Phase 0 and Phase 1 box is ticked, print EXACTLY this and stop (do not start Phase 2):

```
====================================================================
 SONNET WORK COMPLETE. All 15 reel teardowns are written.
 NEXT STEP NEEDS A STRONGER MODEL.
 Start a NEW session (or run /model) and switch to OPUS or FABLE,
 then tell it: "Read plan.md and continue from Phase 2."
 Check /usage first; Phase 2 is short but needs judgment.
====================================================================
```

---

## PHASE 2: Cross-reel synthesis  [OPUS or FABLE]
Only run if STOP GATE 1 has been reached (all Phase 1 boxes ticked). If you are Sonnet, do NOT do this; print the banner above again.
- [x] 2.1 Read all 15 `animations.json` and the key sections of each `BREAKDOWN.md` (overview, signature moves, gaps). Do not re-view videos.
- [x] 2.2 Classify every finding as CORE (in most reels), OPTIONAL, or EXPERIMENTAL. No single reel may rewrite the identity.
- [x] 2.3 Reconcile conflicts between reels (easing, scene types, timings); say which wins and why.
- [x] 2.4 Write `$REF/SYNTHESIS.md`: core/optional/experimental tables, merged animation library (named, with measured
        ranges), scene taxonomy with runtime shares, caption/type rules, colour tokens, sound-cue patterns, gaps.

Phase 2 seeds (from Sonnet's Phase 1; verify, do not trust blindly):
- Candidate CORE: A-roll talking head alternating with a graphic scene (blue ground V01/V05-V07/V12/V14, cream #EBE7E1 V02/V08-V11/V13/V15);
  captions = white sans + one italic-serif script word on the key noun/qualifier + bold on numbers; numbered chapter badge (blue diamond)
  with a title; UI recreations (post cards, toasts, search/comment bars) as proof; typed keyword in a comment bar as the CTA;
  split screen (top graphic pane / bottom A-roll) — pane curves measured in V14 (enter ≈ 1.0 s ease-in-out, expand ≈ 0.85 s ease-in,
  exit ≈ 0.97 s) vs V02 433 ms vs V03 1.0 s vs V07 1.3-1.5 s (RECONCILE: pick one default + range); hard cuts mostly silent
  (cut↔onset hit rate 0-0.33); hand-drawn red ellipse only for scarcity (V07, V09, V10, V12, V15); counters that start before the spoken number.
- Candidate OPTIONAL/EXPERIMENTAL: font-cycle word and glow/holographic cards (V01 only), cylinder carousel/orbit (V01), money confetti (V09, V15),
  pixelated hidden price (V12), 3D post-card push (V10), 2.0× zoom-cut (V01), centred vs lower-left diamond badge (V10 centred; others lower-left).
- Known conflicts to reconcile: easing for card entrances (no-overshoot ease-outs ≈ cubic-bezier(.1,1.4,0,.9) in V12/V14/V15 vs ≈ 20-60% overshoot springs
  in V01/V02); caption height (y≈ 62-66% H on A-roll, y≈ 49% H in V15, top-of-frame for single big lines); A-roll grade (V02-V03 navy/slate, V08+ teal/dark).
- Phase 2 output must separate [MEAS] facts from [EST]; flag every CORE rule that rests only on [EST].

## PHASE 3: Ask Rishi the Stage 0 questions  [OPUS or FABLE]
Ask (one batch, with defaults) before writing the pack: what to copy, how strictly, brand (gradnext lowercase / rishi.docx / original),
video type, build target (Claude Motion / Tesseract / Premiere), sound, languages (Hinglish in Roman script only).
Record answers in `DECISIONS.md` tagged `[R1.0]`. Follow `../Daniel Presley Editing Style/reverse engineer style SKILL.md`
Stages 4-5 for structure (that folder exists next to this one; READ-ONLY, structure/format reference only, never copy its tokens, colours or rules).
Offer defaults grounded in SYNTHESIS.md (e.g. default build target = the one Rishi already uses: Premiere via the `premiere-pro` MCP / Claude Motion / Remotion).
After Phase 2 (SYNTHESIS.md written) STOP and tell Rishi to skim it before Phase 3; continue only on his go.

## PHASE 4: Style pack + edit skill  [OPUS or FABLE writes the SKILL; SONNET may fill the rest]
Create `Rishi's Editing Style copy/Style Pack/` containing: README, SKILL (entry point), DECISIONS, LESSONS_LEARNED (empty at v1.0),
DESIGN_SYSTEM, SCENE_PRINCIPLES, MOTION_LIBRARY, EDITING_PSYCHOLOGY, PRODUCTION_WORKFLOW, SOUND_DESIGN, QUALITY_CONTROL,
VISUAL_REFERENCE_LIBRARY, CHANGELOG. Everything must come from these 15 reels, no inherited tokens from other styles.
- [x] 4.1 `SKILL.md` (edit skill: gates, scene selection, text rules, fixed vs flexible rules)  [OPUS or FABLE]
- [x] 4.2 DESIGN_SYSTEM, SCENE_PRINCIPLES, MOTION_LIBRARY, EDITING_PSYCHOLOGY  [OPUS or FABLE drafts the rules; Sonnet may format]
- [x] 4.3 README, CHANGELOG, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, PRODUCTION_WORKFLOW, SOUND_DESIGN formatting  [SONNET]  (done 2026-11-06; also created LESSONS_LEARNED.md (empty at v1.0) because SKILL.md reads it first. VISUAL_REFERENCE_LIBRARY is an index of reel/frame pointers, no stills copied (third-party, private study).)

When Phase 4 needs Sonnet after an Opus/Fable step, print:
```
====================================================================
 OPUS/FABLE STEP COMPLETE. Remaining items are mechanical.
 Switch back to SONNET (/model or new session) to save tokens,
 then say: "Read plan.md and continue Phase 4.3."
====================================================================
```

## PHASE 5: Pilot edit of `Video Projects/Vid 1.mp4`  [OPUS or FABLE plan, SONNET build]
Vid 1.mp4 is 1920x1080, 51.7 s, landscape. Confirm with Rishi what it is and the target (9:16 reel?) first.
- [x] 5.1 Edit plan: one row per beat (time, script, core idea, function, options A/B/C, why). STOP for Rishi's approval.  [OPUS or FABLE]
- [ ] 5.2 Build after approval; sound only after visuals are approved.  [SONNET, or the model Rishi chooses]
- [ ] 5.3 Revision loop (numbered table: timestamp, problem, expected, fix, status); corrections tagged `[R1.1]...` into LESSONS_LEARNED.

---

## Model cheat-sheet
| Work | Model |
|---|---|
| Setup, symlinks, path fixes, PROGRESS.md | Sonnet |
| Reel teardowns V02-V15 | Sonnet |
| Optional V01/V02 quality check | Opus or Fable |
| Cross-reel synthesis (core vs optional) | Opus or Fable |
| Conflict reconciliation | Opus or Fable |
| Stage 0 questions + DECISIONS | Opus or Fable |
| Writing the edit SKILL.md | Opus or Fable |
| Formatting / filling pack files from decided rules | Sonnet |
| Pilot edit plan (beat table) | Opus or Fable |
| Pilot edit build, revisions | Sonnet |

## Hard rules
- Never state an uncertain transcript word, font or sound as fact. Claude cannot hear: audio claims come from measurement only.
- Everything Rishi sets `[R#.#]` outranks any estimate.
- Third-party frames are for private study only; do not publish them or reuse the creators' assets outside the work folders.
- Write "gradnext" in lowercase. Hinglish in Roman script only, never Devanagari.
- Do not tick a box unless the file it refers to exists and is complete.
