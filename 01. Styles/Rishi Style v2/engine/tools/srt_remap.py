"""srt_remap.py — map an SRT timed on the ORIGINAL recording onto the ROUGH CUT.

Usage:  python srt_remap.py original.mp4 roughcut.mp4 original.srt out_roughcut.srt
Needs:  ffmpeg on PATH, numpy.

How it works (proven on roughcut_v3): raw-waveform cross-correlation FAILS when the rough-cut audio was processed,
so we match 0.6 s windows of log band-energy spectra (24 bands, 10 ms hop), find the original-time offset of every
window, group runs of equal offset into kept segments, then move each SRT chunk by its segment's offset.
Chunks that fall in removed takes are dropped; chunks that straddle a cut keep only their surviving part —
check those by ear (they're printed as WARN).
"""
import subprocess, sys
import numpy as np

SR, HOP, NF, WIN = 8000, 80, 256, 60


def pcm(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32)


def feat(x):
    fr = np.lib.stride_tricks.sliding_window_view(x, NF)[::HOP] * np.hanning(NF)
    sp = np.abs(np.fft.rfft(fr, axis=1)) ** 2
    ed = np.geomspace(2, 128, 25).astype(int)
    f = np.log(np.stack([sp[:, ed[i]:ed[i + 1] + 1].sum(1) for i in range(24)], 1) + 1e3)
    return f - f.mean(1, keepdims=True)


def segments(orig, rc):
    o, r = feat(pcm(orig)), feat(pcm(rc))
    on = [(o[k:k + WIN] - o[k:k + WIN].mean()) / (o[k:k + WIN].std() + 1e-6) for k in range(len(o) - WIN)]
    on = np.stack(on).reshape(len(on), -1)
    offs = []
    for st in range(0, len(r) - WIN, 10):
        w = r[st:st + WIN]; w = ((w - w.mean()) / (w.std() + 1e-6)).ravel()
        sc = on @ w / w.size
        k = int(sc.argmax())
        offs.append((st / 100, round(k / 100 - st / 100, 2), float(sc[k])))
    segs = []                       # (rc_start, rc_end, offset)
    for t, off, sc in offs:
        if sc < 0.9:
            continue
        if segs and abs(segs[-1][2] - off) < 0.06:
            segs[-1][1] = t + 0.6
        else:
            segs.append([t, t + 0.6, off])
    for i in range(1, len(segs)):   # split overlaps at the midpoint
        m = (segs[i - 1][1] + segs[i][0]) / 2
        segs[i - 1][1] = segs[i][0] = m
    segs[0][0] = 0
    segs[-1][1] = len(r) / 100
    return segs


def ts(s):
    h, m, x = s.split(':'); return int(h) * 3600 + int(m) * 60 + float(x.replace(',', '.'))


def fm(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"


def main(orig, rc, srt, out):
    segs = segments(orig, rc)
    print('kept segments (rc_start, rc_end, offset):'); [print(f'  {a:6.2f}–{b:6.2f}  +{o:.2f}') for a, b, o in segs]
    res = []
    for blk in open(srt, encoding='utf-8').read().strip().split('\n\n'):
        l = blk.split('\n'); a, c = map(ts, l[1].split(' --> ')); txt = ' '.join(l[2:])
        for s0, s1, o in segs:
            A, C = max(a, s0 + o), min(c, s1 + o)
            if C - A > 0.15 or C - A >= 0.5 * (c - a):
                if C - A < (c - a) * 0.95:
                    print(f'WARN straddles a cut, check by ear: {a:.2f} "{txt}"')
                res.append((A - o, C - o, txt)); break
    with open(out, 'w', encoding='utf-8') as f:
        for i, (a, c, t) in enumerate(res, 1):
            f.write(f"{i}\n{fm(a)} --> {fm(c)}\n{t}\n\n")
    print('wrote', out, len(res), 'chunks')


if __name__ == '__main__':
    main(*sys.argv[1:5])
