import subprocess,sys,numpy as np
src,f0,f1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); W,H=720,1280
p=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
print("frame,top,bottom,left,right,cx,cy,w,h,tilt_deg,textTop,textLeft")
n=0
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3 or n>f1: break
    if n>=f0:
        f=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(int)
        r,g,bb=f[...,0],f[...,1],f[...,2]
        m=(r-bb>60)&(r>120)  # orange/warm card pixels
        ys,xs=np.nonzero(m)
        dark=(f.max(2)<90)&~m
        # text = dark pixels outside card bbox
        out=""
        if len(xs)>500:
            t,bo,l,ri=ys.min(),ys.max(),xs.min(),xs.max()
            # tilt from top-edge: first card row in two columns
            c1,c2=l+int((ri-l)*.25),l+int((ri-l)*.75)
            def first(c):
                col=np.nonzero(m[:,c])[0]; return col.min() if len(col) else np.nan
            y1,y2=first(c1),first(c2)
            tilt=np.degrees(np.arctan2(y2-y1,c2-c1))
            out=f"{t},{bo},{l},{ri},{xs.mean():.1f},{ys.mean():.1f},{ri-l},{bo-t},{tilt:.2f}"
        else: out=",,,,,,,,"
        d2=dark.copy(); 
        if len(xs)>500: d2[max(t-15,0):bo+15, max(l-15,0):ri+15]=False
        ty,tx=np.nonzero(d2[:, :])
        out+= f",{ty.min() if len(ty) else ''},{tx.min() if len(tx) else ''}"
        print(f"{n},{out}")
    n+=1
