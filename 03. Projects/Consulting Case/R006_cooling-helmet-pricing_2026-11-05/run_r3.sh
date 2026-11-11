#!/bin/bash
# R006 revision 3: video background loop + header back. Final only.
set -uo pipefail
ROOT="/Users/rishi/Documents/Teaching Claude"; cd "$ROOT/03. Projects/Consulting Case"
E="$ROOT/01. Styles/Consulting Case/engine"; P=R006_cooling-helmet-pricing_2026-11-05; X="$ROOT/04. Exports/Consulting Case/R006_cooling-helmet-pricing_2026-11-05"
BGVIDEO="$ROOT/05. Asset Library/videos/gradnext-background-loop-9-16.mp4" AUDIO="$PWD/$P/mix.wav" "$E/compose.sh" $P "${X}_1x.mp4" || { echo "COMPOSE FAILED"; exit 1; }
"$E/speed_music.sh" $P "$X.mp4" "$ROOT/05. Asset Library/music/Background music.mp3" 1.2 15 2>&1 | tr '\r' '\n' | grep -v '^frame=' | tail -2
echo "=== QC 1.2x final"; python3 "$E/qc.py" $P "$X.mp4" 41 1.2
/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg -i "$X.mp4" -vf "crop=810:908:136:858,freezedetect=n=0.002:d=1.0" -an -f null - 2>&1 | grep -cE 'freeze_start' | sed 's/^/face freezes >=1s: /'
ls -la "${X}_green.mp4" "${X}_raw.mp4" | awk '{print $6,$7,$8}'
echo "ALL DONE"
