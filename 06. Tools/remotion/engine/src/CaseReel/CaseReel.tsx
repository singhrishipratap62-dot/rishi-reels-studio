// Consulting case reel (pack v2.0): the whole picture in one Remotion pass.
// S1 hook (panel blur-in over full-bleed face) -> S2 punch-in settle -> S3 board over the bg loop + face card (+ S4 end card,
// which lives on the board). Board, captions and hook panel come from the pack's own board.html engine (boardSrc.ts),
// driven by the project's words.json + beats.js, so the look and timing math stay identical to v1.x.
// The project folder's public/ dir is passed as --public-dir: reel.json, words.json, beats.js, hook.jpg, mbb.png, cut.mp4, bg.mp4.
import React, {useEffect, useLayoutEffect, useRef, useState} from 'react';
import {AbsoluteFill, Loop, OffthreadVideo, continueRender, delayRender, staticFile, useCurrentFrame} from 'remotion';
import {BOARD_BODY, BOARD_CSS, BOARD_SCRIPT} from './boardSrc';

export const FPS = 30000 / 1001;
type Crop = [number, number, number, number]; // w, h, x, y on the 1440x2560 working cut (ffmpeg crop order)
export type Reel = {
  frames: number; s1End: number; s2End: number; bgFrames: number;
  s1: Crop; s2: Crop; s3: Crop; z0: number; blurS: number; blurMax: number; panelH: number;
};
export type CaseReelProps = {green: boolean; reel: Reel | null};

const GREEN = '#00FF00';
const SRC_W = 1440, SRC_H = 2560;
const clamp = (x: number) => Math.max(0, Math.min(1, x));

// A crop of the working cut, scaled (and optionally zoomed about its centre) into a box. Sub-pixel CSS transform (E1.17).
const CropVideo: React.FC<{crop: Crop; w: number; h: number; zoom?: number}> = ({crop, w, h, zoom = 1}) => {
  const [cw, ch, cx0, cy0] = crop;
  const s = (w / cw) * zoom, cx = cx0 + cw / 2, cy = cy0 + ch / 2;
  return (
    <OffthreadVideo src={staticFile('cut.mp4')} muted
      style={{position: 'absolute', left: 0, top: 0, width: SRC_W, height: SRC_H, transformOrigin: '0 0',
        transform: `translate(${w / 2 - cx * s}px, ${h / 2 - cy * s}px) scale(${s})`}} />
  );
};

// The board.html engine, run once per tab, then seek(t) every frame.
type Engine = {seek: (t: number) => void};
const useBoardEngine = (root: React.RefObject<HTMLDivElement | null>) => {
  const [engine, setEngine] = useState<Engine | null>(null);
  useEffect(() => {
    const handle = delayRender('board engine');
    (async () => {
      const dataUrl = (f: string) => fetch(staticFile(f)).then((r) => r.blob()).then((b) => new Promise<string>((ok) => {
        const fr = new FileReader(); fr.onload = () => ok(fr.result as string); fr.readAsDataURL(b);
      }));
      const [words, beats, hook, mbb] = await Promise.all([
        fetch(staticFile('words.json')).then((r) => r.text()),
        fetch(staticFile('beats.js')).then((r) => r.text()),
        dataUrl('hook.jpg'), dataUrl('mbb.png'),  // board.html only uses the logo image for data: URLs
      ]);
      // captions are measured on a canvas at build time: the font must be loaded first
      await Promise.all(['400', '500', '600', '700'].map((w) => document.fonts.load(`${w} 52px 'Avenir Next'`)));
      root.current!.innerHTML = BOARD_BODY;
      const src = beats.replace('HOOKIMG', hook).replace('MBBIMG', mbb);
      // eslint-disable-next-line no-new-func
      const run = new Function(`var WORDS=${words};\n${src}\n${BOARD_SCRIPT}\nwindow.__ready(); return {seek: window.seek};`);
      setEngine(run() as Engine);
      await document.fonts.ready;
      continueRender(handle);
    })();
  }, [root]);
  return engine;
};

export const CaseReel: React.FC<CaseReelProps> = ({green, reel}) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const root = useRef<HTMLDivElement>(null);
  const engine = useBoardEngine(root);
  useLayoutEffect(() => { engine?.seek(t); }, [engine, t]);
  if (!reel) return null;
  const {s1End, s2End} = reel;
  const scene = frame < s1End ? 1 : frame < s2End ? 2 : 3;

  // S1 panel blur-in (R1.7/R1.11): sigma blurMax -> 0, ease-out, panel only (never the face). Not in the green export.
  const bp = clamp(t / reel.blurS), sigma = green ? 0 : reel.blurMax * Math.pow(1 - bp, 3);
  // S2 settle (R1.13/R1.14): z0 -> 1.00, sine in-out over the whole span, exactly 100 % on its last frame.
  const p2 = clamp((frame - s1End) / (s2End - s1End - 1)), z = reel.z0 - (reel.z0 - 1) * (-(Math.cos(Math.PI * p2) - 1) / 2);

  return (
    <AbsoluteFill style={{backgroundColor: scene === 1 ? '#fff' : GREEN}}>
      <style>{BOARD_CSS}</style>
      {scene === 1 && (
        <div style={{position: 'absolute', left: 0, top: reel.panelH, width: 1080, height: 1920 - reel.panelH, overflow: 'hidden', background: GREEN}}>
          {!green && <CropVideo crop={reel.s1} w={1080} h={1920 - reel.panelH} />}
        </div>
      )}
      {scene === 2 && !green && (
        <AbsoluteFill style={{overflow: 'hidden'}}><CropVideo crop={reel.s2} w={1080} h={1920} zoom={z} /></AbsoluteFill>
      )}
      {scene === 3 && (
        <Loop durationInFrames={reel.bgFrames}>
          <OffthreadVideo src={staticFile('bg.mp4')} muted style={{position: 'absolute', inset: 0, width: 1080, height: 1920}} />
        </Loop>
      )}
      {/* board layer. During the blur-in it is clipped to the panel so the blur never spills onto the face */}
      <div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: sigma > 0.01 ? reel.panelH : 1920, overflow: 'hidden',
        background: sigma > 0.01 ? '#fff' : 'transparent'}}>
        <div ref={root} className="cr-root" style={{position: 'absolute', left: 0, top: 0, filter: sigma > 0.01 ? `blur(${sigma}px)` : undefined}} />
      </div>
      {scene === 3 && (
        <div style={{position: 'absolute', left: 136, top: 858, width: 810, height: 908, borderRadius: 28, overflow: 'hidden', background: GREEN}}>
          {!green && <CropVideo crop={reel.s3} w={810} h={908} />}
        </div>
      )}
    </AbsoluteFill>
  );
};
