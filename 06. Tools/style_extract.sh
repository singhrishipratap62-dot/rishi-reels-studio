#!/usr/bin/env bash
# Usage: style_extract.sh <video> <out_dir>
# One decode pass per video: saves a 320x180 frame at every scene change (score > 0.3)
# and at least every 4 s, and logs pts + scene score for each saved frame.
set -euo pipefail
in="$1"; out="$2"
mkdir -p "$out/frames"
ffmpeg -hide_banner -loglevel error -i "$in" -an \
  -vf "scale=480:270,select='gt(scene\,0.3)+isnan(prev_selected_t)+gte(t-prev_selected_t\,4)',metadata=print:file='$out/frames.log',scale=320:180" \
  -fps_mode vfr -q:v 4 "$out/frames/f_%05d.jpg"
echo "done $in"
