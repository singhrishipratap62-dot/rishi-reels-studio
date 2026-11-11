# RULE_AUDIT — where every rule went (restructure 2026-11-11)
Sources audited: old SKILL.md (v1.0, kept as `history/SKILL.v1.0.md`), README, WORKFLOW, DECISIONS (M1–M23), LESSONS_LEARNED (L1–L23), DESIGN_SYSTEM, SOUND_DESIGN, engine script headers.
"SKILL §X" = section of `../SKILL.md` (Workflow step N, Hard rules › Safety / Cutting / Transcript + captions / Graphics / Sound, MCP + toolchain, Paths). Rule text in DECISIONS/LESSONS stays as the historical record; SKILL.md is now authoritative.

## Decisions M1–M23
| ID | Rule (short) | Now lives in | Notes |
|---|---|---|---|
| M1 | Work only on the named sequence; new copies/imports fine | SKILL › Hard rules › Safety | verbatim meaning |
| M2 | Every major stage on a new duplicate: `<seq>` → `<seq> Copy` → `<seq> MG` | SKILL › Safety; Workflow steps 4, 6, 9 | **Amended**: step 4 now first duplicates the named sequence as "<seq> RAW" (untouched backup) — see Conflict 1 |
| M3 | Everything inside the workspace; give Rishi the exact `cp` | SKILL › Workflow 1; Safety | path now `<R>/<inbox_folder>/` instead of `inbox/<case>/` |
| M4 | Never Premiere transcript/text-based editing for cuts | SKILL › Safety | |
| M5 | STOP: silence report (count, time removed, 10 longest, estimate) | SKILL › Workflow 3 | also new length (from WORKFLOW) |
| M6 | STOP: pilot chapter ~first 10–11 min, chapters 1–4 | SKILL › Workflow 10 | wins over v1.0 SKILL "~10 min" and WORKFLOW "~10 s" (Conflict 5) |
| — | Everything else runs without asking; report after | SKILL › Workflow header | |
| M7 | Silence = both tracks below threshold; no clip = silent; −50 dB (floors −70/−77, speech −25/−35) | SKILL › Cutting | |
| M8 | > 1.0 s; 0.12 s pad (0.1–0.15); merge < 0.3 s; all tracks together | SKILL › Cutting | numbers also in `case.json` `silence` |
| M9 | ≤ 50 ranges/call, end → start | SKILL › Cutting; Workflow 4 | |
| M10 | Red markers on 5 longest ("Pause N.Ns", comment = original times) | SKILL › Cutting | silence_plan.py writes them (color 1) |
| M11 | Always remove self-assessment; trim reaction words; quietest 10 ms | SKILL › Workflow 6 | example strings kept |
| M12 | Remove ≤ 2-frame clips after any cut | SKILL › Cutting; Workflow 6 | |
| M13 | Word-level ms transcript, speaker/word, JSON+CSV+SRT; derive, don't re-run Whisper | SKILL › Transcript + captions; Workflow 5, 7 | save location = `inbox_folder` (Conflict 2) |
| M14 | Captions = Premiere caption track (Subtitle) | SKILL › Transcript + captions | |
| M15 | 4–8 words, never 1–3, sentence rules, short replies join next, split 4–6, weak words | SKILL › Transcript + captions | plus code facts from captions.py: > 1.5 s pause ends a caption, min 0.5 s, no overlaps |
| M16 | Proofread with case logic; corrections CSV; flag guesses | SKILL › Transcript + captions; Workflow 7 | merged with L20's mishear list |
| M17 | 16:9; left 70 % (0–1344) graphics; right 30 % speakers, interviewer top | SKILL › Graphics; pixels in reference/DESIGN_SYSTEM.md | |
| M18 | Consulting Case board visual language | SKILL › Graphics | stale name "Consulting case reel edit" → `01. Styles/Consulting Case` |
| M19 | Subtle radii: card 12, boxes/chips 8, pills/tabs/labels 6, speaker cards 10; never pill-round | SKILL › Graphics | bars 4 added from DESIGN_SYSTEM |
| M20 | Name labels "Kashish · Interviewer", "<Name> · Candidate" | SKILL › Graphics | |
| M21 | SFX for every MG event; Minimal Edit sound only; captions silent; own track | SKILL › Sound; Transcript + captions | trigger map in reference/SOUND_DESIGN.md |
| M22 | Daniel Priestley reference = taste guidance only | SKILL intro; path in reference/DESIGN_SYSTEM.md | path → `09. Archive/Unused Styles/Daniel Presley Editing Style/` |
| M23 | Graphics = rendered video on new top track via overwrite; originals untouched | SKILL › Safety; Workflow 9 | |
| Open | Caption placement; logo file; active-speaker glow | reference/README.md › Open items | linked from SKILL "Read only when…" |

