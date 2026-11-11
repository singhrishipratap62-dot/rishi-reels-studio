import subprocess,sys,numpy as np
from PIL import Image
pairs=[tuple(map(int,p.split(':'))) for p in sys.argv[2:]]
need=sorted({f for p in pairs for f in p}); W,H=180,320
p=subprocess.Popen(["ffmpeg","-v","error","-i",sys.argv[1],"-vf","scale=180:320","-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
fr={};n=0
while n<=need[-1]:
    b=p.stdout.read(W*H)
    if len(b)<W*H: break
    if n in need: fr[n]=Image.frombytes('L',(W,H),b)
    n+=1
p.kill()
def warp(im,s,dx,dy):
    w,h=round(W*s),round(H*s); im=im.resize((w,h),Image.BILINEAR); x0=(w-W)//2-dx; y0=(h-H)//2-dy
    return np.asarray(im.crop((x0,y0,x0+W,y0+H)),np.float32)
for a,b in pairs:
    B=np.asarray(fr[b],np.float32)
    def err(X): return np.abs(X[15:105,5:50]-B[15:105,5:50]).mean()+np.abs(X[15:105,140:175]-B[15:105,140:175]).mean()
    best=min((err(warp(fr[a],s,dx,dy)),s,dx,dy) for s in np.arange(0.85,1.35,0.01) for dx in range(-10,11) for dy in range(-10,11))
    print(f"{a}->{b}: scale {best[1]:.2f} dx {best[2]*4}px dy {best[3]*4}px err {best[0]:.2f} ident {err(np.asarray(fr[a],np.float32)):.2f}",flush=True)
