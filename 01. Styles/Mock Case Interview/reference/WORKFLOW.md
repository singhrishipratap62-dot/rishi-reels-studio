# WORKFLOW — mock case interview, exact calls (reference)
`SKILL.md` is the authoritative workflow and wins on any conflict; this file keeps the long-form parameters and commands.
`R` = studio root (`/Users/rishi/Documents/Teaching Claude`), `E` = `R/01. Styles/Mock Case Interview/engine`, `PY` = `R/06. Tools/venv-style/bin/python` (PIL/numpy/soundfile), `P` = `R/03. Projects/Mock Case Interview/R_mock_<topic>_<date>/`, `M` = the case media folder = `case.json` `inbox_folder` (path relative to `R`, e.g. `03. Projects/Mock Case Interview/mock case, 4th November`). New raw drops land in `R/08. Inbox/`. MCP tool names are from `premiere-pro-mcp-leancoderkavy`.
Stops for Rishi: **after step 3** (silence report) and **after step 9** (pilot chapter). Everything else: run, then report.

## 0. Intake (ask only if missing)
- Sequence name (e.g. "4 Nov-CLD"), candidate's name, case media folder (`M`).
- Rishi has Premiere open with the "MCP for Adobe Premiere Pro" panel → "Connector running".

## 1. Connect + inspect (read-only)
1. `claude mcp list` (the server is usually already registered and loaded).
2. `verify_premiere_connection` (backend cep) → `list_sequences` → find the sequence (match case-insensitively). Note its id and `end`.
3. `get_sequence_settings` (fps — 29.97 in our case; sources 1280x720 @ 24).
4. `get_sequence_structure` with `track_type: audio` (window with `start_seconds/end_seconds`, `track_index` — payloads are big) → per-clip `startSeconds`, `endSeconds`, `inPointSeconds` → `case.json` `clips` (use A1; A2 had no clip for the first 88 s → that speaker's `absent`).
5. `find_project_item_by_name` for both camera files → media paths. If outside the studio, give Rishi:
   `! cp "<src folder>/"{name1,name2}-*.mp4 "<R>/<M>/"` [M3]
6. Grab a still of each camera (`ffmpeg -ss 100 -i <file> -frames:v 1 -vf scale=640:-1 x.png`) → set `crop_x` (face centred in a 760-wide crop).
7. Write `P/case.json` from `E/case.example.json` (`inbox_folder` = `M`, relative to `R`).

## 2–3. Silence detection → STOP
1. `python3 E/silence_plan.py P` → `A1.wav`, `A2.wav`, `plan.json`, `silence_report.md` (~15 s).
2. Optional: check noise floors (10 ms RMS percentiles) if the threshold looks wrong; −50 dB worked with floors at −70/−77 dB.
3. **Report to Rishi**: count, time removed, new length, top-10 pauses, estimate (3 batches ≈ 6 MCP calls, ~5–10 min). Wait for approval.

## 4. Cut (on the named sequence)
0. `duplicate_sequence` the named sequence and `rename_project_item` (by name) "<seq> Copy" → "<seq> RAW": an untouched backup (added 2026-11-11 so hand-over's "original untouched" holds). Then `set_active_sequence` on the named sequence.
For each batch in `plan.json["batches"]` (already ordered end → start):
1. `ripple_remove_timeline_ranges` dry run: `sequence_id`, `scope: sync_locked`, `range_content: delete`, `dry_run: true`, **`allow_large_ripple: true`**, `ranges`.
2. Check `trackCounts` (all clip tracks participate), then apply with `dry_run: false` + the `confirmation_token` (same ranges, same flags).
3. After all batches: `add_markers_batch` with `plan.json["markers"]`; `list_sequences` → new end must equal old end − total removed.

## 5. Transcript (cut timeline)
1. `python3 E/timeline_map.py P --audio` (extra_cuts empty for now) → `cut_mix.wav`, `cut_spk1/2.wav`, `src_segments.json`.
2. `zsh E/transcribe.sh P` in the background (~40 min; give Rishi progress = last timestamp ÷ length; progress line: `grep -oE "^\[[0-9:.]+ --> [0-9:.]+\]" P/whisper.log | tail -1`).
3. `python3 E/transcript.py P <seq>_transcript` → `M/<seq>_transcript_words.json/.csv` + `M/<seq>_transcript.srt`.

## 6. Self-assessment cut (always) [M11]
1. `duplicate_sequence` → `set_active_sequence` (the copy).
2. In the transcript find the interviewer's "How do you think you did?" and the start of the feedback ("Cool…/Got it…/I think you did well…"). Cut **from just before the question to just before the first feedback sentence that doesn't react to the self-assessment** (we dropped "Got it. Cool. I mean, sir,").
3. Snap both edges to the quietest 10 ms near the word onsets (look at `cut_spk*.wav` RMS around the edge).
4. Ripple-remove that range (dry run → apply). Add an orange marker at the join.
5. Add the range to `case.json` `extra_cuts_after_silence`, run `python3 E/timeline_map.py P --slivers` → remove any ≤ 2-frame piece with one more ripple cut (merge it into the extra cut range). (This replaces the `check_slivers.py` named in L22, which never existed.)

## 7. Transcript for the copy + captions
1. `python3 E/transcript.py P <seq>-copy_transcript --from M/<seq>_transcript_words.json --remove <a_ms> <b_ms>` (no Whisper re-run).
2. Proofread: read the full text (speaker-grouped) and write `P/corrections.json` (start from `E/corrections.beer-case.json` word rules). `python3 E/fix_words.py M/<seq>-copy_transcript_words.json P/corrections.json P/words.json M/<seq>-copy_caption_corrections.csv`. Flag guesses. (`P/words.json` = the corrected words; the board renderer reads this exact name.)
3. `python3 E/captions.py P/words.json M/<seq>-copy_captions.srt`.
4. `import_media` the SRT → `create_caption_track` (`item_id`, `caption_format: subtitle`, `start_seconds: 0`). Result is "committed_unverified" — ask Rishi to confirm, and if a caption track must be replaced, tell him to delete the old one (identify it by its first caption).

## 8. Graphics plan (no stop)
Write `M/motion_graphics_plan.md`: chapters + beats with times from the corrected words (see DESIGN_SYSTEM "Beat grammar"). Chapters are usually: Problem · Clarify · Structure · Option A · Option B · Recommend · Feedback.

## 9. Build → pilot → STOP → full
1. `duplicate_sequence` (the copy) → `rename_project_item` by **name** "<seq> Copy Copy" → "<seq> MG" → `set_active_sequence`.
2. Copy `E/board_beer_case.py` to `P/board.py` (it is hard-coded to the beer case — adapt the copy, don't refactor the engine file); keep the primitives/renderer, rewrite `CHAPTERS` and the beats section (`at("phrase", after)` gives word times). Words file = `P/words.json` (the corrected words).
3. `PY P/board.py P 0 <pilot_end>` (seconds; pilot ≈ first 10–11 min, chapters 1–4) → `board_concat.txt` + `events_<t0>_<t1>.json`.
4. `PY E/speakers.py P 0 <pilot_end>` (~10 min for 11 min).
5. Composite:
   `ffmpeg -f concat -safe 0 -i P/board_concat.txt -i P/speakers_0_<end>.mp4 -filter_complex "[0:v]fps=30000/1001,format=yuv420p,setpts=PTS-STARTPTS[b];[1:v]setpts=PTS-STARTPTS[s];[b][s]hstack=inputs=2[o]" -map "[o]" -t <end> -r 30000/1001 -c:v libx264 -crf 16 -preset medium -pix_fmt yuv420p P/MG_pilot.mp4`
6. Stills check with ffmpeg (NOT `export_frame`): look for missing glyphs, overlaps, clipped labels.
7. SFX: `PY E/sfx_mg.py P P/events_<t0>_<t1>.json <dur> P/MG_sfx.wav <voice_lufs>` (voice LUFS: `ffmpeg -i P/cut_mix.wav -af ebur128 -f null -`).
8. `import_media` → `overwrite_clip` video on the first empty video track above the originals (track_index 5 = V6) at 0; SFX with `audio_track_index` on the first empty audio track (2 = A3). Verify with `get_sequence_structure` windows.
9. **STOP**: Rishi checks lip-sync, look, SFX level. Then render the full length the same way (full composite ≈ 15 min encode) and overwrite at 0 (replaces the pilot).

## 10. Hand-over checklist
- Lengths: "<seq> RAW" untouched; copy and MG lengths as expected (`list_sequences`; its end includes caption tracks).
- No ≤ 2-frame slivers. Markers in place.
- Files listed with paths; cue sheet `MG_sfx_cues.md`; corrections CSV; plan.
- Remind: Cmd+S in Premiere; captions position still default (bottom-centre).

## 11. Close-out
After Rishi approves the final export: `"R/06. Tools/finalize_reel.sh" "P"` — dry run by default; it looks for the export in `04. Exports/<style>/` by reel-ID prefix, else pass `--export <final.mp4>`; re-run with `--yes` to delete the regenerable intermediates (board frames, SFX stem, etc.).

## Toolchain notes (moved from LESSONS_LEARNED)
- Node/Playwright (reel engine) depends on caches outside the workspace → not usable here; the PIL board renderer replaces it [L16].
- ffmpeg 7 uses `-/filter_complex file.txt` (not `-filter_complex_script`). Very long `aselect` expressions fail — use atrim+concat segments [L17].
