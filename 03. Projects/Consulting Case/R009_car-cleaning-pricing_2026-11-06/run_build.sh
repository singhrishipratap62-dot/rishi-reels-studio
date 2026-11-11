#!/bin/bash
# R009 full build (pack v1.4): sound → board + composite (1x) → 1.2x + music (final) → green → 1080p raw → QC.
set -uo pipefail
export PATH=/opt/homebrew/bin:$HOME/.nvm/versions/node/v24.19.0/bin:$PATH
ROOT="/Users/rishi/Documents/Teaching Claude"; cd "$ROOT/03. Projects/Consulting Case"
E="$ROOT/01. Styles/Consulting Case/engine"; P=R009_car-cleaning-pricing_2026-11-06; X="$ROOT/04. Exports/Consulting Case/R009_car-cleaning-pricing_2026-11-06"
BG="$ROOT/05. Asset Library/videos/gradnext-background-loop-9-16.mp4"; F=/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
echo "=== events $(date +%T)"; node "$E/render.js" $P 0 1 --events $P/events.json || { echo "EVENTS FAILED"; exit 1; }
echo "=== sound pass $(date +%T)"; "$ROOT/06. Tools/venv-style/bin/python" "$E/sfx.py" $P "$ROOT/01. Styles/Minimal Edit/sfx" | tail -3 || { echo "SFX FAILED"; exit 1; }
echo "=== compose 1x $(date +%T)"; BGVIDEO="$BG" AUDIO="$PWD/$P/mix.wav" "$E/compose.sh" $P "${X}_1x.mp4" 2>&1 | tr '\r' '\n' | grep -v '^frame=' | tail -8
[ -s "${X}_1x.mp4" ] || { echo "COMPOSE FAILED"; exit 1; }
echo "=== speed + music $(date +%T)"; "$E/speed_music.sh" $P "$X.mp4" "$ROOT/05. Asset Library/music/Background music.mp3" 1.2 15 2>&1 | tr '\r' '\n' | grep -v '^frame=' | tail -2
echo "=== green $(date +%T)"; BGVIDEO="$BG" "$E/compose_green.sh" $P "${X}_green.mp4" 2>&1 | tr '\r' '\n' | grep -v '^frame=' | tail -2
echo "=== raw 1080 $(date +%T)"; $F -v error -y -i $P/cut.mp4 -vf scale=1080:1920:flags=lanczos -c:v libx264 -preset medium -crf 18 -profile:v high -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "${X}_raw.rendering.mp4" && mv -f "${X}_raw.rendering.mp4" "${X}_raw.mp4"
echo "=== QC 1.2x final $(date +%T)"; python3 "$E/qc.py" $P "$X.mp4" 44 1.2
$F -i "$X.mp4" -vf "crop=810:908:136:858,freezedetect=n=0.002:d=1.0" -an -f null - 2>&1 | grep -cE 'freeze_start' | sed 's/^/face freezes >=1s: /'
for f in "$X.mp4" "${X}_1x.mp4" "${X}_green.mp4" "${X}_raw.mp4"; do echo "$(basename "$f"): $(ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=width,height,nb_read_packets -of csv=p=0 "$f") $(du -h "$f" | cut -f1)"; done
df -h / | tail -1; echo "ALL DONE $(date +%T)"
