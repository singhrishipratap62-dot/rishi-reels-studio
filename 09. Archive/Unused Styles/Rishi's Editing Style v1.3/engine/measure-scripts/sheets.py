"""python sheets.py src.mp4 outdir fps  -> labelled contact sheets (8x3 tiles, 180x320 each)"""
import subprocess,sys,tempfile
from pathlib import Path
from PIL import Image,ImageDraw
src,od,fps=sys.argv[1],Path(sys.argv[2]),float(sys.argv[3]); od.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(dir=od) as tmp:
    subprocess.run(["ffmpeg","-v","error","-i",src,"-vf",f"fps={fps},scale=180:320",f"{tmp}/f_%04d.png"],check=True)
    fr=sorted(Path(tmp).glob("f_*.png")); C,R=8,3; per=C*R
    for s in range(0,len(fr),per):
        chunk=fr[s:s+per]; sheet=Image.new("RGB",(C*180,R*(320+16)),"white"); d=ImageDraw.Draw(sheet)
        for i,f in enumerate(chunk):
            k=s+i; t=k/fps; x,y=(i%C)*180,(i//C)*336
            sheet.paste(Image.open(f),(x,y+16)); d.text((x+3,y+2),f"{t:05.2f}s",fill="black")
        sheet.save(od/f"sheet_{s//per+1:02d}.jpg",quality=82)
