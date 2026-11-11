# Reels Studio (isolated Claude Code workspace)

## Folder rules
- Everything stays inside this folder. Never read or write outside it.
- Raw footage → `inbox/`. Working files → `projects/<REEL_ID>/`. Final renders → `exports/`.
- Reusable assets live in `assets/` (sfx, stickers, luts, fonts, music).
- Helper scripts go in `tools/`. Whisper model: `tools/models/ggml-base.bin`.

## Naming
- Reel ID: `R###_topic_YYYY-MM-DD` (e.g. `R012_resume-tips_2026-11-02`).

## Toolchain
- ffmpeg / ffprobe, mediainfo: inspect + encode
- auto-editor: silence removal (`auto-editor in.mp4 --margin 0.15s -o out.mp4`)
- whisper-cli (whisper.cpp): transcripts/captions; content is often Hindi/Hinglish, use `-l auto`
- magick (ImageMagick): stickers/thumbnails
- yt-dlp: reference downloads
- Premiere Pro via the `premiere-pro` MCP server (call verify_premiere_connection first)

## Default export spec
- 9:16, 1080x1920, 30fps, H.264 High, CRF 18, AAC 192k, -14 LUFS loudness

## Style (edit me)
- Captions: bold, 2–4 words per line, centered lower third, safe zone above IG UI.
- Pacing: tight cuts, no pauses > 0.3s.
