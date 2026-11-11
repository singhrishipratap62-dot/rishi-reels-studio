#!/bin/bash
# Regenerate R003.tsrct from scratch: fonts, images, VO, SFX, media layers, action batch.
set -e
cd "$(dirname "$0")/.."
T="$HOME/Library/Application Support/Tesseract/bin/tsrct"
DS="../../../gradnext-design-system/fonts"; B="../../../_brand-build"; W=.tesseract-work
python3 $W/build.py | tee $W/build.log
rm -f R003.tsrct
"$T" project create --project R003.tsrct >/dev/null
for f in "$DS/AvenirLTProHeavy.otf" "$DS/AvenirLTProBlack.otf" "$DS/AvenirLTProMedium.otf" "$B/Besley-Italic[wght].ttf"; do
  "$T" project import-font --project R003.tsrct --file "$f" >/dev/null 2>&1; done
"$T" project import-asset --project R003.tsrct --file "$B/gradnext-wordmark-rhino.png" --asset-id wordmark-rhino --kind image >/dev/null
"$T" project import-video --project R003.tsrct --file "../../gradnext-background-loop-9-16.mp4" --asset-id bg-loop >/dev/null
"$T" project import-asset --project R003.tsrct --file "$(ls ../ElevenLabs*.mp3)" --asset-id vo --kind audio >/dev/null
for n in $(python3 -c "import json;print(' '.join(json.load(open('$W/sfx-assets.json'))))"); do
  "$T" project import-asset --project R003.tsrct --file $W/sfx/$n.wav --asset-id sfx-$n --kind audio >/dev/null; done
"$T" project checkout --project R003.tsrct --output $W/editable.json >/dev/null
python3 -c "
import json;d=json.load(open('$W/editable.json'));d['duration']=47.5
d['composition']['layers']=json.load(open('$W/media-layers.json'));json.dump(d,open('$W/editable.json','w'))"
"$T" project commit --project R003.tsrct --file $W/editable.json >/dev/null
"$T" project apply --project R003.tsrct --actions $W/edits.json
