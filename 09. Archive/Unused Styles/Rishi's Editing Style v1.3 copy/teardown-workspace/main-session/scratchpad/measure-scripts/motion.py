"""per-frame motion signal: python motion.py src.mp4 out.csv
cols: frame,t,diff(mean abs diff vs prev, 0-255),luma,edge_diff,top/mid/bot region diffs, hist_chi (cut score)"""
import subprocess, sys, numpy as np
src,out=sys.argv[1],sys.argv[2]; W,H=90,160
p=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-vf",f"scale={W}:{H}","-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
prev=None; ph=None; rows=[]; n=0
while True:
    b=p.stdout.read(W*H)
    if len(b)<W*H: break
    f=np.frombuffer(b,np.uint8).reshape(H,W).astype(np.float32)
    h=np.histogram(f,32,(0,256))[0].astype(np.float32); h/=h.sum()
    if prev is None: d=np.zeros_like(f); chi=0
    else:
        d=np.abs(f-prev); chi=float(((h-ph)**2/(h+ph+1e-6)).sum())
    t=n/30.0
    rows.append(f"{n},{t:.3f},{d.mean():.2f},{f.mean():.1f},{d[:53].mean():.2f},{d[53:107].mean():.2f},{d[107:].mean():.2f},{chi:.4f}")
    prev=f; ph=h; n+=1
open(out,"w").write("frame,t,diff,luma,diff_top,diff_mid,diff_bot,cut_chi\n"+"\n".join(rows)+"\n")
