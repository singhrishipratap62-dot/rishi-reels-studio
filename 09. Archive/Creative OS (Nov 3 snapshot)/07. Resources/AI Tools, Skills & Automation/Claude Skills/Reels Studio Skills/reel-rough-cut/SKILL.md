---
name: reel-rough-cut
description: Turn a raw talking-head clip in inbox/ into a silence-trimmed rough cut plus transcript. Use when the user says rough cut, remove silences, tighten, or drops new footage.
---
1. Pick the file in `inbox/` (ask if several). Choose a REEL_ID per CLAUDE.md; `mkdir -p projects/$REEL_ID`.
2. Inspect: `mediainfo --Inform="Video;%Width%x%Height% %FrameRate%fps %Duration/String%" <file>`.
3. Cut silences: `auto-editor <file> --margin 0.15s --no-open -o projects/$REEL_ID/roughcut.mp4`.
4. Transcribe: `ffmpeg -y -i projects/$REEL_ID/roughcut.mp4 -ar 16000 -ac 1 projects/$REEL_ID/audio.wav` then
   `whisper-cli -m tools/models/ggml-base.bin -l auto -osrt -otxt -of projects/$REEL_ID/transcript -f projects/$REEL_ID/audio.wav`.
5. Delete `audio.wav` (disk is tight). Report before/after duration and the transcript path.
