# plan.md — Recreating @asmaijazkhann's editing style in Claude

Single source of truth. Every new chat starts with:
> "Read plan.md in my connected folder 'Azma's style' (also saved in the project as `asmaijazkhann-style/plan.md`). Continue from the next unchecked step. Use the model listed for that step. Update plan.md at the end."

At the end of every session Claude updates: checkboxes, Decisions, Session log (both copies: folder + project doc).

---

## 0. Brief
- **Creator:** https://www.instagram.com/asmaijazkhann/ (talking head + graphics)
- **Goal:** copy her look closely as a standalone style (not rishi.docx, not gradnext)
- **Method:** Joseph's training method: reference videos + style breakdown → skill pack (rule book, lookbook, reference library + index) → per-edit workflow (cut → plan doc → Rishi plans → build → design sheet → revise → sound)
- **Refs:** 15 videos, `Videos/vid-1.mp4 … vid-15.mp4`, 720×1280, ~35 min total (vid-7, 12, 15 are 29.97 fps; rest 24 fps)
- **Division of labour:** Rishi plans each edit and gives revision notes. Claude does everything else (extraction, classifying, breakdown, skill, builds).

## 1. Folder layout (laptop: Documents/Teaching Claude/Azma's style)
```
Azma's style/
  plan.md
  Videos/              vid-1 … vid-15 (originals, never modified)
  Frames of 15 videos/ Rishi's 24 fps PNG export (NOT used by the plan; see Decisions)
  work/
    stills/vid-N/      scene-change stills, 360px JPG (Claude)
    sheets/            contact sheets, 12 stills per image, filenames on tiles (Claude)
    strips/            0.5–1 s motion strips at native fps around animations (Claude)
    transcripts/       vid-N.srt (local Whisper)
    keys/<scene-type>/<animation-type>/   sorted stills
  breakdown/           notes per key, placement study
  skill/               SKILL.md, RULEBOOK.md, LOOKBOOK.md, REFS_INDEX.md, LESSONS.md, refs/
  sfx/                 whoosh/ click/ ui/ riser/ hit/
  edits/               one folder per edited video
```

## 2. Token rules
- Claude never reads raw frames one by one: only contact sheets (downscaled, 12 per image, filename on each tile).
- All ffmpeg / Whisper / sorting runs on Rishi's laptop (device_bash), not the cloud.
- Transcripts as SRT for the study phase, not word-level JSON.
- Motion is read from short strips only (1–2 examples per animation type), not from full 24 fps exports.
- REFS_INDEX.md is what edits load; full reference library opened only for chosen scenes.
- New chat per phase; keep chats short.
- Rough cuts: Gling or manual, not Claude.

## 3. Phase A — Train the style (one time)

