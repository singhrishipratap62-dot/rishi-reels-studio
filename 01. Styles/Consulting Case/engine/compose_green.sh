#!/bin/bash
# Graphics-only export: everything from the final, with every area where the talking-head video appears filled
# with pure green #00FF00 (S1 bottom, S2 full frame, S3 rounded face card). Same audio + timing as the final.
# Reuses board/board.(mp4|mov) and board/s1ov.mov from compose.sh (run that first).
# BGVIDEO set (R1.17): the transparent board.mov is laid over the background loop, as in the final.
# usage: compose_green.sh <projectDir> <out.mp4>
set -euo pipefail
P="$1"; OUT="$2"; F=/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
cd "$P"; source crops.env
NF=$(ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets -of csv=p=0 cut.mp4)
G="color=c=0x00FF00:s=1080x1920:r=30000/1001"
BG=${BGVIDEO:-}; BOARD=board/board.mp4; [ -n "$BG" ] && BOARD=board/board.mov
S3BD="[2:v]format=yuv420p[bd];"
[ -n "$BG" ] && S3BD="[4:v]fps=30000/1001,trim=end_frame=$((NF-S2_END)),setpts=PTS-STARTPTS,format=yuv420p[bgv];[bgv][2:v]overlay=0:0:format=auto,format=yuv420p[bd];"
$F -v error -stats -y -i cut.mp4 -i board/s1ov.mov -i "$BOARD" -loop 1 -framerate 30000/1001 -i mask.png ${BG:+-stream_loop -1 -i "$BG"} \
  -filter_complex "
  ${G}:d=$(echo "$S1_END/29.97002997" | bc -l),trim=end_frame=${S1_END}[g1];
  [g1][1:v]overlay=0:0:format=auto,format=yuv420p[s1];
  ${G},trim=end_frame=$((S2_END-S1_END)),format=yuv420p[s2];
  color=c=0x00FF00:s=810x908:r=30000/1001,trim=end_frame=$((NF-S2_END)),format=yuva420p[gc];
  [3:v]format=gray,scale=810:908[m];[gc][m]alphamerge[gface];
  ${S3BD}[bd][gface]overlay=136:858:shortest=1,format=yuv420p[s3];
  [s1][s2][s3]concat=n=3:v=1:a=0,settb=1001/30000,setpts=N,tpad=stop_mode=clone:stop=30[v]" \
  -map "[v]" -map 0:a -shortest -c:v libx264 -profile:v high -preset medium -crf 16 -pix_fmt yuv420p -r 30000/1001 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "${OUT%.mp4}.rendering.mp4"
mv -f "${OUT%.mp4}.rendering.mp4" "$OUT"
echo "green export: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT") s"
