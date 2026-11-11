# Builds the right-hand speaker column (576x1080): Kashish top, Aditya bottom, rounded cards + name pills.
import json, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
P=sys.argv[1]; T0=float(sys.argv[2]); T1=float(sys.argv[3])
SRC="/Users/rishi/Documents/Teaching Claude/03. Projects/Mock Case Interview/mock case, 4th November/"
segs=json.load(open(P+"/src_segments.json"))
# keep only the part of the timeline in [T0,T1)
out=[];t=0
for a,b in segs:
    d=b-a; lo,hi=max(t,T0),min(t+d,T1)
    if hi>lo: out.append((a+lo-t,a+hi-t))
    t+=d
W,H,R=544,516,10
m=Image.new("L",(W,H),0); ImageDraw.Draw(m).rounded_rectangle((0,0,W-1,H-1),R,fill=255); m.save(P+"/card_mask.png")
F="/System/Library/Fonts/Avenir Next.ttc"
def pill(name,role,fn):
    f1=ImageFont.truetype(F,24,index=2); f2=ImageFont.truetype(F,20,index=5)  # demi / regular
    w=int(f1.getlength(name)+f2.getlength(role)+56); im=Image.new("RGBA",(w,44),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,43),6,fill=(255,255,255,235)); d.text((18,8),name,font=f1,fill=(44,53,82))
    d.text((28+f1.getlength(name),11),role,font=f2,fill=(138,143,160)); im.save(P+"/"+fn)
pill("Kashish","Interviewer","pill_k.png"); pill("Aditya","Candidate","pill_a.png")
crop={"kashish":180,"aditya":276}
fc=[]
for s,name in enumerate(["kashish","aditya"]):
    labs=""
    for i,(a,b) in enumerate(out):
        fc.append(f"[{s}:v]trim=start={a:.6f}:end={b:.6f},setpts=PTS-STARTPTS[{name[0]}{i}]"); labs+=f"[{name[0]}{i}]"
    fc.append(f"{labs}concat=n={len(out)}:v=1:a=0,fps=30000/1001,crop=760:720:{crop[name]}:0,scale={W}:{H}:flags=lanczos,format=rgba[{name}c]")
    fc.append(f"[{name}c][{2}:v]alphamerge[{name}r]" if False else f"[{name}c][m{s}]overlay=0:0[{name}x]")
# rounded corners: use mask as alpha
fc=[x for x in fc if "[m" not in x]
fc+= ["[2:v]format=gray,split=2[m0][m1]",
      "[kashishc][m0]alphamerge[kr]","[adityac][m1]alphamerge[ar]",
      f"color=c=0xE9ECFD:s=576x1080:r=30000/1001:d={T1-T0:.4f}[bg]",
      "[bg][kr]overlay=16:16[b1]","[b1][ar]overlay=16:548[b2]",
      "[b2][3:v]overlay=32:472[b3]","[b3][4:v]overlay=32:1004,format=yuv420p[o]"]
open(P+"/speakers_fc.txt","w").write(";\n".join(fc))
cmd=["ffmpeg","-v","error","-y","-i",SRC+"kashish-792bb451-a8b5-46eb-a207-1-CFR.mp4","-i",SRC+"aditya-c26e72d6-e5e9-49c4-a155-1-CFR.mp4",
     "-loop","1","-i",P+"/card_mask.png","-loop","1","-i",P+"/pill_k.png","-loop","1","-i",P+"/pill_a.png",
     "-/filter_complex",P+"/speakers_fc.txt","-map","[o]","-t",f"{T1-T0:.4f}","-c:v","libx264","-crf","16","-preset","fast",P+f"/speakers_{int(T0)}_{int(T1)}.mp4"]
print(len(out),"segments"); subprocess.run(cmd,check=True)
