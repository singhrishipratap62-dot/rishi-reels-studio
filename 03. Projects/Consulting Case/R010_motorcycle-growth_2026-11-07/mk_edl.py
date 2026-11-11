# Build edl.json for R010 from speech islands (keep last complete take; later file wins, E1.3).
import json, wave, struct, math
V = "../Raw Footage/Video 5"
isl = {n: json.load(open(f'isl_{n}/isl.json')) for n in ('4620', '4621', '4622')}
txt = {n: json.load(open(f'isl_{n}/words.json')) for n in isl}
def env(n):
    w = wave.open(f'raw_{n}.wav'); d = w.readframes(w.getnframes()); s = struct.unpack('<%dh' % (len(d)//2), d)
    return [math.sqrt(sum(x*x for x in s[i:i+160])/160) for i in range(0, len(s)-160, 160)]  # 10 ms
E = {n: env(n) for n in isl}
def split(n, a, b):  # RMS minimum between a and b
    k = min(range(int(a*100), int(b*100)), key=lambda k: sum(E[n][k-2:k+3])); return k/100
def say(n, i): return ' '.join(x[2] for x in txt[n] if x[3] == i)
H, T = 0.04, 0.06
seg = []
def add(n, i, a=None, b=None, note=None):
    s, e = isl[n][i]; a = s - H if a is None else a; b = e + T if b is None else b
    seg.append([n, round(a, 3), round(b, 3), note or f'{n}/{i:02d}: {say(n, i)}'])
for i in [1, 2]: add('4620', i)
# 03 "Your client is a hunt." dropped: flub, restarts as 04
for i in range(4, 11): add('4620', i)
# 11 "What?" fragment dropped; 12 keep only the question (the answer is re-said in 13)
c = split('4620', 37.85, 38.2); add('4620', 12, b=c, note=f'4620/12a: Why aren\'t people buying from us? (split {c})')
for i in [13, 14, 15, 16, 17, 18, 20, 21, 22, 23]: add('4620', i)
c = split('4620', 76.0, 76.13); add('4620', 24, b=c, note=f'4620/24a: does take a test ride (split {c}; "1 and" retaken)')
for i in [25, 26]: add('4620', i)
# 27 "we need to" false start dropped
for i in [28, 29, 30, 31]: add('4620', i)
# 32 blip dropped; 33+34 = "New products for new customers"
for i in range(33, 57): add('4620', i)
# 57/58 partial takes dropped; 59 = complete "Why don't people buy? ... every other bike."
add('4620', 59)
# 4620/60-61 and 4621/00-03 retakes; 4621/04 complete "So fix exactly that, fix the reliability."
add('4621', 4)
# 4621/05 fragment dropped
for i in [6, 7, 8, 9, 10]: add('4621', i)
# 4621/11-13 "This is exactly what … in 2000 it was" abandoned (2.5 s gap) -> dropped
add('4622', 0); add('4622', 1, b=isl['4622'][1][1] + 0.4)
json.dump({'sources': {n: f'{V}/IMG_{n}.MOV' for n in isl}, 'segments': seg}, open('edl.json', 'w'), indent=1)
tot = sum(b - a for _, a, b, _ in seg); print(len(seg), 'segments', round(tot, 2), 's')
