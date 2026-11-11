import React from 'react';
import {AbsoluteFill, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {
	C, S, SANS, SERIF, CARD_SHADOW, prog, lin,
	EASE_OUT, EASE_HERO, EASE_SNAP, SLIDE_IN, PANE_IN, PANE_EXP, PANE_OUT, MORPH, SPRINGPOP, SHEET_RISE, CAPTION_IN,
} from './motion';
import {GROUPS, END_S} from './captions';

const SPLIT = 922; // pane seam (48% H)
const FACE_SHIFT = 420; // source px kept above the seam so the face stays in the lower window

// ---------------------------------------------------------------- pane schedule (frames)
const paneH = (f: number): number => {
	if (f < S(0.5)) return 0; // face opener
	if (f < S(5.27)) return 1920; // beat 1-2: chat card + type beat (full blue)
	if (f < S(5.27) + 30) return SPLIT * prog(f, S(5.27), 30, PANE_IN); // pane-drop
	if (f < S(11.07)) return SPLIT;
	if (f < S(11.07) + 29) return SPLIT * (1 - prog(f, S(11.07), 29, PANE_OUT)); // pane-lift on "ghanta"
	if (f < S(12.46)) return 0;
	if (f < S(14.42)) return 1920; // beat 5 proof (full blue)
	if (f < S(14.42) + 20) return 1920 - (1920 - SPLIT) * prog(f, S(14.42), 20, PANE_OUT); // full -> split
	if (f < S(17.43)) return SPLIT;
	if (f < S(17.43) + 26) return SPLIT + (1920 - SPLIT) * prog(f, S(17.43), 26, PANE_EXP); // pane-expand
	if (f < S(20.91)) return 1920;
	if (f < S(20.91) + 29) return 1920 * (1 - prog(f, S(20.91), 29, PANE_OUT)); // lift to face
	if (f < S(23.04)) return 0;
	if (f < S(26.82)) return 1920; // beat 9 pipeline
	return 0;
};

type Mode = 'face' | 'top' | 'hidden';
const captionMode = (f: number): Mode => {
	if (f < S(0.5)) return 'face';
	if (f < S(4.1)) return 'top';
	if (f < S(5.27)) return 'hidden'; // type beat carries the words
	if (f < S(11.5)) return 'top';
	if (f < S(12.46)) return 'face';
	if (f < S(20.91)) return 'top';
	if (f < S(23.04)) return 'face';
	if (f < S(26.82)) return 'top';
	if (f < S(29.03)) return 'face';
	return 'top'; // CTA sheet owns the lower third
};

// ---------------------------------------------------------------- ground
const BlueGround: React.FC<{f: number}> = ({f}) => (
	<AbsoluteFill style={{background: `linear-gradient(180deg, ${C.blueTop} 0%, ${C.blueBot} 100%)`}}>
		{[0.12, 0.34, 0.58, 0.8].map((x, i) => (
			<div
				key={i}
				style={{
					position: 'absolute', top: -100, height: 2120, width: 150 + i * 30,
					left: `${(x * 100 + Math.sin((f + i * 40) / 140) * 3).toFixed(2)}%`,
					background: 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.10) 50%, rgba(255,255,255,0) 100%)',
					filter: 'blur(26px)', transform: 'skewX(-8deg)',
				}}
			/>
		))}
		<AbsoluteFill
			style={{
				backgroundImage: 'linear-gradient(rgba(255,255,255,0.05) 2px, transparent 2px), linear-gradient(90deg, rgba(255,255,255,0.05) 2px, transparent 2px)',
				backgroundSize: '64px 64px',
			}}
		/>
	</AbsoluteFill>
);

