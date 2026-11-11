import subprocess,sys,numpy as np
src,f0,f1,x=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
W,H=720,1280
p=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
print("frame,edge,face_sharp")
n=0
while True:
  b=p.stdout.read(W*H*3)
  if len(b)<W*H*3 or n>f1: break
  if n>=f0:
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(int)
    col=f[:,x-20:x+20].mean(axis=1)
    blue=(col[:,2]>150)&(col[:,2]-col[:,0]>60)
    # lowest row of contiguous blue region from top
    e=0
    for y in range(H):
      if blue[y]: e=y
      elif y>e+30 and e>0: break
    g=f[e+40:e+440,200:520].mean(axis=2) if e<800 else f[:10,:10].mean(axis=2)
    lap=np.abs(g[:-2,1:-1]+g[2:,1:-1]+g[1:-1,:-2]+g[1:-1,2:]-4*g[1:-1,1:-1]).var()
    print(f"{n},{e},{lap:.1f}")
  n+=1
