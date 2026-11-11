---
name: mock-case-interview-edit
description: Edit a gradnext mock case interview (two speakers, two cameras, ~30–45 min) end to end in Premiere Pro via the premiere-pro MCP — silence removal, self-assessment cut, word-level transcript, 4–8-word captions, a 70/30 motion-graphics case board with sound design. Use when Rishi drops a new mock case interview.
---

# Mock case interview edit (v1.1)

Kashish (interviewer) + a candidate, each with own camera + mic, synced in one Premiere sequence. Output: cleaned 16:9 edit, caption track, case board left 70 %, speakers stacked right 30 %. Taste: calm, premium, one idea at a time (Daniel Priestley reference, guidance only; path in reference/DESIGN_SYSTEM.md) [M22]. Studio rules: `02. Shared Core/` STUDIO.md, GOTCHAS.md, BRAND.md.

**Paths.** `R` = studio root (`/Users/rishi/Documents/Teaching Claude`). `E` = `R/01. Styles/Mock Case Interview/engine`. `PY` = `R/06. Tools/venv-style/bin/python` (PIL/numpy/soundfile; not system python) [L15]. `P` = `R/03. Projects/Mock Case Interview/R_mock_<topic>_<date>/`. `M` = `case.json` `inbox_folder` (relative to `R`): holds camera files; transcripts/captions are written there. New drops: `R/08. Inbox/`. Exports: `R/04. Exports/Mock Case Interview/`.

## Model gate
Check `MODEL_MODE` in the studio root CLAUDE.md, or what Rishi said this session. If it is `opus-only`, skip this section. Otherwise, steps marked [OPUS] (creative planning, storyboard or options, first look-dev of a new scene type, judging QC failures that need taste) need a check: if you are not running on Opus, stop and ask "Next step is creative (<step>). Switch to Opus with /model opus, or continue on Sonnet?" Steps marked [SONNET] (transcribe, cut, captions, building from an approved plan, applying a listed revision, renders, cleanup) run on whatever model is active; if that is Opus, mention once that Sonnet would be cheaper for this stretch.

## Workflow
Two STOPs only (3, 10) [M5, M6]; all else runs, then reports.

