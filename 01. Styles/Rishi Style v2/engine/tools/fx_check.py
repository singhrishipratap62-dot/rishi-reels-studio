"""fx_check.py — effects-only render check + SFX-only / voice-only exports.

Usage:  python fx_check.py <edit_folder> <project.tsrct> <base.tsrct> [--mp3]
  <edit_folder> must contain .tesseract-work/editable.json, .tesseract-work/edits.json and sound_cue_sheet.md.

1. Copies editable.json with the "Voice…" Audio layer muted, commits it into a copy of base.tsrct, applies edits.json,
   exports a 1080p effects-only MP4 (all exports are 1080×1920, always) (.tesseract-work/fxonly.mp4).
2. Checks every cue-sheet time has audio energy within ±60 ms (prints n/total + misses).
3. With --mp3: writes <name>_sfx_only.mp3 (from the fx-only render) and <name>_voice_only.mp3 (from sfx/voice.wav),
   320 kbps, 48 kHz stereo, same length as the video (Rishi asked for these as deliverables).
"""
import json, os, shutil, subprocess, sys
import numpy as np

TSRCT = os.path.expanduser('~/Library/Application Support/Tesseract/bin/tsrct')


def main(edit, project, base, *flags):
    w = os.path.join(edit, '.tesseract-work')
    d = json.load(open(os.path.join(w, 'editable.json')))
    for l in d['composition']['layers']:
        if l['type'] == 'Audio' and l['name'].startswith('Voice'):
            l['volume'] = 0.0
    json.dump(d, open(os.path.join(w, 'fxonly.json'), 'w'))
    fx = os.path.join(w, 'fxonly.tsrct'); shutil.copy(base, fx)
    subprocess.run([TSRCT, 'project', 'commit', '--project', fx, '--file', os.path.join(w, 'fxonly.json')], check=True, capture_output=True)
    subprocess.run([TSRCT, 'project', 'apply', '--project', fx, '--actions', os.path.join(w, 'edits.json')], check=True, capture_output=True)
    mp4 = os.path.join(w, 'fxonly.mp4')
    subprocess.run([TSRCT, 'export', '--project', fx, '--resolution', '1080p', '--output', mp4], check=True, capture_output=True)
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-f', 'f32le', '-ac', '1', '-ar', '48000', '-'], capture_output=True).stdout, np.float32)
    cues = [(float(r.split('|')[1]), r.split('|')[2].strip()) for r in open(os.path.join(edit, 'sound_cue_sheet.md')) if r.startswith('| ') and r[2].isdigit()]
    miss = [(t, n) for t, n in cues if 20 * np.log10(np.abs(x[max(0, int((t - .06) * 48000)):int((t + .06) * 48000)]).max() + 1e-9) <= -45]
    print(f'{len(cues) - len(miss)}/{len(cues)} cues present within ±60 ms', 'misses:', miss[:10])
    if '--mp3' in flags:
        name = os.path.splitext(os.path.basename(project))[0]
        dur = len(x) / 48000
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-vn', '-ar', '48000', '-ac', '2', '-c:a', 'libmp3lame', '-b:a', '320k', os.path.join(edit, name + '_sfx_only.mp3')], check=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(edit, 'sfx', 'voice.wav'), '-t', f'{dur:.2f}', '-ar', '48000', '-ac', '2', '-c:a', 'libmp3lame', '-b:a', '320k', os.path.join(edit, name + '_voice_only.mp3')], check=True)
        print('wrote SFX-only + voice-only MP3s')


if __name__ == '__main__':
    main(*sys.argv[1:])
