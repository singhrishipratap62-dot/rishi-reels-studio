#!/bin/zsh
# Step 5: word-level Whisper on the final timeline's audio. CPU only (-ng): Metal fails inside the sandbox [L14].
# ~36 min audio ≈ 40 min. Run in the background and tell Rishi the ETA.
# usage: transcribe.sh <project_dir>      (needs cut_mix.wav from timeline_map.py --audio)
P="$1"; ROOT="${0:A:h}"; while [ ! -e "$ROOT/.studio-root" ] && [ "$ROOT" != / ]; do ROOT="${ROOT:h}"; done
whisper-cli -m "$ROOT/06. Tools/models/ggml-base.bin" -f "$P/cut_mix.wav" -l auto -ng -ml 1 -sow -ojf -of "$P/whisper_words" -t 8 > "$P/whisper.log" 2>&1
echo "exit $?"; grep -m1 "auto-detected" "$P/whisper.log"
# progress while it runs:  grep -oE "^\[[0-9:.]+ --> [0-9:.]+\]" "$P/whisper.log" | tail -1
