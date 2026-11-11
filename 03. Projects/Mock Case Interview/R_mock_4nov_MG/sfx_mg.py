# SFX stem for the MG timeline. Sound rules: 01. Styles/Minimal Edit/reference/SOUND_DESIGN.md + 01. Styles/Consulting Case/reference/SOUND_DESIGN.md
# (lots of sound, each quiet; peaks aligned to the visual event; 110 ms rule; captions silent).
# usage: python sfx_mg.py <project_dir> <events.json> <duration_s> <out.wav> [voice_lufs]
import json, sys
import numpy as np, soundfile as sf

P, EV, DUR, OUT = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
VOICE = float(sys.argv[5]) if len(sys.argv) > 5 else -15.0
OFFSET = VOICE - (-15.0)          # style levels assume a -15 LUFS program; keep the same SFX-to-voice balance
LIB = "/Users/rishi/Documents/Teaching Claude/03. Projects/Consulting Case/R006_cooling-helmet-pricing_2026-11-05/sfx48/"
SR = 48000
info = json.load(open(LIB + "info.json"))
# visual event -> (sound, target peak dB in a -15 LUFS program, reason)
MAP = {
    "chapter": [("Swoosh", -16, "chapter change: board clears"), ("Mouse_click_different-", -22, "chapter tab activates")],
    "clear":   [("Swoosh", -19, "beat visual clears")],
    "hero":    [("Hi-Tech_Click_", -17, "client question box")],
    "count":   [("Hi-Tech_Click_", -17, "impact number")],
    "result":  [("Hi-Tech_Click_", -17, "result lands")],
    "icon":    [("Highlighter", -20, "icon draws")],
    "bar":     [("Highlighter", -19, "bar / strike draws")],
    "pop":     [("Pop_different-", -19, "chip / pill / card settles")],
    "label":   [("Modern_technology_pop", -22, "label")],
    "text":    [("Modern_technology_pop", -21, "text in")],
}
cues = []
for e in json.load(open(EV)):
    for snd, lvl, why in MAP.get(e["snd"], []):
        dt = 0.19 if snd == "Mouse_click_different-" else 0.0   # tab click just after the swoosh
        cues.append([e["t"] + dt, snd, lvl, why])
kept = []
for c in sorted(cues, key=lambda c: -c[2]):                     # within 110 ms the louder cue wins
    if all(abs(c[0] - k[0]) >= 0.11 for k in kept): kept.append(c)
kept.sort()
stem = np.zeros((int(DUR * SR), 2)); cache = {}
for t, snd, lvl, why in kept:
    if snd not in cache:
        x, _ = sf.read(LIB + snd + ".wav", always_2d=True)
        if x.shape[1] == 1: x = np.repeat(x, 2, axis=1)
        if snd == "Hi-Tech_Click_":
            x = x[:int(0.45 * SR)].copy(); x[-int(0.03 * SR):] *= np.linspace(1, 0, int(0.03 * SR))[:, None]
        cache[snd] = x
    x = cache[snd]; g = 10 ** ((lvl + OFFSET - info[snd]["peak_db"]) / 20)
    st = int((t - info[snd]["peak_t"]) * SR)
    if st < 0: x = x[-st:]; st = 0
    n = min(len(x), len(stem) - st)
    if n > 0: stem[st:st + n] += x[:n] * g
sf.write(OUT, stem, SR, subtype="PCM_24")
with open(OUT.replace(".wav", "_cues.md"), "w") as f:
    f.write(f"# SFX cue sheet\n\nVoice on the timeline ≈ {VOICE:.1f} LUFS, so every level below is placed {OFFSET:+.1f} dB lower in the stem "
            f"(the style levels are for a −15 LUFS program). {len(kept)} cues, {len(cues) - len(kept)} dropped by the 110 ms rule. Captions are silent.\n\n"
            "| # | Time | Sound | Peak (style dB) | Reason |\n|---|---|---|---|---|\n")
    for i, (t, snd, lvl, why) in enumerate(kept, 1):
        f.write(f"| {i} | {int(t // 60)}:{t % 60:06.3f} | {snd.replace('_', ' ').strip(' -')} | {lvl} | {why} |\n")
from collections import Counter
print(len(kept), "cues;", dict(Counter(c[1] for c in kept)), "peak", round(20 * np.log10(np.abs(stem).max() + 1e-9), 1), "dBFS")
