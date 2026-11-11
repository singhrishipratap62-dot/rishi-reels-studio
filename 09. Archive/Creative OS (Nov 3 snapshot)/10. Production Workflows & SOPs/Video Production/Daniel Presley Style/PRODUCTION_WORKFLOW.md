# PRODUCTION WORKFLOW — Daniel Priestley Editing Style (v1.0)

## 1. Pacing targets [MEAS from 28 refs unless noted]
| Metric | 16:9 long-form | 9:16 reel [INF] |
|---|---|---|
| Average shot length | median **7.4 s** across 28 (range 3.9–22.3). Target 5–8 s overall | 2–3.5 s |
| Median shot | 2.7–7.8 s | 1.5–2.5 s |
| Cuts in first 30 s | 6–17 (every video). Target ≥ 10 | ≥ 12 |
| Time to first graphic | < 3 s (B-roll/graphic by 00:01–00:06 in all) | < 1.5 s |
| Name sting | 0:25–1:15 | optional, 0:02–0:05 or skip |
| First chapter wipe | 0:45–3:00 | 0:04–0:08 |
| Density shape | Front-loaded: dense first 5–7 min, then longer whiteboard/A-roll holds (R26, R28 back halves ≥ 4 min uncut) | Even density |
| Rapid montage shots | ≈ 1.1 s each (R18 00:03) ; B&W cold-open 0.3 s (R17) | 0.5–1 s |
| Pauses | Workspace style: no pauses > 0.3 s `[CLAUDE.md]` | same |

## 2. Long-form structure template [OBS all 28]
1. **Cold-open hook** (A-roll, 0:00–0:10) + kinetic keyword title.
2. **Proof montage** (0:05–0:30): name-pilled people, headlines, logos, stage shots, 1 s each.
3. **Name sting → name card** (0:25–1:15).
4. Optional promise/agenda: list + PiP or "About me" PiP.
5. **Chapters 1…N**: arc wipe + tile (+ title) → explanation (A-roll ↔ whiteboard/list PiP ↔ B-roll/examples) → quote card for the key line.
6. Optional CTA mid-video: framed landing page + pill.
7. **Calm ending**: A-roll sign-off or product/webinar page; no branded end card.

## 3. Reel template (9:16) [INF — derived, Rishi to approve]
Hook keyword title (0–2 s) → 2–3 proof shots with name pills (2–5 s) → 1–3 numbered points via arc wipe + tile, each with one PiP/whiteboard or chip beat → one quote card for the key line → sign-off.

## 4. Build pipeline (Claude Motion artifact default; Premiere/ffmpeg alternatives)
1. Ingest footage to `inbox/`; project in `projects/<REEL_ID>/` (`R###_topic_YYYY-MM-DD`).
2. Rough cut: `auto-editor --margin 0.15s` (reel-rough-cut skill); transcript with whisper (`-ng` CPU flag may be needed in sandbox).
3. Beat plan (EDITING_PSYCHOLOGY §2) → **stop for approval**.
4. Build graphics as HTML/CSS components (DESIGN_SYSTEM §7) in Claude Motion; render or composite over A-roll.
5. Assemble in ffmpeg or Premiere (premiere-handoff skill), hard cuts by default.
6. Sound after visuals approved (SOUND_DESIGN §4).
7. Export: 16:9 1920×1080 or 9:16 1080×1920, 30 fps, H.264 High CRF 18, AAC 192k, −14 LUFS (reel-export skill).
