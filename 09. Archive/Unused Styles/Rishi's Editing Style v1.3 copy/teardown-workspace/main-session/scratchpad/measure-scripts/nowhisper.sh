#!/bin/bash
S=/private/tmp/claude-501/-Users-rishi-Documents-Teaching-Claude-DIff-Acc-Rishi-s-Editing-Style/bc3958f7-98ee-4846-bf12-9dd023d4f683/scratchpad
T="/Users/rishi/Documents/Teaching Claude/DIff Acc/tools"; PY="$T/venv-style/bin/python"
cd $S/ref/$1
[ -s motion.csv ] || "$PY" -I $S/bin/motion.py src.mp4 motion.csv
[ -d sheets ] && [ "$(ls sheets|wc -l)" -gt 0 ] || "$PY" -I $S/bin/sheets.py src.mp4 sheets 2
[ -f a16.wav ] || ffmpeg -v error -i src.mp4 -ac 1 -ar 16000 a16.wav -y
[ -f a22.wav ] || ffmpeg -v error -i src.mp4 -ac 1 -ar 22050 a22.wav -y
[ -f frames.log ] || bash "$T/style_extract.sh" src.mp4 . >/dev/null
[ -s audio.json ] || "$PY" -I "$T/style_audio.py" a22.wav frames.log audio.json >/dev/null 2>&1
"$PY" -I $S/bin/events.py motion.csv > events.md; mkdir -p work
echo "prep $1"
