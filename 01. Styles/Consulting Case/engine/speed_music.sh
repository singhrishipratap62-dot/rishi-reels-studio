#!/bin/bash
# Speed up the finished reel and lay a ducked music bed under it (R1.15).
# usage: speed_music.sh <projectDir> <final.mp4> <music file> [speed=1.2] [music_offset_s=15]
# - keeps the 1x final as <final>_1x.mp4 (source for every re-run)
# - picture: setpts/speed, back to 29.97 CFR. Voice+SFX: atempo (pitch kept), from the project's mix.wav (not the AAC)
# - music: NOT sped; starts at music_offset_s; calibrated GAP dB under the voice while speaking (default 13, R1.16),
#   light sidechain duck (threshold 0.1, ratio 2); 1 s fade-in, 2 s fade-out to the end; program −15 LUFS, TP ≤ −1 dBTP
set -euo pipefail
P="$1"; OUT="$2"; MUS="$3"; SP="${4:-1.2}"; OFF="${5:-15}"; F=/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
cd "$P"; ONE="${OUT%.mp4}_1x.mp4"
[ -s "$ONE" ] || cp "$OUT" "$ONE"
D1=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$ONE"); D=$(python3 -c "print($D1/$SP)")
lufs() { $F -i "$1" -af ebur128 -f null - 2>&1 | grep -E '^\s+I:' | tail -1 | awk '{print $2}'; }
# 1) voice+sfx program and voice-only sidechain key, sped (pitch preserved)
$F -v error -y -i mix.wav -af "atempo=$SP" -ar 48000 prog_sp.wav
$F -v error -y -i voice_proc.wav -af "atempo=$SP" -ar 48000 key_sp.wav
# 2) music bed: segment, level to -33 LUFS, fades
$F -v error -y -ss "$OFF" -t "$D" -i "$MUS" -ac 2 -ar 48000 mus_seg.wav
G=$(python3 -c "print(-33-($(lufs mus_seg.wav)))")
FO=$(python3 -c "print(max(0,$D-2.0))")
$F -v error -y -i mus_seg.wav -af "volume=${G}dB,afade=t=in:d=1.0,afade=t=out:st=${FO}:d=2.0" mus_lvl.wav
# 3) duck under speech (sidechain = voice only)
$F -v error -y -i mus_lvl.wav -i key_sp.wav -filter_complex \
  "[1:a]asplit=2[k1][k2];[0:a][k1]sidechaincompress=threshold=0.1:ratio=2:attack=60:release=450:knee=6:makeup=1[d];[k2]anullsink" \
  -map "[d]" mus_duck_raw.wav
# calibrate: music (ducked) sits GAP dB under the voice while speaking (Rishi R1.16: 13 dB; Minimal Edit's 18–24 was too quiet for a soft bed)
GAP=${GAP:-13}   # R1.16: 21 dB was inaudible to Rishi; 13 dB under the voice
G3=$(python3 - <<PY
import subprocess, re
F='$F'
def m(path):
    o=subprocess.run([F,'-i',path,'-af','astats=metadata=1:reset=4800,ametadata=print:key=lavfi.astats.Overall.RMS_level','-f','null','-'],capture_output=True,text=True).stderr
    return [float(x) if x!='-inf' else -120 for x in re.findall(r'RMS_level=(-?[\d.inf]+)',o)]
k,d=m('key_sp.wav'),m('mus_duck_raw.wav'); n=min(len(k),len(d)); sp=[i for i in range(n) if k[i]>-35 and d[i]>-90]
print((sum(k[i] for i in sp)/len(sp)-$GAP)-(sum(d[i] for i in sp)/len(sp)))
PY
)
$F -v error -y -i mus_duck_raw.wav -af "volume=${G3}dB" mus_duck.wav
# 4) mix + trim to -15 LUFS, limit -1.6 dBFS
$F -v error -y -i prog_sp.wav -i mus_duck.wav -filter_complex "[0:a][1:a]amix=inputs=2:normalize=0:duration=first[m]" -map "[m]" final_mix_raw.wav
G2=$(python3 -c "print(-15-($(lufs final_mix_raw.wav)))")
# true-peak safe: limit at 4x oversampling (music adds inter-sample peaks: E1.18)
$F -v error -y -i final_mix_raw.wav -af "volume=${G2}dB,aresample=192000,alimiter=limit=-2.0dB:level=false,aresample=48000" -ar 48000 final_mix.wav
# 5) picture (AUDIO_ONLY=1: keep the already-sped picture of $OUT, swap the audio only)
if [ -n "${AUDIO_ONLY:-}" ]; then
  $F -v error -y -i "$OUT" -i final_mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "${OUT%.mp4}.rendering.mp4"
else
$F -v error -stats -y -i "$ONE" -i final_mix.wav -filter_complex "[0:v]setpts=PTS/${SP},fps=30000/1001[v]" \
  -map "[v]" -map 1:a -shortest -c:v libx264 -profile:v high -preset medium -crf 18 -pix_fmt yuv420p -r 30000/1001 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "${OUT%.mp4}.rendering.mp4"
fi
mv -f "${OUT%.mp4}.rendering.mp4" "$OUT"
echo "speed ${SP}x: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT") s (1x: $D1 s)"
# report: music level vs voice, in speech and in pauses
python3 - <<'EOF'
import subprocess, re
F='/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'
def m(path):
    o=subprocess.run([F,'-i',path,'-af','astats=metadata=1:reset=4800,ametadata=print:key=lavfi.astats.Overall.RMS_level','-f','null','-'],capture_output=True,text=True).stderr
    return [float(x) for x in re.findall(r'RMS_level=(-?[\d.]+)',o)]
k,mu,lv=m('key_sp.wav'),m('mus_duck.wav'),m('mus_lvl.wav')
n=min(len(k),len(mu)); sp=[mu[i] for i in range(n) if k[i]>-35]; pa=[mu[i] for i in range(n) if k[i]<-50]
ks=[k[i] for i in range(n) if k[i]>-35]
avg=lambda a: sum(a)/len(a) if a else float('nan')
import statistics
dk=[lv[i]-mu[i] for i in range(n) if k[i]>-35]; base=statistics.median(dk)
print(f'voice {avg(ks):.1f} dB RMS, music under speech {avg(sp):.1f} -> {avg(ks)-avg(sp):.1f} dB under voice; duck depth (vs undocked, after calibration) median {statistics.median([d-min(dk) for d in dk]):.1f} dB, max {max(dk)-min(dk):.1f} dB')
EOF
