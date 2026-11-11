// R007 ropeway pricing — beat config for engine/board.html. Times anchored to spoken words via at(phrase, word).
const IC = {
  cable: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M26 30H74a8 8 0 0 1 8 8V70a8 8 0 0 1-8 8H26a8 8 0 0 1-8-8V38a8 8 0 0 1 8-8Z"/>
    <path class="s" d="M4 20L96 6"/><path class="s" d="M50 13V30"/><path class="s" d="M26 30H74a8 8 0 0 1 8 8V70a8 8 0 0 1-8 8H26a8 8 0 0 1-8-8V38a8 8 0 0 1 8-8Z"/>
    <path class="s" d="M26 42H74V56H26Z"/><path class="s" d="M42 42V56M58 42V56"/></svg>`,
  walk: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M43 14a7 7 0 1 0 14 0a7 7 0 1 0-14 0"/><path class="s" d="M43 14a7 7 0 1 0 14 0a7 7 0 1 0-14 0"/>
    <path class="s" d="M50 26L46 54"/><path class="s" d="M48 34L34 46M48 34L62 44"/><path class="s" d="M46 54L34 84M46 54L58 70L64 86"/><path class="s" d="M70 30V88"/></svg>`,
  pony: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M28 40H66L78 22L88 28L82 40V58H28Z"/>
    <path class="s" d="M28 46C28 41 32 38 40 38H66L78 22L88 28L82 40V58H28Z"/><path class="s" d="M28 46C20 48 16 58 18 66"/>
    <path class="s" d="M36 58V84M48 58V84M64 58V84M76 58V84"/><path class="s" d="M76 24L74 16"/></svg>`,
  heli: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M34 52a22 15 0 1 0 44 0a22 15 0 1 0-44 0"/><path class="s" d="M34 52a22 15 0 1 0 44 0a22 15 0 1 0-44 0"/>
    <path class="s" d="M34 50H8M8 42V58"/><path class="s" d="M18 26H94M56 26V37"/><path class="s" d="M38 76H80M46 66V76M70 66V76"/><path class="s" d="M60 44H72V54"/></svg>`,
  clock: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M16 50a34 34 0 1 0 68 0a34 34 0 1 0-68 0"/><path class="s" d="M16 50a34 34 0 1 0 68 0a34 34 0 1 0-68 0"/>
    <path class="s" d="M50 28V50L64 58"/></svg>`,
};
const sz = (svg, px) => svg.replace('<svg class="ic"', `<svg class="ic" style="width:${px}px;height:${px}px"`);

var CFG = {
  part: 42, hookImg: 'HOOKIMG', mbbImg: 'MBBIMG', capMaxW: 680, capMaxWords: 4, s1CapTop: 632, bgVideo: true,
  hookQ: 'How do you price a cable car that turns a 4 hour temple climb into 10 minutes?',
  s1End: 134 / (30000/1001), s2End: 198 / (30000/1001),
  els: [],
  init(at) {
    const E = (o) => (this.els.push(o), o);
    const PH = at('So, how do we price it?', 'So,');             // phase switch
    const END = at('This is part 42', 'This');                  // end card
    this.endT = END;
    const L = { x: 36, w: 400 };
    const RX = 470;

    // ---------------- FACTS: pre-root (full card) ----------------
    const tClient = at('Your client is a company', 'client'), tCo = at('Your client is a company', 'company');
    const tRoot = at('what ticket price should be approved?', 'what');
    const tRope = at('build and run a ropeway', 'ropeway'), tObj = at('what is the objective?', 'objective?');
    E({ x: RX, y: 104, in: tClient, out: tRoot, cls: 'lbl', html: 'Client' });
    E({ x: RX, y: 132, in: tCo, out: tRoot, cls: 'h1', html: 'Ropeway operator' });
    E({ x: RX, y: 206, in: at('a state government contract', 'state'), out: tRoot, html: '<span class="pill">State govt contract</span>' });
    E({ x: RX, y: 266, in: at('to build and run', 'build'), out: tRoot, html: '<span class="pill">Build + run</span>' });
    E({ x: RX, y: 326, in: at('a famous hill temple.', 'hill'), out: tRoot, html: '<span class="pill">Up to a hill temple</span>' });
    E({ x: RX, y: 400, in: at('The government is the one asking.', 'government'), out: tRoot, cls: 'lbl', html: 'Government asks' });
    E({ x: L.x + 80, y: 110, w: 260, h: 260, in: tRope, out: tObj, html: sz(IC.cable, 260) });

    // ---------------- FACTS: tree (right) ----------------
    E({ x: RX, y: 84, w: 500, h: 64, fs: 26, in: tRoot, out: END, cls: 'qbox', html: 'What ticket price to approve?',
      moves: [{ t: PH, x: 251, y: 78, w: 500, h: 56, fs: 24 }] });
    E({ x: RX, y: 162, in: at('ask clarifying questions', 'clarifying'), out: PH, cls: 'lbl', html: 'Clarifying questions' });
    const rowY = [194, 242, 290, 338, 386, 434, 482], QX = RX, AX = RX + 198;
    const ROW = (r, cl, q, tq, a, ta) => {
      E({ x: QX, y: rowY[r], in: tq, out: PH, cls: cl, html: q });
      E({ x: AX - 22, y: rowY[r], in: ta, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: ta, out: PH, cls: cl === 'qp' ? 'ap' : 'fv', html: a });
    };
    const tRecover = at('must recover its cost', 'recover'), tAfford = at('to stay affordable for pilgrims', 'affordable');
    const tToday = at('How do people get up today?', 'How'), t1cr = at('about 1 crore pilgrims', '1');
    const tMost = at('Most walk for 4 hours', 'Most');
    const tPony = at('some take a pony', 'pony'), t1500 = at('a pony for 1,500 rupees', '1,500');
    const tHeli = at('a few take a helicopter', 'helicopter'), t3000 = at('a helicopter for 3,000 rupees', '3,000');
    const tCarry = at('can the ropeway carry everyone?', 'can'), tNo = at('She said no.', 'no.');
    const t40 = at('about 40 lakh trips a year,', '40'), tCosts = at('it costs about 2,000 crore', 'costs');
    const t2000 = at('it costs about 2,000 crore', '2,000'), tSurv = at('Surveys show that', 'Surveys');
    const t300 = at('at 300 rupees a trip', '300'), t7 = at('7 in 10 pilgrims', '7');
    const t600 = at('and at 600 rupees, about 4', '600'), t4 = at('about 4 in 10 pilgrims', '4');
    ROW(0, 'qp', 'Objective?', tObj, `Recover cost<span data-in="${tAfford}">&nbsp;+ affordable</span>`, tRecover);
    ROW(1, 'qp', 'How today?', tToday, '1 cr pilgrims / yr', t1cr);
    ROW(2, 'fl', 'Pony · Helicopter', tPony, `₹1,500<span data-in="${t3000}">&nbsp;· ₹3,000</span>`, t1500);
    ROW(3, 'qp', 'Carry everyone?', tCarry, `No<span data-in="${t40}">&nbsp;· 40 lakh trips / yr</span>`, tNo);
    ROW(4, 'fl', 'Cost (30 yrs)', tCosts, '₹2,000 cr', t2000);
    ROW(5, 'fl', 'Demand @ ₹300', t300, '7 in 10', t7);
    ROW(6, 'fl', 'Demand @ ₹600', t600, '4 in 10', t4);

    // ---------------- FACTS: left beat visuals ----------------
    E({ x: L.x + 20, y: 112, in: tObj, out: tToday, cls: 'lbl', html: 'Client wants' });
    E({ x: L.x + 20, y: 150, in: tRecover, out: tToday, html: '<span class="chip">① Recover cost · 30 yrs</span>' });
    E({ x: L.x + 20, y: 214, in: tAfford, out: tToday, html: '<span class="chip res">② Affordable for pilgrims</span>' });
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tToday, out: t1cr, cls: 'ph', html: '? ? ?' });
    E({ x: L.x + 40, y: 150, in: t1cr, out: tMost, html: `<div class="big"><span data-to="1" data-from="0" data-fmt="{n} cr"></span></div><div class="sub" style="margin-top:10px">pilgrims a year</div>` });
    const TILE = (x, ic, t, lbl, val, tv) => E({ x, y: 120, w: 130, in: t, out: tCarry, html:
      `<div style="display:flex;flex-direction:column;align-items:center;gap:6px">${sz(IC[ic], 96)}<div class="sub">${lbl}</div><div class="mid" data-in="${tv}" style="font-size:30px">${val}</div></div>` });
    TILE(L.x, 'walk', at('Most walk for', 'walk'), 'Walk', '4 hrs', at('walk for 4 hours', '4'));
    TILE(L.x + 135, 'pony', tPony, 'Pony', '₹1,500', t1500);
    TILE(L.x + 270, 'heli', tHeli, 'Helicopter', '₹3,000', t3000);
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tCarry, out: t40, cls: 'ph', html: '? ? ?' });
    const cells = Array.from({ length: 100 }, (_, i) => `<div style="background:${i < 40 ? 'var(--accent)' : 'var(--acc-l)'}"></div>`).join('');
    E({ x: L.x + 30, y: 112, in: t40, out: t2000, step: 0.008, html: `<div class="grid" style="grid-template-columns:repeat(10,16px)">${cells}</div>` });
    E({ x: L.x + 260, y: 130, in: t40 + 0.2, out: t2000, html: `<div class="sub">1 cr pilgrims</div><div class="mid" style="color:var(--accent);margin-top:14px">40 lakh</div><div class="sub">seats / yr</div>` });
    E({ x: L.x + 30, y: 150, in: t2000, out: tSurv, html: `<div class="big"><span data-to="2000" data-from="1200" data-fmt="₹{n} cr"></span></div><div class="sub" style="margin-top:10px">Build + run · 30 yrs</div>` });
    E({ x: L.x + 20, y: 116, in: tSurv, out: PH, cls: 'lbl', html: 'Survey · would ride' });
    const SB = (y, tl, lbl, w, tb, txt) => E({ x: L.x + 20, y, in: tl, out: PH, html: `<div style="display:flex;align-items:center;gap:14px">
      <div class="mid" style="width:110px">${lbl}</div><div style="width:240px;height:46px;border-radius:10px;background:var(--acc-xl);overflow:hidden">
      <div class="sbar" data-bar data-at="${tb}" data-dur="0.5" style="width:${w}px"><div style="width:${w}px;background:var(--accent)">${txt}</div></div></div></div>` });
    SB(156, t300, '₹300', 168, t7, '7 in 10');
    SB(226, t600, '₹600', 96, t4, '4 in 10');

    // ---------------- SOLVE: tabs + number line ----------------
    const tCost = at('First, cost;', 'cost;'), tComp = at('second, competition;', 'competition;'), tVal = at('and third, value.', 'value.');
    const tCost2 = at('First, the cost approach.', 'cost'), tComp2 = at('Second, competition.', 'Second,', 2);
    const tVal2 = at('Third is the value.', 'Third'), tRec = at('So should we charge the floor', 'So');
    E({ x: 230, y: 152, in: tCost, out: END, cls: 'tab', html: '<span class="dot"></span>Cost', states: [{ t: tCost2, c: 'on' }, { t: tComp2, c: '' }] });
    E({ x: 400, y: 152, in: tComp, out: END, cls: 'tab', html: '<span class="dot"></span>Competition', states: [{ t: tComp2, c: 'on' }, { t: tVal2, c: '' }] });
    E({ x: 650, y: 152, in: tVal, out: END, cls: 'tab', html: '<span class="dot"></span>Value', states: [{ t: tVal2, c: 'on' }, { t: tRec, c: '' }] });
    const AX0 = 70, AXW = 863, AXY = 508, X = (v) => AX0 + AXW * v / 3000;
    E({ x: AX0, y: AXY, w: AXW, in: tCost, out: END, html: '<div class="axis"></div>' });
    [0, 1000, 2000].forEach(v => E({ x: X(v), y: AXY + 14, in: tCost, out: END, cls: 'axl', html: '₹' + v.toLocaleString('en-IN') }));
    const tFloor = at("That's our floor.", 'floor.'), tCeil = at("That's our ceiling.", 'ceiling.');
    const MK = (v, tin, label, sub, tier, hl = false) => E({ x: X(v), y: AXY - 26 - tier * 26 - 44, in: tin, out: END, m: 'drop', cls: 'mk', z: 3,
      html: `<span class="ms">${sub}</span><span class="ml" style="position:relative">${label}${hl ? `<span class="hlbar" data-bar data-at="${tin + 0.15}" data-dur="0.3"></span>` : ''}</span><span class="stem" style="height:${26 + tier * 26}px"></span>` });
    const GM = (v, tin, txt, right = false) => E({ x: right ? X(v) - 160 : X(v) - 8, y: AXY + 4, w: right ? 168 : null, in: tin, out: END, m: 'drop', z: 3,
      html: `<div style="display:flex;align-items:flex-start;gap:6px;${right ? 'flex-direction:row-reverse' : ''}"><span style="width:3px;height:16px;background:#B7BBCB;border-radius:2px;${right ? 'margin-right:6px' : 'margin-left:6px'}"></span><span style="font-size:16px;font-weight:600;color:var(--grey);margin-top:6px;white-space:nowrap">${txt}</span></div>` });
    E({ x: X(170), y: AXY - 3, in: tCeil + 0.1, out: END, z: 1, html: `<div class="range" data-bar data-at="${tCeil + 0.1}" data-dur="0.5" style="width:${X(1500) - X(170)}px"></div>` });
    MK(170, tFloor, '₹170', 'Floor', 1);
    GM(1500, at('the pony is 1,500 rupees', '1,500'), 'Pony ₹1,500');
    GM(3000, at('the helicopter is 3,000 rupees', '3,000'), 'Helicopter ₹3,000', true);
    MK(1500, tCeil, '₹1,500', 'Ceiling', 0);
    const tA300 = at('At 300, about 70 lakh', '300');
    GM(300, tA300, '₹300');
    const tA600 = at('At 600 rupees, about 40 lakh', '600');
    MK(600, tA600, '₹600', 'Our price', 2, true);

    // ---------------- SOLVE: cost working ----------------
    const chip = (x, y, tin, tout, txt, c = '') => E({ x, y, in: tin, out: tout, html: `<span class="chip ${c}">${txt}</span>` });
    chip(60, 204, at('40 lakh trips a year for 30 years', '40'), tComp2, '40 lakh trips × 30 yrs');
    chip(370, 204, at('about 12 crore trips.', '12'), tComp2, '= 12 cr trips', 'res');
    chip(60, 262, at('2,000 crore over 12 crore', '2,000'), tComp2, '₹2,000 cr ÷ 12 cr trips');
    chip(400, 262, at('about 170 rupees a trip.', '170'), tComp2, '≈ ₹170 / trip', 'res');

    // ---------------- SOLVE: competition working ----------------
    const CT = (x, ic, t, lbl, val) => E({ x, y: 200, in: t, out: tVal2, html:
      `<div style="display:flex;align-items:center;gap:12px">${sz(IC[ic], 76)}<div><div class="sub">${lbl}</div><div class="mid">${val}</div></div></div>` });
    CT(70, 'walk', at('Walking is free,', 'Walking'), 'Walk', 'Free');
    CT(330, 'pony', at('the pony is 1,500 rupees', 'pony'), 'Pony', '₹1,500');
    CT(610, 'heli', at('the helicopter is 3,000 rupees', 'helicopter'), 'Helicopter', '₹3,000');
    const tBench = at('the pony sets the benchmark.', 'benchmark.');
    E({ x: 316, y: 186, w: 240, h: 112, in: tBench, out: tVal2, z: 0, html: '<div style="width:240px;height:112px;border:3px solid var(--accent);border-radius:18px"></div>' });
    chip(330, 312, tBench, tVal2, 'Benchmark', 'res');

    // ---------------- SOLVE: value working ----------------
    E({ x: 60, y: 192, in: at('The ropeway saves about', 'saves'), out: tRec, html: sz(IC.clock, 92) });
    E({ x: 170, y: 212, in: at('saves about 4 hours', '4'), out: tRec, cls: 'mid', html: 'Saves ~4 hrs' });
    chip(450, 214, at('far more comfortable than a pony.', 'comfortable'), tRec, 'More comfortable than a pony');
    chip(60, 306, at('should pay at least what the pony costs.', 'pay'), tRec, 'Willing to pay ≥ ₹1,500', 'dark');

    // ---------------- SOLVE: recommendation ----------------
    const tNo2 = at('No. At 300,', 'No.');
    chip(60, 204, tRec, END, 'Charge the floor (₹170)?');
    E({ x: 66, y: 226, w: 330, h: 4, in: tNo2, out: END, z: 4, html: '<div data-bar data-dur="0.25" style="width:330px;height:4px;background:#E0524B;border-radius:2px;transform-origin:left"></div>' });
    E({ x: 412, y: 200, in: tNo2, out: END, m: 'pop', z: 4, html: '<div class="cross" style="font-size:48px;line-height:1">✗</div>' });
    const DB = (y, tin, w, txt) => E({ x: 60, y, in: tin, out: END, html:
      `<div class="sbar" data-bar data-at="${tin}" data-dur="0.5" style="width:${w}px"><div style="width:${w}px;background:var(--accent);justify-content:flex-start;padding-left:14px">${txt}</div></div>` });
    DB(266, at('about 70 lakh people want', '70'), 420, '@ ₹300 · 70 lakh want');
    const tCap = at('we only have 40 lakh.', '40');
    E({ x: 298, y: 254, in: tCap, out: END, z: 5, html: '<div style="width:4px;height:120px;background:var(--navy);border-radius:2px"></div>' });
    E({ x: 230, y: 380, in: tCap, out: tA600, cls: 'sub', html: 'Capacity 40 lakh' });
    const tQ = at('The queue at the bottom', 'queue'), tWipe = at('that wipes out the very time', 'wipes');
    chip(520, 266, tQ, tA600, 'Queue: hours to clear');
    chip(520, 324, tWipe, tA600, '✗ Wipes out time saved');
    DB(324, at('about 40 lakh people want it,', '40'), 240, '@ ₹600 · 40 lakh');
    chip(330, 324, at('exactly our capacity.', 'capacity.'), END, '= capacity ✓', 'res');
    chip(560, 204, at('less than half the pony fare,', 'half'), END, '< ½ pony fare (₹750)');
    chip(540, 266, at('brings in about 240 crore', '240'), END, '40 lakh × ₹600 = ₹240 cr / yr', 'res');
    E({ x: 550, y: 330, in: at('against a 2,000 crore cost.', '2,000'), out: END, cls: 'sub', html: 'vs ₹2,000 cr cost (30 yrs)' });

    // ---------------- END CARD ----------------
    const tFollow = at('Follow for part 43.', 'Follow');
    E({ x: 0, y: 92, w: 1003, in: END, html: `<div class="ec" style="margin-top:40px"><div class="s" style="font-weight:600;font-size:44px;color:var(--navy)">Solving real consultant cases</div><div class="p">Part 42</div>
      <div class="f" data-in="${tFollow}">Follow for Part 43</div></div>` });
  }
};
