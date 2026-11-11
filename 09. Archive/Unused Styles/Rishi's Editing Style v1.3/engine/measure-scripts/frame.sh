#!/bin/bash
# frame.sh <src.mp4> <frame_number> <out.png> [crop=w:h:x:y]   full-res 720x1280 native frame (exact frame index)
f=$2; vf="select=eq(n\,$f)"; [ -n "$4" ] && vf="$vf,crop=$4"
ffmpeg -v error -i "$1" -vf "$vf" -frames:v 1 -fps_mode vfr "$3" -y
