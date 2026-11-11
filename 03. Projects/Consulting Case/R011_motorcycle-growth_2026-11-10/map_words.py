import json
edl=json.load(open('edl.json'))['segments']; W={n:json.load(open(f'isl_{n}/words.json')) for n in ('4620','4621','4622')}
out=[]; t=0
for k,(n,a,b,_) in enumerate(edl):
    for s,e,w,i in W[n]:
        if a<=(s+e)/2<b: out.append([round(t+max(s,a)-a,3), round(t+min(e,b)-a,3), w, k])
    t+=b-a
json.dump(out,open('words_cut_raw.json','w'))
