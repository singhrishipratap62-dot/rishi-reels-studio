# Step 7: sentence-aligned captions, 4–8 words, no 1–3-word captions. [M15]
#  - every sentence end (. ? !) or pause > 1.5 s ends a caption; a new sentence starts a new caption
#  - 1–3-word sentences ("Sure.", "Cool.") join the START of the next sentence
#  - sentences of 4–8 words stay whole; longer ones split into 4–6-word chunks at the best break
#    (after . , ; :, before and/so/but/which…, never right after weak words like "I would", "the", "to")
#  - min 0.5 s on screen, no overlaps
# usage: python captions.py <fixed_words.json> <out.srt>
import json, sys
from collections import Counter
W = json.load(open(sys.argv[1])); W = W["words"] if isinstance(W, dict) else W
END = lambda w: w["word"][-1] in ".?!"
S, cur = [], []
for i, w in enumerate(W):
    cur.append(w); nxt = W[i + 1] if i + 1 < len(W) else None
    if END(w) or nxt is None or nxt["start_ms"] - w["end_ms"] > 1500: S.append(cur); cur = []
U, buf = [], []
for s in S:
    buf += s
    if len(buf) >= 4: U.append(buf); buf = []
if buf:
    if U: U[-1] += buf
    else: U.append(buf)
WEAK = set("i we you they he she it a an the to of in on at for with by from and or but so that is are was were be would will can "
           "could should do does did have has had my our your their this these those very not as if than then which what how about "
           "any some per it's i'm we're there going want like just".split())
STARTERS = set("and so but because which that then or where when if while since whereas given before after instead".split())
norm = lambda t: t.lower().strip(".,?!;:\"'")
def brk(u, j):
    p, q = u[j - 1]["word"], u[j]["word"]; c = 1.0
    if p[-1] in ".?!": c -= 3
    elif p[-1] in ",;:—-": c -= 1.5
    if norm(q) in STARTERS: c -= 0.8
    if norm(p) in WEAK and p[-1] not in ".,?!;:": c += 2
    return c
def split(u):
    n = len(u)
    if n <= 8: return [u]
    INF = 1e9; best = [INF] * (n + 1); prv = [0] * (n + 1); best[0] = 0
    for j in range(4, n + 1):
        for s in (4, 5, 6):
            i = j - s
            if i >= 0 and best[i] < INF:
                v = best[i] + abs(s - 5) * 0.4 + (brk(u, j) if j < n else 0)
                if v < best[j]: best[j] = v; prv[j] = i
    out, j = [], n
    while j > 0: out.append(u[prv[j]:j]); j = prv[j]
    return out[::-1]
L = [c for u in U for c in split(u)]
tc = lambda ms: f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
out, prev = [], 0
for n, l in enumerate(L):
    s = max(l[0]["start_ms"], prev); e = l[-1]["end_ms"]
    if n + 1 < len(L): e = min(max(e, s + 500), L[n + 1][0]["start_ms"])
    out.append(f"{n + 1}\n{tc(s)} --> {tc(e)}\n{' '.join(x['word'] for x in l)}\n"); prev = e
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
print(len(L), "captions; sizes:", sorted(Counter(len(l) for l in L).items()),
      "| captions holding a joined short reply:", sum(1 for l in L if any(END(w) for w in l[:-1])))
