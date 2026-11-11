#!/usr/bin/env python3
"""S2 punch-in settle (R1.13/R1.14): sub-pixel zoom Z0 -> 100 % with a sine ease-in-out, centred on the S2 crop.
ffmpeg's scale/crop snap to whole pixels per frame, which made the zoom wobble (E1.17). This renders each frame
with one affine transform (bicubic, sub-pixel) instead.
usage (project venv python): s2zoom.py <projectDir> [Z0=1.10]
reads cut.mp4 + crops.env (S2_CROP, S1_END, S2_END) -> board/s2zoom.mp4 (1080x1920, 29.97, CRF 10)
"""
import sys, os, subprocess, math, re
from PIL import Image
P = sys.argv[1]; Z0 = float(sys.argv[2]) if len(sys.argv) > 2 else 1.10
os.chdir(P); F = '/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'
env = dict(re.findall(r'^(\w+)=(\S+)', open('crops.env').read(), re.M))
cw, ch, cx0, cy0 = map(float, env['S2_CROP'].split(':')); a, b = int(env['S1_END']), int(env['S2_END']); N = b - a
W, H, OW, OH = 1440, 2560, 1080, 1920
cx, cy, s0 = cx0 + cw / 2, cy0 + ch / 2, OW / cw
dec = subprocess.Popen([F, '-v', 'error', '-i', 'cut.mp4', '-vf', f'select=between(n\\,{a}\\,{b - 1}),setpts=N/(30000/1001)/TB',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
os.makedirs('board', exist_ok=True)
enc = subprocess.Popen([F, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{OW}x{OH}', '-framerate', '30000/1001',
                        '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '10', '-pix_fmt', 'yuv420p', 'board/s2zoom.mp4'], stdin=subprocess.PIPE)
for f in range(N):
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: raise SystemExit(f'only {f} frames decoded, expected {N}')
    p = f / (N - 1); e = -(math.cos(math.pi * p) - 1) / 2          # sine ease-in-out, exact 100 % on the last frame
    S = s0 * (Z0 - (Z0 - 1) * e)
    im = Image.frombytes('RGB', (W, H), buf).transform((OW, OH), Image.Transform.AFFINE,
          (1 / S, 0, cx - (OW / 2) / S, 0, 1 / S, cy - (OH / 2) / S), resample=Image.Resampling.BICUBIC)
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait(); dec.kill()
print(f's2zoom: {N} frames, {Z0:.2f} -> 1.00, sine in-out')
