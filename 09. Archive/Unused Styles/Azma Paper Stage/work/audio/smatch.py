import numpy as np,glob
from scipy.signal import stft,fftconvolve
SR=8000
def S(x):
    f,t,Z=stft(x,SR,nperseg=256,noverlap=176)
    m=(f>=800)&(f<=3900)
    return np.log1p(np.abs(Z[m])*50)
V={v:S(np.load(f'npy/vid-{v}.npy')) for v in range(1,16)}
res=[]
for fn in sorted(glob.glob('npy/sfx_*.npy')):
    n=fn[8:-4];x=np.load(fn);T=S(x)
    e=T.sum(0);keep=np.where(e>e.max()*0.15)[0]
    T=T[:,keep[0]:min(keep[-1]+1,keep[0]+120)]
    F,L=T.shape;Tz=(T-T.mean());Tn=np.sqrt((Tz**2).sum())
    if L<4: print(n,'too short');continue
    allh=[]
    for v,X in V.items():
        num=sum(fftconvolve(X[b],Tz[b][::-1],'valid') for b in range(F))
        s1=fftconvolve(X.sum(0),np.ones(L),'valid')
        s2=fftconvolve((X**2).sum(0),np.ones(L),'valid')
        nn=F*L;var=np.maximum(s2-s1**2/nn,1e-9)
        r=num/(np.sqrt(var)*Tn)
        order=np.argsort(-r);taken=[]
        for j in order[:3000]:
            if r[j]<0.45:break
            if all(abs(j-k)>50 for k in taken): taken.append(j);allh.append((v,j/100,r[j]))
    strong=[h for h in allh if h[2]>=0.6]
    print(f'{n:26s} L={L/100:.2f}s >=.45:{len(allh):3d} >=.6:{len(strong):3d} top:{[(h[0],round(h[1],1),round(h[2],2)) for h in sorted(allh,key=lambda h:-h[2])[:4]]}')
    res+= [(n,)+h for h in allh]
open('smatches.tsv','w').write('\n'.join(f'{a}\t{b}\t{c:.2f}\t{d:.2f}' for a,b,c,d in res))