## Lessons L1–L23
| ID | Lesson (short) | Now lives in | Notes |
|---|---|---|---|
| L1 | Ripple works on 29.97 (frame-snaps); dry run first; single-use token | SKILL › Workflow 4 | |
| L2 | > 400 clips → apply refused + token consumed; always `allow_large_ripple: true` | SKILL › Workflow 4 | |
| L3 | Sequence must be active for ripple (QE); `set_active_sequence` after duplicate | SKILL › Workflow 4, 6, 9 | |
| L4 | Copies named "<name> Copy"; rename by name (by ID → "Item not found" + lock) | SKILL › Workflow 9 (and 4) | |
| L5 | HOST_RECOVERY_REQUIRED → inspect (file, read revisions with python, sandbox off) → acknowledge | SKILL › MCP + toolchain | |
| L6 | `export_frame` fails + recovery lock → ffmpeg stills | SKILL › Workflow 9 | |
| L7 | `add_to_timeline` inserts/ripples → `overwrite_clip` (track_index / audio_track_index) | SKILL › Safety; Workflow 9 | |
| L8 | Caption track readback unavailable; MCP can't delete caption tracks; re-imports stack | SKILL › Transcript + captions; Workflow 7 | |
| L9 | `nest_clips` unavailable on CEP; Rounded Crop not batch-editable → render speakers | SKILL › Graphics | |
| L10 | Window `get_sequence_structure` payloads | SKILL › Workflow 1, 9 | |
| L11 | `list_sequences` end includes caption tracks (2075.907 vs 2075.707) | SKILL › MCP + toolchain | |
| L12 | Both cameras share source in/out → one clip table | SKILL › Workflow 1 | |
| L13 | Sources outside the workspace blocked → Rishi copies them in | SKILL › Safety; Workflow 1 | destination now `inbox_folder` |
| L14 | whisper-cli Metal fails in sandbox → `-ng`; 36 min ≈ 40 min CPU; background | SKILL › Workflow 5 | `-ng` is baked into transcribe.sh |
| L15 | PIL/numpy/soundfile python = `06. Tools/venv-style/bin/python` | SKILL › Paths (`PY`) | |
| L16 | Node/Playwright unusable here; PIL renderer replaces it | reference/WORKFLOW.md › Toolchain notes | dropped from SKILL: non-actionable (the workflow only uses the PIL renderer) |
| L17 | ffmpeg 7 `-/filter_complex file.txt`; long `aselect` fails → atrim+concat | SKILL › MCP + toolchain; reference/WORKFLOW.md | |
| L18 | Avenir Next has no "→"; use words; ×, ÷, −, ≈, “ ” fine | SKILL › Graphics (no →); full list in reference/DESIGN_SYSTEM.md tokens | |
| L19 | Avenir Next.ttc faces 0 Bold, 2 Demi, 5 Medium, 7 Regular | reference/DESIGN_SYSTEM.md › Tokens; engine FACE dict | pointer in SKILL › Graphics |
| L20 | Whisper base mishears jargon (kegs/canning/barrels/"your client") | SKILL › Transcript + captions | |
| L21 | Louder-track speaker labels noisy; smooth before use | SKILL › Transcript + captions | |
| L22 | Cut within 1–2 frames of an edit leaves a sliver; check edit points | SKILL › Cutting; Workflow 6 | **Superseded tool**: `engine/check_slivers.py` never existed → `timeline_map.py --slivers` |
| L23 | Rishi notices abrupt caption breaks, single-word captions, round corners | SKILL › Workflow 12 | |

