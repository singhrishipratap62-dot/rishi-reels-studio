#!/usr/bin/env python3
"""Align a corrected script to ASR word times; snap onsets to audio; fix squashed segments.
usage: align.py words_cut_raw.json script.txt cut.wav edl.json -> words.json
words_cut_raw: [[start,end,text,segIdx],...] (cut time)."""
import json, sys, re, wave, struct, math, difflib
raw = json.load(open(sys.argv[1])); script = open(sys.argv[2]).read().split()
wav = sys.argv[3]; edl = json.load(open(sys.argv[4]))['segments']
NUM = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','ten':'10'}
def norm(t):
    t = t.lower().replace(',', '').replace('₹', '')
    t = re.sub(r"[^a-z0-9&']", '', t).replace("'", '')
    t = re.sub(r'k+$', '', t) if re.match(r'^\d+k+$', t) else t
    return NUM.get(t, t)
# envelope 10 ms
w = wave.open(wav); sr = w.getframerate(); d = w.readframes(w.getnframes())
s = struct.unpack('<%dh' % (len(d)//2), d); hop = sr//100
env = [20*math.log10(math.sqrt(sum(x*x for x in s[i:i+hop])/hop)+1e-9) - 90.3 for i in range(0, len(s)-hop, hop)]
def lvl(t): i = int(t*100); return env[i] if 0 <= i < len(env) else -120
# segment spans in cut time
spans = []; t = 0
for _, a, b, *_ in edl: spans.append((t, t+b-a)); t += b-a
# 1) fix squashed / non-monotonic segments by char-length redistribution over voiced span
bysg = {}
for i, r in enumerate(raw): bysg.setdefault(r[3], []).append(i)
for sg, idx in bysg.items():
    st = [raw[i][0] for i in idx]
    bad = any(st[k+1] < st[k] for k in range(len(st)-1)) or sum(1 for i in idx if raw[i][1]-raw[i][0] < 0.04) > 1
    if not bad: continue
    a, b = spans[sg]; v = [x/100 for x in range(int(a*100), int(b*100)) if lvl(x/100) > -45]
    a, b = (v[0], v[-1]) if v else (a, b)
    L = [len(raw[i][2]) + 2 for i in idx]; tot = sum(L); c = a
    for i, l in zip(idx, L): raw[i][0] = round(c, 3); c += (b-a)*l/tot; raw[i][1] = round(c, 3)
# 2) align
A = [norm(r[2]) for r in raw]; B = [norm(x) for x in script]
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
out = [None]*len(script)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for k in range(i2-i1): out[j1+k] = [raw[i1+k][0], raw[i1+k][1]]
    elif tag == 'replace' and i2 > i1:
        a, b = raw[i1][0], raw[i2-1][1]; n = j2-j1
        for k in range(n): out[j1+k] = [a+(b-a)*k/n, a+(b-a)*(k+1)/n]
# interpolate leftovers
for j in range(len(out)):
    if out[j] is None:
        p = next((out[k][1] for k in range(j-1, -1, -1) if out[k]), 0.0)
        q = next((out[k][0] for k in range(j+1, len(out)) if out[k]), p+0.3)
        out[j] = [p, max(p+0.05, min(q, p+0.3))]
# 3) snap onsets: nearest energy rise within [-0.20, +0.12]
def rise(t):
    best = None
    for k in range(int((t-0.20)*100), int((t+0.12)*100)):
        if lvl(k/100) > -42 and lvl((k-3)/100) < lvl(k/100) - 8:
            if best is None or abs(k/100-t) < abs(best-t): best = k/100
    return best
snapped = 0
for j, o in enumerate(out):
    r = rise(o[0])
    if r is not None: o[0] = r; snapped += 1
for j in range(1, len(out)):  # monotonic
    if out[j][0] < out[j-1][0] + 0.03: out[j][0] = out[j-1][0] + 0.03
for j in range(len(out)-1): out[j][1] = max(out[j][0]+0.05, min(out[j][1], out[j+1][0]))
json.dump([{'w': script[j], 's': round(out[j][0], 3), 'e': round(out[j][1], 3)} for j in range(len(script))], open('words.json', 'w'), indent=0)
eq = sum(i2-i1 for t_, i1, i2, *_ in sm.get_opcodes() if t_ == 'equal')
print(f'{len(script)} words, {eq} matched to ASR, {snapped} snapped to onsets')
