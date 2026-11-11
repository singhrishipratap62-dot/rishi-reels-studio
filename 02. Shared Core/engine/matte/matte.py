"""Person matte for behind-subject graphics (DEPTH_AND_ORBIT.md option A).

Robust Video Matting (MobileNetV3, TorchScript) -> a grayscale ALPHA video, same frame count as the input window.
White = speaker, black = background. Remotion/CSS uses it as a mask so graphics can sit BEHIND the speaker.

Usage (run with the existing venv, nothing else to install):
  "<studio root>/06. Tools/venv-style/bin/python" -I "<studio root>/02. Shared Core/engine/matte/matte.py" IN.mp4 OUT_matte.mp4 \
      [--start S] [--dur D] [--w 1080] [--h 1920] [--fps 30] [--ds 0.25] [--device auto|mps|cpu]

- Decodes with ffmpeg (rotation metadata is applied, so a portrait phone clip comes out upright), scales to --w x --h.
- --ds is RVM's downsample_ratio: ~0.25 for 1080x1920, 0.375-0.5 for 720x1280. Lower = faster, coarser edges.
- The recurrent state carries across frames (temporal stability); it resets only at the start of a run.
- Output is H.264 yuv420p (gray stored as luma), crf 10, so it plays everywhere. Frame N of the matte = frame N of the input window.
"""
import argparse, subprocess, sys, time
from pathlib import Path
import numpy as np
import torch

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--start", type=float, default=0.0); ap.add_argument("--dur", type=float, default=0.0)
ap.add_argument("--w", type=int, default=1080); ap.add_argument("--h", type=int, default=1920)
ap.add_argument("--fps", type=float, default=30.0); ap.add_argument("--ds", type=float, default=0.25)
ap.add_argument("--device", default="auto")
a = ap.parse_args()

model_path = Path(__file__).parent / "models" / "rvm_mobilenetv3_fp32.torchscript"
devs = ["mps", "cpu"] if a.device == "auto" else [a.device]
model = None
for d in devs:
    try:
        m = torch.jit.load(str(model_path), map_location=d).eval()
        z = torch.zeros(1, 3, 64, 64, device=d)
        with torch.no_grad(): m(z, None, None, None, None, 1.0)  # smoke test on this device
        model, device = m, d; break
    except Exception as e:
        print(f"[matte] {d} unavailable: {str(e)[:120]}", file=sys.stderr)
if model is None: sys.exit("no usable device")
print(f"[matte] device={device} size={a.w}x{a.h} ds={a.ds}", file=sys.stderr)

cmd = ["ffmpeg", "-v", "error", "-ss", str(a.start), "-i", a.src]
if a.dur: cmd += ["-t", str(a.dur)]
cmd += ["-vf", f"fps={a.fps},scale={a.w}:{a.h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
dec = subprocess.Popen(cmd, stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{a.w}x{a.h}",
                        "-r", str(a.fps), "-i", "-", "-c:v", "libx264", "-crf", "10", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", a.out], stdin=subprocess.PIPE)
rec = [None] * 4; n = 0; t0 = time.time(); fb = a.w * a.h * 3
with torch.no_grad():
    while True:
        b = dec.stdout.read(fb)
        if len(b) < fb: break
        x = torch.from_numpy(np.frombuffer(b, np.uint8).reshape(a.h, a.w, 3).copy()).to(device)
        x = x.permute(2, 0, 1).float().div(255).unsqueeze(0)
        fgr, pha, *rec = model(x, *rec, a.ds)
        enc.stdin.write((pha[0, 0].clamp(0, 1) * 255).byte().cpu().numpy().tobytes())
        n += 1
        if n % 30 == 0: print(f"[matte] {n} frames, {n/(time.time()-t0):.2f} fps", file=sys.stderr)
enc.stdin.close(); enc.wait(); dec.wait()
print(f"[matte] done: {n} frames in {time.time()-t0:.1f}s ({n/max(time.time()-t0,1e-6):.2f} fps) -> {a.out}", file=sys.stderr)