## Other hard rules (old SKILL / WORKFLOW / DESIGN_SYSTEM / SOUND_DESIGN / engine)
| Rule | Now lives in |
|---|---|
| Connect: `claude mcp list` → `verify_premiere_connection` (cep) → `list_sequences`; names case-insensitive | SKILL › Workflow 1 |
| Intake: sequence, candidate, media folder; panel "Connector running" | SKILL › Workflow 0 |
| `get_sequence_settings` (29.97; sources 1280×720 @ 24) | SKILL › Workflow 1 (fps); full in reference/WORKFLOW.md §1 |
| `clips` from A1 `[start, end, source_in]`; `absent` spans | SKILL › Workflow 1 |
| `crop_x` = 760×720 crop, face centred, from an ffmpeg still at 100 s | SKILL › Workflow 1 (still cmd in reference/WORKFLOW.md §1) |
| Noise-floor check (10 ms RMS percentiles) | SKILL › Workflow 2 |
| Ripple params `scope: sync_locked`, `range_content: delete`, check `trackCounts`; new end = old end − removed | SKILL › Workflow 4 |
| Whisper progress = last timestamp ÷ length | SKILL › Workflow 5; grep line in reference/WORKFLOW.md §5 |
| Self-assessment: orange marker at the join; add range to `extra_cuts_after_silence` | SKILL › Workflow 6 |
| Copy transcript via `--from … --remove a b` | SKILL › Workflow 7 |
| `create_caption_track` (`item_id`, `caption_format: subtitle`, `start_seconds: 0`) → "committed_unverified", ask Rishi | SKILL › Workflow 7 |
| Graphics plan in the media folder, no stop; usual chapters | SKILL › Workflow 8 |
| board_beer_case.py is hard-coded; copy + adapt per case, don't refactor | SKILL › Workflow 9 (new explicit note); engine header comment |
| speakers.py ~10 min per 11 min | SKILL › Workflow 9 |
| Composite ffmpeg hstack command (crf 16, preset medium, yuv420p, 30000/1001) | reference/WORKFLOW.md §9.5 (pointer in SKILL › Workflow 9) |
| Stills check: missing glyphs, overlaps, clipped labels | SKILL › Workflow 9 |
| Voice LUFS via ebur128; `sfx_mg.py … <voice_lufs>` | SKILL › Workflow 9; Sound |
| Overwrite at 0: V6 (`track_index` 5), A3 (`audio_track_index` 2); verify windowed | SKILL › Workflow 9 |
| Full render ≈ 15 min encode; overwrite replaces pilot | SKILL › Workflow 11 |
| Hand-over: lengths, no slivers, markers, file list, Cmd+S, captions default bottom-centre | SKILL › Workflow 12 |
| SFX: phone check, move whole stem in 2 dB steps | SKILL › Workflow 10 |
| SFX levels assume −15 LUFS program; offset = voice_lufs − (−15) (−28.9 → −13.9 dB) | SKILL › Sound |
| SFX: peak aligned to visual; 110 ms louder-wins; lots of sound, each quiet | SKILL › Sound; reference/SOUND_DESIGN.md |
| SFX trigger map + per-event levels; tab click +0.19 s; 131 cues / −29.9 dBFS peak (first case) | reference/SOUND_DESIGN.md (and engine/sfx_mg.py) |
| Layout pixels, caption band y 910–1070, tokens/hex colours, components G1–G14 | SKILL › Graphics (band, 70/30); rest reference/DESIGN_SYSTEM.md |
| Motion: 220 ms rise 8 px, bars 500 ms, count-up 60 %→value 450 ms, 250 ms fade; persistent elements; feedback clears card | reference/DESIGN_SYSTEM.md › Motion |
| Beat grammar + quiet zones | reference/DESIGN_SYSTEM.md (SKILL › Workflow 8 points there) |
| Old SKILL "Read DECISIONS first — they win over everything" | **Superseded** by SKILL.md being the single authoritative read (decisions compiled into it) |
| New: Model gate, Learning loop, close-out with finalize_reel.sh | SKILL › Model gate, Learning loop, Workflow 13 |

## Conflicts resolved
1. **Silence cut vs "original untouched".** WORKFLOW cut silence directly on the named sequence (M2 lists `<seq>` as the silence-cut stage) but the hand-over checklist said "original untouched", and M2's intent is "previous stage stays safe". Resolution: step 4 first duplicates the named sequence as "<seq> RAW" (untouched backup), then cuts the named sequence as before. Stage names M2 → unchanged. *Flag for Rishi: veto if he doesn't want the extra sequence.*
2. **Output folder.** M3/M13/L13 say `inbox/<case>/`; the engine (later) writes to `case.json` `inbox_folder`, now `03. Projects/Mock Case Interview/<case folder>`. Script behaviour wins.
3. **Sliver check tool.** L22 names `engine/check_slivers.py` (never existed); WORKFLOW (later) uses `timeline_map.py --slivers`. WORKFLOW wins.
4. **Corrected-words filename.** WORKFLOW 7.3 used `P/fixed_words.json`, but 9.2 and board_beer_case.py read `P/words.json`. Resolution: `fix_words.py` writes `P/words.json` directly and captions read it (no code change).
5. **Pilot length.** v1.0 SKILL "~first 10 min", WORKFLOW 9.3 "(seconds; ~10 s)", M6 "~first 10–11 min, chapters 1–4". M6 wins; "~10 s" read as render time.
6. **Captions "stay whole".** M15 "7–8-word sentences stay whole" vs captions.py "4–8"; compatible — compiled as "≤ 8-word sentences stay whole" (1–3-word ones still join the next).
7. **Stale paths.** "Consulting case reel edit" → `01. Styles/Consulting Case`; `Daniel Presley Editing Style/` → `09. Archive/Unused Styles/…`; `projects/`, `inbox/` → new layout; reel pack MOTION_LIBRARY → `01. Styles/Consulting Case/MOTION_LIBRARY.md`.
