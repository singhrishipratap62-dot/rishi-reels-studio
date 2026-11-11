// R011 motorcycle growth (R010 beats on Rishi's Premiere cut; 4621 "why" take, no gear line) — beat config for engine/board.html. Times anchored to spoken words via at(phrase, word).
// First growth case: SOLVE = Ansoff 2x2 (shrinks to a mini-matrix) + four move tabs + a 0–6,000 sales bar in place of the ₹ line.
const IC = {
  bike: `<svg class="ic" viewBox="0 0 120 100"><path class="f" d="M44 44Q50 34 64 34H74Q80 34 80 42L78 50H48Z"/>
    <path class="s" d="M28 76a16 16 0 1 0 0.1 0M92 76a16 16 0 1 0 0.1 0"/><path class="s" d="M28 76L46 50H80L92 76"/>
    <path class="s" d="M44 44Q50 34 64 34H74Q80 34 80 42L78 50H48Z"/><path class="s" d="M46 50L58 76H70L80 50"/>
    <path class="s" d="M84 42L92 26M86 26H100M24 50H40"/><path class="s" d="M98 34a4 4 0 1 0 0.1 0"/></svg>`,
};
const sz = (svg, px) => svg.replace('<svg class="ic"', `<svg class="ic" style="width:${px}px;height:${px * 100 / 120}px"`);

