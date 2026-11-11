#!/bin/bash
# one.sh <Vdir>
S=/private/tmp/claude-501/-Users-rishi-Documents-Teaching-Claude-DIff-Acc-Rishi-s-Editing-Style/bc3958f7-98ee-4846-bf12-9dd023d4f683/scratchpad
T="/Users/rishi/Documents/Teaching Claude/DIff Acc/tools"; PY="$T/venv-style/bin/python"
d=$1; cd $d
"$PY" -I $S/bin/motion.py src.mp4 motion.csv
"$PY" -I $S/bin/sheets.py src.mp4 sheets 2
ffmpeg -v error -i src.mp4 -ac 1 -ar 16000 a16.wav -y
ffmpeg -v error -i src.mp4 -ac 1 -ar 22050 a22.wav -y
bash "$T/style_extract.sh" src.mp4 . >/dev/null
"$PY" -I "$T/style_audio.py" a22.wav frames.log audio.json 2>/dev/null
whisper-cli -ng -m "$T/models/ggml-base.bin" -l auto -ml 1 -sow -ojf -oj -osrt -of words -f a16.wav >/dev/null 2>&1
whisper-cli -ng -m "$T/models/ggml-base.bin" -l auto -otxt -osrt -of sent -f a16.wav >/dev/null 2>&1
echo "done $d"
