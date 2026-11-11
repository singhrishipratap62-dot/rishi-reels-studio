"""Usage: python -I style_audio.py <wav> <frames.log> <out.json>
Full-mix audio measurement (used when stem separation is unavailable):
- HPSS percussive onsets (proxy for SFX hits: whooshes, pops, risers' ends)
- each visual cut (scene_score > 0.3 in frames.log) matched to the nearest onset: hit rate within
  +/-100 ms and the median offset (onset - cut, ms)
- per-onset cue character: duration, spectral centroid, attack (rise time), peak dBFS
- floor level between speech: 10th-percentile RMS in 50 ms windows (estimate of music bed under voice)
"""
import json, re, sys
import numpy as np, librosa

wav, log, out = sys.argv[1:4]
y, sr = librosa.load(wav, sr=22050, mono=True)
dur = len(y) / sr
times, scores = [], []
for line in open(log):
    m = re.search(r"pts_time:([\d.]+)", line)
    if m: times.append(float(m.group(1)))
    m = re.search(r"scene_score=([\d.]+)", line)
    if m: scores.append(float(m.group(1)))
cuts = [t for t, s in zip(times, scores) if s > 0.3 and t < dur]

_, yp = librosa.effects.hpss(y)
env = librosa.onset.onset_strength(y=yp, sr=sr)
on = librosa.onset.onset_detect(onset_envelope=env, sr=sr, units="time", backtrack=False, delta=0.3)
strength = env[librosa.time_to_frames(on, sr=sr)] if len(on) else np.array([])
strong = on[strength > np.percentile(strength, 75)] if len(on) else on

offs = []
for c in cuts:
    if len(strong):
        d = strong - c; i = np.argmin(np.abs(d))
        if abs(d[i]) <= 0.1: offs.append(d[i] * 1000)

cues = []
for t in strong:
    a, b = int(t * sr), int(min(dur, t + 0.6) * sr)
    seg = y[a:b]
    if len(seg) < 256: continue
    rms = librosa.feature.rms(y=seg, frame_length=512, hop_length=128)[0]
    pk = rms.argmax(); above = np.where(rms > rms.max() * 0.25)[0]
    cues.append({"t": round(float(t), 2),
                 "dur_ms": round(float((above[-1] - above[0] + 1) * 128 / sr * 1000)),
                 "attack_ms": round(float(pk * 128 / sr * 1000)),
                 "centroid_hz": round(float(librosa.feature.spectral_centroid(y=seg, sr=sr).mean())),
                 "peak_dbfs": round(float(20 * np.log10(np.abs(seg).max() + 1e-9)), 1)})

rms = librosa.feature.rms(y=y, frame_length=1102, hop_length=1102)[0]
db = 20 * np.log10(rms + 1e-9)
res = {"file": wav, "dur_s": round(dur, 1), "cuts": len(cuts), "strong_onsets": int(len(strong)),
       "onsets_per_s": round(len(strong) / dur, 2),
       "cuts_with_hit_100ms": len(offs), "hit_rate": round(len(offs) / max(1, len(cuts)), 2),
       "median_offset_ms": round(float(np.median(offs)), 0) if offs else None,
       "rms_p10_db": round(float(np.percentile(db, 10)), 1), "rms_p50_db": round(float(np.percentile(db, 50)), 1),
       "rms_p90_db": round(float(np.percentile(db, 90)), 1),
       "cue_medians": {k: float(np.median([c[k] for c in cues])) for k in ("dur_ms", "attack_ms", "centroid_hz", "peak_dbfs")} if cues else {},
       "cues": cues}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "cues"}))
