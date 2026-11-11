# Step 7: proofread ASR with case logic. Phrase + word corrections from a JSON file; logs every change. [M16]
# usage: python fix_words.py <words.json> <corrections.json> <out_fixed_words.json> <log.csv>
# corrections.json: {"phrases": [["heard phrase", "corrected phrase"], ...],
#                    "words": [["^regex", "replacement"], ...]}   (word rules keep trailing punctuation)
# Example for the beer case: corrections.beer-case.json. Re-check every guess with Rishi.
import csv, json, re, sys
src, corr, out, logf = sys.argv[1:5]
W = json.load(open(src)); W = W["words"] if isinstance(W, dict) else W
R = json.load(open(corr)); log = []
tc = lambda ms: f"{ms // 60000:02d}:{ms // 1000 % 60:02d}.{ms % 1000:03d}"
for old, new in R.get("phrases", []):
    o, n = old.split(), new.split(); i = hits = 0
    while i <= len(W) - len(o):
        if [w["word"] for w in W[i:i + len(o)]] == o:
            s, e, sp = W[i]["start_ms"], W[i + len(o) - 1]["end_ms"], W[i]["speaker"]; step = (e - s) / len(n)
            W[i:i + len(o)] = [{"start_ms": round(s + k * step), "end_ms": round(s + (k + 1) * step), "word": t,
                                "speaker": sp, "confidence": None} for k, t in enumerate(n)]
            log.append((tc(s), old, new)); hits += 1; i += len(n)
        else: i += 1
    if not hits: print("NO MATCH:", old)
for w in W:
    for pat, rep in R.get("words", []):
        m = re.match(pat, w["word"])
        if m:
            nw = re.sub(pat, rep, w["word"])
            if nw != w["word"]: log.append((tc(w["start_ms"]), w["word"], nw)); w["word"] = nw
            break
json.dump(W, open(out, "w"), ensure_ascii=False)
with open(logf, "w", newline="") as f:
    c = csv.writer(f); c.writerow(["timecode", "heard", "corrected"]); c.writerows(log)
print(len(log), "corrections ->", logf)
