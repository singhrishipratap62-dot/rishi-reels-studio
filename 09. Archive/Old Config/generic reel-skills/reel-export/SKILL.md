---
name: reel-export
description: Export a finished reel to platform spec (IG Reels / YouTube Shorts) into exports/. Use for export, render, final, deliver.
---
1. Check free disk (`df -h ~`) first; warn if under 2 GB.
2. Input: newest of `captioned.mp4` / `roughcut.mp4` in `projects/$REEL_ID/`.
3. Render 9:16 1080x1920 30fps with loudness normalized to -14 LUFS:
   `ffmpeg -y -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,fps=30" -af loudnorm=I=-14:TP=-1:LRA=11 -c:v libx264 -profile:v high -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart exports/$REEL_ID.mp4`.
4. Verify with ffprobe (resolution, fps, duration) and report file size.
