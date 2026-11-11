#!/usr/bin/env python3
"""Sound pass (R1.10): 01. Styles/Minimal Edit/reference/SOUND_DESIGN.md rules applied to this pack's board events.
usage (project venv python): sfx.py <projectDir> <sfxLibDir>
Inputs: events.json (render.js --events), cut.mp4 (voice), sfx48/ (48 kHz WAV copies + info.json with peak times).
Outputs: sfx_stem.wav, voice_proc.wav, mix.wav (-15 LUFS, TP <= -1 dBTP), sound_cue_sheet.md
"""
import json, sys, os, random, subprocess, re
import numpy as np, soundfile as sf
P = sys.argv[1]; os.chdir(P)
F = '/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'; SR = 48000
ev = json.load(open('events.json')); info = json.load(open('sfx48/info.json'))
s1End, s2End = ev['s1End'], ev['s2End']
random.seed(6)
cues = []  # (time_of_peak, sound, level_dB, reason)
def C(t, snd, lvl, why): cues.append([round(t, 3), snd, lvl, why])

# --- scene-level cues ---
C(0.55, 'Woosh', -17, 'opening blur-in resolves')
C(s2End, 'Woosh', -17, 'cut into the board scene')
# --- board elements ---
for e in ev['els']:
    t, cls, txt = e['t'], e['cls'].split(' ')[0], e['text']
    if t < s2End: continue
    if cls in ('arrow', 'axl'): continue                       # ride on their row's cue
    if 'Follow for Part' in txt and 'Solving' in txt:            # end card
        C(t, 'Swoosh', -16, 'board -> end card'); continue
    if cls == 'qbox':
        C(t, 'Hi-Tech_Click_', -17, 'client question box (hero)')
        for m in e['moves']: C(m, 'Swoosh', -16, 'phase switch: board clears, question moves up')
        continue
    if cls == 'mk':
        if 'Regular' in txt: C(t + 0.12, 'Modern_technology_pop', -22, 'reference marker drops')
        else: C(t + 0.12, 'Riser_+_Tick', -19, f'number-line marker lands: {txt}')
        continue
    if cls == 'tab':
        C(t, 'Modern_technology_pop', -21, f'tab appears: {txt}')
        for st in e['states']: C(st, 'Mouse_click_different-', -22, f'tab state change: {txt}')
        continue
    if e['grid']: C(t, 'multi_flicker', -23, 'unit grid switches on'); continue
    if e['count'] and not e['bar']:
        C(t, 'Hi-Tech_Click_', -17, f'impact number: {txt}')
    elif e['svg']:
        C(t, 'Highlighter', -20, f'icon draws: {txt or "icon"}')
    elif cls in ('qp', 'ap', 'fv', 'ph') or e['m'] == 'pop':
        C(t, 'Pop_different-', -19, f'piece settles: {txt}')
    elif cls in ('lbl', 'fl', 'sub'):
        C(t, 'Modern_technology_pop', -22, f'label: {txt}')
    elif not e['bar']:
        C(t, 'Modern_technology_pop', -21, f'element in: {txt}')
    for bt in e['bars']: C(bt, 'Highlighter', -19, f'bar/strip draws: {txt}')
    for st in e['subs']: C(st, 'Pop_different-', -19, f'result lands: {txt}')
# --- NO per-word sounds (R1.12): captions and the hook word-darkening stay silent; only animations get SFX ---
if os.environ.get('CAPTION_TICKS') == '1':
    for ph in ev['caps']:
        for w in ph:
            if s1End <= w < s2End: continue
            C(w + 0.04, 'flick', -28 + random.uniform(-2, 2), 'caption word')

# --- one family per moment: within 110 ms the louder cue wins ---
cues.sort(key=lambda c: (c[0], -c[2]))
kept = []
for c in sorted(cues, key=lambda c: -c[2]):
    if all(abs(c[0] - k[0]) >= 0.11 for k in kept): kept.append(c)
kept.sort()
# opening lift: +3 dB in the first 5 s, easing to 0 by 6 s
for c in kept:
    lift = 3.0 if c[0] < 5 else (3.0 * (6 - c[0]) if c[0] < 6 else 0)
    c[2] = round(c[2] + lift, 1)

