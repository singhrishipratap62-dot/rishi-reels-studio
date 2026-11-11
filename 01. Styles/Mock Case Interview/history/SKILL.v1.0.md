<!-- Archived copy of SKILL.md v1.0 (pre-2026-11-11 restructure). Not a live skill; paths are stale (inbox/ = case media folder). Current: ../SKILL.md -->
---
name: mock-case-interview-edit
description: Edit a gradnext mock case interview (two speakers, two cameras, ~30–45 min) end to end in Premiere Pro via the premiere-pro MCP — silence removal, self-assessment cut, word-level transcript, 4–8-word captions, a 70/30 motion-graphics case board with sound design. Use when Rishi drops a new mock case interview.
---

# Mock case interview edit (v1.0, built on the 4 Nov 2026 beer-client case)

A mock case = Kashish (interviewer) + a candidate, each on their own camera + mic, already laid out in a Premiere sequence (two video tracks + two audio tracks, synced). Output = a cleaned 16:9 long-form edit with a self-building case board on the left 70 % and both speakers stacked on the right 30 %.

## Read first
1. `DECISIONS.md` — Rishi's rules from the first edit. They win over everything else.
2. `LESSONS_LEARNED.md` — MCP + sandbox gotchas that cost time.
3. `WORKFLOW.md` — the exact steps and commands.
4. `DESIGN_SYSTEM.md` (layout, tokens, graphics toolkit) and `SOUND_DESIGN.md`.
5. Engine scripts in `engine/` — reuse, extend, never rewrite from scratch.

## The pipeline (one line each)
1. Connect: `claude mcp list` → `verify_premiere_connection` → `list_sequences`; find the named sequence (names are case-insensitive in practice, e.g. "4 nov-cld").
2. Inspect tracks (`get_sequence_structure`), get both source paths (`find_project_item_by_name`), ask Rishi to copy the sources into `inbox/` (we never read outside the workspace).
3. Silence: per-speaker detection, a pause counts only if BOTH tracks are silent > 1.0 s → **STOP: report** (count, time removed, top-10 pauses, est. time).
4. Cut: batch ripple-remove (≤ 50 ranges/call, end → start, dry run → apply), 0.12 s padding, merge pauses < 0.3 s apart, markers on the 5 longest.
5. Transcript: Whisper word-level on the cut audio (CPU, `-ng`), speaker label per word, JSON/CSV/SRT into the case folder in `inbox/`.
6. Self-assessment: duplicate the sequence → cut from "How do you think you did?" to the start of the interviewer's feedback; trim any reaction words ("Got it. Cool. I mean,") so the join reads clean; remove any 1–2-frame slivers left at cut joins.
7. Derive the copy's transcript (no re-transcription), proofread with case logic, build 4–8-word sentence-aligned captions → caption track.
8. Graphics: plan beats from the transcript (no approval stop), duplicate the timeline → "<name> MG", render board + speakers + SFX → **STOP after the pilot chapter** (~first 10 min) → then render the full length.
9. Hand over: what changed, what to check (lip-sync, captions position, SFX level on phone), Cmd+S reminder.

## Never
- Touch any sequence other than the one named (and the copies we create).
- Use Premiere's transcript/text-based editing for cuts (Rishi: inaccurate).
- Use `add_to_timeline` to place renders (it INSERTS and ripples everything) — use `overwrite_clip`.
- Retry a failed MCP call in a loop; inspect + acknowledge recovery first.
