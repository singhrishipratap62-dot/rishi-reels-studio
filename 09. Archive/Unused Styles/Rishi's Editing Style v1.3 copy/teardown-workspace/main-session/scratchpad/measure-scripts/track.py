"""Track an element across native frames to get keyframe curves.
python -I track.py src.mp4 f0 f1 x0 y0 x1 y1 --ref FRAME|bgcolor:R,G,B [--thr 25]
Region in SOURCE px (720x1280). For each frame: pixels differing from reference (a clean
background frame, or a flat colour) by > thr are 'element'. Outputs CSV:
frame,t,area,cx,cy,bw,bh,left,top,right,bottom,mean_luma_el,sharpness
Use cx/cy for position, bw/bh (or sqrt(area)) for scale, area/mean for opacity-ish, sharpness (Laplacian var) for blur."""
import subprocess,sys,argparse,numpy as np
a=argparse.ArgumentParser(); a.add_argument("src"); a.add_argument("f0",type=int); a.add_argument("f1",type=int)
for k in "x0 y0 x1 y1".split(): a.add_argument(k,type=int)
a.add_argument("--ref",required=True); a.add_argument("--thr",type=float,default=25)
o=a.parse_args(); W,H=720,1280
def frames():
    p=subprocess.Popen(["ffmpeg","-v","error","-i",o.src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    n=0
    while True:
        b=p.stdout.read(W*H*3)
        if len(b)<W*H*3: break
        yield n,np.frombuffer(b,np.uint8).reshape(H,W,3); n+=1
ref=None
if o.ref.startswith("bgcolor:"): ref=np.array([int(v) for v in o.ref[8:].split(",")],np.float32)
else: rf=int(o.ref)
store={}
print("frame,t,area,cx,cy,bw,bh,left,top,right,bottom,mean_luma_el,sharpness")
for n,f in frames():
    if ref is None and n==rf: ref=f[o.y0:o.y1,o.x0:o.x1].astype(np.float32)
    if o.f0<=n<=o.f1: store[n]=f[o.y0:o.y1,o.x0:o.x1].astype(np.float32)
    if n>max(o.f1, 0 if ref is not None else rf): break
for n in sorted(store):
    r=store[n]; d=np.abs(r-ref).max(axis=2); m=d>o.thr; A=int(m.sum())
    g=r.mean(axis=2); lap=np.abs(g[:-2,1:-1]+g[2:,1:-1]+g[1:-1,:-2]+g[1:-1,2:]-4*g[1:-1,1:-1]).var() if m.any() else 0
    if A==0: print(f"{n},{n/30:.3f},0,,,,,,,,,,"); continue
    ys,xs=np.nonzero(m); l,t,rr,b=xs.min()+o.x0,ys.min()+o.y0,xs.max()+o.x0,ys.max()+o.y0
    print(f"{n},{n/30:.3f},{A},{xs.mean()+o.x0:.1f},{ys.mean()+o.y0:.1f},{rr-l},{b-t},{l},{t},{rr},{b},{g[m].mean():.1f},{lap:.1f}")
