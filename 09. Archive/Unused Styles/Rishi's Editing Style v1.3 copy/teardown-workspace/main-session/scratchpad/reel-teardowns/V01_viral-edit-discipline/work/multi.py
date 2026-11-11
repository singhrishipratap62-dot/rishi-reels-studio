import subprocess,sys,numpy as np
W,H=720,1280
p=subprocess.Popen(["ffmpeg","-v","error","-i",sys.argv[1],"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
def bbox(m,x0=0,y0=0):
    if not m.any(): return "0,,,,,"
    ys,xs=np.nonzero(m); return f"{int(m.sum())},{xs.min()+x0},{ys.min()+y0},{xs.max()+x0},{ys.max()+y0},{xs.mean()+x0:.1f}"
out={k:open(f"m_{k}.csv","w") for k in ["typeon","holo","course","welcome","capOne","capEven","face"]}
for k,f in out.items(): f.write("frame,area,left,top,right,bottom,cx\n" if k not in("capOne","capEven") else "frame,top200_luma,n_white\n")
n=0
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3 or n>1420: break
    a=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(int); R,G,B=a[...,0],a[...,1],a[...,2]
    if 486<=n<=532:
        s=a[560:720]; m=(s[...,2]-s[...,0]>70)&(s[...,0]<140); out["typeon"].write(f"{n},{bbox(m,0,560)}\n")
    if 845<=n<=925:
        s=a[700:1200,200:720]; m=(s[...,2]>200)&(s[...,1]>170)&(s[...,0]<170); out["holo"].write(f"{n},{bbox(m,200,700)}\n")
    if 1095<=n<=1125:
        m=(R>170)&(G<70)&(B<90); out["course"].write(f"{n},{bbox(m)}\n")
    if 1018<=n<=1100:
        m=(R>190)&(G<90)&(B>150); out["welcome"].write(f"{n},{bbox(m)}\n")
        # face circle: dark-blue disk centre approx: pixels B>120,R<40,G<80
        m2=(B>110)&(R<35)&(G<90)&(G>40); out["face"].write(f"{n},{bbox(m2)}\n")
    if 1348<=n<=1372:
        s=a[640:760,120:250].mean(axis=2).ravel(); s.sort(); out["capOne"].write(f"{n},{s[-200:].mean():.1f},{int((s>200).sum())}\n")
    if 612<=n<=630:
        s=a[640:760,100:260].mean(axis=2).ravel(); s.sort(); out["capEven"].write(f"{n},{s[-200:].mean():.1f},{int((s>200).sum())}\n")
    n+=1
for f in out.values(): f.close()
