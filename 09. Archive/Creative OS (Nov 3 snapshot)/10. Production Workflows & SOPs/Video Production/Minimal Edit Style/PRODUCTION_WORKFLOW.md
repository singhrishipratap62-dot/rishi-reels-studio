# Production Workflow — v1.1

Tutorial timings for reference (57 s edit): cuts + plan doc 15 min · human planning 15 min · build 60 min · revisions 10 min · sound 15 min. `[TX 18:53–19:36]`

Hard gates: **no animation before the plan is approved; no sound design before visuals are approved.**

---

## Stage 0 — Ask up front (v1.1)
Ask these before analysing, so they don't surface mid-edit:
- Design style (default: this system).
- Framing for split-screen or multi-cam sources.
- **Platform safe zone** (default: the Instagram Reels template).
- **SFX library** (default: `minimal-edit-system/SFX/`).
- Music track (licensed, supplied).
- Any names or words to verify.

Also read `LESSONS_LEARNED.md`.

## Stage 1 — Raw footage analysis
1. Ingest talking-head clip (+ SRT if supplied).
2. Word-level transcript with timestamps (millisecond level). `[TX 12:51]`
   - Local method that worked (v1.1): `mlx-whisper` with `whisper-turbo` and word timestamps. Snap word edges to `silencedetect` (−35 dB, 120 ms) boundaries.
   - Save JSON + SRT + a table. Flag words with confidence < 0.7 as uncertain; don't state them as fact.
3. Detect silences; cut them leaving **30 ms padding** each side (tutorial's demonstrated value — adjust per speaker; raise to 60–100 ms if breaths/attacks get clipped). `[TX]`
4. Protect delivery: keep intentional pauses before punchlines; remove false starts and orphan words ("But"). `[TX revision #4, INF]`
5. Output: cut list + retimed transcript.

## Stage 2 — Edit plan (review document)
Recreate the tutorial's planning doc `[OBS 13:06–15:24]`: title "‹clip› · edit plan", "N beats · total s". Per beat:

| Field | Content |
|---|---|
| Beat # + time | e.g. Beat 5 · 0:14.2–0:17.0 |
| Script | exact words (right column, with clip player) |
| Core idea | ≤ 3 words |
| Function | announce/explain/… (EDITING_PSYCHOLOGY §3) |
| "Seen in the reels" | which reference pattern this mirrors and why |
| Design options A/B/C | title · category tags (e.g. "Graphs + Visual Representations · Cut-away scene") · 1–2 line description · reference ID |
| Animation | motion IDs from MOTION_LIBRARY |
| Assets | needed files + source idea |
| Camera | e.g. "Medium shot 0–1.9 s" |
| Editor notes | free text box: "Write your plan for this beat — or pick a design" |
| Status | My pick / Chosen |

Deliver as an interactive page (pick buttons + notes + "copy plan") or a doc. **Stop and wait for the human's picks.** `[TX 13:15–15:49]`

## Stage 3 — References & assets
- Pull the chosen reference IDs and list exact designs to copy. `[OBS 16:06]`
- Asset list with source + licence per item: paintings (Wikipedia/Wikimedia public domain), stock (Pexels), photos of the speaker (user-supplied or properly licensed). `[OBS 16:18]`
- Mark missing assets; ask the user rather than substituting something unrelated.
- Fonts: Inter + Playfair Display (Google Fonts). `[OBS 16:30 "Installed Inter + Playfair Display"]`

## Stage 4 — Build scenes
Order observed `[OBS 16:24–16:42]`: captions on full A-roll first → cinematic text design → painting → character → B-roll+text → object callout → graphs → line+text → spiral → final illustration. Build each scene as a reusable component (DESIGN_SYSTEM §8). Tutorial used Remotion.

**Tesseract build (v1.1, proven on the first edit):**
- Keep the whole edit in one regenerable `build.py`: footage JSON → native graphics action batch → sound layers.
- Rebuild from a clean base `.tsrct` that already has the footage, fonts and audio imported.
- Archive each draft in `Versions/` and keep a revision table in `NOTES.md`.
- Run the safe-zone audit on every build.
- The engine gotchas are in `LESSONS_LEARNED.md` §8.
- Reference implementation: `edits/first-principles-kashish/.tesseract-work/build.py`.

## Stage 5 — Assemble & first render
Chronological assembly, sync to audio, check transitions/pacing, render 1080×1920. Expect the first draft to be **60–70 % there**. `[TX 17:00]`

## Stage 6 — Revisions
Log every note in a table and fix in one pass, then re-render and ask "ready for sound design, or more revisions?" `[OBS 17:24]`

| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| example (tutorial's six) `[OBS 17:22]` | | | | | |
| 1 | 0:00–0:01 | first-scene text design weak | keep "psychologically" on the same scene as "four" | re-layout caption pair | done |
| 2 | ~0:06 | rough cut graph → next shot | hold graph text until 0:06, then cut | extend hold | done |
| 3 | painting | paint texture too heavy, static | half strength, moves with painting | texture inside camera group | done |
| 4 | 0:24 | bad cut | remove tiny "But" clip | trim | done |
| 5 | spiral | leaves too early | hold through "for every 7 to 12 years" with slow zoom-out | extend + M22 | done |
| 6 | end text scene | no quote marks | add small quotation marks | M26 | done |

## Stage 7 — Sound design
Only after visual approval. See SOUND_DESIGN.md (v1.1: dense but quiet, library first, a sound on every text entry, effects-only placement check, lip-sync check). Tutorial result: music + 74 SFX in 57 s `[OBS 17:48]`. First Tesseract edit: 103 cues in 33 s.

## Stage 8 — Final QC & export
Run QUALITY_CONTROL.md. Export H.264 MP4, 1080×1920, 30 fps, AAC 48 kHz; loudness −15 LUFS integrated (−16 to −14), true peak ≤ −1 dBTP, measured on the exported MP4 (v1.1). Watch on a phone.

---

### Training a new style (meta-workflow the tutorial teaches) `[TX 08:06–11:39]`
1. Collect ~20 of the best reels in the style. 2. Watch each as an editor: why this scene/design/colour/effect/animation? 3. Screenshot every good scene onto a board (~130 pieces). 4. Sort into principle categories; annotate fonts, colours, sizes, patterns. 5. Give Claude the videos + board; ask for word-level transcripts and frame-by-frame breakdown of (a) where animations sit vs script, (b) design composition, (c) animation logic/duration. 6. Package as a skill with a reference library (tutorial: 225 animations, each folder = stills + keyframe sheet + clip + notes, named `V##-A##`).
