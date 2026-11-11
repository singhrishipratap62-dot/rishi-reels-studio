"""sfx_prep.py — measure peak level + peak time of every WAV in a folder → sfx_meta.json.

Usage:  python sfx_prep.py <sfx_folder> [out_meta.json]

The cue system in build_template.py aligns each sound's PEAK (not its file start) to the visual event and sets its
gain from the measured peak so every cue lands at its target dBFS in the mix. Re-run whenever a file is added or
re-trimmed. The pack's assets/sfx/ already ships trimmed files + sfx_meta.json.

Trimming recipe used for the pack (ffmpeg):
  short cues : -t <len> -af "afade=t=out:st=<len-0.05>:d=0.05"   (hitech 0.45, flick 0.35, highlighter 0.8, pop 0.5, …)
  swooshes   : -af "afade=t=in:d=0.25,afade=t=out:st=1.15:d=0.35"  (full length + fade-in = "smoother, longer")
  always     : -ar 48000 -ac 2  (convert MP3 → WAV before importing into Tesseract)
"""
import glob, json, os, subprocess, sys
import numpy as np


def main(folder, out=None):
    out = out or os.path.join(folder, 'sfx_meta.json')
    meta = {}
    for f in sorted(glob.glob(os.path.join(folder, '*.wav'))):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-f', 'f32le', '-ac', '1', '-ar', '48000', '-'], capture_output=True).stdout
        x = np.frombuffer(raw, np.float32); a = np.abs(x); i = int(a.argmax())
        meta[os.path.basename(f)[:-4]] = dict(peak_db=round(float(20 * np.log10(a.max() + 1e-9)), 1), peak_t=round(i / 48000, 3), dur=round(len(x) / 48000, 3))
    json.dump(meta, open(out, 'w'), indent=1)
    print(json.dumps(meta, indent=1))


if __name__ == '__main__':
    main(*sys.argv[1:3])
