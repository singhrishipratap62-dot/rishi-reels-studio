# DECISIONS — Rishi's rules for mock case edits
> **History (archived 2026-11-11).** Every rule below is compiled into `../SKILL.md` or `../reference/`; see `RULE_AUDIT.md`. Do not edit rules here — change SKILL.md. Paths updated to the new studio layout (old `inbox/<case>/` = the case media folder, `case.json` `inbox_folder`).

Set during the 4 Nov 2026 edit (beer client: kegs vs canning; Kashish × Aditya). These outrank estimates and defaults.

## Scope & safety
- [M1] Work only on the named sequence. Never modify other sequences, bins or project items. New items we create (copies, imported SRTs/renders) are fine.
- [M2] Every major stage happens on a **new duplicate** so the previous stage stays safe:
  `<seq>` (silence-cut) → `<seq> Copy` (self-assessment removed, captions) → `<seq> MG` (motion graphics).
- [M3] Everything stays inside the workspace. If the sources live elsewhere, give Rishi the exact `cp` command to copy them into the case media folder (`case.json` `inbox_folder`, e.g. `03. Projects/Mock Case Interview/<case folder>/`).
- [M4] Never use Premiere's transcript/text-based editing for cutting. Audio-based detection only.

## Approval stops (only these two)
- [M5] **Silence report** before cutting: number of pauses, total time removed, the 10 longest with timecodes, estimated cut time.
- [M6] **Pilot chapter** of the motion graphics (~first 10–11 min, chapters 1–4) before rendering the full length.
- Everything else runs without asking (graphics plan, self-assessment cut, captions) — report after.

## Cutting
- [M7] Silence = BOTH speakers silent (A1 and A2 each below threshold). A track with no clip counts as silent. Threshold set from each track's noise floor (−50 dB worked: floors −70/−77, speech −25/−35).
- [M8] Remove pauses > 1.0 s; keep 0.12 s padding each side (0.1–0.15 allowed); merge pauses < 0.3 s apart into one cut; all tracks cut together (sync).
- [M9] Batch where possible (≤ 50 ranges/call), process batches from the END of the timeline to the start.
- [M10] Red markers on the 5 longest removed pauses (name "Pause N.Ns", comment = original times).
- [M11] **Always remove the self-assessment**: from the interviewer's "How do you think you did?" to the end of the candidate's self-assessment. Resume on the interviewer's feedback. Trim reaction words that only made sense as a reply (e.g. "Got it. Cool. I mean, sir,") so it reads "…Thank you so much. | I think you did well…". Cut at the quietest 10 ms near word onsets.
- [M12] After any cut, check for clips ≤ 2 frames anywhere on the timeline and remove them (a 1-frame sliver appeared at a join last time).

## Transcript & captions
- [M13] Transcript = word-level, millisecond timestamps, speaker per word; JSON + CSV + SRT, saved in the case media folder (`inbox_folder`). Derive later versions by removing/shifting words — don't re-run Whisper.
- [M14] Captions are a **Premiere caption track** (Subtitle), not graphics.
- [M15] Captions: 4–8 words; never 1–3 words; a sentence end always ends a caption and a new sentence starts a new caption. Short replies (1–3 words: "Sure.", "Cool.", "OK.") join the START of the next sentence. 7–8-word sentences stay whole; longer ones split 4–6 at commas / "and/so/which", never after weak words ("I would", "the", "to").
- [M16] Proofread captions with case logic (kegs not "cakes", canning not "casing/scanning", barrels not "batteries", numbers must add up). Log every change in a corrections CSV; flag guesses for Rishi.

## Motion graphics
- [M17] Layout 16:9: left 70 % (0–1344 px) = graphics; right 30 % = speakers stacked — interviewer top, candidate bottom.
- [M18] Visual language = the `01. Styles/Consulting Case` board (white card, lavender bg, navy Avenir Next, element appears on the word that says it) — adapted to 16:9.
- [M19] Corners: **subtle**. Rectangles with small radii (card 12, boxes/chips 8, pills/tabs/name labels 6, speaker cards 10). Never pill-round or very rounded.
- [M20] Name labels on speaker cards: "Kashish · Interviewer", "<Name> · Candidate".
- [M21] Sound design is required for every motion-graphic event (Minimal Edit sound rules — sound only, never its visuals). Captions are silent. SFX go on their own audio track.
- [M22] Daniel Priestley reference (`09. Archive/Unused Styles/Daniel Presley Editing Style/` pack): calm, premium, one idea at a time — use as taste guidance, not a layout to copy.
- [M23] The graphics are a rendered video placed on a new top video track via overwrite; the original tracks stay underneath untouched.

## Open (decide next time / ask if it matters)
- Caption placement/style (default bottom-centre can touch the candidate card; Rishi will decide).
- gradnext logo: the board header currently uses typeset "gradnext"; Rishi may supply the correct logo file (or use "Gradnext logo - Blue (2).png" from the project).
- Active-speaker glow on the speaker cards (not built yet).
