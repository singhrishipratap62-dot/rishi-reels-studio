"""Usage: python -I style_sheets.py <work_dir> [threshold]
Reads <work_dir>/frames/*.jpg + frames.log (from style_extract.sh).
- Cut stats: scene_score > 0.3 = cut; writes cuts.json (cut times, ASL).
- Dedup: keeps a frame only if its perceptual hash differs from every frame kept so far
  by more than `threshold` bits, so repeated talking-head angles collapse and
  distinct looks (graphics, B-roll, text cards) stay.
- Tiles kept frames 6x5 with timestamp labels into sheets/sheet_NN.jpg and writes sheets/index.csv.
"""
import json, re, sys
from pathlib import Path
from PIL import Image, ImageDraw
import imagehash

work = Path(sys.argv[1]); thr = int(sys.argv[2]) if len(sys.argv) > 2 else 12
log = (work / "frames.log").read_text().split("\n")
times, scores = [], []
for line in log:
    m = re.search(r"pts_time:([\d.]+)", line)
    if m: times.append(float(m.group(1)))
    m = re.search(r"scene_score=([\d.]+)", line)
    if m: scores.append(float(m.group(1)))
frames = sorted((work / "frames").glob("f_*.jpg"))
n = min(len(frames), len(times))
cuts = [times[i] for i in range(n) if i < len(scores) and scores[i] > 0.3]
dur = times[n - 1] if n else 0
shots = [b - a for a, b in zip([0] + cuts, cuts + [dur]) if b > a]
(work / "cuts.json").write_text(json.dumps({
    "duration_s": dur, "cuts": len(cuts), "asl_s": round(dur / (len(cuts) + 1), 2) if dur else None,
    "median_shot_s": round(sorted(shots)[len(shots) // 2], 2) if shots else None,
    "cut_times": cuts}, indent=0))

kept, hashes = [], []
for i in range(n):
    h = imagehash.phash(Image.open(frames[i]))
    if all(h - k > thr for k in hashes):
        hashes.append(h); kept.append(i)

out = work / "sheets"; out.mkdir(exist_ok=True)
for old in out.glob("*"): old.unlink()
W, H, C, R = 320, 180, 6, 5
rows = ["sheet,cell,time_s,mmss,scene_score"]
for s in range(0, len(kept), C * R):
    sheet = Image.new("RGB", (W * C, H * R), "black"); d = ImageDraw.Draw(sheet)
    for c, i in enumerate(kept[s:s + C * R]):
        x, y = (c % C) * W, (c // C) * H
        sheet.paste(Image.open(frames[i]), (x, y))
        t = times[i]; lab = f"{int(t // 60):02d}:{int(t % 60):02d}"
        d.rectangle([x, y, x + 46, y + 14], fill="black"); d.text((x + 3, y + 2), lab, fill="yellow")
        rows.append(f"{s // (C * R) + 1},{c + 1},{t:.2f},{lab},{scores[i] if i < len(scores) else ''}")
    sheet.save(out / f"sheet_{s // (C * R) + 1:02d}.jpg", quality=80)
(out / "index.csv").write_text("\n".join(rows))
print(f"{work.name}: frames={n} kept={len(kept)} sheets={-(-len(kept) // (C * R))} cuts={len(cuts)} asl={dur / (len(cuts) + 1):.1f}s")
