"""Fit every track CSV in a reel's work/ (recursive). python -I fitall.py <reel>/work
Per csv: pick cols bw,bh,cx,cy (track.py format) with net change >=15% or >=40px; print start->end, frames, ms,
peak/final, best free bezier rmse + best named easing rmse; applies QUALITY_NOTES Q3 gate label."""
import sys,csv,glob,os,numpy as np
sys.path.insert(0,os.path.dirname(__file__))
CAND={"easeOutQuart":lambda t:1-(1-t)**4,"easeOutCubic":lambda t:1-(1-t)**3,"easeOutQuad":lambda t:1-(1-t)**2,"easeOutExpo":lambda t:1-2**(-10*t),
"easeInQuad":lambda t:t*t,"easeInCubic":lambda t:t**3,"easeInOutCubic":lambda t:np.where(t<.5,4*t**3,1-(-2*t+2)**3/2),"easeInOutQuad":lambda t:np.where(t<.5,2*t*t,1-(-2*t+2)**2/2),
"easeOutSine":lambda t:np.sin(t*np.pi/2),"easeOutBack":lambda t:1+2.70158*(t-1)**3+1.70158*(t-1)**2,"linear":lambda t:t}
def bez(p1x,p1y,p2x,p2y,t):
    u=np.linspace(0,1,400); x=3*(1-u)**2*u*p1x+3*(1-u)*u*u*p2x+u**3; y=3*(1-u)**2*u*p1y+3*(1-u)*u*u*p2y+u**3
    return np.interp(t,x,y)
G=[(a,b,c,d) for a in (0,.1,.2,.3,.4,.5,.7) for b in (0,.3,.6,.9,1.4) for c in (0,.2,.4,.6,.9) for d in (.6,.9,1,1.1)]
def run(path):
    rows=[r for r in csv.DictReader(open(path))]
    if not rows or "frame" not in rows[0]: return
    for col in ("bw","bh","cx","cy"):
        if col not in rows[0]: continue
        pts=[(int(r["frame"]),float(r[col])) for r in rows if r.get(col) not in ("",None)]
        if len(pts)<5: continue
        fr=np.array([p[0] for p in pts]); v=np.array([p[1] for p in pts])
        v0,v1=v[0],v[-1]; net=v1-v0
        if abs(net)<40 and abs(net)<.15*max(abs(v0),1): continue
        t=(fr-fr[0])/max(fr[-1]-fr[0],1); y=(v-v0)/net
        best=min(((np.sqrt(np.mean((bez(*g,t)-y)**2)),g) for g in G),key=lambda z:z[0])
        nm=min(((np.sqrt(np.mean((f(t)-y)**2)),n) for n,f in CAND.items()),key=lambda z:z[0])
        pk=(v.max() if net>0 else v.min())/v1 if v1 else 0
        gate="bezier[MEAS]" if best[0]<=.05 else ("named[MEAS]~" if best[0]<=.12 else "family-only[EST]")
        print(f"{os.path.relpath(path)[-34:]:34} {col} {v0:.0f}->{v1:.0f} #{fr[0]}-{fr[-1]} {round((fr[-1]-fr[0])*1000/30)}ms peak/final {pk:.2f} bez{best[1]} rmse{best[0]:.3f} {nm[1]} {nm[0]:.3f} {gate}")
for p in sorted(glob.glob(sys.argv[1]+"/**/*.csv",recursive=True)): run(p)
