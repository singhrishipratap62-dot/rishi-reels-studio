import subprocess,sys,numpy as np
W,H=720,1280
def frames(f0,f1):
    cmd=["ffmpeg","-v","quiet","-i","src.mp4","-vf",f"select='between(n\\,{f0}\\,{f1})'","-fps_mode","passthrough","-f","rawvideo","-pix_fmt","rgb24","-"]
    p=subprocess.run(cmd,capture_output=True).stdout
    n=len(p)//(W*H*3); a=np.frombuffer(p[:n*W*H*3],np.uint8).reshape(n,H,W,3)
    for i in range(n): yield f0+i,a[i]
for rng in sys.argv[1:]:
    f0,f1=map(int,rng.split('-'))
    print("##",rng)
    for n,im in frames(f0,f1):
        col=im[:, 20:60].astype(float); blue=(col[:,:,2]>150)&(col[:,:,2]-col[:,:,0]>60)
        rows=blue.mean(axis=1)>0.8
        # boundary = last blue row in contiguous top run
        b=0
        while b<H and rows[b]: b+=1
        g=im[300:700,200:520].mean(axis=2); lap=np.abs(g[:-2,1:-1]+g[2:,1:-1]+g[1:-1,:-2]+g[1:-1,2:]-4*g[1:-1,1:-1]).var()
        print(n,f"{n/30:.2f}","bound_y",b,f"{b/H*100:.1f}%","sharp",f"{lap:.1f}")