| # | Step | Who | Model | Status |
|---|------|-----|-------|--------|
| A1 | Folder connected, 15 refs in `Videos/` | Rishi | – | [x] |
| A2 | (Dropped) Manual frame export not needed | – | – | [x] |
| A3 | **Prep:** extract scene-change stills (ffmpeg `select='gt(scene,0.15)'` + 1 still/2 s fallback, 360px JPG) → dedupe → contact sheets | Claude, laptop | Sonnet | [x] |
| A4 | **Transcripts:** vid-N.srt for all 15 (from Rishi's combined SRT, split by video length + 5 s gaps) | Claude | Sonnet | [x] |
| A5 | **First-pass sort:** read contact sheets, tag each still with scene type (§5), move into `work/keys/`; write `work/keys/INDEX.md` (still → vid, time, scene type, one-line description) | Claude | Sonnet | [x] all 15 videos, segment-level; stills copied to `work/keys/<type>/` + `MAP.tsv` |
| A6 | **Motion strips:** for 1–2 examples per scene type, cut 0.5–1 s strip at native fps around the animation, tile into one image each | Claude, laptop | Sonnet | [x] 23 strips + README |
| A7 | **Style study:** review sort; split each scene type by animation type (§5); name her keys | Claude | **Opus** | [x] `breakdown/KEYS.md`: 22 named keys K01–K22 × 12 animation types; example stills in `breakdown/keys/<key>/` (from `keys.tsv`) |
| A8 | **Placement study:** map graphics to SRT lines; rules for graphic vs plain A-roll; hook vs body density | Claude | **Opus** | [x] `breakdown/PLACEMENT.md` (stats via `work/a7/place.py`) |
| A9 | **Breakdown notes** per key: fonts, sizes, placement, colours, textures, timing, easing | Claude | **Opus** | [x] `breakdown/NOTES.md` (global tokens + per-key specs at 1080×1920) |
| A10 | Rishi reviews keys; confirms fonts (WhatTheFont/Font Ninja if unsure). Open questions listed in NOTES.md → Fonts: name display font (v10 "HAMILTON"), squarish grotesk (v1 92 s "then AI happened."), black italic (v8 "BEST THING EVER"), handwriting (v1 notebook, v7 "Good Hook"). Also sanity-check colours | Rishi | – | [x] via the A10 Review Desk artifact; results folded into KEYS/NOTES/PLACEMENT |
| A11 | **Skill pack:** SKILL.md, RULEBOOK.md, LOOKBOOK.md, REFS_INDEX.md, refs/ (still + strip + how-built note per animation). Decide build target (Motion vs Remotion) | Claude | **Opus** | [ ] |
| A12 | **Blind test:** plan one held-out video from its SRT only, compare to her real edit, fix rule book | Claude | **Opus** | [ ] |
| A13 | **Sound:** sort SFX into folders; note where her refs use each sound type; SOUND.md | Claude | Sonnet | [ ] blocked: no sfx/ files yet |
| A14 | Propose the skill to Rishi (propose_skills) | Claude | Sonnet | [ ] |

## 4. Phase B — Edit a video (every time)

| # | Step | Who | Model |
|---|------|-----|-------|
| B1 | Rough cut (Gling/manual) + SRT into `edits/<name>/` | Rishi | – |
| B2 | Planning doc: script lines + ~4 suggested scenes each from REFS_INDEX | Claude | Sonnet |
| B3 | Plan the edit (~15 min) | Rishi | – |
| B4 | Build scenes. New scene type → Opus; reused proven template → Sonnet | Claude | **Opus** first edit / Sonnet after |
| B5 | Design sheet (stills) for approval before full render | Claude | Sonnet |
| B6 | Revisions from timestamped notes. Small fixes → Sonnet; "doesn't feel like her" → Opus | Rishi + Claude | Sonnet / Opus |
| B7 | Cue sheet + SFX + music (−20 dB) | Claude | Sonnet |
| B8 | Render; add feedback to LESSONS.md | Claude | Sonnet |

## 5. Classification scheme (from Joseph; refined in A7)
Scene types (first pass):
1. captions — A-roll with captions (font pairing, placement, emphasis words)
2. hook — speaker + text + visual in first ~3 s
3. chapter-ui — numbered chapter/listicle markers, reused through the video
4. onscreen-pop — UI over A-roll: notification, before/after, counter/timer, list card, lower-half card
5. half-screen — graphic on one half, speaker on the other
6. fs-text — full-screen text
7. fs-object — full-screen object / illustration / person
8. fs-data — charts, graphs, UI mockups
9. broll-text — B-roll with treatment + text
10. camera — zooms, tracking, out-of-screen zooms, transitions
11. other

Animation types (second axis): first guess was pop-blur-fade, word-by-word, slide, scale-bounce, draw-on, mask-wipe, counter-roll, camera-push/pan, hard-cut. **Final list (A7) is A1–A12 in `breakdown/KEYS.md`**; scene types are refined there too (final keys K01–K22).

## 6. Decisions
- 2026-11-08: Copy her look closely as a standalone style.
- 2026-11-08: Claude drafts breakdown; Rishi only reviews.
- 2026-11-08: Rishi's 24 fps PNG export (~700 KB/frame; full set ≈ 50k frames ≈ 34 GB vs ~20 GB free) is not needed. Claude extracts small stills + targeted strips from `Videos/` instead. Rishi may stop/delete it.
- 2026-11-08: Transcripts: laptop Whisper too slow (~4 min/video) and HF blocked. Rishi supplied one combined 35:49 SRT (15 videos, 5 s gaps); Claude split it into `work/transcripts/vid-N.srt` (sentence-level lines). Boundaries verified against video durations. Laptop Whisper (sherpa-onnx, `work/tr2.py`) abandoned.
- Sandbox notes: background jobs die between device_bash calls (run foreground, <170 s, resumable); deleting files on the laptop is blocked, so stale files are left (`work/stills/vid-2/tmp_*.jpg`, `work/transcripts/vid-1.old`) and can be deleted by Rishi.
- 2026-11-08 (A7): hook is a position, not a scene type; no chapter-ui; no standalone fs-text; "camera" = grade beats (K02/K03); no bounce/overshoot or draw-on in her motion. Poppins is the main font for everything.
- 2026-11-08 (A10, Rishi): fonts = **Inter** (main) + **Playfair Display** (accent); Inter Tight Black Italic for heavy italic; Patrick Hand only in notebook props; Helvetica for annotations. Colours approved. Captions **below his chin** on A-roll. Dropped keys: K12, K13 (memes), K21 (podcast split), K22 (today-card). On request only: K03 (nose-tracked wiggle), K14 (b-roll). K05 gold-tag pending (Rishi unsure). K08 heads wiggle subtly; K09 gradient pixel cursor; K15 adds sharp zoom on key words; K17 mock-ups of tools/sites he mentions; K18 darkens his lower half and uses the brand's colour; K18/K19 colours agreed per video; K20 can be on white.
- Build target (Motion vs Remotion): decide in A11 (default Motion, as for Minimal Editorial).

## 7. Session log
- 2026-11-08 (Opus): Process designed from Joseph's transcripts; plan.md created; folder connected. Next: A3–A6 on Sonnet ("Phase A — Prep & first-pass sort").
- 2026-11-08 (Sonnet): A3 done: 15 videos → 2,222 stills (`work/stills/vid-N/v{N}_t{sec}.jpg`) and 212 contact sheets (`work/sheets/vid-N_sNN.jpg`, 12 per sheet, filename on each tile). A4 done via Rishi's combined SRT. Next: A5 (first-pass sort, read sheets, ~212 images: do in a fresh chat, maybe a few videos per chat) then A6 strips.
- 2026-11-08 (Sonnet, 2nd session): **A3–A6 complete.** A5: read all 82 thinned contact sheets (`work/sheets2/`, 1,474 stills) for all 15 videos; `work/keys/INDEX.md` = segment-level rows (video, time range, scene type, description) + tally. All 2,449 stills copied (not moved) into `work/keys/<scene-type>/` (captions 698, broll-text 736, fs-object 615, fs-data 309, onscreen-pop 43, hook 23, camera 15, half-screen 9, other 1) with `work/keys/MAP.tsv`. Type assignment is by time range from INDEX (uncovered stills = captions; stills <4 s = hook) so A7 should re-check boundaries. No chapter-ui in her style. A6: 23 strips + `work/strips/README.md` mapping scene types to strips; the blur→sharp A-roll return lasts only ~3 frames (`focus-pull-native_v2_9s_24fps`). Not done on purpose: A7+ (next, Opus). A13 (sound) is blocked until SFX files are added to `sfx/`.
- 2026-11-08 (Opus, 3rd session): **A7–A9 complete.** Rough check of A3–A6: OK (2,668 stills, 15 SRTs ending ~3 s before each video end, INDEX covers all 15, 23 strips). Known A5 limit: time-range sorting puts ~5–10 % edge frames in the wrong folder; not re-sorted, refs come from `breakdown/keys/` instead. New: 16 full-res type frames + 2 sheets in `work/a7/`; `work/a7/place.py` (placement stats). Key numbers: ~50 % runtime is graphics, ~11 cuts/min, median graphic 2 s, A-roll stretches median 2.8 s / max ~8 s, first graphic ≤3 s in 12/15 videos. Next: A10 (Rishi: fonts + review), then A11 skill pack on Opus.
- 2026-11-08 (Opus, 4th session): **A10 complete** via the A10 Review Desk artifact (https://claude.ai/artifact/HQNREmjeauVy6jhuZVZoPJ). Rishi's verdicts written into `breakdown/KEYS.md` (A10 status column), `NOTES.md` (Inter/Playfair font system + A10 line per key), `PLACEMENT.md` (no memes/today-card/b-roll by default). Open: K05 gold-tag (confirm keep/drop). Next: A11 skill pack on Opus.
