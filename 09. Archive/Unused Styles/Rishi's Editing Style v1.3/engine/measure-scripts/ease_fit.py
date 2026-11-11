"""Fit an animation curve to standard easings.
python -I ease_fit.py data.csv COL [--f0 N --f1 N]   (csv from track.py, or any csv with frame + COL)
Normalises COL between its value at f0 and f1 (progress 0..1), compares against easings,
prints ranked fit (RMSE), duration in frames/ms, and overshoot % (spring/back detection)."""
import sys,csv,argparse,numpy as np
a=argparse.ArgumentParser(); a.add_argument("csv"); a.add_argument("col"); a.add_argument("--f0",type=int); a.add_argument("--f1",type=int)
o=a.parse_args(); rows=[r for r in csv.DictReader(open(o.csv)) if r.get(o.col) not in ("",None)]
fr=np.array([int(r["frame"]) for r in rows]); v=np.array([float(r[o.col]) for r in rows])
f0=o.f0 if o.f0 is not None else fr[0]; f1=o.f1 if o.f1 is not None else fr[-1]
sel=(fr>=f0)&(fr<=f1); fr,v=fr[sel],v[sel]
v0,v1=v[0],v[-1]
if abs(v1-v0)<1e-6: sys.exit("no change between f0 and f1")
p=(v-v0)/(v1-v0); x=(fr-fr[0])/(fr[-1]-fr[0])
over=max(0,(p.max()-1))*100
def bez(x1,y1,x2,y2):
    def f(xx):
        ts=np.linspace(0,1,2001); bx=3*(1-ts)**2*ts*x1+3*(1-ts)*ts**2*x2+ts**3; by=3*(1-ts)**2*ts*y1+3*(1-ts)*ts**2*y2+ts**3
        return np.interp(xx,bx,by)
    return f
E={"linear":lambda t:t,"easeInSine":lambda t:1-np.cos(t*np.pi/2),"easeOutSine":lambda t:np.sin(t*np.pi/2),
"easeInOutSine":lambda t:-(np.cos(np.pi*t)-1)/2,"easeOutQuad":lambda t:1-(1-t)**2,"easeInQuad":lambda t:t*t,
"easeInOutQuad":lambda t:np.where(t<.5,2*t*t,1-(-2*t+2)**2/2),"easeOutCubic":lambda t:1-(1-t)**3,"easeInCubic":lambda t:t**3,
"easeInOutCubic":lambda t:np.where(t<.5,4*t**3,1-(-2*t+2)**3/2),"easeOutQuart":lambda t:1-(1-t)**4,"easeInOutQuart":lambda t:np.where(t<.5,8*t**4,1-(-2*t+2)**4/2),
"easeOutQuint":lambda t:1-(1-t)**5,"easeOutExpo":lambda t:np.where(t>=1,1,1-2**(-10*t)),"easeInOutExpo":lambda t:np.where(t<.5,2**(20*t-10)/2,(2-2**(-20*t+10))/2),
"easeOutCirc":lambda t:np.sqrt(1-(t-1)**2),"easeOutBack(1.70)":lambda t:1+2.70158*(t-1)**3+1.70158*(t-1)**2,
"AE_easyEase(33%)":bez(.33,0,.67,1),"AE_easeOut_infl80":bez(0,0,.2,1),"css_ease":bez(.25,.1,.25,1),"apple_spring_like(.16,1,.3,1)":bez(.16,1,.3,1),"(.22,1,.36,1)":bez(.22,1,.36,1),
"(.65,0,.35,1)":bez(.65,0,.35,1),"(.83,0,.17,1)":bez(.83,0,.17,1),"(.7,0,.84,0)in":bez(.7,0,.84,0)}
res=sorted((float(np.sqrt(np.mean((E[k](x)-p)**2))),k) for k in E)
# best free cubic bezier (coarse grid search)
best=(9,None); g=np.linspace(0,1,11)
for x1 in g:
  for y1 in np.linspace(0,1.4,15):
    for x2 in g:
      for y2 in [0.6,0.8,0.9,1.0,1.05,1.1]:
        e=float(np.sqrt(np.mean((bez(x1,y1,x2,y2)(x)-p)**2)))
        if e<best[0]: best=(e,tuple(float(round(q,2)) for q in (x1,y1,x2,y2)))
n=fr[-1]-fr[0]
print(f"frames {fr[0]}->{fr[-1]} = {n} f = {n/30*1000:.0f} ms | value {v0:.1f} -> {v1:.1f} | overshoot {over:.1f}%")
print(f"best free cubic-bezier{best[1]} rmse {best[0]:.3f}")
for e,k in res[:6]: print(f"  {k:28s} rmse {e:.3f}")
print("progress per frame:", " ".join(f"{q:.2f}" for q in p))
