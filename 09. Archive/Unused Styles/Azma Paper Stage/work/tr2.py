import json,time,sherpa_onnx,subprocess,os,sys,numpy as np
BUDGET=float(os.environ.get('B','120'))
A=os.path.expanduser('~/asr'); R=os.path.dirname(os.path.abspath(__file__))
M=A+'/sherpa-onnx-whisper-small/small-'
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'encoder.int8.onnx',decoder=M+'decoder.int8.onnx',tokens=M+'tokens.txt',language='',task='transcribe',num_threads=4)
def ts(t):
    return f'{int(t//3600):02d}:{int(t%3600//60):02d}:{int(t%60):02d},{int(round((t-int(t))*1000)):03d}'
for n in sys.argv[1:]:
    o=f'{R}/transcripts/vid-{n}.srt'
    if os.path.exists(o): continue
    raw=subprocess.run(['ffmpeg','-v','quiet','-i',f'{R}/../Videos/vid-{n}.mp4','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,dtype=np.float32)
    c=sherpa_onnx.VadModelConfig(); c.silero_vad.model=A+'/silero_vad.onnx'; c.silero_vad.min_silence_duration=0.3; c.silero_vad.max_speech_duration=25; c.sample_rate=16000
    v=sherpa_onnx.VoiceActivityDetector(c,buffer_size_in_seconds=60)
    segs=[]
    for i in range(0,len(x),512):
        v.accept_waveform(x[i:i+512])
        while not v.empty(): segs.append((v.front.start,v.front.samples)); v.pop()
    v.flush()
    while not v.empty(): segs.append((v.front.start,v.front.samples)); v.pop()
    sp=[]
    for st,s in segs:
        s=np.asarray(s); L=len(s); pos=0
        while L-pos>12*16000:
            lo=pos+8*16000; hi=pos+11*16000
            w=np.abs(s[lo:hi]); k=lo+int(np.argmin(np.convolve(w,np.ones(1600)/1600,'same')[800:-800]))+800
            sp.append((st+pos,s[pos:k])); pos=k
        sp.append((st+pos,s[pos:]))
    segs=sp
    cf=os.path.expanduser(f'~/asr/cache{n}.json'); cache=json.load(open(cf)) if os.path.exists(cf) else {}
    T0=time.time(); out=[]; incomplete=False
    for st,s in segs:
        k=str(st)
        if k in cache: t=cache[k]
        elif time.time()-T0>BUDGET: incomplete=True; continue
        else:
            r=rec.create_stream(); r.accept_waveform(16000,s); rec.decode_stream(r); t=r.result.text.strip(); cache[k]=t; json.dump(cache,open(cf,'w'))
        if t: out.append((st/16000,(st+len(s))/16000,t))
    if incomplete: print(n,'partial',len(cache),'/',len(segs),flush=True); sys.exit()
    for st,s in []:
        r=rec.create_stream(); r.accept_waveform(16000,s); rec.decode_stream(r)
        t=r.result.text.strip()
        if t: out.append((st/16000,(st+len(s))/16000,t))
    with open(o,'w') as f:
        for i,(a,b,t) in enumerate(out,1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
    print(n,len(out),flush=True)
