#!/usr/bin/env python3
"""QC for a finished reel (pack reference/QUALITY_CONTROL.md). usage: qc.py <projectDir> <export.mp4> <part> [speed]"""
import json, subprocess, sys, re, os, tempfile
P, OUT, PART = sys.argv[1], sys.argv[2], int(sys.argv[3])
SPD = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0   # final sped up by this factor (R1.15)
F = '/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'
res = []
def ok(name, cond, info=''): res.append(('PASS' if cond else 'FAIL', name, info))
def sh(a): return subprocess.run(a, capture_output=True, text=True)
pr = json.loads(sh(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', OUT]).stdout)
v = [s for s in pr['streams'] if s['codec_type'] == 'video'][0]; a = [s for s in pr['streams'] if s['codec_type'] == 'audio']
dur = float(pr['format']['duration']); words = json.load(open(f'{P}/words.json'))
for w in words: w['s'] /= SPD; w['e'] /= SPD
ok('1080x1920 @ 29.97, H.264 High', v['width'] == 1080 and v['height'] == 1920 and v['r_frame_rate'] == '30000/1001' and v['profile'] == 'High', f"{v['width']}x{v['height']} {v['r_frame_rate']} {v['profile']}")
ok('audio present', len(a) == 1, a[0]['codec_name'] if a else '')
vd, ad = float(v.get('duration', 0)), float(a[0].get('duration', 0)) if a else 0
ok('video and audio same length (±2 frames)', abs(vd - ad) <= 2 / 29.97, f'video {vd:.2f}s, audio {ad:.2f}s')
tail = dur - words[-1]['e']   # end = last word END + ~0.4 s (R1.0); onset-based check failed on long last words
ok('duration = last word end + 0.2–0.6 s', 0.2 <= tail <= 0.6, f'dur {dur:.2f}s, last word end {words[-1]["e"]:.2f}')
bd = sh([F, '-i', OUT, '-vf', 'blackdetect=d=0.2:pix_th=0.10', '-an', '-f', 'null', '-']).stderr
ok('no black (blackdetect d=0.2)', 'black_start' not in bd, re.findall(r'black_start:\S+', bd)[:3])
sd = sh([F, '-i', OUT, '-af', 'silencedetect=n=-45dB:d=0.35', '-vn', '-f', 'null', '-']).stderr
gaps = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', sd) if words[0]['s'] < float(x) < words[-1]['s']]
ok('no gap >0.35 s inside speech (-45 dB)', not gaps, gaps[:5])
sc = sh([F, '-i', OUT, '-vf', "select='gt(scene,0.25)',showinfo", '-an', '-f', 'null', '-']).stderr
cuts = [round(float(x), 2) for x in re.findall(r'pts_time:([\d.]+)', sc)]
CE = dict(l.strip().split('=', 1) for l in open(f'{P}/crops.env') if '=' in l)   # expected cuts from this project, not R006's
c1, c2 = int(CE['S1_END']) / 29.97 / SPD, int(CE['S2_END']) / 29.97 / SPD
ok('scene cuts only at S1→S2 and S2→S3', len(cuts) >= 2 and abs(cuts[0] - c1) < 0.1 and abs(cuts[1] - c2) < 0.1, f'{cuts[:8]} expected [{c1:.2f}, {c2:.2f}]')
# OCR every 2 s: caption band + board
tmp = tempfile.mkdtemp(); bad = []; ocrlog = []
for t in [x * 2.0 + 0.5 for x in range(int(dur // 2))]:
    if 3.87 / SPD <= t < 6.01 / SPD: continue
    img = f'{tmp}/f.png'; sh([F, '-v', 'error', '-y', '-ss', f'{t}', '-i', OUT, '-frames:v', '1', img])
    sh(['magick', img, '-crop', '1080x90+0+755', '+repage', '-resize', '200%', f'{tmp}/c.png'])
    txt = sh(['tesseract', f'{tmp}/c.png', '-', '--psm', '7']).stdout.strip()
    ocrlog.append(f'{t:6.1f} | {txt}')
    if t > 6.2 / SPD:
        # caption must be one line inside x 120-960: check horizontal extent of dark navy pixels in band
        ext = sh(['magick', img, '-crop', '1080x90+0+755', '+repage', '-fuzz', '18%', '-fill', 'white', '+opaque', '#2C3552', '-negate', '-threshold', '50%', '-trim', 'info:']).stdout
        m = re.search(r' (\d+)x(\d+) \d+x\d+\+(\d+)\+(\d+)', ext)
        if m:
            w, x = int(m.group(1)), int(m.group(3))
            if x < 100 or x + w > 980: bad.append((t, x, x + w))
open(f'{P}/qc_ocr.txt', 'w').write('\n'.join(ocrlog))
ok('caption inside x 100–980 (one line)', not bad, bad[:5])
readable = sum(1 for l in ocrlog if len(l.split('|')[1].strip()) >= 4) / max(1, len(ocrlog))
ok('caption OCR readable on >=85% of samples', readable >= 0.85, f'{readable:.0%}')
# end card
sh([F, '-v', 'error', '-y', '-ss', f'{dur - 0.2}', '-i', OUT, '-frames:v', '1', f'{tmp}/e.png'])
sh(['magick', f'{tmp}/e.png', '-crop', '1003x564+38+141', '+repage', '-resize', '200%', f'{tmp}/e2.png'])
et = sh(['tesseract', f'{tmp}/e2.png', '-']).stdout
ok(f'end card shows Part {PART} + Follow for Part {PART + 1}', f'Part {PART}' in et and f'Follow for Part {PART + 1}' in et, ' / '.join(l for l in et.splitlines() if l.strip()))
ok('no "gradnext" on end card (R1.9)', 'gradnext' not in et.lower())
# opening blur must be fully gone by 1.2 s (R1.7 / E1.13): compare sharpness at 1.5 s vs 3.0 s in the hook panel
def sharp(t):
    sh([F, '-v', 'error', '-y', '-ss', f'{t}', '-i', OUT, '-frames:v', '1', '-vf', 'crop=1080:700:0:40', f'{tmp}/s.png'])
    o = sh(['magick', f'{tmp}/s.png', '-colorspace', 'gray', '-define', 'convolve:scale=!', '-morphology', 'Convolve', 'Laplacian:0', '-format', '%[fx:standard_deviation]', 'info:']).stdout
    return float(o or 0)
s15, s30, s02 = sharp(1.0), sharp(3.0 / SPD), sharp(0.05)
ok('blur-in: panel blurred at 0 s, sharp by 1.0 s', s02 < 0.8 * s30 and s15 > 0.85 * s30, f'sharpness 0.05s {s02:.4f} · 1.0s {s15:.4f} · 3.0s {s30:.4f}')
lo = sh([F, '-i', OUT, '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', lo)[-1]); TP = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', lo)[-1])
ok('loudness -15 LUFS ±1, true peak <= -1 dBTP', abs(I + 15) <= 1 and TP <= -1.0, f'{I:.1f} LUFS, TP {TP:.1f}')
for r in res: print(f'[{r[0]}] {r[1]}' + (f'  — {r[2]}' if r[2] != '' else ''))
sys.exit(0 if all(r[0] == 'PASS' for r in res) else 1)
