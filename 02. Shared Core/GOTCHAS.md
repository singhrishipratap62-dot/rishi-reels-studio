# Environment gotchas (all styles)

These are lessons each style learned separately, collected here so they're learned once. Read the section for the tool you're about to use. Style-specific build quirks stay in that style's `reference/` docs.

## Sandbox (Claude Code)
- **Metal is blocked.** `whisper-cli` aborts ("failed to allocate Metal buffer"). Always pass `-ng` (CPU); the consulting engine does this with `WHISPER_NG=1`.
- **VideoToolbox is blocked.** `h264_videotoolbox` fails with -12908. Encoding scripts (consulting `cut.py`, `render.js`, `compose.sh`, `speed_music.sh`, `run_build.sh`) and the Tesseract CLI (`~/Library/Application Support/Tesseract/bin/tsrct`) must run **outside the sandbox**.
- `npx` and node from `~/.nvm` can't be read inside the sandbox either.
- **Headless Chrome / Playwright:**
  - `render.js` loads playwright-core from `~/.npm/_npx/9833c18b2d85bc59/` and Chrome from `~/Library/Caches/ms-playwright`.
  - Screenshots hang at random, so keep the 4 s timeout and retries.
  - Never pipe Playwright frames straight into ffmpeg; that once produced a silently truncated reel.

## Paths
- Folder names contain spaces ("03. Projects", "06. Tools"), so quote every path in shell.
- Scripts find the studio root by walking up to `.studio-root` (snippet in `STUDIO.md`). Don't hard-code `../../` jumps across top-level folders.
- `ffmpeg-full` (`/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg`) is needed for libass captions. Scripts hard-code it.
- Node v24.19.0 is put on PATH by the consulting `run_build.sh` (`~/.nvm/versions/node/v24.19.0/bin`).

## Transcription
- **whisper.cpp (ggml-base at `06. Tools/models/ggml-base.bin`):**
  - Timestamps drift about 1 s on long files, and `-dtw` does nothing.
  - Parallel jobs sometimes drop an output.
  - Hinglish needs `-l auto`.
- **mlx-whisper turbo** (used in Minimal Edit) gives better word timings. Snap word edges to `silencedetect` (−35 dB / 120 ms) and flag words below 0.7 confidence.
- Rishi v2 raw videos come without an SRT, and that pack has no transcription tool. Ask Rishi which route to use.
- **Devanagari SRTs** use precomposed nukta letters (U+095B), so compare with NFD. Put caption-mode boundaries slightly before word starts.

## Audio (Claude can't listen; measure everything)
- Check with `ffmpeg -af ebur128=peak=true` on the **final MP4**, not on stems. Pause trims add about 3 dB.
- AAC raises true peak by 0.3–0.5 dB, so limit with 4x oversampling.
- Convert MP3 SFX to 48 kHz WAV before importing.
- **Measure each SFX file's peak inside its trimmed window.** A peak value reused from another edit was once 8 dB off.
- Library SFX peak near 0 dBFS; procedural ones sit at −12.
- Rishi does the final listening check on his phone.

## ffmpeg traps
- `gblur` needs `sigmaV` sent along with `sigma`.
- `scale eval=frame` + `crop` zooms wobble; do sub-pixel zooms in PIL.
- Converting fps per segment loses about 0.5 s; pad with `tpad`.
- Check renders with `blackdetect=d=0.1:pix_th=0.05`, and check duration against the cut.

## Tesseract CLI 0.4.0 (Rishi v2, Minimal, IG, Before-After)
- **Building:**
  - Always rebuild from a clean `base.tsrct`.
  - Export defaults to 1080p; never pass `--resolution 720p`.
- **Layers and masks:**
  - Children added with `append` land under the background; use `prepend`.
  - Keyframes on a nested Video don't stick: wrap the Video in a Group and animate the Group.
  - Every `gaussianBlur` needs `layerSize: [1080, 1920]` and `repeatEdgePixels: false`.
  - Shape fill opacity goes in `fills[0].opacity`; colour alpha is ignored. `cornerRadius` is a fraction of the half-side (about 0.12 for cards).
  - Mask `cornerRadius` is ignored, so draw Bézier corners. Mask ids must be unique.
  - `source.cropRect` does nothing; use scale + position + mask.
- **Keyframes and timing:**
  - Duplicate keyframe times are rejected.
  - A second `setFxPropertyKeyframes` call on the same property replaces the first.
  - `positionY` keys alone are rejected; send X and Y together.
  - Keyframe `layerTime` is local to the layer. Video keys run on the source clock.
  - `playback.mapping.input.start` must equal `inputRange.start`.
  - Write `t-(-0.05)`, not `t--0.05`.
  - A negative activeRange breaks the whole batch.
- **Audio:**
  - There is no action to create audio layers; use editable JSON + `project commit`.
  - Picture copies of a Video carry audio, which doubles the voice; omit `volume` on them.
- **Matte, text and effects:**
  - Built-in `personMatte` can come back empty. Use `02. Shared Core/engine/matte/matte.py` (RVM; `--ds` 0.25 for 1080×1920) or a MediaPipe matte as a `lumaInverted` track matte.
  - Point text wraps above about 900 px wide.
  - Grain at 0.25 is invisible; use 0.8 on light grounds and 1.0 on dark.
  - Fontsource latin TTFs lack ✓ ↑ ●, so draw them as shapes. Fonts must be imported (`import-font`); system fonts aren't seen.
- The browser editor needs the File System Access API (Chrome; it's off by default in Brave).

## Premiere Pro (premiere-pro MCP)
- Run `verify_premiere_connection` first. Duplicate the timeline before anything destructive.
- Silence trims leave only about 0.06 s after the last word.

## Machine
- Disk is tight. Each consulting reel needs about 3 GB free while building, and 4K HEVC is about 1.3 GB per 3 min. Run `finalize_reel.sh` after approval.
- Renders slow to about 9 s/frame when the Mac idles; keep it awake (`caffeinate -i`).
- Images pasted into chat never reach disk; ask for a file path.
- Two terminals at once need different R### numbers; claim one with `mkdir`.
