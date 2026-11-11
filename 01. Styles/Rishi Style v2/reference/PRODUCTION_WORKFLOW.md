# Production workflow: Rishi v2

> Defaults, not rules. Rishi can skip or reorder stages; follow what he asks for this video.

## Stage 0: intake
- **Inputs from Rishi:**
  - the raw video or the rough cut `03. Projects/Rishi Style v2/<Video N>/<name>.mp4` (Gling or manual);
  - the original recording;
  - the SRT of the **original** (Hindi script, mixed English).
- **Ask up front, only if missing:**
  - which video and its CTA keyword;
  - any brand or product to show (fetch real logos into `assets/logos/`);
  - photos or stickers to use.
- **Raw footage (vid2, vid5):** don't ask about head/tail or silence/unclear-sound trims; cut them yourself (silencedetect + cut on a quiet frame) and report it. But a pause that carries a joke or a beat (vid5: 0.7 s before "wow!") is not dead air: keep it and say which pauses you kept.
- **No SRT supplied:** ask Rishi before choosing a transcription route (this pack has no transcription tool).
- **Remap:** `engine/tools/srt_remap.py`. Note the chunks it flags as straddling cuts. Treat the SRT as a draft; flag mis-heard words that change the meaning.
- **Romanise:** write `roman_map.json` (romanised Hinglish exactly as spoken), then run `roman_captions.py` → `words.json`. Tell Rishi which words near cuts are inferred.
- **Track the face:** `face_track.py` → `<video>.face.json`.
- **Person matte**, if any behind-head scene is likely: see `DEPTH_AND_MATTE.md` (new matte for every cut).

## Stage 1: options board (STOP after)
- One section per **frame type**, i.e. per beat or function: hook, reaction, list, thesis, proof, contrast, explanation, iteration, CTA. Plus a **caption-style** section when it's still open.
- **≥5 options each**, drawn as phone-frame mock-ups over real stills from the rough cut. Sources:
  - the scene recipes in `SCENE_LIBRARY.md`;
  - the option pools at the end of `SCENE_LIBRARY.md`;
  - fresh ideas.
- Each option shows: a source tag, a name, a one-line description, the motion line, and Keep / Maybe / No. Mark one as "my pick".
- Format: `REVIEW_FORMATS.md`. Copy the pack's `templates/options_board.html` to `03. Projects/Rishi Style v2/<Video N>/storyboard/<name>_v1/index.html`.
- Wait for Rishi's "Copy my picks" paste. Expect mixes ("B as baseline + bits of A and C") and build exactly that.

## Stage 2: storyboard
- `templates/storyboard.html` → `storyboard/<name>_vN/`. For each beat: a "before" still, a drawn "after" frame, the changes, the timings, and the F-numbers.
- Put an **assumptions box** at the top for anything ambiguous.
- When an animation idea is unclear, give **≥5 interpretations as 5-frame strips** and let him pick.
- If he said "proceed", start building after sharing it. If he said "storyboard only", stop.

## Stage 3: build (Tesseract)
- **New folder** `03. Projects/Rishi Style v2/<Video N>/<name>_edit_vN/`, claimed with `mkdir` (no `-p`). Never touch earlier drafts.
- Start from `engine/` (lib + build template). Retime and replace scenes freely.
- Build order: captions system → scenes in time order → A-roll motion → sound cues.
- **Review loop:**
  - portrait filmstrips (270×480 tiles) of every changed beat;
  - fix what you see, then re-filmstrip;
  - targeted frame checks for glitches (glyph clipping, gaps, bars).

## Stage 4: feedback rounds
- Split Rishi's (often voice-transcribed) notes into a numbered **F-list**, one item per change, each with a timestamp.
- **Storyboard first** for any non-trivial change, then build the next draft in a new folder.
- Small fixes found during the build (e.g. a layer order bug) can go straight in; mention them in the report.

## Stage 5: sound
- Per `SOUND_DESIGN.md`. Since draft 2, sound has been built with the visuals.
- Always do the effects-only check (`engine/tools/fx_check.py`).

## Stage 6: QC + delivery
- Run `QUALITY_CONTROL.md`.
- Export **1080×1920 / 30 fps** (never 720p) and confirm with `ffprobe`.
- **Deliver, all in the draft folder:**
  - `<name>_draftN.mp4`;
  - the editable `.tsrct`;
  - `Previews/Filmstrip-draftN.jpg`;
  - `sound_cue_sheet.md`;
  - SFX-only and voice-only MP3s on request (`fx_check.py --mp3`).
- **Report:** what changed, what was checked (filmstrips, loudness, cue check, black frames), what wasn't (no listening), and what's still open.
- Append Rishi's notes for the round to `../FEEDBACK_LOG.md` (fold into SKILL.md / reference/ when the reel is approved; see SKILL.md "Learning loop").

## Stage 7: close-out
- After Rishi approves the final export, run `"<studio root>/06. Tools/finalize_reel.sh" "<project folder>"` (deletes only regenerable intermediates after confirming the export exists).

## Rules that apply to every stage
- No Claude artifacts. All review pages are local HTML, plus a PNG snapshot (headless Chromium in the Playwright cache works).
- Timebox side investigations (tools, GUIs) to 2–3 minutes; drop them if undecided.
- Installs, browser flags and new infrastructure: feasibility report → explicit approval → only the approved phase.
- Keep the conversation output short: links to files, what to look at, what to decide.
