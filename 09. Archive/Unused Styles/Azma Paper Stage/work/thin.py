import os,glob,re,sys
from PIL import Image,ImageChops,ImageDraw
R=os.path.dirname(os.path.abspath(__file__))
tot=0
for n in range(1,16):
    fs=sorted(glob.glob(f'{R}/stills/vid-{n}/v{n}_t*.jpg'),key=lambda f:float(re.search(r't([\d.]+)\.jpg',f).group(1)))
    keep=[];lt=None;li=None
    for f in fs:
        t=float(re.search(r't([\d.]+)\.jpg',f).group(1)); im=Image.open(f).convert('L').resize((24,40))
        if lt is None: ok=True
        else:
            d=sum(ImageChops.difference(im,li).tobytes())/960
            ok=(t-lt>=1.0) or (t-lt>=0.5 and d>22)
        if ok: keep.append(f);lt=t;li=im
    tot+=len(keep)
    for i in range(0,len(keep),18):
        g=keep[i:i+18]; ims=[Image.open(f).convert('RGB') for f in g]
        cw=160; ch=int(cw*ims[0].height/ims[0].width)
        sh=Image.new('RGB',(cw*6,(ch+13)*3),'white'); dr=ImageDraw.Draw(sh)
        for k,(f,im) in enumerate(zip(g,ims)):
            x=(k%6)*cw;y=(k//6)*(ch+13); sh.paste(im.resize((cw,ch)),(x,y+13)); dr.text((x+2,y+1),os.path.basename(f)[:-4],fill='black')
        sh.save(f'{R}/sheets2/vid-{n}_p{i//18+1:02d}.jpg',quality=75)
    print(n,len(fs),len(keep),flush=True)
print(tot)
