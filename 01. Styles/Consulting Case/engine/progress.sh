#!/bin/bash
# Live render progress for compose.sh. usage: progress.sh <projectDir>   (Ctrl-C to stop)
P="$1"; LOG="${2:-compose.log}"; cd "$P" || exit 1
while true; do
  clear
  echo "R-render progress  $(date +%H:%M:%S)   ($(basename "$PWD"))"
  echo "--------------------------------------------------------------"
  done_n=0; total=0
  for a in $(seq 180 400 4803); do
    total=$((total+1)); b=$((a+400)); [ $b -gt 4804 ] && b=4804
    f=$(printf 'board/b_%05d.mp4' $a); [ -e "${f%.mp4}.mov" ] || [ -e "${f%.mp4}.mov.tmp.mov" ] && f="${f%.mp4}.mov"
    t0=$(awk -v f=$a 'BEGIN{printf "%d:%02d", int(f/29.97/60), int(f/29.97)%60}')
    if [ -s "$f" ]; then done_n=$((done_n+1)); st="DONE"
    elif [ -e "$f.tmp.mp4" ] || [ -e "$f.tmp.mov" ]; then
      t=$f.tmp.mp4; [ -e "$t" ] || t=$f.tmp.mov; full=540000; [ "${f##*.}" = mov ] && full=41000000
      sz=$(stat -f%z "$t"); pct=$(( sz * 100 / full )); [ $pct -gt 99 ] && pct=99
      bar=$(printf '%*s' $((pct/5)) '' | tr ' ' '#'); st="rendering ~${pct}%  [$(printf '%-20s' "$bar")]"
    else st="waiting"; fi
    printf "  frames %4d-%4d  (from %s)  %s\n" $a $b "$t0" "$st"
  done
  echo "--------------------------------------------------------------"
  echo "  board chunks: $done_n / $total done"
  [ -s board/board.mp4 ] || [ -s board/board.mov ] && echo "  board joined: yes"
  if pgrep -f "compose.sh|speed_music.sh|qc.py" >/dev/null; then echo "  [composite running]";
    last=$(tail -c 400 $LOG 2>/dev/null | tr '\r' '\n' | grep -E '^frame=' | tail -1)
    [ -n "$last" ] && echo "  final composite: $last"
    echo "  retries so far: $(grep -c 'retry screenshot' $LOG 2>/dev/null)"
  else
    echo "  compose.sh finished:"; grep -E 'export duration|expected|Error|speed 1.2x|PASS|FAIL|ALL DONE|FAILED' $LOG | tail -3 | sed 's/^/    /'
  fi
  sleep 2
done
