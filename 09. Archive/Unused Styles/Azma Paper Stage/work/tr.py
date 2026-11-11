import sys,os
from faster_whisper import WhisperModel
R=os.path.dirname(os.path.abspath(__file__))
m=WhisperModel('small',device='cpu',compute_type='int8')
def ts(t):
    h=int(t//3600);mi=int(t%3600//60);s=t%60
    return f'{h:02d}:{mi:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}'
for n in range(1,16):
    o=f'{R}/transcripts/vid-{n}.srt'
    if os.path.exists(o): continue
    segs,info=m.transcribe(f'{R}/../Videos/vid-{n}.mp4',vad_filter=True)
    with open(o,'w') as f:
        for i,s in enumerate(segs,1): f.write(f'{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n\n')
    print(n,info.language,flush=True)
