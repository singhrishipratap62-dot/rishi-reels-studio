import shutil,subprocess,re,os,sys,glob
from PIL import Image,ImageDraw,ImageChops
R=os.path.dirname(os.path.abspath(__file__))
V=os.path.join(R,'..','Videos')
def stills(n):
    d=f'{R}/stills/vid-{n}'; os.makedirs(d,exist_ok=True)
    T=os.path.expanduser(f'~/tmpst/vid-{n}'); os.makedirs(T,exist_ok=True)
    for f in glob.glob(T+'/*.jpg'): os.remove(f)
    cmd=['ffmpeg','-hide_banner','-i',f'{V}/vid-{n}.mp4','-vf',"select='gt(scene,0.15)+isnan(prev_selected_t)+gte(t-prev_selected_t,2)',showinfo,scale=360:-2",'-vsync','vfr','-q:v','4',f'{T}/tmp_%04d.jpg']
    p=subprocess.run(cmd,capture_output=True,text=True)
    ts=[float(x) for x in re.findall(r'pts_time:([\d.]+)',p.stderr)]
    fs=sorted(glob.glob(T+'/tmp_*.jpg'))
    kept=[];prev=None
    for t,f in zip(ts,fs):
        im=Image.open(f).convert('L').resize((24,40))
        if prev is not None:
            diff=sum(ImageChops.difference(im,prev).getdata())/(24*40)
            if diff<3: continue
        prev=im; kept.append((t,f))
    out=[]
    for t,f in kept:
        nf=f'{d}/v{n}_t{t:06.2f}.jpg'; shutil.copyfile(f,nf); out.append(nf)
    return out
def sheets(n,files):
    for i in range(0,len(files),12):
        grp=files[i:i+12]; W,H=360,640
        ims=[Image.open(f).convert('RGB') for f in grp]; H=ims[0].height
        sh=Image.new('RGB',(W*6//1 if False else 4*W//2*1,0)) if False else None
        cw,ch=180,int(180*H/360)
        sheet=Image.new('RGB',(cw*6,(ch+14)*2),'white'); dr=ImageDraw.Draw(sheet)
        for k,(f,im) in enumerate(zip(grp,ims)):
            x=(k%6)*cw; y=(k//6)*(ch+14)
            sheet.paste(im.resize((cw,ch)),(x,y+14)); dr.text((x+2,y+1),os.path.basename(f)[:-4],fill='black')
        sheet.save(f'{R}/sheets/vid-{n}_s{i//12+1:02d}.jpg',quality=80)
if __name__=='__main__':
    for n in sys.argv[1:]:
        if os.path.exists(f'{R}/stills/vid-{n}/.done'): continue
        fl=stills(n); sheets(n,fl); open(f'{R}/stills/vid-{n}/.done','w').write(str(len(fl))); print(n,len(fl),flush=True)
