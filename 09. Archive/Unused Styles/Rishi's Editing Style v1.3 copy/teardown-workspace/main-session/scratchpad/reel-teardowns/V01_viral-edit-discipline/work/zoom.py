import subprocess,sys,numpy as np
from PIL import Image
src=sys.argv[1]; pairs=[tuple(map(int,p.split(':'))) for p in sys.argv[2:]]
need=sorted({f for p in pairs for f in p}); W,H=720,1280
fr={}
p=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
n=0
while n<=need[-1]:
    b=p.stdout.read(W*H)
    if len(b)<W*H: break
    if n in need: fr[n]=np.frombuffer(b,np.uint8).reshape(H,W).astype(np.float32)
    n+=1
p.kill()
def warp(a,s,dx,dy):
    im=Image.fromarray(a.astype(np.uint8)); w,h=int(W*s),int(H*s)
    im=im.resize((w,h),Image.BILINEAR); x0=(w-W)//2-dx; y0=(h-H)//2-dy
    return np.asarray(im.crop((x0,y0,x0+W,y0+H)),np.float32)
for a,b in pairs:
    A,B=fr[a],fr[b]; best=None
    # region: background top-left 0-25% height (static wall), avoid face
    def err(X): return np.abs(X[60:420,20:200]-B[60:420,20:200]).mean()+np.abs(X[60:420,560:700]-B[60:420,560:700]).mean()
    for s in np.arange(0.90,1.30,0.01):
        for dx in range(-30,31,6):
            for dy in range(-30,31,6):
                e=err(warp(A,s,dx,dy))
                if best is None or e<best[0]: best=(e,s,dx,dy)
    e,s,dx,dy=best
    for s2 in np.arange(s-0.01,s+0.011,0.002):
        for dx2 in range(dx-6,dx+7,2):
            for dy2 in range(dy-6,dy+7,2):
                e2=err(warp(A,s2,dx2,dy2))
                if e2<best[0]: best=(e2,s2,dx2,dy2)
    print(f"{a}->{b}: scale {best[1]:.3f} dx {best[2]} dy {best[3]} err {best[0]:.2f} (identity err {err(A):.2f})")