# --- render stem: align each file's PEAK to the cue time; scale so its peak hits the target level ---
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'cut.mp4'], capture_output=True, text=True).stdout)
stem = np.zeros((int((dur + 3) * SR), 2))
cache = {}
for t, snd, lvl, why in kept:
    if snd not in cache:
        x, sr = sf.read(f'sfx48/{snd}.wav', always_2d=True)
        if snd == 'Hi-Tech_Click_': x = x[:int(0.45 * SR)]; x[-int(0.03 * SR):] *= np.linspace(1, 0, int(0.03 * SR))[:, None]
        cache[snd] = x
    x = cache[snd]; g = 10 ** ((lvl - info[snd]['peak_db']) / 20)
    st = int((t - info[snd]['peak_t']) * SR)
    if st < 0: x = x[-st:]; st = 0
    n = min(len(x), len(stem) - st); stem[st:st + n] += x[:n] * g
stem = stem[:int(dur * SR)]
sf.write('sfx_stem.wav', stem, SR, subtype='PCM_24')

# --- voice chain (Minimal Edit): 75 Hz HPF -> 2.5:1 comp @ -24 dB (15/180 ms) -> makeup -> limiter -1.5 dBFS, then -15 LUFS ---
subprocess.run([F, '-v', 'error', '-y', '-i', 'cut.mp4', '-vn', '-af',
    'highpass=f=75,acompressor=threshold=-24dB:ratio=2.5:attack=15:release=180:makeup=4dB,alimiter=limit=-1.5dB:level=false',
    '-ar', str(SR), '-ac', '2', 'voice_chain.wav'], check=True)
def lufs(path, extra=''):
    o = subprocess.run([F, '-i', path, '-af', (extra + ',' if extra else '') + 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1]); TP = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', o)[-1]); LRA = float(re.findall(r'LRA:\s+(-?[\d.]+) LU', o)[-1])
    return I, TP, LRA
Iv, _, _ = lufs('voice_chain.wav')
subprocess.run([F, '-v', 'error', '-y', '-i', 'voice_chain.wav', '-af', f'volume={-15 - Iv:.2f}dB,alimiter=limit=-1.5dB:level=false', 'voice_proc.wav'], check=True)
# --- mix, then trim the program to -15 LUFS / TP <= -1 ---
subprocess.run([F, '-v', 'error', '-y', '-i', 'voice_proc.wav', '-i', 'sfx_stem.wav', '-filter_complex',
    '[0:a][1:a]amix=inputs=2:normalize=0:duration=first[m]', '-map', '[m]', 'mix_raw.wav'], check=True)
Im, _, _ = lufs('mix_raw.wav')
subprocess.run([F, '-v', 'error', '-y', '-i', 'mix_raw.wav', '-af', f'volume={-15 - Im:.2f}dB,alimiter=limit=-1.6dB:level=false', '-ar', str(SR), 'mix.wav'], check=True)
I, TP, LRA = lufs('mix.wav')

with open('sound_cue_sheet.md', 'w') as f:
    f.write(f'# R006 sound cue sheet (R1.10, Minimal Edit sound design)\n\nProgram: **{I:.1f} LUFS**, true peak **{TP:.1f} dBFS**, LRA {LRA:.1f} LU. '
            f'{len(kept)} cues ({len(cues) - len(kept)} dropped by the 110 ms rule). Peaks aligned to the visual event; level = target peak in the mix before the final −15 LUFS trim.\n\n'
            '| # | Time | Sound | Peak dB | Reason |\n|---|---|---|---|---|\n')
    for i, (t, snd, lvl, why) in enumerate(kept, 1):
        f.write(f'| {i} | {int(t // 60)}:{t % 60:06.3f} | {snd.replace("_", " ").strip()} | {lvl:+.1f} | {why} |\n')
from collections import Counter
print(f'{len(kept)} cues kept ({len(cues)} raw). Program {I:.1f} LUFS, TP {TP:.1f}, LRA {LRA:.1f}')
print(Counter(c[1] for c in kept))
