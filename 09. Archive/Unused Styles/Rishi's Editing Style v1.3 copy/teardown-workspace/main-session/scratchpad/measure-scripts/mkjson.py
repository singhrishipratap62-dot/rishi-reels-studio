"""mkjson(reel_dir, prefix, rows): rows=(name,category,start_f,end_f,props,easing,bezier,overshoot_pct,trigger,evidence)
dur_ms=(end-start)*1000/30 (Q1); category 'style'/'cut' -> dur_ms None/0 (Q2)."""
import json
def mkjson(d,prefix,rows):
    out=[]
    for i,(n,c,s,e,p,ea,bz,ov,tw,ev) in enumerate(rows,1):
        dur=None if c=="style" else (0 if c=="cut" else round((e-s)*1000/30))
        out.append(dict(id=f"{prefix}-A{i:02d}",name=n,category=c,element=n,start_f=s,end_f=e,dur_ms=dur,props=p,easing=ea,bezier=bz,overshoot_pct=ov,trigger_word=tw,evidence=ev))
    json.dump(out,open(d+"/animations.json","w"),indent=1); print(len(out),"animations")
