"""Paper Stage builder helpers: emit Tesseract editable-JSON layers + action batches."""
import json

W, H = 1080, 1920
EASE = {"type": "cubicBezier", "x1": 0.2, "y1": 0.8, "x2": 0.2, "y2": 1}   # RULEBOOK entry ease
EIO = {"type": "cubicBezier", "x1": 0.65, "y1": 0, "x2": 0.35, "y2": 1}
LIN = {"type": "linear"}
HOLD = {"type": "hold"}

F_LIGHT = ("Inter Light", "Regular")
F_REG = ("Inter", "Regular")
F_MED = ("Inter Medium", "Regular")
F_SEMI = ("Inter SemiBold", "Regular")
F_BOLD = ("Inter", "Bold")
F_PF = ("Playfair Display Medium", "Italic")


def hexc(h, a=1.0):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [a]


INK, LEAD, GHOST = hexc('1E1E1E'), hexc('6E6E6E'), hexc('CFCFCF')
WHITE = [1, 1, 1, 1]


def ms(s):
    return int(round(s * 1000))


def tf(x=0, y=0, ax=0, ay=0, s=100, r=0, o=100):
    sx, sy = (s, s) if not isinstance(s, (list, tuple)) else s
    return {"anchorPoint": [ax, ay], "position": [x, y], "scale": [sx, sy], "rotation": r, "opacity": o}


