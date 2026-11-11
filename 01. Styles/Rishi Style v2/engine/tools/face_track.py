"""face_track.py <video> [out.json] [--step 0.5]
Samples frames, finds the largest face (OpenCV YuNet, model file next to this script), writes per-sample face box,
chin_y and nose (x,y) as fractions of the frame. Used for:
  - K01 caption placement below the chin (caption_top = chin_y + 0.02, clamp 0.50-0.80)
  - K03 nose-tracked wiggle (follow nose with a few px lag)
Gaps (no face) are filled from the nearest sample. Runs on the laptop (cv2 only)."""
import cv2,json,sys
v=sys.argv[1];out=sys.argv[2] if len(sys.argv)>2 and not sys.argv[2].startswith('--') else v.rsplit('.',1)[0]+'.face.json'
step=float(sys.argv[sys.argv.index('--step')+1]) if '--step' in sys.argv else 0.5
cap=cv2.VideoCapture(v);fps=cap.get(5) or 30;n=int(cap.get(7));W=cap.get(3);H=cap.get(4)
import os
det=cv2.FaceDetectorYN.create(os.path.join(os.path.dirname(os.path.abspath(__file__)),'face_detection_yunet_2023mar.onnx'),'',(360,int(360*H/W)),0.7)
res=[];t=0.0
while t*fps<n:
    cap.set(1,int(t*fps));ok,f=cap.read()
    if not ok:break
    s=360/W;g=cv2.resize(f,(360,int(360*H/W)))
    _,fs=det.detect(g)
    if fs is not None and len(fs):
        r=max(fs,key=lambda r:r[2]*r[3]);r=[float(a) for a in r];x,y,w,h=[a/s for a in r[:4]];nx,ny=r[8]/s,r[9]/s;my=(r[11]+r[13])/2/s
        chin=my+(my-ny)*1.3  # chin estimated below the mouth
        res.append(dict(t=round(t,2),box=[round(x/W,3),round(y/H,3),round(w/W,3),round(h/H,3)],
            chin_y=round(max(chin,y+h)/H,3),nose=[round(nx/W,3),round(ny/H,3)]))
    else: res.append(dict(t=round(t,2),box=None))
    t+=step
last=None
for r in res:
    if r['box']:last=r
    elif last:r.update({k:last[k] for k in('box','chin_y','nose')},filled=True)
nxt=None
for r in reversed(res):
    if r['box']:nxt=r
    elif nxt:r.update({k:nxt[k] for k in('box','chin_y','nose')},filled=True)
json.dump(dict(video=v,width=W,height=H,fps=fps,step=step,samples=res),open(out,'w'))
ch=[r['chin_y'] for r in res if r.get('chin_y')]
print(out,len(res),'samples; faces found',sum(1 for r in res if not r.get('filled') and r['box']),'; chin_y median',sorted(ch)[len(ch)//2] if ch else None)
