# Step 5/7: Whisper JSON -> words with speaker labels -> JSON / CSV / SRT (ms timestamps).
# usage: python transcript.py <project_dir> <out_basename_in_case_media_folder (case.json inbox_folder)> [--from words.json] [--remove a_ms b_ms ...]
#   default input: whisper_words.json (+ cut_spk1/2.wav for speaker labels by louder track)
#   --from <words.json>     reuse an existing words file instead of Whisper output (no re-transcription) [M13]
#   --remove a b [a b ...]  drop words inside [a,b) ms and shift later words (derive a copy's transcript)
import csv, json, os, subprocess, sys
P, BASE = sys.argv[1], sys.argv[2]
C = json.load(open(os.path.join(P, "case.json")))
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
ROOT = _studio_root()
OUT = os.path.join(ROOT, C["inbox_folder"], BASE)
names = [s["name"].lower() for s in C["speakers"]]
args = sys.argv[3:]

def levels(wav):  # 10 ms RMS dB
    o = subprocess.run(["ffmpeg", "-v", "error", "-i", wav, "-af", "asetnsamples=n=160,astats=metadata=1:reset=1:measure_overall=none:"
                        "measure_perchannel=RMS_level,ametadata=print:key=lavfi.astats.1.RMS_level:file=-", "-f", "null", "-"],
                       capture_output=True, text=True).stdout
    return [-120.0 if "inf" in l else float(l.split("=")[1]) for l in o.splitlines() if "RMS_level=" in l]

if "--from" in args:
    W = json.load(open(args[args.index("--from") + 1]))
    W = W["words"] if isinstance(W, dict) else W
else:
    L = [levels(os.path.join(P, f"cut_spk{k}.wav")) for k in (1, 2)]
    J = json.load(open(os.path.join(P, "whisper_words.json"), encoding="utf-8", errors="replace"))
    W = []
    for seg in J["transcription"]:
        t = seg["text"].strip()
        if not t: continue
        s, e = seg["offsets"]["from"], seg["offsets"]["to"]
        en = [sum(10 ** (x / 10) for x in lv[s // 10:max(s // 10 + 1, e // 10)]) for lv in L]
        toks = [x for x in seg.get("tokens", []) if not x["text"].startswith("[_")]
        W.append({"start_ms": s, "end_ms": e, "word": t, "speaker": names[0] if en[0] >= en[1] else names[1],
                  "confidence": round(sum(x["p"] for x in toks) / len(toks), 3) if toks else None})
if "--remove" in args:
    r = [int(x) for x in args[args.index("--remove") + 1:]]
    for a, b in sorted(zip(r[::2], r[1::2]), reverse=True):
        NW = []
        for x in W:
            x = dict(x)
            if x["start_ms"] < a: x["end_ms"] = min(x["end_ms"], a); NW.append(x)
            elif x["start_ms"] >= b or x["end_ms"] > b + 50:
                x["start_ms"] = max(a, x["start_ms"] - (b - a)); x["end_ms"] -= b - a; NW.append(x)
        W = NW
json.dump({"words": W}, open(OUT + "_words.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tc = lambda ms: f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d}.{ms % 1000:03d}"
with open(OUT + "_words.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["start_ms", "end_ms", "start_tc", "word", "speaker", "confidence"])
    for x in W: w.writerow([x["start_ms"], x["end_ms"], tc(x["start_ms"]), x["word"], x["speaker"], x["confidence"]])
lines, cur = [], []
for x in W:
    if cur and (x["speaker"] != cur[-1]["speaker"] or x["start_ms"] - cur[-1]["end_ms"] > 500 or len(cur) >= 8):
        lines.append(cur); cur = []
    cur.append(x)
lines.append(cur)
with open(OUT + ".srt", "w", encoding="utf-8") as f:
    for n, l in enumerate(lines, 1):
        f.write(f"{n}\n{tc(l[0]['start_ms']).replace('.', ',')} --> {tc(l[-1]['end_ms']).replace('.', ',')}\n"
                f"[{l[0]['speaker']}] {' '.join(x['word'] for x in l)}\n\n")
print(f"{len(W)} words -> {OUT}_words.json/.csv + .srt")
