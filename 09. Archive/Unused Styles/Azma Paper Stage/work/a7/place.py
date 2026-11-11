import re,subprocess,json,collections
idx=open('keys/INDEX.md').read().splitlines()
segs=collections.defaultdict(list)
for l in idx:
    m=re.match(r'- v(\d+) \| ([^|]+) \| ([^|]+) \| (.*)',l)
    if not m: continue
    v,t,ty,note=int(m[1]),m[2].strip(),m[3].strip(),m[4]
    if t=='other': continue
    for part in t.split(','):
        part=part.strip()
        if '–' in part: a,b=map(float,part.split('–'))
        else: a=float(part); b=a+1.5
        segs[v].append((a,b,ty.split('+')[0].split('/')[0],note))
def srt(v):
    out=[];txt=open(f'transcripts/vid-{v}.srt').read().strip().split('\n\n')
    for b in txt:
        ls=b.split('\n')
        if len(ls)<3: continue
        a,c=ls[1].split(' --> ')
        f=lambda s:(lambda h,m,x:int(h)*3600+int(m)*60+float(x.replace(',','.')))(*s.split(':'))
        out.append((f(a),f(c),' '.join(ls[2:])))
    return out
tot=collections.Counter();rows=[]
allg=[]
for v in range(1,16):
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'../Videos/vid-{v}.mp4']))
    S=sorted([s for s in segs[v] if s[2] not in('captions','hook')])
    cov=collections.Counter()
    for a,b,ty,_ in S: cov[ty]+=min(b,d)-a; tot[ty]+=min(b,d)-a
    g=sum(cov.values())
    # A-roll gaps
    t=0;gaps=[]
    for a,b,_,_ in S:
        if a>t: gaps.append(a-t)
        t=max(t,b)
    gaps.append(d-t)
    first=S[0][0] if S else None
    hook=sum(max(0,min(b,5)-a) for a,b,_,_ in S if a<5)
    durs=[b-a for a,b,_,_ in S]
    allg+=durs
    rows.append((v,round(d),len(S),round(len(S)/d*60,1),round(g/d*100),round(hook/5*100),first,round(max(gaps),1),round(sorted(gaps)[len(gaps)//2],1),round(sum(durs)/len(durs),1),dict((k,round(x)) for k,x in cov.items())))
print('v dur n per_min graphic% hook0-5% first_gfx longest_Aroll median_Aroll mean_gfx_dur cov')
for r in rows: print(*r)
print('total',{k:round(x) for k,x in tot.items()})
allg.sort();print('gfx dur p25/50/75/max',allg[len(allg)//4],allg[len(allg)//2],allg[3*len(allg)//4],allg[-1])
# outro: last graphic end vs duration
print('====')
import sys
for v in (7,15):
    L=srt(v);S=sorted([s for s in segs[v] if s[2] not in('captions','hook')])
    print('## v',v)
    t=0
    for a,b,ty,note in S+[(999,999,'end','')]:
        if a-t>4:
            tx=' '.join(x[2] for x in L if x[0]<a and x[1]>t)
            print(f'  [A-roll {t:.0f}-{min(a,1e3):.0f}] {tx[:140]}')
        if ty=='end':break
        # find the srt line(s) overlapping and approximate word position
        tx=''
        for s0,s1,txt in L:
            if s0<b and s1>a:
                w=txt.split();n=len(w)
                i0=max(0,int((a-s0)/(s1-s0)*n));i1=min(n,int((b-s0)/(s1-s0)*n)+1)
                tx+=' '.join(w[i0:i1])+' / '
        print(f'{a:.1f}-{b:.1f} {ty}: "{tx[:110]}"  <{note[:50]}>')
        t=max(t,b)