class Build:
    def __init__(self):
        self.nid = 100
        self.neff = 5000
        self.actions = []
        self.kid = 0

    def id(self):
        self.nid += 1
        return self.nid

    # ---- layers -------------------------------------------------------
    def rect(self, name, a, d, x, y, w, h, color, round_=0, o=100, ax=None, ay=None, stroke=None, grad=None, effects=None):
        L = {"type": "Rect", "id": self.id(), "name": name, "blendMode": "normal",
             "activeRange": {"start": ms(a), "duration": ms(d)},
             "transform": tf(x, y, w / 2 if ax is None else ax, h / 2 if ay is None else ay, o=o),
             "rect": {"size": [w, h], "fillColor": color, "roundness": round_, "position": [0, 0]}}
        if grad:
            (c0, c1), (p0, p1) = grad
            L["rect"]["fillPaint"] = {"type": "gradient", "gradientType": "linear", "start": p0, "end": p1,
                                      "stops": [{"offset": 0, "color": c0}, {"offset": 1, "color": c1}]}
        if stroke:
            L["rect"].update(strokeEnabled=True, strokeColor=stroke[0], strokeWidth=stroke[1])
        if effects:
            L["effects"] = effects
        return L

    def text(self, name, a, d, x, y, txt, font, size, color, just="left", box=None, o=100, track=0, ax=0, ay=0, effects=None):
        st = {"text": txt, "fontFamily": font[0], "fontStyle": font[1], "fontSize": size, "fillColor": color,
              "justification": just, "strokeWidth": 0, "tracking": track}
        if box:
            st.update(boxText=True, boxPosition=[0, 0], boxSize=box)
        L = {"type": "Text", "id": self.id(), "name": name, "blendMode": "normal",
             "activeRange": {"start": ms(a), "duration": ms(d)}, "transform": tf(x, y, ax, ay, o=o), "sourceText": st}
        if effects:
            L["effects"] = effects
        return L

    def image(self, name, a, d, x, y, w, h, asset, o=100):
        return {"type": "Image", "id": self.id(), "name": name, "blendMode": "normal",
                "activeRange": {"start": ms(a), "duration": ms(d)}, "transform": tf(x, y, w / 2, h / 2, o=o),
                "source": {"assetId": asset, "fit": "contain", "sourceRect": {"x": 0, "y": 0, "width": w, "height": h}}}

    def shape(self, name, a, d, cmds, fill=None, stroke=None, x=0, y=0, ax=0, ay=0, o=100, ellipse=None, grad=None, effects=None):
        sh = {"path": {"commands": cmds}, "fills": [], "strokes": []}
        if ellipse:
            sh["ellipse"] = {"position": ellipse[0], "size": ellipse[1]}
        if grad:
            (c0, c1), (p0, p1) = grad
            sh["fills"].append({"blendMode": "normal", "fillRule": "nonZeroWinding", "opacity": 100,
                                "paint": {"type": "gradient", "gradientType": "linear", "start": p0, "end": p1,
                                          "stops": [{"offset": 0, "color": c0}, {"offset": 1, "color": c1}]}})
        elif fill:
            sh["fills"].append({"blendMode": "normal", "fillRule": "nonZeroWinding", "opacity": 100,
                                "paint": {"type": "solid", "color": fill}})
        if stroke:
            sh["strokes"].append({"blendMode": "normal", "cap": "round", "join": "round", "miterLimit": 4, "opacity": 100,
                                  "width": stroke[1], "paint": {"type": "solid", "color": stroke[0]}})
        L = {"type": "Shape", "id": self.id(), "name": name, "blendMode": "normal",
             "activeRange": {"start": ms(a), "duration": ms(d)}, "transform": tf(x, y, ax, ay, o=o), "shape": sh}
        if effects:
            L["effects"] = effects
        return L

    def group(self, name, a, d, layers, x=0, y=0, ax=0, ay=0, s=100, effects=None):
        g = {"type": "Group", "id": self.id(), "name": name, "blendMode": "normal",
             "playback": {"type": "windowed", "inputRange": {"start": ms(a), "duration": ms(d)},
                          "mapping": {"type": "linear", "input": {"start": ms(a), "duration": ms(d)},
                                      "output": {"start": 0, "duration": ms(d)}}, "inputOffsetMs": 0},
             "transform": tf(x, y, ax, ay, s=s), "layers": layers}
        if effects:
            g["effects"] = effects
        return g

    def video(self, name, a, d, src_a, asset, dur_ms, vol=1.0, effects=None):
        return {"type": "Video", "id": self.id(), "name": name, "blendMode": "normal",
                "playback": {"type": "windowed", "inputRange": {"start": ms(a), "duration": ms(d)},
                             "mapping": {"type": "linear", "input": {"start": ms(a), "duration": ms(d)},
                                         "output": {"start": 0, "duration": ms(d)}}, "inputOffsetMs": ms(src_a)},
                "sourceRange": {"start": ms(src_a), "duration": ms(d)}, "sourceIntrinsicDuration": dur_ms,
                "volume": vol, "transform": tf(0, 0, 0, 0),
                "source": {"assetId": asset, "fit": "cover", "sourceRect": {"x": 0, "y": 0, "width": W, "height": H}},
                **({"effects": effects} if effects else {})}

    # ---- effects ------------------------------------------------------
    def blur(self, px=0):
        self.neff += 1
        return {"id": self.neff, "enabled": True, "effect": {"type": "gaussianBlur", "blurriness": px, "repeatEdgePixels": False, "layerSize": [W, H]}}

    def huesat(self, sat=0, light=0):
        self.neff += 1
        return {"id": self.neff, "enabled": True, "effect": {"type": "hueSaturation", "hue": 0, "saturation": sat, "lightness": light}}

    def effect_js(self, layer, eff, param, code):
        self.actions.append({"type": "setFxLayerEffectParamAnimator", "compositionId": "main", "layerId": layer["id"],
                             "effectId": eff["id"], "paramName": param,
                             "animator": {"type": "jsScript", "layerTimeJsCode": code}, "dependencies": []})

    def blur_in(self, layer, eff, t0=0.0, px=16, dur=0.17):
        """blur px->0 over dur, starting at layer-local t0 (seconds)."""
        self.effect_js(layer, eff, "blurriness",
                       f"const t=(input.time.seconds-{t0})/{dur};if(t<=0)return {px};if(t>=1)return 0;"
                       f"const e=1-Math.pow(1-t,3);return {px}*(1-e);")

    # ---- animation ----------------------------------------------------
    def kf(self, layer, prop, keys, color=False):
        """keys: [(t_seconds_local, value, easing)]"""
        out = []
        for t, v, e in keys:
            self.kid += 1
            out.append({"id": f"k{self.kid}", "layerTime": ms(t), "easing": e,
                        "value": {"type": "color", "value": v} if color else {"type": "float", "value": v}})
        self.actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main",
                             "property": {"layerId": layer["id"], "propertyType": prop}, "keyframes": out})

    def js(self, layer, prop, code):
        self.actions.append({"type": "setFxPropertyAnimator", "compositionId": "main",
                             "property": {"layerId": layer["id"], "propertyType": prop},
                             "animator": {"type": "jsScript", "layerTimeJsCode": code}, "dependencies": []})

    def fade_in(self, layer, t0=0.0, dur=0.17):
        self.kf(layer, "opacity", [(t0, 0, LIN), (t0 + dur, 100, EASE)])

    def scale_kf(self, layer, keys):
        self.kf(layer, "scaleX", keys)
        self.kf(layer, "scaleY", keys)

    def drift(self, layer, d, s0=100, s1=105):
        self.scale_kf(layer, [(0, s0, LIN), (d, s1, LIN)])

    def slide_in(self, layer, axis, frm, to, t0=0.0, dur=0.2):
        self.kf(layer, "position" + axis, [(t0, frm, LIN), (t0 + dur, to, EASE)])

    def ink(self, layer, t, frm=None, to=None):
        """ghost -> ink colour over 6 frames at local time t."""
        frm = frm or GHOST
        to = to or INK
        self.kf(layer, "fillColor", [(max(0, t - 0.01), frm, LIN), (t + 0.2, to, EASE)], color=True)


def save(doc, layers, actions, dur):
    doc["duration"] = dur
    doc["composition"]["layers"] = layers
    json.dump(doc, open('editable.json', 'w'), indent=1)
    json.dump(actions, open('edits.json', 'w'), indent=1)
