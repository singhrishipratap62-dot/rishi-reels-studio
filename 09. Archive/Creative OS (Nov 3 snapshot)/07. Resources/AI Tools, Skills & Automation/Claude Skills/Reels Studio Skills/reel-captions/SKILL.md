---
name: reel-captions
description: Create styled captions from a reel transcript and burn them in with ffmpeg. Use for captions, subtitles, or text on a reel.
---
1. Need `projects/$REEL_ID/transcript.srt` (run reel-rough-cut first if missing). Fix obvious transcription errors with the user.
2. Re-chunk to 2–4 words per cue (style in CLAUDE.md). Write `captions.srt`.
3. Burn in: `ffmpeg -y -i roughcut.mp4 -vf "subtitles=captions.srt:force_style='FontName=Montserrat Black,FontSize=14,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=180'" -c:a copy captioned.mp4`.
4. Grab a frame (`ffmpeg -ss 3 -i captioned.mp4 -frames:v 1 check.png`) and view it to verify placement.
