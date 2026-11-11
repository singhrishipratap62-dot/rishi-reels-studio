# Steps 5–8 helper: map the FINAL edited timeline back to source time, render its audio, check for sliver clips.
# usage: python timeline_map.py <project_dir> [--audio] [--slivers]
#   reads case.json + plan.json (silence cuts, frame-snapped) + case.json "extra_cuts_after_silence"
#   (ranges in the silence-cut timeline, e.g. the self-assessment cut + any 1-frame sliver cuts)
#   writes src_segments.json  [[src_in, src_out], ...]  -> used by speakers.py (both cameras share source times)
#   --audio : cut_mix.wav, cut_spk1.wav, cut_spk2.wav (16 kHz) of the final timeline -> Whisper + speaker labels
#   --slivers: prints every piece <= 2 frames between edit points (remove them with a ripple cut)
import json, os, subprocess, sys
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
P = sys.argv[1]; C = json.load(open(os.path.join(P, "case.json"))); plan = json.load(open(os.path.join(P, "plan.json")))
F = 1 / C["fps"]; END = C["sequence_end"]
snap = lambda t: round(t / F) * F
cuts = sorted((snap(a), snap(b)) for a, b in plan["cuts"])
extra = sorted(C.get("extra_cuts_after_silence", []))

def to_cut(t):                     # original timeline -> silence-cut timeline
    s = t
    for a, b in cuts:
        if t >= b: s -= b - a
        elif t > a: return None
    return s

keep, p = [], 0.0                  # keep intervals of the silence-cut timeline, in ORIGINAL coords
for a, b in cuts: keep.append((p, a)); p = b
keep.append((p, END))
segs = []                          # final-timeline segments as source ranges, split at clip boundaries
for a, b in keep:
    pts = sorted({a, b} | {st for st, en, i in C["clips"] if a < st < b})
    for x, y in zip(pts, pts[1:]):
        cx = to_cut(x); cy = cx + (y - x)
        pieces = [(cx, cy)]
        for e0, e1 in extra:
            pieces = [q for lo, hi in pieces for q in ((lo, min(hi, e0)), (max(lo, e1), hi)) if q[1] - q[0] > 1e-6]
        for lo, hi in pieces:
            ox = x + (lo - cx)
            st, en, src_in = [c for c in C["clips"] if c[0] <= ox + 1e-9 < c[1]][0]
            segs.append((round(src_in + ox - st, 6), round(src_in + ox - st + hi - lo, 6)))
json.dump(segs, open(os.path.join(P, "src_segments.json"), "w"))
total = sum(b - a for a, b in segs)
print(f"{len(segs)} segments, final timeline {total:.4f} s ({total / 60:.2f} min)")

if "--slivers" in sys.argv:        # edit points on the final timeline: clip boundaries + every cut join
    B = set()
    for st, en, i in C["clips"]:
        v = to_cut(st)
        if v is not None: B.add(round(v, 4))
    off = 0
    for a, b in cuts: B.add(round(a - off, 4)); off += b - a
    B.add(round(END - off, 4))
    FB = set()
    for t in B:
        sh = sum(e1 - e0 for e0, e1 in extra if e1 <= t + 1e-6)
        if not any(e0 < t < e1 for e0, e1 in extra): FB.add(round(t - sh, 4))
    for e0, e1 in extra: FB.add(round(e0 - sum(y - x for x, y in extra if y <= e0 + 1e-6), 4))
    FB = sorted(FB)
    short = [(x, y) for x, y in zip(FB, FB[1:]) if y - x <= 2 * F + 1e-3]
    print("slivers (<= 2 frames):", short or "none")

if "--audio" in sys.argv:
    ROOT = _studio_root()
    for k, sp in enumerate(C["speakers"], 1):
        parts = [f"[0:a]atrim=start={a:.6f}:end={b:.6f},asetpts=PTS-STARTPTS[s{i}]" for i, (a, b) in enumerate(segs)]
        fc = ";".join(parts) + ";" + "".join(f"[s{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1[o]"
        open(os.path.join(P, f"seg{k}.fc"), "w").write(fc)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(ROOT, C["inbox_folder"], sp["file"]),
                        "-/filter_complex", os.path.join(P, f"seg{k}.fc"), "-map", "[o]", "-ar", "16000", "-ac", "1",
                        "-c:a", "pcm_s16le", os.path.join(P, f"cut_spk{k}.wav")], check=True)
    # NOTE: a speaker's "absent" spans still contain their camera audio here; mute them if that track had no clip.
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(P, "cut_spk1.wav"), "-i", os.path.join(P, "cut_spk2.wav"),
                    "-filter_complex", "amix=inputs=2:normalize=0", "-c:a", "pcm_s16le", os.path.join(P, "cut_mix.wav")], check=True)
    print("wrote cut_mix.wav, cut_spk1.wav, cut_spk2.wav")