// ---------------------------------------------------------------- entrance helpers
/** hero-settle: scale .86 -> 1, rise 50px, blur 8 -> 0, fade 8f */
const hero = (f: number, start: number, dur = 30): React.CSSProperties => {
	const p = prog(f, start, dur, EASE_HERO);
	return {
		transform: `translateY(${50 * (1 - p)}px) scale(${0.86 + 0.14 * p})`,
		opacity: lin(f, start, 8),
		filter: `blur(${(8 * (1 - lin(f, start, 14))).toFixed(2)}px)`,
	};
};
/** card-snap: wipe in from the left edge */
const snap = (f: number, start: number, dur = 12, radius = 28): React.CSSProperties => {
	const p = prog(f, start, dur, EASE_SNAP);
	return {clipPath: `inset(0 ${(100 - 100 * p).toFixed(2)}% 0 0 round ${radius}px)`, opacity: lin(f, start, 4)};
};
/** slide-in card: x -60 -> 0 */
const slide = (f: number, start: number, dur = 12, dx = -60): React.CSSProperties => {
	const p = prog(f, start, dur, SLIDE_IN);
	return {transform: `translateX(${dx * (1 - p)}px)`, opacity: lin(f, start, 6)};
};
/** spring-pop for small objects */
const pop = (f: number, start: number, dur = 16): React.CSSProperties => {
	const p = prog(f, start, dur, SPRINGPOP);
	return {transform: `scale(${0.4 + 0.6 * p})`, opacity: lin(f, start, 4)};
};

const Asterisk: React.FC<{size: number; color?: string}> = ({size, color = C.claudeOrange}) => (
	<svg width={size} height={size} viewBox="-50 -50 100 100">
		{Array.from({length: 8}).map((_, i) => (
			<line key={i} x1={0} y1={0} x2={0} y2={-44} stroke={color} strokeWidth={13} strokeLinecap="round" transform={`rotate(${i * 45})`} />
		))}
	</svg>
);

const DocIcon: React.FC<{size?: number; color?: string}> = ({size = 52, color = C.badgeBlue}) => (
	<div style={{width: size, height: size, borderRadius: size * 0.26, background: color, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: size * 0.1, padding: size * 0.24}}>
		{[1, 0.7, 0.85].map((w, i) => <div key={i} style={{height: size * 0.07, width: `${w * 100}%`, background: '#fff', borderRadius: 4, opacity: 0.95}} />)}
	</div>
);

const typed = (text: string, f: number, start: number, fpc: number) =>
	text.slice(0, Math.max(0, Math.min(text.length, Math.floor((f - start) / fpc) + 1)));

const white = (extra: React.CSSProperties = {}): React.CSSProperties => ({
	background: C.white, borderRadius: 28, boxShadow: CARD_SHADOW, ...extra,
});

