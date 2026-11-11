"""roman_captions.py — romanised-Hinglish word timings + caption SRT from a (rough-cut) SRT.

Usage:  python roman_captions.py roughcut.srt roman_map.json out_words.json out_captions.srt

roman_map.json maps each Devanagari / mixed SRT chunk to its romanised text EXACTLY as spoken, e.g.
  {"Claude में": "claude mein", "है। पहली": "pehli"}
Write it per video (Claude drafts it, Rishi checks words near cuts). Pure-English chunks are lower-cased automatically.
A chunk that still contains Devanagari after mapping stops the script, so nothing un-romanised slips into captions.

Word times are interpolated inside each SRT chunk by character length (good enough for word-by-word reveals;
re-check heroes that land on a cut). Caption groups: ≤ ~22 chars, ≤ 4 words, break at . , ? and at gaps > 0.3 s.
The build template uses out_words.json; out_captions.srt is just for reading.
"""
import json, re, sys


def ts(s):
    h, m, x = s.split(':'); return int(h) * 3600 + int(m) * 60 + float(x.replace(',', '.'))


def fm(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"


def main(srt, mapfile, out_words, out_srt):
    M = json.load(open(mapfile, encoding='utf-8'))
    words = []
    for blk in open(srt, encoding='utf-8').read().strip().split('\n\n'):
        l = blk.split('\n'); a, c = map(ts, l[1].split(' --> ')); t = ' '.join(l[2:])
        r = M.get(t, t.lower())
        if re.search('[ऀ-ॿ]', r):
            sys.exit(f'Not romanised, add to {mapfile}: "{t}"')
        ws = r.split(); tot = sum(len(w) for w in ws) or 1; x = a
        for w in ws:
            d = (c - a) * len(w) / tot; words.append(dict(s=round(x, 3), e=round(x + d, 3), w=w)); x += d
    json.dump(words, open(out_words, 'w'), ensure_ascii=False)
    caps, cur = [], []
    for w in words:
        L = len(' '.join(x['w'] for x in cur + [w]))
        if cur and (L > 22 or len(cur) >= 4 or w['s'] - cur[-1]['e'] > 0.3):
            caps.append(cur); cur = []
        cur.append(w)
        if re.search(r'[.,?]$', w['w']):
            caps.append(cur); cur = []
    if cur:
        caps.append(cur)
    with open(out_srt, 'w') as f:
        for i, c in enumerate(caps, 1):
            f.write(f"{i}\n{fm(c[0]['s'])} --> {fm(c[-1]['e'])}\n{' '.join(x['w'] for x in c)}\n\n")
    print(len(words), 'words,', len(caps), 'caption groups')


if __name__ == '__main__':
    main(*sys.argv[1:5])
