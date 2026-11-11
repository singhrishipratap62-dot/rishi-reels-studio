# Step 3: timeline-aligned speaker audio -> "both silent" pauses -> cut plan + report.
# usage: python silence_plan.py <project_dir>      (reads case.json; writes A*.wav, plan.json, silence_report.md)
import json, os, re, subprocess, sys
P = sys.argv[1]; C = json.load(open(os.path.join(P, "case.json")))
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
ROOT = _studio_root()
SRC = os.path.join(ROOT, C["inbox_folder"]); END = C["sequence_end"]; S = C["silence"]
F = 1 / C["fps"]

def aligned_wav(sp, out):
    """Concatenate the speaker's source audio in timeline order; 'absent' spans (no clip on the track) become silence."""
    absent = sp.get("absent", [])
    pieces = []                                   # ordered: ("src", in, out) or ("sil", duration)
    for st, en, src_in in C["clips"]:
        cuts = sorted([(max(a, st), min(b, en)) for a, b in absent if a < en and b > st])
        t = st
        for a, b in cuts:
            if a > t: pieces.append(("src", src_in + t - st, src_in + a - st))
            pieces.append(("sil", b - a)); t = b
        if en > t: pieces.append(("src", src_in + t - st, src_in + en - st))
    parts, labels = [], ""
    for k, p in enumerate(pieces):
        if p[0] == "src": parts.append(f"[0:a]atrim=start={p[1]:.6f}:end={p[2]:.6f},asetpts=PTS-STARTPTS,aresample=16000[p{k}]")
        else: parts.append(f"anullsrc=r=16000:cl=mono,atrim=duration={p[1]:.6f}[p{k}]")
        labels += f"[p{k}]"
    fc = ";".join(parts) + f";{labels}concat=n={len(pieces)}:v=0:a=1[o]"
    open(out + ".fc", "w").write(fc)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(SRC, sp["file"]), "-/filter_complex", out + ".fc",
                    "-map", "[o]", "-ac", "1", "-c:a", "pcm_s16le", out], check=True)

def silences(wav):
    o = subprocess.run(["ffmpeg", "-i", wav, "-af", f"silencedetect=noise={S['threshold_db']}dB:d=0.1", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    out, s = [], None
    for l in o.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", l)
        if m: s = float(m.group(1))
        m = re.search(r"silence_end: ([\d.]+)", l)
        if m and s is not None: out.append((s, float(m.group(1)))); s = None
    if s is not None: out.append((s, END))
    return out

tracks = []
for i, sp in enumerate(C["speakers"]):
    w = os.path.join(P, f"A{i + 1}.wav"); aligned_wav(sp, w); tracks.append(silences(w))
both = tracks[0]
for tr in tracks[1:]:                                       # intersect: silent on every track
    i = j = 0; res = []
    while i < len(both) and j < len(tr):
        s, e = max(both[i][0], tr[j][0]), min(both[i][1], tr[j][1])
        if e > s: res.append((s, e))
        if both[i][1] < tr[j][1]: i += 1
        else: j += 1
    both = res
pauses = [[s, e] for s, e in both if e - s > S["min_pause"]]
merged = []
for s, e in pauses:                                         # merge pauses < merge_gap apart
    if merged and s - merged[-1][1] < S["merge_gap"]: merged[-1][1] = e
    else: merged.append([s, e])
cuts = [[round(round((s + S["pad"]) / F) * F, 6), round(round((e - S["pad"]) / F) * F, 6), e - s] for s, e in merged]
batches = [cuts[i:i + 50] for i in range(0, len(cuts), 50)][::-1]   # last batch (end of timeline) first
top = sorted(range(len(cuts)), key=lambda i: -cuts[i][2])[:5]
markers = []
for i in top:
    shift = sum(c[1] - c[0] for c in cuts[:i])
    markers.append({"time_seconds": round(cuts[i][0] - shift, 3), "name": f"Pause {cuts[i][2]:.1f}s",
                    "comments": f"removed pause, orig {cuts[i][0] - S['pad']:.2f}-{cuts[i][1] + S['pad']:.2f}s", "color": 1})
json.dump({"pauses": pauses, "cuts": [c[:2] for c in cuts],
           "batches": [[{"start": a, "end": b} for a, b, _ in x] for x in batches], "markers": markers},
          open(os.path.join(P, "plan.json"), "w"), indent=1)
tc = lambda t: f"{int(t // 60):02d}:{t % 60:05.2f}"
rem = sum(c[1] - c[0] for c in cuts)
with open(os.path.join(P, "silence_report.md"), "w") as f:
    f.write(f"# Silence report\n\nPauses > {S['min_pause']} s (both speakers silent < {S['threshold_db']} dB): **{len(pauses)}** "
            f"→ {len(cuts)} cuts after merging gaps < {S['merge_gap']} s.\nRemoved with {S['pad']} s padding: **{rem:.1f} s ({rem / 60:.1f} min)** → "
            f"new length {(END - rem) / 60:.1f} min. Batches of ≤ 50: {len(batches)}.\n\n## 10 longest\n")
    for s, e in sorted(pauses, key=lambda p: p[0] - p[1])[:10]: f.write(f"- {tc(s)} – {tc(e)} ({e - s:.2f} s)\n")
print(open(os.path.join(P, "silence_report.md")).read())
