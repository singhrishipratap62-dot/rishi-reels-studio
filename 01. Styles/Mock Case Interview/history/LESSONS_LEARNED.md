# LESSONS_LEARNED — what cost time on the first mock case (4 Nov 2026)
> **History (archived 2026-11-11).** Every rule below is compiled into `../SKILL.md` or `../reference/`; see `RULE_AUDIT.md`. Do not edit rules here — change SKILL.md. Paths updated to the new studio layout (old `inbox/<case>/` = the case media folder, `case.json` `inbox_folder`).


## Premiere MCP (premiere-pro-mcp-leancoderkavy, CEP backend)
- [L1] `ripple_remove_timeline_ranges` says "integer frame rates only" but **worked on 29.97** (it frame-snaps ranges). Always dry-run first; the dry run returns a single-use `confirmation_token`.
- [L2] If more than 400 clips move, the apply is refused and **the token is consumed** — re-run the dry run WITH `allow_large_ripple: true`, then apply with the new token. Always pass `allow_large_ripple: true` on mock cases (11 video+audio tracks → hundreds of clips).
- [L3] The sequence must be **active** for ripple edits (QE). `set_active_sequence` after `duplicate_sequence`.
- [L4] `duplicate_sequence` names the copy "<name> Copy". `rename_project_item` by **name** works; by sequence ID returned "Item not found" and triggered a recovery lock.
- [L5] Any failed/uncertain call → `HOST_RECOVERY_REQUIRED`. Fix: `inspect_operation_recovery` (output is huge, gets saved to a file; read `recoveryRevision` + `hostStateRevision` with python — that file needs the sandbox disabled to read) → `acknowledge_operation_recovery` with both revisions.
- [L6] `export_frame` failed ("QE wrote no file") and caused a recovery lock. Don't use it; grab stills with ffmpeg from the source/render instead.
- [L7] `add_to_timeline` **inserts** (ripples all sync-locked tracks). Use `overwrite_clip` (video: `track_index`; audio-only: `audio_track_index`).
- [L8] Captions: `create_caption_track` works but readback is unavailable ("committed_unverified"); the MCP **cannot delete caption tracks** (`delete_track` is video/audio only). Every re-import adds another track → tell Rishi which to delete by its first caption text. Prefer getting captions right before importing.
- [L9] `nest_clips` is unavailable on CEP. Per-clip third-party effects (Rounded Crop) can't be batch-edited → re-layout speakers by rendering, not by editing 266 clips.
- [L10] `get_sequence_structure` payloads are big: use `start_seconds/end_seconds`, `track_type`, `track_index` windows.
- [L11] Sequence end shown by `list_sequences` includes caption tracks (copy showed 2075.907 vs 2075.707 video).
- [L12] Both cameras shared identical source in/out points (synced recordings) → one clip table maps both.

## Sandbox / tooling
- [L13] Sources outside the workspace are blocked (and forbidden by CLAUDE.md) → Rishi copies them into the case media folder (`inbox_folder`).
- [L14] whisper-cli crashes on Metal inside the sandbox ("failed to allocate buffer") → run with `-ng` (CPU). 36 min of audio ≈ 40 min on CPU with ggml-base. Run in background; ping Rishi.
- [L15] Python with PIL + numpy + soundfile: `06. Tools/venv-style/bin/python`. System python has no PIL/numpy.
- [L16] Node/Playwright (reel engine) depends on caches outside the workspace → not usable here; the PIL board renderer replaces it.
- [L17] ffmpeg 7 uses `-/filter_complex file.txt` (not `-filter_complex_script`). Very long `aselect` expressions fail — use atrim+concat segments.
- [L18] Avenir Next has no "→" glyph (renders a box). Use words ("=", "to", "&", ":") instead. ×, ÷, −, ≈, “ ” are fine.
- [L19] Avenir Next.ttc faces: 0 Bold, 2 Demi Bold, 5 Medium, 7 Regular.

## Editorial
- [L20] Whisper base mishears case jargon badly (kegs→cakes, canning→casing/scanning/calving, barrels→batteries/battles/balance, "your client"→"Yog Lion"). Budget a proofreading pass with case arithmetic.
- [L21] Speaker labels from "which track is louder" are noisy on single words; smooth before using them for captions or active-speaker effects.
- [L22] A cut that starts within 1–2 frames of an existing edit leaves a sliver clip — compute all edit points and check (`engine/timeline_map.py --slivers`; check_slivers.py never existed).
- [L23] Rishi notices: abrupt caption breaks ("next?" at the start of a caption), single-word captions, overly round corners. Check these before handing over.