var CFG = {
  part: 45, hookImg: 'HOOKIMG', mbbImg: 'MBBIMG', capMaxW: 680, capMaxWords: 4, s1CapTop: 632, bgVideo: true,
  hookQ: "How would you grow a motorcycle brand that's about to shut down?",
  s1End: 107 / (30000/1001), s2End: 170 / (30000/1001),
  els: [],
  init(at) {
    const E = (o) => (this.els.push(o), o);
    const PH = at('So how do we grow it?', 'So');                 // phase switch (2nd "how do we grow it")
    const END = at('This is part 45', 'This');                    // end card
    this.endT = END;
    const L = { x: 36 }, RX = 470;
    // matrix cells light up through the states engine: .on = active move
    E({ x: 0, y: 0, in: 0, html: `<style>.cell{font-size:40px;border-radius:16px;background:var(--acc-xl);color:var(--navy);font-weight:700;display:flex;align-items:center;justify-content:center}
      .cell.on{background:var(--accent);color:#fff}.ghost{height:14px;border:2px dashed #B9C0F5;border-radius:7px}</style>` });

    // ---------------- FACTS: pre-root (full card) ----------------
    const tClient = at('Your client is a 100-year-old', 'client'), t100 = at('Your client is a 100-year-old', '100-year-old');
    const tMoto = at('a 100-year-old motorcycle company.', 'motorcycle');
    const tFact = at('Its factory can make', 'factory'), t6k = at('make 6,000 bikes a month,', '6,000'), t2k = at('selling only 2,000.', '2,000.');
    const tShut = at('thinking about shutting it down.', 'shutting'), tCEO = at('The CEO asks you:', 'CEO');
    const tRoot = at('how do we grow it?', 'how');
    E({ x: RX, y: 104, in: tClient, out: tRoot, cls: 'lbl', html: 'Client' });
    E({ x: RX, y: 132, in: tMoto, out: tRoot, cls: 'h1', html: 'Motorcycle maker' });
    E({ x: RX, y: 206, in: t100, out: tRoot, html: '<span class="pill">100 years old</span>' });
    E({ x: RX, y: 266, in: t6k, out: tRoot, html: '<span class="pill">Factory · 6,000 / mo</span>' });
    E({ x: RX, y: 326, in: t2k, out: tRoot, html: '<span class="pill">Selling · 2,000 / mo</span>' });
    E({ x: RX, y: 400, in: tCEO, out: tRoot, cls: 'lbl', html: 'CEO asks' });
    E({ x: L.x + 60, y: 120, w: 300, h: 250, in: tMoto, out: tFact, html: sz(IC.bike, 300) });
    E({ x: L.x + 20, y: 116, in: tFact, out: tRoot, cls: 'lbl', html: 'Bikes / month' });
    const SB = (y, tl, lbl, w, tb, txt) => E({ x: L.x + 20, y, in: tl, out: tRoot, html: `<div style="display:flex;align-items:center;gap:14px">
      <div class="sub" style="width:110px;color:var(--ink);font-weight:600">${lbl}</div><div style="width:270px;height:46px;border-radius:10px;background:var(--acc-xl);overflow:hidden">
      <div class="sbar" data-bar data-at="${tb}" data-dur="0.5" style="width:${w}px"><div style="width:${w}px;background:var(--accent)">${txt}</div></div></div></div>` });
    SB(156, tFact, 'Capacity', 270, t6k, '6,000');
    SB(226, t2k, 'Selling', 90, t2k, '2,000');
    E({ x: L.x + 150, y: 300, in: tShut, out: tRoot, m: 'pop', rot: -6, html: '<span class="stamp">SHUT DOWN?</span>' });

    // ---------------- FACTS: tree (right) ----------------
    E({ x: RX, y: 84, w: 500, h: 64, fs: 26, in: tRoot, out: END, cls: 'qbox', html: 'How do we grow it?',
      moves: [{ t: PH, x: 251, y: 78, w: 500, h: 56, fs: 24 }] });
    const tClar = at('a few clarifying questions,', 'clarifying');
    E({ x: RX, y: 162, in: tClar, out: PH, cls: 'lbl', html: 'Clarifying questions' });
    const rowY = [194, 242, 290, 338, 386], QX = RX, AX = RX + 198;
    const ROW = (r, cl, q, tq, a, ta) => {
      E({ x: QX, y: rowY[r], in: tq, out: PH, cls: cl, html: q });
      E({ x: AX - 22, y: rowY[r], in: ta, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: ta, out: PH, cls: cl === 'qp' ? 'ap' : 'fv', html: a });
    };
    const tWhy = at("Why aren't people buying from us?", 'Why'), tHeavy = at('our bikes are heavy,', 'heavy,');
    const tOld = at('heavy, old-fashioned and unreliable,', 'old-fashioned'), tUnrel = at('old-fashioned and unreliable,', 'unreliable,');
    const tJap = at('and Japanese commuter bikes', 'Japanese'), tCheap = at('are cheaper and give better mileage.', 'cheaper');
    const tMile = at('give better mileage.', 'mileage.');
    const tWho = at('who still buys from us?', 'who'), tLoyal = at('a small group of loyal fans,', 'loyal');
    const tOlder = at('mostly older men,', 'older'), tThump = at("love the bike's thump", 'thump'), tHist = at('and its history.', 'history.');
    const tSell = at('how do we sell today?', 'how'), t200 = at('through 200 dealers,', '200'), t10 = at('about 10 bikes a month.', '10');
    const tMo = at('about 10 bikes a month.', 'month.');
    const tTest = at('does take a test ride,', 'test'), t1in5 = at('1 in 5 end up buying.', '1'), tBuy = at('1 in 5 end up buying.', 'buying.');
    const tProb = at('The problem is very few people', 'problem'), tFew = at('The problem is very few people', 'few');
    ROW(0, 'qp', 'Why not buying?', tWhy, 'Heavy · dated · unreliable', tHeavy);
    ROW(1, 'qp', 'Who still buys?', tWho, 'Loyal fans · older men', tLoyal);
    ROW(2, 'qp', 'How do we sell?', tSell, '200 dealers × 10 / mo', t200);
    ROW(3, 'fl', 'Test ride', tTest, '1 in 5 buy', t1in5);
    ROW(4, 'fl', 'Problem', tProb, 'Very few test rides', tFew);

    // ---------------- FACTS: left beat visuals ----------------
    E({ x: L.x + 20, y: 112, in: tRoot, out: tClar, cls: 'lbl', html: 'Selling vs capacity' });
    E({ x: L.x + 20, y: 150, in: tRoot, out: tClar, html: `<div class="big">2,000<span style="color:var(--grey);font-size:44px"> / 6,000</span></div><div class="sub" style="margin-top:10px">bikes a month</div>` });
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tClar, out: tWhy, cls: 'ph', html: '? ? ?' });
    E({ x: L.x + 20, y: 112, in: tWhy, out: tWho, cls: 'lbl', html: 'Customers think' });
    const X_ = (y, t, txt) => E({ x: L.x + 20, y, in: t, out: tWho, html: `<span class="chip"><span class="cross">✗</span>&nbsp;${txt}</span>` });
    X_(150, tHeavy, 'Heavy'); X_(206, tOld, 'Old-fashioned'); X_(262, tUnrel, 'Unreliable');
    E({ x: L.x + 20, y: 336, in: tJap, out: tWho, html: `<div class="sub" style="color:var(--ink);font-weight:600">vs Japanese commuters</div>
      <div style="display:flex;gap:10px;margin-top:10px"><span class="chip res" data-in="${tCheap}">Cheaper</span><span class="chip res" data-in="${tMile}">Better mileage</span></div>` });
    E({ x: L.x + 20, y: 112, in: tLoyal, out: tSell, cls: 'lbl', html: 'Loyal fans' });
    E({ x: L.x + 20, y: 150, in: tOlder, out: tSell, cls: 'mid', html: 'Mostly older men' });
    E({ x: L.x + 20, y: 220, in: tThump, out: tSell, html: '<span class="chip">❤&nbsp;The thump</span>' });
    E({ x: L.x + 200, y: 220, in: tHist, out: tSell, html: '<span class="chip">❤&nbsp;The history</span>' });
    E({ x: L.x + 20, y: 150, in: t200, out: tTest, html: `<div class="big"><span data-to="200" data-from="80"></span></div><div class="sub" style="margin-top:10px">dealers</div>` });
    E({ x: L.x + 200, y: 168, in: t10, out: tTest, html: `<div class="mid">× 10</div><div class="sub" style="margin-top:10px">bikes each / mo</div>` });
    E({ x: L.x + 20, y: 290, in: tMo, out: tTest, html: '<span class="chip res">= 2,000 / mo</span>' });
    E({ x: L.x + 20, y: 112, in: tTest, out: PH, cls: 'lbl', html: 'Test rides' });
    const dots = [0, 1, 2, 3, 4].map(i => `<div style="position:relative;width:52px;height:52px;border-radius:50%;background:#D7DBF5">${i === 0 ?
      `<div data-in="${tBuy}" style="position:absolute;inset:0;border-radius:50%;background:var(--accent)"></div>` : ''}</div>`).join('');
    E({ x: L.x + 20, y: 154, in: t1in5, out: PH, html: `<div style="display:flex;gap:16px">${dots}</div><div class="sub" style="margin-top:14px">1 in 5 riders buy</div>` });
    E({ x: L.x + 20, y: 290, in: tFew, out: PH, html: '<span class="chip dark">But very few take one</span>' });

    // ---------------- SOLVE: sales bar (0–6,000 bikes / month) ----------------
    const t3x = at('We need to 3x our sales,', '3x'), tWays = at('4 ways to grow any brand:', 'ways');
    const AX0 = 70, AXW = 863, AXY = 508, X = (v) => AX0 + AXW * v / 6000;
    E({ x: AX0, y: AXY, w: AXW, in: t3x, out: END, html: '<div class="axis"></div>' });
    [0, 2000, 4000].forEach(v => E({ x: X(v), y: AXY + 14, in: t3x, out: END, cls: 'axl', html: v.toLocaleString('en-IN') }));
    const SEG = (a, b, t, col) => E({ x: X(a), y: AXY - 5, in: t, out: END, z: 2, html:
      `<div data-bar data-at="${t}" data-dur="0.5" style="width:${X(b) - X(a)}px;height:14px;border-radius:7px;background:${col};transform-origin:left"></div>` });
    const MK = (v, tin, label, sub, tier) => E({ x: X(v), y: AXY - 26 - tier * 26 - 44, in: tin, out: END, m: 'drop', cls: 'mk', z: 3,
      html: `<span class="ms">${sub}</span><span class="ml">${label}</span><span class="stem" style="height:${26 + tier * 26}px"></span>` });
    SEG(0, 2000, t3x, 'var(--navy)'); MK(2000, t3x, '2,000', 'Today', 1);
    MK(6000, t3x, '6,000', '3x · capacity', 1);

    // ---------------- SOLVE: Ansoff matrix -> mini-matrix ----------------
    const tQ = [at('the same product to the same customers,', 'same'), at('the same product to new customers,', 'same'),
      at('new products for the same customers,', 'new'), at('new products for new customers.', 'new')];
    const tAns = at('the Ansoff matrix.', 'Ansoff');
    const tM = [at('First: same bike,', 'First:'), at('Second: same bike,', 'Second:'), at('Third: new products', 'Third:'), at('Fourth: new products', 'Fourth:')];
    const tRec = at("So, I'd start with the first two,", 'start');
    E({ x: 330, y: 158, w: 260, in: tWays, out: tM[0], cls: 'sub', html: '<div style="text-align:center">Same bike</div>' });
    E({ x: 600, y: 158, w: 260, in: tWays, out: tM[0], cls: 'sub', html: '<div style="text-align:center">New product</div>' });
    E({ x: 130, y: 228, w: 190, in: tWays, out: tM[0], cls: 'sub', html: '<div style="text-align:right">Same customers</div>' });
    E({ x: 130, y: 328, w: 190, in: tWays, out: tM[0], cls: 'sub', html: '<div style="text-align:right">New customers</div>' });
    E({ x: 430, y: 404, in: tAns, out: tM[0], html: '<span class="pill">Ansoff matrix</span>' });
    // cell order = spoken order: ① same/same, ② same bike/new customers, ③ new product/same customers, ④ new/new
    const CELL = [[330, 196], [330, 296], [600, 196], [600, 296]], MINI = [[60, 200], [60, 256], [136, 200], [136, 256]];
    const NUM = ['①', '②', '③', '④'];
    CELL.forEach(([x, y], i) => E({ x, y, w: 260, h: 90, fs: 40, in: tQ[i], out: END, cls: 'cell', html: NUM[i],
      moves: [{ t: tM[0], x: MINI[i][0], y: MINI[i][1], w: 70, h: 50, fs: 24 }],
      states: [{ t: tM[i], c: 'on' }, { t: tM[i + 1] ?? tRec, c: '' }, ...(i < 2 ? [{ t: tRec, c: 'on' }] : [])] }));

    // ---------------- SOLVE: four move tabs ----------------
    const TABS = [[100, '① Fans'], [300, '② Trials'], [510, '③ Fix the bike'], [760, '④ Accessories']];
    TABS.forEach(([x, txt], i) => E({ x, y: 152, in: tM[0], out: END, cls: 'tab', html: `<span class="dot"></span>${txt}`,
      states: [{ t: tM[i], c: 'on' }, { t: tM[i + 1] ?? tRec, c: '' }, ...(i < 2 ? [{ t: tRec, c: 'on' }] : [])] }));

    const chip = (x, y, tin, tout, txt, c = '') => E({ x, y, in: tin, out: tout, html: `<span class="chip ${c}">${txt}</span>` });
    const WX = 240;
    // ① fans
    chip(WX, 200, at('our best salespeople,', 'salespeople,'), tM[1], `Fans = best salespeople<span data-in="${at('turn them into a channel.', 'channel.')}">&nbsp;→ a channel</span>`);
    chip(WX, 256, at('runs a monthly group ride,', 'group'), tM[1], 'Monthly group ride · every dealer');
    chip(WX, 312, at('brings in a buyer', 'buyer'), tM[1], `Bring a buyer<span data-in="${at('gets a free service.', 'free')}">&nbsp;→ free service</span>`);
    const t1kA = at("that's about 1,000 more bikes.", '1,000');
    chip(WX, 368, at('each of our 200 dealers', '200'), tM[1], `200 dealers × <span data-in="${at('sells about 5 more bikes', '5')}">5 more / mo</span>`);
    chip(WX + 360, 368, t1kA, tM[1], '= +1,000 / mo', 'res');
    SEG(2000, 3000, t1kA, 'var(--accent)'); MK(3000, t1kA, '+1,000', '① Fans', 2);
    // ② trials
    chip(WX, 200, at('People who ride this bike love it.', 'love'), tM[2], '<span class="tick">✓</span>&nbsp;Riders love it');
    chip(WX + 240, 200, at('too few people ever ride it,', 'few'), tM[2], '<span class="cross">✗</span>&nbsp;Too few ever ride it');
    chip(WX, 256, at('increase our trials.', 'trials.'), tM[2], 'Goal: more first rides', 'dark');
    chip(WX, 312, at('Put rental bikes in Goa,', 'rental'), tM[2], `Rentals:<span data-in="${at('in Goa,', 'Goa,')}">&nbsp;Goa</span><span data-in="${at('Goa, Manali and Leh,', 'Manali')}">&nbsp;· Manali</span><span data-in="${at('Manali and Leh,', 'Leh,')}">&nbsp;· Leh</span>`);
    chip(WX, 368, at('offer doorstep test drives', 'doorstep'), tM[2], `Doorstep test drives<span data-in="${at('booked online.', 'online.')}">&nbsp;· online</span>`);
    const t1kB = at('brings in a thousand more bikes.', 'thousand');
    chip(WX + 400, 256, at('Since 1 in 5 test riders', '1'), tM[2], '1 in 5 riders buy');
    chip(WX + 400, 312, at('every 5,000 extra first rides', '5,000'), tM[2], '5,000 extra rides ÷ 5');
    chip(WX + 400, 368, t1kB, tM[2], '= +1,000 / mo', 'res');
    SEG(3000, 4000, t1kB, 'var(--accent)'); MK(4000, t1kB, '+1,000', '② Trials', 1);
    // ③ fix the bike
    const XC = (x, t, txt) => chip(x, 200, t, tM[3], `<span class="cross">✗</span>&nbsp;${txt}`);
    XC(WX, at("Because it's heavy,", 'heavy,'), 'Heavy');
    XC(WX + 150, at('it breaks down.', 'breaks'), 'Breaks down');
    chip(WX, 256, at('fix the reliability,', 'reliability,'), tM[3], '<span class="tick">✓</span>&nbsp;Fix reliability');
    chip(WX + 240, 256, at('make a lighter version,', 'lighter'), tM[3], '<span class="tick">✓</span>&nbsp;Lighter version');
    chip(WX, 312, at('but keep the thump,', 'keep'), tM[3], `Keep:<span data-in="${at('but keep the thump,', 'thump,')}">&nbsp;thump</span><span data-in="${at('the shape and the history,', 'shape')}">&nbsp;· shape</span><span data-in="${at('the shape and the history,', 'history,')}">&nbsp;· history</span>`);
    chip(WX, 368, at('let go of the legacy.', 'legacy.'), tM[3], 'Don’t lose the legacy', 'dark');
    // ④ accessories
    const AC = (x, t, txt) => chip(x, 200, t, tRec, txt);
    AC(WX, at('riding jackets,', 'jackets,'), 'Riding jackets'); AC(WX + 210, at('helmets,', 'helmets,'), 'Helmets');
    AC(WX + 350, at('saddlebags and custom parts', 'saddlebags'), 'Saddlebags'); AC(WX + 520, at('and custom parts', 'custom'), 'Custom parts');
    E({ x: WX, y: 266, in: at('through dealers and online.', 'dealers'), out: tRec, cls: 'sub', html: 'Sold via dealers + online' });
    chip(WX, 312, at('already on the road', 'road'), tRec, 'Every bike on the road = a customer again', 'dark');
    // recommendation
    chip(WX, 200, tRec, END, `Start: ① + ②<span data-in="${at("because they don't need a new factory", 'need')}">&nbsp;· no new factory or product</span>`, 'dark');
    chip(WX, 256, at('fix the bike in parallel', 'parallel'), END, '③ Fix the bike in parallel');
    chip(WX, 312, at('and add accessories in the existing dealers', 'accessories'), END, `④ Accessories<span data-in="${at('once the brand is growing again.', 'growing')}">&nbsp;once growing again</span>`);
    E({ x: X(4000), y: AXY - 5, in: tRec, out: END, z: 1, html: `<div class="ghost" style="width:${X(6000) - X(4000)}px"></div>` });

    // ---------------- END CARD ----------------
    const tFollow = at('Follow for part 46.', 'Follow');
    E({ x: 0, y: 92, w: 1003, in: END, html: `<div class="ec" style="margin-top:40px"><div class="s" style="font-weight:600;font-size:44px;color:var(--navy)">Solving real consultant cases</div><div class="p">Part 45</div>
      <div class="f" data-in="${tFollow}">Follow for Part 46</div></div>` });
  }
};
