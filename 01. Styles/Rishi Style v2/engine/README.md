# engine/: a helping hand, not a rulebook

Everything here is **proven code from roughcut_v3 draft 4**. Use it to avoid rebuilding solved problems (caption layout, smooth reveals, behind-head mattes, cue mixing). **Nothing is rigid:** retime, drop, rewrite or replace any scene for a new video, and Rishi's per-video feedback always wins.

Verified 2026-11-09: `build_template.py` with the roughcut_v3 config reproduces draft 4's `editable.json` and `edits.json` byte-for-byte.

## Files
| file | what it is |
|---|---|
| `lib.py` | Small builder over Tesseract editable JSON: rect/text/image/shape/group/video layers, keyframes, JS animators, blur (always with `layerSize`), `save()` |
| `build_template.py` | The whole draft 4 edit as one regenerable script: CONFIG block, 9 scene blocks (`# B1` hook … `# B9` CTA), A-roll motion JS (punch-ins, B&W nose-track, split reframing, cut-hiding zoom), caption system (all 5 modes), sound cue system + cue sheet |
| `tools/srt_remap.py` | Original-recording SRT → rough-cut SRT (spectral audio matching, auto-detects kept segments, warns on chunks that straddle cuts) |
| `tools/roman_captions.py` | Rough-cut SRT + romanisation map → word timings JSON (+ readable caption SRT) |
| `tools/face_track.py` (+ YuNet model) | Face/chin/nose track → `<video>.face.json` (nose drives the B&W tracking beat) |
| `tools/sfx_prep.py` | Measures peak level/time of SFX WAVs → `sfx_meta.json` |
| `tools/fx_check.py` | Effects-only render + ±60 ms cue check; `--mp3` writes SFX-only and voice-only MP3s |

Person matte (behind-the-head): `02. Shared Core/engine/matte/matte.py` (RVM). See `../reference/DEPTH_AND_MATTE.md`.

## Starting a new edit (typical)
`<studio root>` = the folder with `.studio-root` (`/Users/rishi/Documents/Teaching Claude`). Intake files (cut, SRT, `roman_map.json`, words, face track, matte) can live in `<Video N>/` or in the edit folder; point CONFIG at them (CONFIG paths are relative to `.tesseract-work/`).
```sh
S="<studio root>"; P="$S/01. Styles/Rishi Style v2"; PY="$S/06. Tools/venv-style/bin/python"   # venv has numpy, opencv-python-headless, fonttools, torch
T="$HOME/Library/Application Support/Tesseract/bin/tsrct"
EDIT="$S/03. Projects/Rishi Style v2/<Video N>/<name>_edit_v1"; mkdir "$EDIT" && cd "$EDIT" && mkdir -p .tesseract-work fonts sfx Previews
"$PY" "$P/engine/tools/srt_remap.py" original.mp4 roughcut.mp4 original.srt roughcut.srt
"$PY" "$P/engine/tools/roman_captions.py" roughcut.srt roman_map.json words.json captions_roman.srt
"$PY" "$P/engine/tools/face_track.py" roughcut.mp4
"$PY" -I "$S/02. Shared Core/engine/matte/matte.py" roughcut.mp4 matte.mp4      # only if a behind-head scene is planned
cp "$P/assets/sfx/"*.wav sfx/ ; cp "$P/assets/sfx/sfx_meta.json" .tesseract-work/
# fonts: Inter 300-700 + Playfair Display 500/700 italic TTFs (fontsource latin TTFs) → fonts/
#   (a ready set: cp "$S/03. Projects/Rishi Style v2/video 5/vid5_edit_v1/fonts/"*.ttf fonts/ ; build_template.py expects these exact filenames)
"$T" project create --project p.tsrct ; "$T" project import-video --project p.tsrct --file roughcut.mp4 --asset-id aroll
# import matte (asset-id matte), fonts, logos (logo-claude, logo-github-k, logo-github-w, …), avatar2, every sfx (asset-id sfx-<name>)
cp p.tsrct .tesseract-work/base.tsrct ; "$T" project checkout --project p.tsrct --output .tesseract-work/editable.orig.json
cp "$P/engine/lib.py" "$P/engine/build_template.py" .tesseract-work/   # then edit CONFIG + scene blocks
cd .tesseract-work && "$PY" build_template.py && cd ..
cp .tesseract-work/base.tsrct p.tsrct && "$T" project commit --project p.tsrct --file .tesseract-work/editable.json && "$T" project apply --project p.tsrct --actions .tesseract-work/edits.json
"$T" filmstrip ... ; "$T" export --project p.tsrct --output <name>_draft1.mp4     # 1080p default; never --resolution 720p
"$PY" "$P/engine/tools/fx_check.py" . p.tsrct .tesseract-work/base.tsrct --mp3  # effects-only ±60 ms check (+ SFX-only / voice-only MP3s)
```
Python needs `numpy`, `opencv-python-headless` (face track) and `fonttools` (caption widths): all present in `06. Tools/venv-style`.
`build_template.py` encodes draft 4 (v2.0). The v2.1 upgrades (soft caption exit C-out, lower support line at hero + 0.55 × support size, R01+/R02+/R03+, motion blur on big moves) are not in it yet: add them per video (see `../reference/MOTION_LIBRARY.md`, `../reference/CAPTION_SYSTEM.md`).

## Asset ids the template expects
`aroll`, `matte`, `logo-claude`, `logo-github-k`, `logo-github-w`, `avatar2`, `sfx-<name>` for every file in `assets/sfx/` plus `sfx-voice` (the voice WAV: rough-cut audio, 75 Hz HPF, −1.5 dB).