0. **Intake** [SONNET]. Ask only if missing: sequence name, candidate name, media folder. Premiere's MCP panel shows "Connector running".
1. **Connect + inspect** (read-only) [SONNET]. `claude mcp list`, `verify_premiere_connection` (cep), `list_sequences`; match case-insensitively; note id + end. `get_sequence_settings` (fps). `get_sequence_structure` (audio, windowed [L10]) → `case.json` `clips` = A1's `[timeline_start, timeline_end, source_in]` (cameras share source times [L12]); spans with no clip on a track → that speaker's `absent`. `find_project_item_by_name` both cameras; if outside the studio, give Rishi `! cp "<src>/"{name1,name2}-*.mp4 "<R>/<M>/"` [M3]. ffmpeg still per camera → `crop_x` (left edge of a 760×720 crop, face centred). Write `P/case.json` from `E/case.example.json`.
2. **Silence plan** [SONNET]. `python3 E/silence_plan.py P` → `plan.json`, `silence_report.md`. Threshold wrong? Check noise floors (10 ms RMS percentiles).
3. **STOP — silence report** [M5]: count, time removed, new length, 10 longest with timecodes, estimate (4 Nov: 3 batches ≈ 6 calls, 5–10 min).
4. **Cut** [SONNET]. `duplicate_sequence` the named sequence; rename the copy (by name) "<seq> RAW", untouched backup. `set_active_sequence` (named) [L3]. Per `plan.json` batch (end → start): `ripple_remove_timeline_ranges` {`sequence_id`, `scope: sync_locked`, `range_content: delete`, `allow_large_ripple: true`, `ranges`, `dry_run: true`} → check `trackCounts` (all clip tracks) → repeat with `dry_run: false` + the single-use `confirmation_token`. Works on 29.97; without `allow_large_ripple`, > 400 moving clips = refused + token burnt [L1, L2]. Then `add_markers_batch` (`plan.json["markers"]`); check new end = old end − removed.
5. **Transcript** [SONNET]. `python3 E/timeline_map.py P --audio`; `zsh E/transcribe.sh P` in background (CPU `-ng` [L14]; 36 min audio ≈ 40 min; report progress); `python3 E/transcript.py P <seq>_transcript` → `M/<seq>_transcript_words.json/.csv/.srt`.
6. **Self-assessment cut, always** [SONNET] [M11]. `duplicate_sequence` → "<seq> Copy" → `set_active_sequence`. Cut from just before the interviewer's "How do you think you did?" to just before the first feedback sentence not reacting to the self-assessment (drop "Got it. Cool. I mean, sir," → "…Thank you so much. | I think you did well…"). Snap edges to the quietest 10 ms near word onsets (`cut_spk*.wav`). Ripple-remove (dry run, apply); orange marker at the join. Add the range to `case.json` `extra_cuts_after_silence`; `python3 E/timeline_map.py P --slivers`; ripple out any ≤ 2-frame piece (merge into that range).
7. **Captions** [SONNET]. `python3 E/transcript.py P <seq>-copy_transcript --from M/<seq>_transcript_words.json --remove <a_ms> <b_ms>`. Proofread the full text; write `P/corrections.json` (from `E/corrections.beer-case.json` word rules); `python3 E/fix_words.py M/<seq>-copy_transcript_words.json P/corrections.json P/words.json M/<seq>-copy_caption_corrections.csv`. `python3 E/captions.py P/words.json M/<seq>-copy_captions.srt`. `import_media` → `create_caption_track` (`item_id`, `caption_format: subtitle`, `start_seconds: 0`) → "committed_unverified": ask Rishi to confirm.
8. **Graphics plan, no stop** [OPUS]. `M/motion_graphics_plan.md`: chapters + beats timed from `P/words.json` (beat grammar: reference/DESIGN_SYSTEM.md). Usual chapters: Problem · Clarify · Structure · Option A · Option B · Recommend · Feedback.
9. **Pilot** [OPUS for a new beat type's first look-dev, else SONNET]. `duplicate_sequence` (Copy) → `rename_project_item` by name "<seq> Copy Copy" → "<seq> MG" (by ID fails + locks [L4]) → `set_active_sequence`. `board_beer_case.py` is hard-coded to the beer case: copy to `P/board.py`, keep primitives/renderer, rewrite `CHAPTERS` + beats (`at("phrase", after)` = word time); don't refactor the engine copy. `PY P/board.py P 0 <end>`; `PY E/speakers.py P 0 <end>` (~10 min per 11 min); composite (hstack command: reference/WORKFLOW.md §9) → `P/MG_pilot.mp4`. ffmpeg stills (`export_frame` fails + locks [L6]): check glyphs, overlaps, clipped labels. Voice LUFS (`ffmpeg -i P/cut_mix.wav -af ebur128 -f null -`) → `PY E/sfx_mg.py P P/events_<t0>_<t1>.json <dur> P/MG_sfx.wav <voice_lufs>`. `import_media` → `overwrite_clip` at 0 on the first empty tracks above the originals (4 Nov: video `track_index` 5 = V6; SFX `audio_track_index` 2 = A3). Verify with windowed `get_sequence_structure`.
10. **STOP — pilot** [M6]: ~first 10–11 min (chapters 1–4). Rishi checks lip-sync, look, SFX level on phone (move the whole stem in 2 dB steps). Taste judgments [OPUS]; listed fixes [SONNET].
11. **Full render** [SONNET]. Same commands, full length (~15 min encode); `overwrite_clip` at 0 replaces the pilot.
12. **Hand-over** [SONNET]. RAW untouched; Copy/MG lengths right; no slivers; markers in place; list files (plan, corrections CSV, `MG_sfx_cues.md`); check what Rishi notices [L23]: abrupt caption breaks ("next?" opening one), single-word captions, round corners. Remind: Cmd+S; captions still default bottom-centre.
13. **Close-out** [SONNET]. After Rishi approves the final export: `"<studio root>/06. Tools/finalize_reel.sh" "<project folder>"` (dry run first; `--export <file>` if not auto-found), show Rishi, then `--yes`. Fold the feedback log.

## Hard rules
**Safety.** Touch only the named sequence and our copies/imports [M1]; each stage on its own sequence (`<seq>`, Copy, MG) [M2]. Never read outside the studio root [M3, L13]. Never cut with Premiere's transcript/text-based editing [M4]. Never place renders with `add_to_timeline` (it inserts, rippling every track); use `overwrite_clip`, originals untouched underneath [L7, M23]. Never retry a failed MCP call in a loop.

**Cutting.** Silence = BOTH tracks below threshold; no clip = silent. −50 dB worked (floors −70/−77, speech −25/−35) [M7]. Pauses > 1.0 s; 0.12 s padding (0.1–0.15 ok); merge pauses < 0.3 s apart; all tracks together [M8]. ≤ 50 ranges/call, end → start [M9]. Red markers on the 5 longest ("Pause N.Ns", comment = original times) [M10]. After any cut, remove clips ≤ 2 frames (cuts within 1–2 frames of an edit leave them) [M12, L22].

**Transcript + captions.** Word-level, ms, speaker per word; JSON + CSV + SRT; derive later versions, don't re-run Whisper [M13]. Caption track (Subtitle), never graphics, never SFX [M14, M21]. 4–8 words, never 1–3. A sentence end (or > 1.5 s pause) ends a caption; a new sentence starts one. 1–3-word replies ("Sure.", "Cool.", "OK.") join the START of the next sentence. ≤ 8-word sentences stay whole; longer split 4–6 at commas / "and/so/which", never after weak words ("I would", "the", "to"). Min 0.5 s, no overlaps [M15]. Proofread with case logic (kegs not "cakes", canning not "casing/scanning/calving", barrels not "batteries/battles/balance", "your client" not "Yog Lion"; numbers add up); log every change; flag guesses [M16, L20]. Louder-track speaker labels are noisy on single words; smooth before reuse [L21]. MCP can't delete caption tracks and re-imports stack: get captions right first; tell Rishi which to delete by first caption [L8].

**Graphics** (tokens: reference/DESIGN_SYSTEM.md). 1920×1080, 29.97 fps. Left 70 % (x 0–1344) board; right 30 % speakers, interviewer top, candidate bottom [M17]; y 910–1070 free for captions. `01. Styles/Consulting Case` board look: white card, lavender bg, navy Avenir Next, element appears on the word that says it [M18]. Subtle corners: card 12, boxes/chips 8, pills/tabs/labels 6, bars 4, speaker cards 10; never pill-round [M19]. Labels "Kashish · Interviewer", "<Name> · Candidate" [M20]. Avenir Next has no "→" — write "=", "to", "&", ":" [L18] (font faces: reference/DESIGN_SYSTEM.md [L19]). Re-lay out speakers by rendering, never by editing clips (no `nest_clips` on CEP; Rounded Crop not batch-editable) [L9].

**Sound** (map: reference/SOUND_DESIGN.md). Every graphic event gets a quiet sound, peak on the visual; within 110 ms the louder wins; Minimal Edit sound rules only, never its visuals; own track [M21]. Levels assume a −15 LUFS program; stem gain = `voice_lufs + 15` dB (4 Nov: −28.9 LUFS → −13.9 dB).

## MCP + toolchain
- `HOST_RECOVERY_REQUIRED` → `inspect_operation_recovery` (output saved to a file; read `recoveryRevision` + `hostStateRevision` with python, sandbox disabled) → `acknowledge_operation_recovery` with both [L5].
- `list_sequences` end includes caption tracks (+0.2 s seen) [L11]. ffmpeg 7: `-/filter_complex file.txt`; long `aselect` fails, use atrim+concat [L17].

## Read only when…
| Doc | When |
|---|---|
| reference/WORKFLOW.md | Step 9 composite; a call fails or needs an unlisted parameter |
| reference/DESIGN_SYSTEM.md | Steps 8–9, any visual change |
| reference/SOUND_DESIGN.md | Step 9 SFX; sound/level questions |
| reference/README.md | Reference-project map; open items (caption placement, logo, speaker glow) |
| history/ | Where a rule went (RULE_AUDIT.md); original wording |

## Learning loop
During a reel, append Rishi's raw notes to `FEEDBACK_LOG.md` (date, reel, note). When the reel is approved, fold the durable rules into this SKILL.md or the right reference/ doc, delete any rule they reverse, add a line to `history/CHANGELOG.md`, and mark the log entries as folded. Keep SKILL.md under about 1,500 words; move detail to reference/ instead of growing it.
