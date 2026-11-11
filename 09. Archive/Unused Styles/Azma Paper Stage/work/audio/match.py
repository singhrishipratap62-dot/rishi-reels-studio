import numpy as np,glob,os
from scipy.signal import fftconvolve
SR=8000
vids={v:np.load(f'npy/vid-{v}.npy') for v in range(1,16)}
out=open('matches.tsv','w');out.write('sfx\tvid\ttime\tncc\n')
for f in sorted(glob.glob('npy/sfx_*.npy')):
    n=f[8:-4];t=np.load(f)
    # trim leading/trailing quiet, cap 1.2 s
    a=np.abs(t);thr=a.max()*0.05;idx=np.where(a>thr)[0]
    t=t[idx[0]:min(idx[-1]+1,idx[0]+int(1.2*SR))];t=t-t.mean();L=len(t);tn=np.sqrt((t**2).sum())
    hits=[]
    for v,x in vids.items():
        c=fftconvolve(x,t[::-1],'valid')
        e=np.sqrt(np.maximum(fftconvolve(x**2,np.ones(L),'valid'),1e-9))
        ncc=c/(e*tn)
        # peaks
        i=np.argsort(-np.abs(ncc))
        taken=[]
        for j in i[:4000]:
            if abs(ncc[j])<0.35:break
            if all(abs(j-k)>SR*0.5 for k in taken):
                taken.append(j);hits.append((v,j/SR,abs(ncc[j])))
    for v,tt,s in sorted(hits): out.write(f'{n}\t{v}\t{tt:.2f}\t{s:.2f}\n')
    hs=[h for h in hits if h[2]>=0.5]
    print(f'{n:28s} L={L/SR:.2f}s hits>=.35:{len(hits):3d} >=.5:{len(hs):3d} vids:{sorted(set(h[0] for h in hs))}')
