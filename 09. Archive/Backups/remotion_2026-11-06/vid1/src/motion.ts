import {Easing, interpolate} from 'remotion';

export const FPS = 30;
export const S = (sec: number) => Math.round(sec * FPS);

// Style Pack v1.1 colour tokens (reference values, [R1.1])
export const C = {
	blueTop: '#4279BB',
	blueBot: '#205AA4',
	white: '#FFFFFF',
	unspoken: '#8E8E8E',
	claudeCream: '#F4F2EC',
	cardDark: 'rgba(30,30,30,0.92)',
	textDark: '#1B1B1F',
	badgeBlue: '#2F80FF',
	claudeOrange: '#D97757',
	red: '#E83A3A',
	green: '#2FD26B',
};
export const SANS = "'Inter', system-ui, sans-serif";
export const SERIF = "'Playfair Display', Georgia, serif";
export const CARD_SHADOW = '0 24px 60px rgba(8,30,70,0.28), 0 4px 14px rgba(8,30,70,0.12)';

// MOTION_LIBRARY easings
export const EASE_OUT = Easing.bezier(0.1, 0.9, 0, 1);
export const EASE_HERO = Easing.bezier(0.1, 1.4, 0, 0.9);
export const EASE_SNAP = Easing.bezier(0, 0.9, 0, 1);
export const SLIDE_IN = Easing.bezier(0.5, 0.9, 0.4, 1);
export const PANE_IN = Easing.bezier(0.7, 0.1, 0.4, 0.9);
export const PANE_EXP = Easing.bezier(0.7, 0, 0.7, 0.8);
export const PANE_OUT = Easing.bezier(0.6, 0.1, 0.4, 0.9);
export const MORPH = Easing.bezier(0.2, 1.4, 0.6, 0.9);
export const SPRINGPOP = Easing.bezier(0.2, 1.4, 0.2, 1.1);
export const SHEET_RISE = Easing.bezier(0.7, 0.6, 0.6, 1);
export const CAPTION_IN = Easing.bezier(0.2, 0, 0, 0.9);

/** 0 → 1 progress of a move starting at `start` lasting `dur` frames */
export const prog = (f: number, start: number, dur: number, ease: (t: number) => number = EASE_OUT) =>
	interpolate(f, [start, start + dur], [0, 1], {easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

export const lin = (f: number, start: number, dur: number) =>
	interpolate(f, [start, start + dur], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
