import numpy as np,re,collections,random
from scipy.signal import stft
SR=8000
def flux(x):
    f,t,Z=stft(x,SR,nperseg=256,noverlap=176);A=np.log1p(np.abs(Z)*50)
    hi=A[(f>=2000)].copy();lo=A[(f>=100)&(f<2000)]
    fx=np.maximum(np.diff(hi,axis=1),0).sum(0);return fx,hi.sum(0)
segs=collections.defaultdict(list)
for l in open('keys/INDEX.md'):
    m=re.match(r'- v(\d+) \| ([^|]+) \| ([^|]+) \|(.*)',l)
    if not m or m[2].strip()=='other':continue
    for p in m[2].split(','):
        p=p.strip();a=float(p.split('–')[0]);b=float(p.split('–')[1]) if '–' in p else None
        segs[int(m[1])].append((a,b,m[3].strip().split('+')[0].split('/')[0],m[4]))
stat=collections.defaultdict(lambda:[0,0]);rnd=[0,0];whoosh=collections.defaultdict(lambda:[0,0]);exitc=[0,0]
for v in range(1,16):
    x=np.load(f'audio/npy/vid-{v}.npy');fx,hi=flux(x);z=(fx-np.median(fx))/ (np.percentile(fx,90)-np.median(fx)+1e-9)
    hz=(hi-np.median(hi))/(np.percentile(hi,90)-np.median(hi)+1e-9)
    def spike(t,w=0.12):
        i=int(t*100);a=z[max(0,i-int(w*100)):i+int(w*100)+1];return a.size and a.max()>2.5
    def rise(t):
        i=int(t*100);a=hz[max(0,i-40):i+5]; return a.size and a.max()>2.0 and a[-10:].mean()>a[:10].mean()+0.8
    for a,b,ty,n in segs[v]:
        if ty in('captions','hook'):continue
        stat[ty][1]+=1;stat[ty][0]+=spike(a);whoosh[ty][1]+=1;whoosh[ty][0]+=rise(a)
        if b: exitc[1]+=1;exitc[0]+=spike(b)
    for _ in range(40):
        t=random.uniform(3,len(x)/SR-3);rnd[1]+=1;rnd[0]+=spike(t)
print('transient at entry (±0.12s):');[print(f'  {k:13s} {a}/{b} = {a/b:.0%}') for k,(a,b) in stat.items()]
print(f'  random baseline {rnd[0]}/{rnd[1]} = {rnd[0]/rnd[1]:.0%}')
print(f'  at exit {exitc[0]}/{exitc[1]} = {exitc[0]/exitc[1]:.0%}')
print('rising high-band 0.4s into entry (whoosh/riser-like):');[print(f'  {k:13s} {a}/{b} = {a/b:.0%}') for k,(a,b) in whoosh.items()]
