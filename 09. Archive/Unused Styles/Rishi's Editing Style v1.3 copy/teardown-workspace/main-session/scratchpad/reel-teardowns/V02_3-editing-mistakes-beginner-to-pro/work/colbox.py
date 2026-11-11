# colbox.py src f0 f1 x0 y0 x1 y1 mode  -> per-frame bbox of pixels matching colour mode
import subprocess,sys,numpy as np
src=sys.argv[1]; f0,f1,x0,y0,x1,y1=map(int,sys.argv[2:8]); mode=sys.argv[8]; W,H=720,1280
p=subprocess.Popen(["ffmpeg","-v","quiet","-i",src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
print("frame,t,area,cx,cy,bw,bh,left,top,right,bottom,mean_luma_el,sharpness")
n=0
while n<=f1:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    if n>=f0:
        f=np.frombuffer(b,np.uint8).reshape(H,W,3)[y0:y1,x0:x1].astype(int); r,g,bb=f[...,0],f[...,1],f[...,2]
        if mode=="blue": m=(bb-r>90)&(bb>170)
        elif mode=="black": m=(f.max(2)<40)
        elif mode=="red": m=(r-bb>120)&(r>180)
        elif mode=="white": m=(f.min(2)>=254)
        elif mode=="dark": m=(f.mean(2)<120)
        elif mode=="eye": m=(f.mean(2)<150)|((r-bb)>40)
        ys,xs=np.nonzero(m); A=len(xs)
        if A<5: print(f"{n},{n/30:.3f},0,,,,,,,,,,")
        else:
            l,t,rr,bo=xs.min()+x0,ys.min()+y0,xs.max()+x0,ys.max()+y0
            print(f"{n},{n/30:.3f},{A},{xs.mean()+x0:.1f},{ys.mean()+y0:.1f},{rr-l},{bo-t},{l},{t},{rr},{bo},{f.mean(2)[m].mean():.1f},0")
    n+=1
p.kill()
