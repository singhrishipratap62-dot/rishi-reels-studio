#!/usr/bin/env python3
"""Speech islands + per-island whisper (lesson E1.2: whole-file word timings drift up to ~1 s).
usage: islands.py <in16k.wav> <outDir> [model]
- 20 ms RMS envelope, speech > -50 dBFS, merge gaps < 0.18 s, drop islands < 0.15 s
- writes outDir/isl.json [[start,end],...] and per island NNN.wav + NNN.json (whisper -ml 1 -sow -oj)
- words.json in outDir: [[start,end,text,islandIdx],...] in source time
Runs whisper sequentially (parallel runs drop outputs: Metal contention).
WHISPER_NG=1 runs whisper on CPU (Metal alloc fails inside the Claude Code sandbox, E1.24)."""
import sys, os, wave, struct, math, json, subprocess
src, out = sys.argv[1], sys.argv[2]
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
model = sys.argv[3] if len(sys.argv) > 3 else os.path.join(_studio_root(), '06. Tools/models/ggml-base.bin')
os.makedirs(out, exist_ok=True)
w = wave.open(src); sr = w.getframerate(); n = w.getnframes()
data = struct.unpack('<%dh' % n, w.readframes(n))
hop = int(sr * 0.02); speech = []
for i in range(0, n - hop, hop):
    blk = data[i:i + hop]; rms = math.sqrt(sum(x * x for x in blk) / hop) / 32768
    speech.append(20 * math.log10(rms + 1e-9) > -50)
isl = []; s = None
for k, v in enumerate(speech + [False]):
    t = k * 0.02
    if v and s is None: s = t
    if not v and s is not None: isl.append([s, t]); s = None
merged = []
for a, b in isl:
    if merged and a - merged[-1][1] < 0.18: merged[-1][1] = b
    else: merged.append([a, b])
merged = [[round(a, 3), round(b, 3)] for a, b in merged if b - a >= 0.15]
json.dump(merged, open(f'{out}/isl.json', 'w'))
words = []
for i, (a, b) in enumerate(merged):
    a0, b0 = max(0, a - 0.05), b + 0.05
    wav = f'{out}/{i:03d}.wav'
    subprocess.run(['/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg', '-v', 'error', '-y', '-i', src, '-ss', f'{a0:.3f}', '-to', f'{b0:.3f}', wav], check=True)
    for attempt in range(2):
        subprocess.run(['whisper-cli'] + (['-ng'] if os.environ.get('WHISPER_NG') else []) + ['-m', model, '-l', 'en', '-ml', '1', '-sow', '-oj', '-of', f'{out}/{i:03d}', '-f', wav],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(f'{out}/{i:03d}.json'): break
    j = json.load(open(f'{out}/{i:03d}.json', encoding='utf-8', errors='replace'))
    for seg in j.get('transcription', []):
        txt = seg['text'].strip()
        if not txt or txt.startswith('['): continue
        o = seg['offsets']
        words.append([round(a0 + o['from'] / 1000, 3), round(a0 + o['to'] / 1000, 3), txt, i])
json.dump(words, open(f'{out}/words.json', 'w'))
print(f'{len(merged)} islands, {len(words)} words')
