import subprocess,numpy as np,glob,os,sys
SR=8000
def dec(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32)
os.makedirs('work/audio/npy',exist_ok=True)
for v in range(1,16):
    np.save(f'work/audio/npy/vid-{v}.npy',dec(f'Videos/vid-{v}.mp4'))
for f in sorted(glob.glob('sfx/*.*')):
    n=os.path.splitext(os.path.basename(f))[0].strip(' -.')
    np.save(f'work/audio/npy/sfx_{n}.npy',dec(f))
print(len(os.listdir('work/audio/npy')))
