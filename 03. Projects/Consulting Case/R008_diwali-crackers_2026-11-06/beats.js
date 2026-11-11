// R008 Diwali crackers (market sizing) — beat config for engine/board.html. Times anchored to spoken words via at(phrase, word).
// First sizing reel: SOLVE = Demand/Supply tabs, Cities + Villages tables, 0–400 cr count bar (replaces the ₹ floor/ceiling line).
const IC = {
  rocket: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M50 8L62 28V68H38V28Z"/>
    <path class="s" d="M50 8L62 28V68H38V28Z"/><path class="s" d="M38 54L26 70V76L38 68M62 54L74 70V76L62 68"/>
    <path class="s" d="M44 68L50 84L56 68"/><path class="s" d="M50 40a5 5 0 1 0 0.1 0"/></svg>`,
  sparkler: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M64 34a10 10 0 1 0 0.1 0"/>
    <path class="s" d="M26 92L60 40"/><path class="s" d="M64 22V10M64 46V58M76 34H88M52 34H40M73 25L81 17M55 43L47 51M73 43L81 51M55 25L47 17"/></svg>`,
  ladi: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M14 40H24V66H14ZM34 46H44V72H34ZM56 46H66V72H56ZM76 40H86V66H76Z"/>
    <path class="s" d="M6 28Q50 48 94 28"/><path class="s" d="M14 40H24V66H14ZM34 46H44V72H34ZM56 46H66V72H56ZM76 40H86V66H76Z"/>
    <path class="s" d="M19 34V40M39 39V46M61 39V46M81 34V40"/></svg>`,
};
const sz = (svg, px) => svg.replace('<svg class="ic"', `<svg class="ic" style="width:${px}px;height:${px}px"`);

var CFG = {
  part: 43, hookImg: 'HOOKIMG', mbbImg: 'MBBIMG', capMaxW: 680, capMaxWords: 4, s1CapTop: 632, bgVideo: true,
  hookQ: 'How many crackers does India burst on Diwali?',
  s1End: 89 / (30000/1001), s2End: 158 / (30000/1001),
  els: [],
  init(at) {
    const E = (o) => (this.els.push(o), o);
    const PH = at('So, how do we estimate it?', 'So,');        // phase switch
    const END = at('This is part 43', 'This');                // end card
    this.endT = END;
    const L = { x: 36, w: 400 };
    const RX = 470;

    // ---------------- FACTS: pre-root (full card) ----------------
    const tClient = at('Your client is a firecracker', 'client'), tFirm = at('Your client is a firecracker', 'firecracker');
    const tRoot = at('how many crackers will India burst this Diwali?', 'how');
    E({ x: RX, y: 104, in: tClient, out: tRoot, cls: 'lbl', html: 'Client' });
    E({ x: RX, y: 132, in: tFirm, out: tRoot, cls: 'h1', html: '<span style="font-size:38px">Firecracker manufacturer</span>' });
    E({ x: RX, y: 206, in: at("planning next year's production.", 'production.'), out: tRoot, html: '<span class="pill">Planning next year\'s production</span>' });
    E({ x: RX, y: 280, in: at('The CEO asks:', 'CEO'), out: tRoot, cls: 'lbl', html: 'CEO asks' });
    E({ x: L.x + 80, y: 110, w: 260, h: 260, in: tFirm, out: tRoot, html: sz(IC.rocket, 260) });

    // ---------------- FACTS: tree (right) ----------------
    E({ x: RX, y: 84, w: 500, h: 84, fs: 27, in: tRoot, out: END, cls: 'qbox', html: 'How many crackers will India burst this Diwali?',
      moves: [{ t: PH, x: 151, y: 76, w: 700, h: 52, fs: 24 }] });
    const tClar = at('ask clarifying questions', 'clarifying');
    E({ x: RX, y: 182, in: tClar, out: PH, cls: 'lbl', html: 'Clarifying questions' });
    const rowY = [214, 262, 310], QX = RX, AX = RX + 262;
    const ROW = (r, cl, q, tq, a, ta) => {
      E({ x: QX, y: rowY[r], in: tq, out: PH, cls: cl, html: q });
      E({ x: AX - 22, y: rowY[r], in: ta, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: ta, out: PH, cls: cl === 'qp' ? 'ap' : 'fv', html: a });
    };
    const tCounts = at('what counts as one cracker', 'counts'), tAny = at('anything you light once.', 'anything');
    const tPhul = at('a phuljhadi stick', 'phuljhadi'), tLadi = at('so does a ladi.', 'ladi.');
    const tSizing = at('Are we sizing', 'sizing'), tAll = at('She said all of India,', 'all'), tDiw = at('only for Diwali.', 'Diwali.');
    const tHold = at('anything holding demand back?', 'holding'), tYes = at('She said yes.', 'yes.');
    const tBan = at('banned crackers,', 'banned'), tApt = at('live in apartments', 'apartments');
    ROW(0, 'qp', 'What counts as one?', tCounts, 'Anything lit once', tAny);
    ROW(1, 'qp', 'All India or region?', tSizing, `All India<span data-in="${tDiw}">&nbsp;· Diwali</span>`, tAll);
    ROW(2, 'qp', 'Holding demand back?', tHold, 'Yes', tYes);

    // ---------------- FACTS: left beat visuals ----------------
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tRoot, out: tPhul, cls: 'ph', html: '? ? cr' });
    E({ x: L.x + 40, y: 316, w: 320, in: tRoot, out: tPhul, cls: 'sub', html: '<div style="text-align:center">crackers this Diwali</div>' });
    const TILE = (x, ic, t, lbl) => E({ x, y: 120, w: 160, in: t, out: tSizing, html:
      `<div style="display:flex;flex-direction:column;align-items:center;gap:6px">${sz(IC[ic], 120)}<div class="sub">${lbl}</div><div class="mid" style="font-size:34px">= 1</div></div>` });
    TILE(L.x + 30, 'sparkler', tPhul, 'Phuljhadi');
    TILE(L.x + 210, 'ladi', tLadi, 'Ladi');
    E({ x: L.x + 30, y: 150, in: tAll, out: tHold, html: `<div class="big" style="font-size:72px">All India</div><div class="sub" data-in="${tDiw}" style="margin-top:14px">Diwali only</div>` });
    E({ x: L.x + 20, y: 112, in: tHold, out: PH, cls: 'lbl', html: 'Holding demand back' });
    E({ x: L.x + 20, y: 150, in: tBan, out: PH, html: '<span class="chip">① Bans in some states</span>' });
    E({ x: L.x + 20, y: 214, in: tApt, out: PH, html: '<span class="chip">② Apartments: can\'t burst</span>' });

    // ---------------- SOLVE: tabs + count bar ----------------
    const tDem = at('from the demand side, counting', 'demand'), tSup = at('or from the supply side,', 'supply');
    const tBuild = at("I'll build it from the demand side", 'demand'), tCheck = at('use supply to check', 'check');
    const tNow = at('Now, the check from the supply side.', 'Now,');
    E({ x: 300, y: 142, in: tDem, out: END, cls: 'tab', html: '<span class="dot"></span>Demand side', states: [{ t: tBuild, c: 'on' }, { t: tNow, c: '' }] });
    E({ x: 560, y: 142, in: tSup, out: END, cls: 'tab', html: '<span class="dot"></span>Supply side', states: [{ t: tNow, c: 'on' }] });
    E({ x: 590, y: 172, in: tCheck, out: tNow, cls: 'sub', html: '<span style="font-size:16px">check</span>' });
    const BX = 70, BW = 863, BY = 470, X = (v) => BX + BW * v / 400;
    E({ x: BX, y: BY - 28, in: tSup, out: END, cls: 'lbl', html: '<span style="font-size:14px">Crackers this Diwali</span>' });
    E({ x: BX, y: BY, w: BW, in: tSup, out: END, html: `<div style="width:${BW}px;height:40px;border-radius:10px;background:var(--acc-xl)"></div>` });
    [0, 100, 200, 300, 400].forEach(v => E({ x: X(v), y: BY + 48, in: tSup, out: END, cls: 'axl', html: v ? v + ' cr' : '0' }));
    const t160 = at('about 160 crore crackers from cities.', '160'), t200 = at('about 200 crore from villages.', '200');
    const t360 = at('about 360 crore crackers on Diwali,', '360'), tThan = at('in villages than cities.', 'villages');
    const SEG = (v0, v1, tin, col, txt) => E({ x: X(v0), y: BY, in: tin, out: END, z: 2, html:
      `<div class="sbar" data-bar data-at="${tin}" data-dur="0.5" style="width:${X(v1) - X(v0)}px;height:40px;border-radius:${v0 ? '0 10px 10px 0' : '10px 0 0 10px'}"><div style="width:${X(v1) - X(v0)}px;background:${col}">${txt}</div></div>` });
    SEG(0, 160, t160, 'var(--navy)', 'Cities 160 cr');
    SEG(160, 360, t200, 'var(--accent)', 'Villages 200 cr');
    E({ x: X(160) - 4, y: BY - 4, w: X(360) - X(160) + 8, in: tThan, out: END, z: 3, html: `<div style="width:${X(360) - X(160) + 8}px;height:48px;border:3px solid var(--hl);border-radius:12px;box-shadow:0 0 0 2px var(--accent)"></div>` });
    E({ x: X(360), y: BY - 30 - 44, in: t360, out: END, m: 'drop', cls: 'mk', z: 3,
      html: `<span class="ms">India · Diwali</span><span class="ml" style="position:relative">360 cr<span class="hlbar" data-bar data-at="${t360 + 0.15}" data-dur="0.3"></span></span><span class="stem" style="height:30px"></span>` });
    E({ x: 862, y: 84, in: t360, out: END, z: 3, html: '<span class="pill" style="font-size:20px;padding:6px 14px;background:var(--hl)">≈ 360 cr</span>' });

    // ---------------- SOLVE: equation + households ----------------
    const tSecond = at('Second, we will then look at cities.', 'Second,');
    const tHH = at('households times share', 'households'), tShare = at('times share that buy', 'share'), tPer = at('times crackers per household.', 'crackers');
    const chip = (x, y, tin, tout, txt, c = '') => E({ x, y, in: tin, out: tout, html: `<span class="chip ${c}">${txt}</span>` });
    chip(60, 196, tHH, tSecond, 'Households');
    E({ x: 252, y: 204, in: at('households times share', 'times'), out: tSecond, cls: 'mid', html: '<span style="font-size:28px;color:var(--grey)">×</span>' });
    chip(290, 196, tShare, tSecond, 'Share that buy');
    E({ x: 520, y: 204, in: at('times crackers per household.', 'times'), out: tSecond, cls: 'mid', html: '<span style="font-size:28px;color:var(--grey)">×</span>' });
    chip(558, 196, tPer, tSecond, 'Crackers / home');
    chip(60, 196, at("look at here is households.", 'households.'), tSecond, 'Households', 'dark');
    E({ x: 60, y: 272, in: at('about 140 crore people.', '140'), out: tSecond, html: `<div class="big" style="font-size:72px"><span data-to="140" data-from="80" data-fmt="{n} cr"></span></div><div class="sub" style="margin-top:6px">people</div>` });
    chip(380, 266, at('About 40 crore live in cities', '40'), tSecond, 'Urban 40 cr ÷ 4');
    chip(660, 266, at('10 crore urban households.', '10'), tSecond, '= 10 cr homes', 'res');
    chip(380, 330, at('The other 100 crore are rural', '100'), tSecond, 'Rural 100 cr ÷ 5');
    chip(660, 330, at('20 crore rural households.', '20'), tSecond, '= 20 cr homes', 'res');

    // ---------------- SOLVE: tables (Cities, Villages) ----------------
    const TBL = (tin, tout, title, rows) => {
      const cell = (v, t, w, b = false) => `<div data-in="${t}" style="width:${w}px;font-size:24px;font-weight:${b ? 600 : 500};color:var(--ink)">${v}</div>`;
      const hd = (v, w) => `<div style="width:${w}px;font-size:14px;font-weight:500;letter-spacing:1.2px;text-transform:uppercase;color:var(--grey)">${v}</div>`;
      const W = [120, 140, 130, 170];
      const body = rows.map(r => `<div style="display:flex;align-items:center;height:38px;border-top:1.5px solid #ECEEF6">
        ${cell(r[0], r[1][1], W[0])}${cell(r[1][0], r[1][1], W[1], true)}${cell(r[2][0], r[2][1], W[2], true)}${cell(r[3][0], r[3][1], W[3], true)}</div>`).join('');
      E({ x: 60, y: 192, in: tin, out: tout, html: `<div class="lbl" style="margin-bottom:10px">${title}</div>
        <div style="display:flex;height:24px;align-items:center">${hd('', W[0])}${hd('Homes', W[1])}${hd('% buy', W[2])}${hd('Crackers each', W[3])}</div>${body}` });
    };
    const tHalf = at('about half the rich', 'half'), tAfter = at('at 100, 40 and 15', '100');
    TBL(tSecond, at('Third, villages.', 'Third,'), 'Cities · 10 cr homes', [
      ['Rich', ['1 cr', at('into 1 crore rich, 4 crore', '1')], ['50%', tHalf], ['100', tAfter]],
      ['Middle', ['4 cr', at('4 crore middle and 5', '4')], ['50%', tHalf], ['40', at('at 100, 40 and 15', '40')]],
      ['Low', ['5 cr', at('and 5 crore low income', '5')], ['40%', at('about 40% of the low', '40%')], ['15', at('at 100, 40 and 15', '15')]],
    ]);
    chip(680, 330, at('Because of bans and apartments,', 'bans'), at('Third, villages.', 'Third,'), 'Bans + apartments');
    E({ x: 680, y: 196, in: t160, out: at('Third, villages.', 'Third,'), html: `<div class="big" style="font-size:72px">≈ <span data-to="160" data-from="96" data-fmt="{n} cr"></span></div><div class="sub" style="margin-top:6px">crackers from cities</div>` });
    const tThird = at('Third, villages.', 'Third,');
    TBL(tThird, tNow, 'Villages · 20 cr homes', [
      ['Rich', ['1 cr', at('1 crore rich, 5 crore middle', '1')], ['80%', at('80%, 60% and half,', '80%')], ['50', at('at 50, 30 and 10', '50,')]],
      ['Middle', ['5 cr', at('5 crore middle and 14', '5')], ['60%', at('80%, 60% and half,', '60%')], ['30', at('at 50, 30 and 10', '30')]],
      ['Low', ['14 cr', at('and 14 crore low.', '14')], ['50%', at('80%, 60% and half,', 'half,')], ['10', at('at 50, 30 and 10', '10')]],
    ]);
    E({ x: 680, y: 196, in: t200, out: tNow, html: `<div class="big" style="font-size:72px">≈ <span data-to="200" data-from="120" data-fmt="{n} cr"></span></div><div class="sub" style="margin-top:6px">crackers from villages</div>` });
    chip(680, 330, tThan, tNow, 'Villages > cities', 'res');

    // ---------------- SOLVE: supply check ----------------
    chip(60, 204, at('around 16 rupees a cracker,', '16'), END, '₹16 / cracker');
    chip(290, 204, at('360 crore crackers is about', '360'), END, '× 360 cr crackers');
    E({ x: 580, y: 204, in: at('is about 6,000 crore,', '6,000'), out: END, html: `<span class="chip res">≈ ₹<span data-to="6000" data-from="3600" data-fmt="{n}"></span>&nbsp;cr</span>` });
    chip(60, 280, at('the cracker market does in a year.', 'market'), END, '≈ industry\'s yearly sales');
    const tHolds = at('So the number holds up.', 'holds');
    chip(460, 280, tHolds, END, 'Holds up ✓', 'res');

    // ---------------- END CARD ----------------
    const tFollow = at('Follow for part 44.', 'Follow');
    E({ x: 0, y: 92, w: 1003, in: END, html: `<div class="ec" style="margin-top:40px"><div class="s" style="font-weight:600;font-size:44px;color:var(--navy)">Solving real consultant cases</div><div class="p">Part 43</div>
      <div class="f" data-in="${tFollow}">Follow for Part 44</div></div>` });
  }
};
