#!/bin/bash
# R010 picture render with Remotion (pack v2.0 trial) -> exports/<ID>_1x.mp4 (or _green with GREEN=1).
# Audio: mix.wav if the sound pass has run, else the cut's own voice.
# usage: bash render_remotion.sh            (final picture, 1x)
#        GREEN=1 bash render_remotion.sh    (graphics on #00FF00)
set -euo pipefail
export PATH=$HOME/.nvm/versions/node/v24.19.0/bin:/opt/homebrew/bin:$PATH
P="$(cd "$(dirname "$0")" && pwd)"; ID=$(basename "$P"); R="$P/../../../06. Tools/remotion/engine"; X="$P/../../../04. Exports/Consulting Case"
F=/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
# Remotion's own chrome-headless-shell is broken on this Mac (icudtl.dat); use Playwright's
CH=$(find ~/Library/Caches/ms-playwright -name chrome-headless-shell -type f | sort | tail -1)
# refresh public/ (Remotion skips symlinks; big files are hard links, no extra disk)
cp "$P/words.json" "$P/beats.js" "$P/hook.jpg" "$P/public/"
ln -f "$P/cut.mp4" "$P/public/cut.mp4"
SUF=_1x; PROPS='{"green":false}'; [ -n "${GREEN:-}" ] && { SUF=_green; PROPS='{"green":true}'; }
TMP="$P/remotion$SUF.mp4"
cd "$R"
npx remotion render src/index.ts CaseReel "$TMP" --public-dir="$P/public" --browser-executable="$CH" \
  --props="$PROPS" --codec=h264 --crf=18 --pixel-format=yuv420p --muted --concurrency=${CONC:-4}
AUD="$P/cut.mp4"; [ -s "$P/mix.wav" ] && AUD="$P/mix.wav"
$F -v error -y -i "$TMP" -i "$AUD" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest \
  -movflags +faststart "$X/$ID$SUF.rendering.mp4"
mv -f "$X/$ID$SUF.rendering.mp4" "$X/$ID$SUF.mp4"   # never rewrite a file in place (R1.2)
rm -f "$TMP"
echo "done: $X/$ID$SUF.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$X/$ID$SUF.mp4") s)"
