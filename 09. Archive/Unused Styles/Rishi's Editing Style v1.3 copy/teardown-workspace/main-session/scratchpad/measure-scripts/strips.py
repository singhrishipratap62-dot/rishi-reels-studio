"""python -I strips.py src.mp4 outdir  -> EVERY native frame, 12x5 tiles (2 s per image), 144x256 each, labelled frame#/time"""
import subprocess,sys,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
src,od=sys.argv[1],Path(sys.argv[2]); od.mkdir(parents=True,exist_ok=True)
W,H,C,R=144,256,12,5
with tempfile.TemporaryDirectory(dir=od) as tmp:
    subprocess.run(["ffmpeg","-v","error","-i",src,"-vf",f"scale={W}:{H}",f"{tmp}/f_%05d.png"],check=True)
    fr=sorted(Path(tmp).glob("f_*.png")); per=C*R
    for s in range(0,len(fr),per):
        ch=fr[s:s+per]; im=Image.new("RGB",(C*W,R*(H+14)),"white"); d=ImageDraw.Draw(im)
        for i,f in enumerate(ch):
            k=s+i; x,y=(i%C)*W,(i//C)*(H+14)
            im.paste(Image.open(f),(x,y+14)); d.text((x+2,y+1),f"#{k} {k/30:.2f}s",fill="black")
        im.save(od/f"strip_{s/30:06.2f}s.jpg",quality=80)
