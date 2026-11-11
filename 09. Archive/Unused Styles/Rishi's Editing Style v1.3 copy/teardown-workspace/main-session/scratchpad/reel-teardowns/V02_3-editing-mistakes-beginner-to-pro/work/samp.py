import sys,numpy as np
from PIL import Image
def hx(c): return '#%02X%02X%02X'%tuple(int(v) for v in c)
def S(f,x0,y0,x1,y1,mode='med'):
    a=np.asarray(Image.open(f).convert('RGB'))[y0:y1,x0:x1].reshape(-1,3).astype(float)
    if mode=='med': return hx(np.median(a,0))
    if mode=='sat':  # most saturated pixels (text fill)
        s=a.max(1)-a.min(1); return hx(np.median(a[s>=np.percentile(s,90)],0))
    if mode=='bright': l=a.mean(1); return hx(np.median(a[l>=np.percentile(l,95)],0))
    if mode=='dark': l=a.mean(1); return hx(np.median(a[l<=np.percentile(l,5)],0))
for spec in sys.argv[1:]:
    f,*r=spec.split(':'); x0,y0,x1,y1=map(int,r[0].split(',')); m=r[1] if len(r)>1 else 'med'
    print(spec, S(f,x0,y0,x1,y1,m))
