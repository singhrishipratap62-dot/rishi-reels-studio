---
name: before-after-reel
description: Build Rishi's "Raw vs Opus 5.5" before/after comparison reel in Tesseract from a raw clip, an edited clip, (optionally) a final-audio file and a comment keyword. Use when the user drops raw + edited videos and asks for the before/after, comparison, raw-vs-edited, or "Opus 5.5" reel, or names a keyword like "EDIT" for the caption.
---

# Before/after reel ("Raw" vs "Opus 5.5")

One command turns two synced clips into the approved 9:16 comparison reel: the raw clip
sits in a smaller, desaturated card tilted back on the left, the edited clip plays in the big
front card, and a caption asks viewers to comment a keyword. Everything is a native,
editable Tesseract layer. `assets/approved_look.png` shows the signed-off look.

## What to ask for (nothing else)

1. **Raw video**: the unedited cut. **Edited video**: the finished edit. Both are usually 1080×1920.
2. **Audio file** (optional): use it when the user names one, e.g. a 720p `audio.mp4` that
   holds the final mix. Otherwise the edited video's own audio is used. Only one audio
   source ever plays; both cards are muted.
3. **Keyword** for the caption (e.g. `EDIT`). It is always shown in caps, in quotes, orange and bold.

The three files must share one timeline (same cut, starting together). The script warns if
durations differ. Check that with the user rather than guessing an offset.

## Build

Put the three files in a new project folder `03. Projects/Before-After/R0XX_<topic>_<YYYY-MM-DD>/` (claim the R number with a plain `mkdir`), then run from inside it. Tesseract runs outside the sandbox:

```bash
python3 "<studio root>/01. Styles/Before-After/.claude/skills/before-after-reel/scripts/make_before_after.py" \
  --raw raw.mp4 --edited edited.mp4 --audio audio.mp4 --keyword EDIT \
  --out "Before-After"
```

`--out` must be a new folder; the script refuses to overwrite. It creates the project,
imports the media plus the bundled Inter font, lays out every layer, auto-centres the
caption, and exports. It prints the spec, loudness and preview paths. It takes about 15 s.

Outputs inside `--out`:
- `BeforeAfter_<KEYWORD>.mp4` (deliverable: 1080×1920, 30 fps, H.264 + AAC)
- `BeforeAfter.tsrct` (the editable project; it opens in the Tesseract browser editor)
- `Previews/Layout.png` and `Previews/Export_frames.png` (start/middle/end frames)

## Review before handing over

Open `Previews/Export_frames.png` and compare it with `assets/approved_look.png`. Check:
- Both cards show the right footage, in sync, with no black frames.
- The caption is centred and the keyword reads correctly.
- The reported loudness roughly matches the source mix (the reference mix was about −14 LUFS).
  If the user only supplied raw + edited, say whose audio was used.

Then copy `BeforeAfter_<KEYWORD>.mp4` to `04. Exports/Before-After/R0XX_<topic>_<YYYY-MM-DD>.mp4`, send it to the user (SendUserFile) with a short summary, and once approved run `"06. Tools/finalize_reel.sh" "<project folder>"`.

The whole skill is [SONNET] work: the look is already approved and built into the script.

## Model gate
Check `MODEL_MODE` in the studio root CLAUDE.md, or what Rishi said this session. If it is `opus-only`, skip this section. Otherwise, steps marked [OPUS] (creative planning, storyboard or options, first look-dev of a new scene type, judging QC failures that need taste) need a check: if you are not running on Opus, stop and ask "Next step is creative (<step>). Switch to Opus with /model opus, or continue on Sonnet?" Steps marked [SONNET] (transcribe, cut, captions, building from an approved plan, applying a listed revision, renders, cleanup) run on whatever model is active; if that is Opus, mention once that Sonnet would be cheaper for this stretch.


## The approved style (already encoded in the script; don't re-derive)

- **Canvas:** 1080×1920. Off-white diagonal gradient, a faded peach 11-ray starburst
  (42% opacity) centred behind the cards, and a soft white radial haze.
- **Edited card:** 538×956 at (383, 425), rounded corners, strong soft shadow cast
  down and slightly left onto the raw card. Above it sits a dark gradient pill with an orange
  12-ray starburst icon and **"Opus 5.5"**.
- **Raw card:** 340×604. Its vertical centre is locked to the edited card's centre.
  - **Tilted inward** (`rotationY −16°`): the inner/right edge recedes behind the edited card.
    The user rejected the outward tilt.
  - **"● Raw" pill:** red dot, tilted on the same 3D plane as the card.
  - **Before look:** `primaryGrade` with saturation −0.65, contrast −0.35, blacks +0.35, exposure +0.1.
- **Caption:** Inter Medium 60px, tight tracking, two lines centred at baselines 1484/1560:
  `Follow & comment “KEYWORD”` / `for the full guide`. The keyword is Inter Bold in #E2703F.

## Revision knobs

Re-layout an existing build without re-importing (it re-exports too):

```bash
python3 .claude/skills/before-after-reel/scripts/make_before_after.py --rebuild --out "<folder>" --keyword EDIT [knobs]
```

| Request | Flag (default) |
|---|---|
| More or less tilt on the raw card | `--tilt -16` (more negative = more inward; positive flips it outward, which was rejected) |
| Bigger or smaller raw card (centre stays locked) | `--raw-scale 1.0` (e.g. `1.1`) |
| More or less grey on the raw card | `--saturation -0.65` (−1 = black and white) |
| More or less washed-out look | `--fade 1.0` (0 = no fade, 1.5 = stronger) |
| Different pill labels | `--raw-label Raw`, `--edited-label "Opus 5.5"` |
| Different caption text | `--line1 "Follow & comment "` (keep the trailing space), `--line2 "for the full guide"` |

Always pass `--keyword` again on rebuilds. Before a rebuild, back up the previous MP4 when
the user may want to compare. For changes the flags don't cover (card sizes, positions,
shadows), edit the geometry block in `scripts/make_before_after.py`, rebuild, and look at
`Previews/Layout.png`. Move the pills with their cards; they're derived from card position.

## Tesseract quirks (already handled, relevant when editing the script)

- CLI: `~/Library/Application Support/Tesseract/bin/tsrct`, version 0.4.0. For deeper engine
  work, read the `tesseract-video` skill.
- Rect `rect.position` is the rect's top-left in layer space, not its centre.
- Video `cornerRadius` is not pixels: 0.165 ≈ 30 px on the 538 px card. A value of 22+ turns the card into a pill.
- `primaryGrade` needs every field present (temperature … vibrance) or commit fails.
- 3D `rotationY` renders true perspective. To keep a label on the card's plane, pivot it on the
  card centre (`on_back_plane()`).
- Leave the document `backgroundColor` unset; the browser editor rejects a non-black one.
  The Background layer covers the canvas.
- Caption centring uses a right-justified black run plus a left-justified orange keyword
  meeting at `split_x`. The script measures the rendered line and corrects it automatically.
