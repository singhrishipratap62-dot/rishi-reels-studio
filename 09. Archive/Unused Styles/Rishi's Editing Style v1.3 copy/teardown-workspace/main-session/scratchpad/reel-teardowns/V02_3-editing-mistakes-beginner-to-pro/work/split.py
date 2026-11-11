import subprocess,sys,numpy as np
W,H=720,1280
rng=[(255,275),(400,425),(605,630),(708,735),(800,822),(985,1010),(1105,1120),(1300,1316)]
p=subprocess.Popen(["ffmpeg","-v","error","-i","src.mp4","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
n=0;out=[]
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3 or n>1316: break
    if any(a<=n<=c for a,c in rng):
        f=np.frombuffer(b,np.uint8).reshape(H,W,3)
        col=f[:,5:15].mean(1).mean(1); row=f[630:650].mean(0).mean(1)
        cream=col>200
        # boundary: last cream row from top contiguous
        ys=np.nonzero(cream)[0]
        bot=ys.max() if len(ys) else -1; top=ys.min() if len(ys) else -1
        xs=np.nonzero(row>200)[0]
        print(n,"creamY",top,bot,"frac",round(cream.mean(),3),"creamX",(xs.min(),xs.max()) if len(xs) else None)
    n+=1
