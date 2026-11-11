#!/bin/bash
# Composite the finished reel. usage: compose.sh <projectDir> <out.mp4>
# Needs in projectDir: cut.mp4 (1440x2560 working res), words.json, beats.js, hook.jpg, mask.png, crops.env
# crops.env: S1_CROP, S2_CROP, S3_CROP (ffmpeg crop args on the 1440x2560 cut), S1_END, S2_END (frame numbers)
# Board frames are rendered in chunks (parallel, resumable) to board/*.mp4, then joined. Never pipe the whole
# board straight into the final encode: a stalled/dead renderer silently truncates the reel (lesson R006).
set -euo pipefail
ROOT="$(d="$(cd "$(dirname "$0")" && pwd)"; while [ ! -e "$d/.studio-root" ] && [ "$d" != / ]; do d="$(dirname "$d")"; done; echo "$d")"
P="$1"; OUT="$2"; E="$(cd "$(dirname "$0")" && pwd)"; F=/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
CH=${CHUNK:-400}; JOBS=${JOBS:-3}
cd "$P"; source crops.env
NF=$(ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets -of csv=p=0 cut.mp4)
echo "cut frames: $NF"
mkdir -p board
# 2) board chunks
# BGVIDEO set (R1.17): board rendered with a transparent background (qtrle .mov) and the video loop plays behind it
BG=${BGVIDEO:-}; EXT=mp4; [ -n "$BG" ] && EXT=mov
render_chunk() { a=$1; b=$2; o=$(printf "board/b_%05d.$EXT" $a)
  [ -s "$o" ] && return 0
  if [ "$EXT" = mov ]; then
    node "$E/render.js" . $a $b --alpha | $F -v error -y -f image2pipe -framerate 30000/1001 -c:v png -i - -c:v qtrle "$o.tmp.mov"
  else
    node "$E/render.js" . $a $b | $F -v error -y -f image2pipe -framerate 30000/1001 -c:v png -i - \
      -c:v libx264 -preset veryfast -crf 10 -pix_fmt yuv420p "$o.tmp.mov"
  fi
  n=$(ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets -of csv=p=0 "$o.tmp.mov")
  [ "$n" -eq $((b-a)) ] || { echo "chunk $a-$b has $n frames, expected $((b-a))" >&2; return 1; }
  mv "$o.tmp.mov" "$o"; echo "chunk $a-$b ok"; }
export -f render_chunk; export E F EXT
seq $S2_END $CH $((NF-1)) | xargs -P $JOBS -I{} bash -c 'a={}; b=$((a+'$CH')); [ $b -gt '$NF' ] && b='$NF'; render_chunk $a $b'
ls board/b_*.$EXT | sed "s/^/file '/; s/$/'/; s#file '#file '$PWD/#" > board/list.txt
$F -v error -y -f concat -safe 0 -i board/list.txt -c copy board/board.$EXT
BN=$(ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets -of csv=p=0 board/board.$EXT)
[ "$BN" -eq $((NF-S2_END)) ] || { echo "board has $BN frames, expected $((NF-S2_END))" >&2; exit 1; }
[ -n "${CHUNKS_ONLY:-}" ] && { echo "board chunks done ($BN frames)"; exit 0; }
# S1 overlay with alpha (rendered last: it depends on hook assets such as the MBB logo file)
[ -s board/s1ov.mov ] || node "$E/render.js" . 0 "$S1_END" --alpha | $F -v error -y -f image2pipe -framerate 30000/1001 -c:v png -i - -c:v qtrle board/s1ov.mov
# Opening blur-in (R1.7, R1.11): subtle gaussian on the white hook panel only, sigma BLUR_MAX -> 0 over BLUR_S s, ease-out
BLUR_S=${BLUR_S:-0.8}; BLUR_MAX=${BLUR_MAX:-12}; PANEL_H=${PANEL_H:-750}
BC=$(python3 -c "
b=$BLUR_S;mx=$BLUR_MAX;out=[]
for f in range(int(b*29.97)+2):
    t=f/29.97;p=min(1,t/b);sg=mx*(1-(1-(1-p)**3))
    v=max(sg,0.01); out.append(f'{t:.4f} gblur@b sigma {v:.3f}, gblur@b sigmaV {v:.3f}')  # set BOTH (E1.13)
print(';'.join(out))")
# S2 punch-in settle (R1.13/R1.14): sub-pixel zoom 110% -> 100%, sine in-out, rendered by s2zoom.py (never ffmpeg scale/crop: E1.17)
[ -s board/s2zoom.mp4 ] || "$ROOT/06. Tools/venv-style/bin/python" "$E/s2zoom.py" . ${Z0:-1.10}
AUD=${AUDIO:-}; AMAP=0:a; AI=5; [ -n "$BG" ] && AI=6; [ -n "$AUD" ] && AMAP=$AI:a
S3BD="[2:v]format=yuv420p[bd];"
[ -n "$BG" ] && S3BD="[5:v]fps=30000/1001,trim=end_frame=$((NF-S2_END)),setpts=PTS-STARTPTS,format=yuv420p[bgv];[bgv][2:v]overlay=0:0:format=auto,format=yuv420p[bd];"
# 3) final composite
$F -v error -stats -y -i cut.mp4 -i board/s1ov.mov -i board/board.$EXT -loop 1 -framerate 30000/1001 -i mask.png -i board/s2zoom.mp4 ${BG:+-stream_loop -1 -i "$BG"} ${AUD:+-i "$AUD"} \
  -filter_complex "
  [0:v]split=2[a][c];
  [a]trim=end_frame=${S1_END},setpts=PTS-STARTPTS,crop=${S1_CROP},scale=1080:1170:flags=lanczos,pad=1080:1920:0:750:white[f1];
  [f1][1:v]overlay=0:0:format=auto,format=yuv420p,split[s1a][s1b];
  [s1b]crop=1080:${PANEL_H}:0:0,sendcmd=c='${BC}',gblur@b=sigma=${BLUR_MAX}:sigmaV=${BLUR_MAX}:steps=3:enable='lt(t,${BLUR_S}+0.05)'[top];
  [s1a][top]overlay=0:0[s1];
  [4:v]setpts=PTS-STARTPTS,format=yuv420p[s2];
  [c]trim=start_frame=${S2_END},setpts=PTS-STARTPTS,crop=${S3_CROP},scale=810:908:flags=lanczos,format=yuva420p[fc];
  [3:v]format=gray,scale=810:908[m];[fc][m]alphamerge[face];
  ${S3BD}[bd][face]overlay=136:858:shortest=1,format=yuv420p[s3];
  [s1][s2][s3]concat=n=3:v=1:a=0,settb=1001/30000,setpts=N,tpad=stop_mode=clone:stop=30[v]" \
  -map "[v]" -map $AMAP -shortest -c:v libx264 -profile:v high -preset medium -crf 18 -pix_fmt yuv420p -r 30000/1001 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "${OUT%.mp4}.rendering.mp4"
mv -f "${OUT%.mp4}.rendering.mp4" "$OUT"   # never rewrite a file in place (R1.2)
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"); echo "export duration: $D s"
