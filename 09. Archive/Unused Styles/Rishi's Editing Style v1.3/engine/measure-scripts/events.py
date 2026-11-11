"""python -I events.py motion.csv > events.md : index of hard cuts + animation bursts from the per-frame signal."""
import csv,sys,numpy as np
r=list(csv.DictReader(open(sys.argv[1]))); d=np.array([float(x["diff"]) for x in r]); c=np.array([float(x["cut_chi"]) for x in r])
base=np.median(d); print(f"# Motion index ({len(r)} frames, median frame diff {base:.2f})\n")
cuts=[i for i in range(1,len(r)) if c[i]>0.25 and d[i]>max(12,4*base)]
print("## Hard cuts / full-frame changes (frame: diff, hist-chi)"); print(", ".join(f"#{i} {i/30:.2f}s ({d[i]:.0f},{c[i]:.2f})" for i in cuts) or "none")
print("\n## Motion bursts (consecutive frames with diff > 2.2x median; start-end, peak)")
thr=2.2*base; i=0; out=[]
while i<len(d):
    if d[i]>thr:
        j=i
        while j+1<len(d) and d[j+1]>thr: j+=1
        if j-i>=1: out.append(f"#{i}-{j} ({i/30:.2f}-{j/30:.2f}s, {j-i+1}f, peak {d[i:j+1].max():.1f})")
        i=j+1
    else: i+=1
print("; ".join(out))
print(f"\nAvg shot length (hard cuts only): {len(r)/30/(len(cuts)+1):.2f}s over {len(cuts)+1} shots")
