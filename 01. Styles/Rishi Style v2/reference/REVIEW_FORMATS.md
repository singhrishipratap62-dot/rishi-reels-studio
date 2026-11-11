# Review formats: how Rishi reviews

> Rishi reviews visually, in local HTML files he opens in a browser. Never Claude artifacts, never long chat tables. Templates: the pack's `templates/options_board.html`, `templates/storyboard.html` (copy them; edit the data arrays at the bottom).

## Common rules
- Self-contained HTML in `03. Projects/Rishi Style v2/<Video N>/storyboard/<name>_vN/`, with `stills/` beside it (extract with ffmpeg at 360 px wide).
- Phone-frame mock-ups (9:16, rounded 10–12 px), built with CSS container units (`cqw`) so they scale. Use real stills and real logos (the pack's `assets/logos/`; the templates' `../../assets/logos/...` paths must be retargeted to wherever the board can reach them).
- Fonts via Google Fonts: Inter + Playfair Display (italic 700) + Caveat (only if needed).
- Header: title, one-line instruction, a sticky **Copy my picks** button (copies to the clipboard and also shows the text below as a fallback), and **Download picks .txt** on options boards.
- Every option has **Keep / Maybe / No** (toggle) + a per-section **notes** textarea. Save state in `localStorage`, wrapped in try/catch.
- Mark one option per section "my pick".
- Check the page in headless Chromium before handing it over:
  - run `node --check` on the extracted script (an apostrophe inside a JS string once broke a whole page);
  - take a screenshot;
  - save a PNG snapshot next to the HTML.

## Options board (stage 1)
- Sections = frame types; **5 options each** (10 sections × 5 = 50 frames is normal).
- Each option card shows:
  - the letter;
  - a source tag (Minimal / Rishi / Presley / Paper Stage / Draft N);
  - a name (≤6 words);
  - a description (1–2 lines);
  - a motion line (durations, eases);
  - buttons.
- Intro boxes at the top: how to use, sources mixed, what's fixed either way.
- Picks summary format (what Rishi pastes back):
  ```
  roughcut_v3 options board v2: my picks
  1 · Hook …
    B KEEP: Footage shrinks into the chat
    note: …
  ```

## Storyboard (stage 2 and after each feedback round)
- Top: a feedback checklist (F1…Fn) + an **assumptions box** (tell me if wrong).
- Per beat:
  - the "Draft N" still;
  - the drawn "Draft N+1" frame;
  - the time range;
  - the line spoken;
  - bullets of exact changes with timings and F-tags.
- For ambiguous motion: **frame strips** at 0.00 / 0.15 / 0.30 / 0.50 / 0.72 s (or the relevant times), 5 interpretations.
- For A/B layout questions (e.g. captions above vs below): two options side by side with Keep / Maybe / No.
- Mock-ups are sketches. Say so where they differ from the build (e.g. "the real build uses the body matte"), because Rishi reads them literally (he flagged a drawn oval gap and a black bar).

## Reports in chat
- Paths to files, what changed, what was checked, what's still open, what to decide.
- Name the timestamps he should look at.

## v2.1 rules (Style Lab, 2026-11-09)
- Options boards **re-offer every option Rishi already liked** for that frame type (see SCENE_LIBRARY v2.1 pools), Keeps first, even past 5; new ideas after them.
- Motion options are best reviewed as **looping animated tiles** (CSS keyframes, click to replay; template: `<studio root>/03. Projects/Rishi Style v2/style_lab_v1/index.html`).