// ---------------------------------------------------------------- scene 1: Claude chat (beat 1-2)
const ChatScene: React.FC<{f: number}> = ({f}) => {
	const a = S(0.5);
	if (f < a || f >= S(4.1)) return null;
	const prompt = 'Edit this video like a pro';
	const struck = prog(f, S(3.0), 8, (t) => t);
	const dead = lin(f, S(3.3), 10);
	const dim = lin(f, S(3.3), 10);
	return (
		<AbsoluteFill>
			<div style={{position: 'absolute', left: 80, top: 480, width: 920, height: 560, ...hero(f, a), filter: `${hero(f, a).filter} blur(${(dim * 6).toFixed(1)}px)`}}>
				<div style={{...white({background: C.claudeCream, height: '100%', padding: 44, position: 'relative'})}}>
					<div style={{display: 'flex', alignItems: 'center', gap: 16}}>
						<Asterisk size={52} />
						<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 40, color: C.textDark}}>Claude</div>
					</div>
					<div style={{marginTop: 44, ...snap(f, a + 3, 12, 22), display: 'inline-flex', alignItems: 'center', gap: 14, background: '#fff', borderRadius: 22, padding: '16px 26px', boxShadow: '0 4px 14px rgba(0,0,0,0.08)'}}>
						<div style={{width: 44, height: 44, borderRadius: 12, background: '#16161a', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
							<div style={{borderLeft: '16px solid #fff', borderTop: '10px solid transparent', borderBottom: '10px solid transparent', marginLeft: 4}} />
						</div>
						<div style={{fontFamily: SANS, fontWeight: 500, fontSize: 32, color: C.textDark}}>video.mp4</div>
					</div>
					<div style={{marginTop: 34, fontFamily: SANS, fontWeight: 500, fontSize: 44, color: C.textDark, minHeight: 60, lineHeight: 1.25}}>
						{typed(prompt, f, S(1.11), 1.5)}
						<span style={{display: 'inline-block', width: 4, height: 44, background: C.claudeOrange, marginLeft: 4, verticalAlign: 'middle', opacity: Math.floor(f / 8) % 2 ? 0 : 1}} />
					</div>
				</div>
			</div>
			{/* "result" card */}
			<div style={{position: 'absolute', left: 430, top: 960, width: 570, height: 420, ...pop(f, S(1.73), 18), transformOrigin: '50% 50%'}}>
				<div style={{position: 'absolute', inset: 0, transform: `translateY(${dead * 20}px)`, filter: `grayscale(${dead}) saturate(${1 - dead * 0.5})`, opacity: 1 - dead * 0.35}}>
					<div style={{...white({height: '100%', overflow: 'hidden', borderRadius: 34})}}>
						<div style={{height: 300, background: 'linear-gradient(135deg,#ff5fa2,#ffb347 50%,#7b5cff)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 92}}>✨</div>
						<div style={{padding: '22px 30px', fontFamily: SANS, fontWeight: 700, fontSize: 36, color: C.textDark}}>Pro video ready</div>
					</div>
				</div>
				{/* red strike (negation) */}
				<svg viewBox="0 0 570 420" style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
					<path d="M -20 60 C 160 120, 360 300, 600 380" pathLength={1} stroke={C.red} strokeWidth={14} strokeLinecap="round" fill="none"
						strokeDasharray={1} strokeDashoffset={1 - struck} />
				</svg>
			</div>
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- scene 2: type beat (drum-roll)
const TypeBeat: React.FC<{f: number}> = ({f}) => {
	if (f < S(4.1) || f >= S(5.27)) return null;
	const second = f >= S(4.68);
	return (
		<AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>
			{!second ? (
				<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 88, color: '#fff', textAlign: 'center', lineHeight: 1.15, padding: '0 80px'}}>This doesn't work</div>
			) : (
				<div style={{fontFamily: SERIF, fontStyle: 'italic', fontWeight: 500, fontSize: 124, color: '#fff'}}>like that.</div>
			)}
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- scene 3: skills + repos wall (split pane, y 450-900)
const SKILLS = ['pdf-reader', 'seo-writer', 'web-scraper', 'sql-helper', 'ui-design', 'code-review', 'email-draft',
	'data-viz', 'translator', 'resume-fix', 'slide-maker', 'api-docs', 'test-writer', 'git-helper', 'brand-voice',
	'xlsx-tools', 'ocr-scan', 'meeting-notes', 'chart-maker', 'prompt-lab', 'doc-writer', 'seo-audit', 'log-parser',
	'form-filler', 'cal-sync', 'img-resize', 'copy-edit', 'lint-fix', 'ab-tester', 'pitch-deck', 'rss-reader', 'qa-bot', 'ocr-lite', 'sheet-bot', 'docx-tools', 'clip-maker', 'tag-sorter', 'note-linker', 'csv-clean', 'mail-merge', 'api-mock', 'file-sync'];
const REPOS = ['awesome-prompts', 'ai-toolkit', 'agent-kit', 'llm-recipes', 'mcp-servers', 'prompt-hub', 'auto-agents', 'dev-skills', 'ai-cookbook', 'open-agents', 'claude-tricks', 'skill-vault', 'tool-belt', 'agentic-kit', 'repo-radar', 'mega-list', 'build-bots', 'prompt-pack', 'ai-labs', 'code-agents'];
const COLS = 7;
const ROWS = 6;
const CW = 168, CH = 96, GAP = 14;

const Wall: React.FC<{f: number}> = ({f}) => {
	const a = S(5.27), b = S(8.17) + 12;
	if (f < a || f >= b) return null;
	const zoom = 1 - 0.3 * prog(f, S(7.55), 30, PANE_IN);
	const out = lin(f, S(8.17), 12);
	const gw = COLS * CW + (COLS - 1) * GAP;
	const gh = ROWS * CH + (ROWS - 1) * GAP;
	const cells: React.ReactNode[] = [];
	for (let r = 0; r < ROWS; r++) {
		for (let c = 0; c < COLS; c++) {
			const i = r * COLS + c;
			const x = c * (CW + GAP);
			const y = r * (CH + GAP);
			// skills wall-build on "skills"
			const sp = prog(f, S(5.89) + 1.2 * (r + c), 22, EASE_OUT);
			const isRepo = (r + c) % 2 === 1;
			const rp = prog(f, S(7.01) + 1.4 * (r + c), 14, SLIDE_IN);
			cells.push(
				<div key={'s' + i} style={{position: 'absolute', left: x, top: y, width: CW, height: CH, opacity: sp, transform: `scale(${0.8 + 0.2 * sp})`, filter: `blur(${6 * (1 - sp)}px)`}}>
					<div style={{...white({width: '100%', height: '100%', borderRadius: 20, display: 'flex', alignItems: 'center', gap: 10, padding: '0 16px', boxSizing: 'border-box'})}}>
						<Asterisk size={26} />
						<div style={{fontFamily: SANS, fontWeight: 500, fontSize: 20, color: C.textDark}}>{SKILLS[i % SKILLS.length]}</div>
					</div>
				</div>,
			);
			if (isRepo) {
				cells.push(
					<div key={'r' + i} style={{position: 'absolute', left: x, top: y, width: CW, height: CH, opacity: rp, transform: `translateX(${60 * (1 - rp)}px)`}}>
						<div style={{width: '100%', height: '100%', borderRadius: 20, background: 'rgba(30,30,30,0.92)', boxShadow: CARD_SHADOW, boxSizing: 'border-box', padding: '14px 16px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
							<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 19, color: '#fff'}}>{REPOS[i % REPOS.length]}</div>
							<div style={{fontFamily: SANS, fontWeight: 500, fontSize: 18, color: '#cfd6e0'}}>★ {(3 + ((i * 7) % 40)) / 2}k</div>
						</div>
					</div>,
				);
			}
		}
	}
	return (
		<div style={{position: 'absolute', left: 540 - gw / 2, top: 680 - gh / 2, width: gw, height: gh, transform: `scale(${zoom})`, opacity: 1 - out, filter: `blur(${out * 10}px)`}}>
			{cells}
		</div>
	);
};

// ---------------------------------------------------------------- scene 4: design-skill card -> doc (split pane)
const DesignDoc: React.FC<{f: number}> = ({f}) => {
	const a = S(8.17) + 6, b = S(11.07) + 29;
	if (f < a || f >= b) return null;
	const m = prog(f, S(9.47), 35, MORPH);
	const w = 440 + 220 * m;
	const h = 250 - 30 * m;
	const barsIn = lin(f, S(9.47) + 14, 16);
	return (
		<div style={{position: 'absolute', left: 540 - w / 2, top: 690 - h / 2, width: w, height: h, ...hero(f, a, 30)}}>
			<div style={{...white({height: '100%', padding: '26px 34px', boxSizing: 'border-box', overflow: 'hidden'})}}>
				<div style={{display: 'flex', alignItems: 'center', gap: 14}}>
					<Asterisk size={44} />
					<div style={{fontFamily: SANS, fontWeight: 700, fontSize: 38, color: C.textDark}}>design-skill</div>
				</div>
				<div style={{marginTop: 20, opacity: barsIn, display: 'flex', flexDirection: 'column', gap: 14}}>
					{[0.92, 0.7, 0.82].map((x, i) => <div key={i} style={{height: 14, width: `${x * 100}%`, background: '#D9DDE5', borderRadius: 8}} />)}
				</div>
			</div>
		</div>
	);
};

// ---------------------------------------------------------------- scene 5: "this video is the proof" (full blue)
const SessionScene: React.FC<{f: number}> = ({f}) => {
	const a = S(12.46);
	if (f < a || f >= S(14.42)) return null;
	return (
		<AbsoluteFill>
			<div style={{position: 'absolute', left: 90, top: 520, width: 900, height: 330, ...hero(f, a)}}>
				<div style={{...white({background: C.claudeCream, height: '100%', padding: 40, boxSizing: 'border-box'})}}>
					<div style={{display: 'flex', alignItems: 'center', gap: 14}}>
						<Asterisk size={46} />
						<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 36, color: C.textDark}}>Claude Code</div>
					</div>
					<div style={{marginTop: 34, fontFamily: SANS, fontWeight: 500, fontSize: 40, lineHeight: 1.3, color: C.textDark}}>
						<span style={{color: C.claudeOrange}}>&gt; </span>Read plan.md and continue from Phase 2.
					</div>
				</div>
			</div>
			<div style={{position: 'absolute', left: 90, top: 900, ...pop(f, S(13.35), 16)}}>
				<div style={{background: C.badgeBlue, color: '#fff', fontFamily: SANS, fontWeight: 700, fontSize: 44, padding: '18px 40px', borderRadius: 999, boxShadow: CARD_SHADOW}}>end-to-end</div>
			</div>
			<div style={{position: 'absolute', left: 90, top: 1080, width: 700, ...snap(f, S(14.01), 12, 28)}}>
				<div style={{...white({display: 'flex', alignItems: 'center', gap: 22, padding: '28px 32px'})}}>
					<DocIcon size={72} />
					<div>
						<div style={{fontFamily: SANS, fontWeight: 700, fontSize: 40, color: C.textDark}}>SKILL.md</div>
						<div style={{fontFamily: SANS, fontWeight: 500, fontSize: 28, color: '#7a7f8a', marginTop: 4}}>rishi-editing-style</div>
					</div>
				</div>
			</div>
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- scene 6: this edit vs AI slop (split pane)
const Contrast: React.FC<{f: number}> = ({f}) => {
	const a = S(14.42) + 12;
	if (f < a || f >= S(17.43) + 4) return null;
	const out = lin(f, S(17.43) - 4, 8);
	const x = prog(f, S(16.62), 10, (t) => t);
	const grey = lin(f, S(16.62) + 8, 8);
	return (
		<AbsoluteFill style={{opacity: 1 - out}}>
			<div style={{position: 'absolute', left: 60, top: 470, width: 450, height: 400, ...slide(f, S(15.28), 12)}}>
				<div style={{...white({height: '100%', overflow: 'hidden'})}}>
					<div style={{height: 270, background: `linear-gradient(180deg, ${C.blueTop}, ${C.blueBot})`, position: 'relative'}}>
						<div style={{position: 'absolute', left: 36, top: 40, width: 230, height: 130, borderRadius: 18, background: '#fff', boxShadow: '0 8px 20px rgba(0,0,0,0.18)'}} />
						<div style={{position: 'absolute', left: 170, top: 120, width: 220, height: 120, borderRadius: 18, background: 'rgba(255,255,255,0.88)', boxShadow: '0 8px 20px rgba(0,0,0,0.18)'}} />
					</div>
					<div style={{padding: '18px 26px', fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.textDark}}>this edit</div>
				</div>
			</div>
			<div style={{position: 'absolute', left: 570, top: 470, width: 450, height: 400, ...slide(f, S(16.38), 12, 60), filter: `grayscale(${grey})`}}>
				<div style={{...white({height: '100%', overflow: 'hidden'})}}>
					<div style={{height: 270, background: 'linear-gradient(135deg,#ff2d95,#ffb000 55%,#00e0ff)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 80, letterSpacing: 6}}>🔥🚀💥</div>
					<div style={{padding: '18px 26px', fontFamily: SANS, fontWeight: 800 as any, fontSize: 34, color: C.textDark}}>NEW!! AI VIDEO 🤯</div>
				</div>
				<svg viewBox="0 0 450 400" style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
					<path d="M 70 70 L 380 330 M 380 70 L 70 330" pathLength={1} stroke={C.red} strokeWidth={14} strokeLinecap="round" fill="none"
						strokeDasharray={1} strokeDashoffset={1 - x} />
				</svg>
			</div>
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- scene 7: real Style Pack files + counter (full blue)
const FILES = ['DESIGN_SYSTEM.md', 'SCENE_PRINCIPLES.md', 'MOTION_LIBRARY.md', 'EDITING_PSYCHOLOGY.md', 'SOUND_DESIGN.md'];
const Files: React.FC<{f: number}> = ({f}) => {
	const a = S(17.43) + 26;
	if (f < a || f >= S(20.91) + 8) return null;
	const out = lin(f, S(20.91), 8);
	const cnt = Math.round(15 * prog(f, S(17.96), 30, EASE_OUT));
	const bracket = (start: number, y0: number, y1: number, label: string) => {
		const p = prog(f, start, 11, (t) => t);
		return (
			<div style={{position: 'absolute', left: 0, top: 0}}>
				<svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
					<path d={`M 890 ${y0} L 912 ${y0} L 912 ${y1} L 890 ${y1}`} pathLength={1} stroke="#fff" strokeWidth={5} fill="none" strokeLinecap="round" strokeDasharray={1} strokeDashoffset={1 - p} />
				</svg>
				<div style={{position: 'absolute', left: 924, top: (y0 + y1) / 2 - 22, fontFamily: SERIF, fontStyle: 'italic', fontSize: 40, color: '#fff', opacity: lin(f, start + 6, 6)}}>{label}</div>
			</div>
		);
	};
	const top = 770, step = 108;
	return (
		<AbsoluteFill style={{opacity: 1 - out}}>
			<div style={{position: 'absolute', left: 90, top: 470, display: 'flex', alignItems: 'baseline', gap: 22, opacity: lin(f, S(17.96), 8)}}>
				<div style={{fontFamily: SANS, fontWeight: 700, fontSize: 160, color: '#fff', lineHeight: 1}}>{cnt}</div>
				<div style={{fontFamily: SANS, fontWeight: 500, fontSize: 48, color: '#fff'}}>reels studied</div>
			</div>
			{FILES.map((name, i) => {
				const st = S(17.96) + 4 * i;
				return (
					<div key={name} style={{position: 'absolute', left: 90, top: top + i * step, width: 790, ...slide(f, st, 12, -60)}}>
						<div style={{...white({display: 'flex', alignItems: 'center', gap: 20, padding: '0 28px', height: 92, borderRadius: 26})}}>
							<DocIcon size={48} />
							<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 34, color: C.textDark}}>{name}</div>
						</div>
					</div>
				);
			})}
			{bracket(S(19.93), top + 6, top + step + 86, 'what')}
			{bracket(S(20.49), top + 2 * step + 6, top + 2 * step + 86, 'how')}
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- scene 9: pipeline ticks (full blue)
const GATES = ['Analyse', 'Plan', 'Build', 'Captions', 'Export'];
const Pipeline: React.FC<{f: number}> = ({f}) => {
	const a = S(23.04);
	if (f < a || f >= S(26.82)) return null;
	const push = 1 + 0.04 * lin(f, a, S(26.82) - a);
	const tick0 = S(23.3), tickStep = (S(25.14) - S(23.3)) / 4;
	return (
		<AbsoluteFill style={{transform: `scale(${push})`}}>
			<div style={{position: 'absolute', left: 110, top: 600, width: 860, ...hero(f, a)}}>
				<div style={{...white({padding: '44px 48px'})}}>
					<div style={{display: 'flex', alignItems: 'center', gap: 16, marginBottom: 30}}>
						<Asterisk size={50} />
						<div style={{fontFamily: SANS, fontWeight: 700, fontSize: 44, color: C.textDark}}>Edit pipeline</div>
					</div>
					{GATES.map((g, i) => {
						const t = tick0 + tickStep * i;
						const p = prog(f, t, 12, SPRINGPOP);
						return (
							<div key={g} style={{display: 'flex', alignItems: 'center', gap: 26, height: 96, borderTop: i ? '2px solid #ECEEF2' : 'none'}}>
								<div style={{width: 52, height: 52, borderRadius: 26, border: `4px solid ${p > 0.05 ? C.badgeBlue : '#C9CED8'}`, background: p > 0.05 ? C.badgeBlue : 'transparent', display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${p > 0.05 ? 0.85 + 0.15 * p : 1})`}}>
									{p > 0.05 && (
										<svg width={30} height={30} viewBox="0 0 30 30"><path d="M 6 16 L 12 22 L 24 8" stroke="#fff" strokeWidth={4.5} fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
									)}
								</div>
								<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 42, color: p > 0.05 ? C.textDark : '#9aa0ac'}}>{g}</div>
							</div>
						);
					})}
				</div>
			</div>
		</AbsoluteFill>
	);
};

// ---------------------------------------------------------------- CTA: Comments sheet
const CommentsSheet: React.FC<{f: number}> = ({f}) => {
	const a = S(29.03);
	if (f < a) return null;
	const p = prog(f, a, 11, SHEET_RISE);
	const word = typed('EDIT', f, S(29.3), 7);
	const press = S(30.33);
	const pressed = interpolate(f, [press, press + 4, press + 10], [1, 0.88, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	return (
		<div style={{position: 'absolute', left: 40, top: 1250, width: 1000, height: 480, transform: `translateY(${(1 - p) * 520}px)`, opacity: lin(f, a, 5)}}>
			<div style={{width: '100%', height: '100%', borderRadius: 40, background: C.cardDark, backdropFilter: 'blur(24px)', boxShadow: '0 -10px 50px rgba(0,0,0,0.35)', padding: '34px 36px', boxSizing: 'border-box'}}>
				<div style={{width: 80, height: 8, borderRadius: 4, background: 'rgba(255,255,255,0.3)', margin: '0 auto 26px'}} />
				<div style={{fontFamily: SANS, fontWeight: 600, fontSize: 38, color: '#fff', textAlign: 'center'}}>Comments</div>
				<div style={{marginTop: 54, display: 'flex', alignItems: 'center', gap: 20}}>
					<div style={{width: 84, height: 84, borderRadius: 42, background: 'linear-gradient(135deg,#8fb3ff,#4a6dd8)', flex: 'none'}} />
					<div style={{flex: 1, height: 96, borderRadius: 48, background: 'rgba(255,255,255,0.12)', display: 'flex', alignItems: 'center', padding: '0 34px', fontFamily: SANS, fontSize: 44, color: '#fff', fontWeight: 500}}>
						{word.length ? word : <span style={{color: 'rgba(255,255,255,0.45)'}}>Add a comment…</span>}
						{word.length > 0 && <span style={{display: 'inline-block', width: 4, height: 46, background: '#fff', marginLeft: 4, opacity: Math.floor(f / 8) % 2 ? 0 : 1}} />}
					</div>
					<div style={{width: 96, height: 96, borderRadius: 48, background: C.badgeBlue, flex: 'none', display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${pressed})`}}>
						<svg width={44} height={44} viewBox="0 0 44 44"><path d="M 22 36 L 22 10 M 10 21 L 22 9 L 34 21" stroke="#fff" strokeWidth={5} fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
					</div>
				</div>
			</div>
		</div>
	);
};

// ---------------------------------------------------------------- captions (grey -> white word build)
type Tok = {t: string; kind: 'plain' | 'bold' | 'italic'};
const tokenize = (text: string): Tok[] =>
	text.split(/\s+/).filter(Boolean).map((w) => {
		const b = w.match(/^\*\*(.+)\*\*([^*]*)$/);
		if (b) return {t: b[1] + b[2], kind: 'bold'};
		const m = w.match(/^\*(.+)\*([^*]*)$/);
		if (m) return {t: m[1] + m[2], kind: 'italic'};
		return {t: w.replace(/\*/g, ''), kind: 'plain'};
	});

// join "*step-by-step*"-style tokens that were split by spaces (none here) — group strings have no spaces inside markers
const Captions: React.FC<{f: number}> = ({f}) => {
	const mode = captionMode(f);
	if (mode === 'hidden') return null;
	const fs = f / 30;
	let gi = -1;
	for (let i = 0; i < GROUPS.length; i++) if (GROUPS[i].s <= fs + 0.02) gi = i;
	if (gi < 0) return null;
	const g = GROUPS[gi];
	if (!g.text) return null;
	const next = GROUPS[gi + 1] ? GROUPS[gi + 1].s : END_S;
	const dur = next - g.s;
	const toks = tokenize(g.text);
	const n = toks.length;
	const base: React.CSSProperties =
		mode === 'face'
			? {position: 'absolute', left: 90, right: 90, bottom: 1920 - 1500, display: 'flex', flexWrap: 'wrap', justifyContent: 'center', alignItems: 'baseline', gap: '0 16px'}
			: {position: 'absolute', left: 90, right: 90, top: 262, display: 'flex', flexWrap: 'wrap', justifyContent: 'center', alignItems: 'baseline', gap: '0 16px'};
	return (
		<div style={{...base, textShadow: '0 2px 16px rgba(0,0,0,0.5)', lineHeight: 1.25}}>
			{toks.map((tk, i) => {
				const wf = (g.s + (i / n) * dur * 0.9) * 30;
				const spoken = f >= wf - 1;
				const p = prog(f, wf, 8, CAPTION_IN);
				const style: React.CSSProperties =
					tk.kind === 'bold' ? {fontFamily: SANS, fontWeight: 700, fontSize: 52}
						: tk.kind === 'italic' ? {fontFamily: SERIF, fontStyle: 'italic', fontWeight: 500, fontSize: 62}
							: {fontFamily: SANS, fontWeight: 500, fontSize: 38};
				return (
					<span key={i} style={{...style, color: spoken ? C.white : C.unspoken, opacity: spoken ? 0.25 + 0.75 * p : 1, filter: spoken ? `blur(${(4 * (1 - p)).toFixed(2)}px)` : 'none'}}>{tk.t}</span>
				);
			})}
		</div>
	);
};

// ---------------------------------------------------------------- main
export const Main: React.FC = () => {
	const f = useCurrentFrame();
	const ph = paneH(f);
	// pane slides with its content while it is smaller than the split height
	const slideY = Math.min(0, ph - SPLIT);
	const videoShift = (Math.min(ph, SPLIT) * (SPLIT - FACE_SHIFT)) / SPLIT; // translateY of the A-roll
	const hold = f >= S(20.91) && f < S(23.04) ? 1 + 0.04 * lin(f, S(20.91), S(2.13)) : 1;
	return (
		<AbsoluteFill style={{backgroundColor: '#0d0f12'}}>
			<AbsoluteFill style={{transform: `translateY(${videoShift}px) scale(${hold})`, transformOrigin: '50% 40%'}}>
				<OffthreadVideo src={staticFile('roughcut_v3.mp4')} />
			</AbsoluteFill>
			<div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: 700, background: 'linear-gradient(180deg, rgba(0,0,0,0), rgba(0,0,0,0.42))', opacity: ph < 5 ? 1 : 0}} />
			{ph > 0.5 && (
				<div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: ph, overflow: 'hidden'}}>
					<div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1920, transform: `translateY(${slideY}px)`}}>
						<BlueGround f={f} />
						<ChatScene f={f} />
						<TypeBeat f={f} />
						<Wall f={f} />
						<DesignDoc f={f} />
						<SessionScene f={f} />
						<Contrast f={f} />
						<Files f={f} />
						<Pipeline f={f} />
					</div>
				</div>
			)}
			<Captions f={f} />
			<CommentsSheet f={f} />
		</AbsoluteFill>
	);
};
