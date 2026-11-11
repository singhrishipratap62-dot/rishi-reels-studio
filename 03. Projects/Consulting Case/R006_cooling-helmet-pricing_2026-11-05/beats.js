// R006 cooling helmet — beat config for engine/board.html. Times anchored to spoken words via at(phrase, word).
const IC = {
  helmet: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M12 62C12 32 34 14 58 14C80 14 94 32 94 54V70C94 77 89 82 82 82H40C24 82 12 74 12 62Z"/>
    <path class="s" d="M12 62C12 32 34 14 58 14C80 14 94 32 94 54V70C94 77 89 82 82 82H40C24 82 12 74 12 62Z"/>
    <path class="s" d="M52 38H94V60H60C55 60 52 56 52 52Z"/><path class="s" d="M24 46C30 34 40 26 52 24"/><path class="s" d="M30 70H50"/></svg>`,
  snow: `<svg class="ic" viewBox="0 0 100 100" style="width:30px;height:30px"><path class="s" d="M50 10V90M15 30L85 70M85 30L15 70M40 14L50 24L60 14M40 86L50 76L60 86"/></svg>`,
  thermo: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M42 66V18a8 8 0 0 1 16 0V66a16 16 0 1 1-16 0Z"/>
    <path class="s" d="M42 66V18a8 8 0 0 1 16 0V66a16 16 0 1 1-16 0Z"/><path class="s" d="M50 40V78"/><path class="s" d="M64 26H72M64 38H72M64 50H72"/></svg>`,
  weight: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M28 44H72L80 86H20Z"/><path class="s" d="M28 44H72L80 86H20Z"/><path class="s" d="M38 44C38 24 62 24 62 44"/></svg>`,
  battery: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M14 34H78V68H14Z"/><path class="s" d="M14 34H78V68H14Z"/><path class="s" d="M78 44H86V58H78"/><path class="s" d="M50 38L40 52H52L44 64"/></svg>`,
  shop: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M20 40V84H80V40Z"/><path class="s" d="M12 40L20 18H80L88 40Z"/><path class="s" d="M20 40V84H80V40"/><path class="s" d="M42 84V62H58V84"/><path class="s" d="M12 40C12 46 22 50 30 44C36 50 46 50 50 44C54 50 64 50 70 44C78 50 88 46 88 40"/></svg>`,
  scooter: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M48 30H78V58H48Z"/><path class="s" d="M48 30H78V58H48Z"/><path class="s" d="M10 74a10 10 0 1 0 20 0a10 10 0 1 0-20 0M70 74a10 10 0 1 0 20 0a10 10 0 1 0-20 0"/>
    <path class="s" d="M20 74H40L48 58H80L82 74"/><path class="s" d="M20 74L26 40H18"/></svg>`,
  sun: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M32 50a18 18 0 1 0 36 0a18 18 0 1 0-36 0"/><path class="s" d="M32 50a18 18 0 1 0 36 0a18 18 0 1 0-36 0"/>
    <path class="s" d="M50 8V20M50 80V92M8 50H20M80 50H92M20 20L28 28M72 72L80 80M80 20L72 28M28 72L20 80"/></svg>`,
};
const sz = (svg, px) => svg.replace('<svg class="ic"', `<svg class="ic" style="width:${px}px;height:${px}px"`);

var CFG = {
  part: 41, hookImg: 'HOOKIMG', mbbImg: 'MBBIMG', capMaxW: 680, capMaxWords: 4, s1CapTop: 632, bgVideo: true,
  hookQ: 'How do you price a helmet that keeps your head 10 degrees cooler?',
  s1End: 116/ (30000/1001), s2End: 180/(30000/1001),
  els: [],
  init(at) {
    const E = (o) => (this.els.push(o), o);
    const PH = at('So, how do we price it?', 'So');            // phase switch
    const END = at('This is part 41', 'This');                 // end card
    this.endT = END;
    const L = { x: 36, w: 400 };                                 // left zone
    const RX = 470;                                              // right zone x

    // ---------------- FACTS: pre-root (full card) ----------------
    const tClient = at('Your client is a helmet', 'client'), tHelmet = at('Your client is a helmet', 'helmet');
    const tRoot = at('how do we price this?', 'how');
    E({ x: RX, y: 104, in: tClient, out: tRoot, cls: 'lbl', html: 'Client' });
    E({ x: RX, y: 132, in: tHelmet, out: tRoot, cls: 'h1', html: 'Helmet company' });
    E({ x: L.x + 90, y: 120, w: 240, h: 240, in: tHelmet, out: at('On a 45 degree', '45'), html: sz(IC.helmet, 240) });
    E({ x: RX, y: 206, in: at('two-wheeler helmet', 'two-wheeler'), out: tRoot, html: '<span class="pill">Two-wheeler helmet</span>' });
    E({ x: RX, y: 266, in: at('with built-in cooling', 'built-in'), out: tRoot, html: `<span class="pill">${IC.snow} Built-in cooling</span>` });
    // thermometer comparison (L)
    const t45 = at('On a 45 degree', '45'), t35 = at("feels like it's 35", '35'), tNext = at('over the next five years', 'next');
    E({ x: L.x + 10, y: 96, in: t45, out: tNext, html: sz(IC.thermo, 120) });
    E({ x: L.x + 140, y: 104, in: t45, out: tNext, html: `<div class="big"><span data-to="45" data-from="27" data-fmt="{n}°C"></span></div><div class="sub" style="margin-top:6px">Afternoon</div>` });
    E({ x: L.x + 150, y: 236, in: t35, out: tNext, cls: 'sub', html: '↓' });
    E({ x: L.x + 140, y: 280, in: t35, out: tNext, html: `<div class="big" style="color:var(--accent)"><span data-to="35" data-from="45" data-fmt="{n}°C"></span></div><div class="sub" style="margin-top:6px">Feels like</div>` });
    E({ x: L.x + 10, y: 300, in: t35 + 0.3, out: tNext, html: '<span class="chip res">−10°C</span>' });
    E({ x: RX, y: 340, in: at('The marketing director', 'marketing'), out: tRoot, cls: 'lbl', html: 'Marketing director asks' });

    // ---------------- FACTS: tree (right) ----------------
    const root = E({ x: RX, y: 84, w: 500, h: 64, fs: 27, in: tRoot, out: END, cls: 'qbox', html: 'How do we price this?',
      moves: [{ t: PH, x: 271, y: 78, w: 460, h: 56, fs: 25 }] });
    E({ x: RX, y: 166, in: at('I asked clarifying questions', 'clarifying'), out: PH, cls: 'lbl', html: 'Clarifying questions' });
    const rowY = [196, 248, 300, 352, 404, 456], QX = RX, AX = RX + 198;
    const QA = (r, q, tq, a, ta) => {
      E({ x: QX, y: rowY[r], in: tq, out: PH, cls: 'qp', html: q });
      E({ x: AX - 22, y: rowY[r], in: ta, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: ta, out: PH, cls: 'ap', html: a });
    };
    QA(0, 'Objective?', at('what is the objective', 'what'), 'Max profit · 5 yrs', at('as much profit', 'profit'));
    QA(1, 'Anything similar?', at('Is there anything like it', 'Is'), 'None · patent pending', at('She said no', 'no'));
    QA(2, 'Downsides?', at('have any downside?', 'downside?'), 'Charges overnight, same weight', at('it charges overnight', 'charges'));
    const FACT = (r, l, tl, v, tv) => {
      E({ x: QX, y: rowY[r], in: tl, out: PH, cls: 'fl', html: l });
      E({ x: AX - 22, y: rowY[r], in: tv, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: tv, out: PH, cls: 'fv', html: v });
    };
    const t1000 = at('about 1,000 rupees', '1,000'), t1200 = at('costs 1,200 rupees', '1,200'), t30 = at('R&D cost of 30 crore', '30');
    FACT(3, 'Regular helmet', at('A regular helmet sells', 'regular'), '₹1,000', t1000);
    FACT(4, 'Cost to make', at('The new one costs', 'new'), '₹1,200', t1200);
    FACT(5, 'R&D', at('and R&D cost', 'R&D'), '₹30 cr', t30);

    // ---------------- FACTS: left beat visuals ----------------
    const tMarket = at('anything like it in the market', 'market');
    const tFive = at('the next five years', 'five');
    E({ x: L.x, y: 150, w: L.w, in: tNext, out: tMarket, html: `<div class="lbl" style="margin-bottom:16px">Profit horizon</div>
      <div class="yb">${[1,2,3,4,5].map(i => `<div><i data-bar data-at="${(tNext + (tFive + 0.5 - tNext) * (i - 1) / 5).toFixed(3)}" data-dur="0.18"></i><b>Y${i}</b></div>`).join('')}</div>
      <div class="mid" style="margin-top:22px"><span data-to="5" data-from="1" data-at="${tNext}" data-fmt="{n} years"></span></div>` });
    const tNo = at('She said no', 'no'), tPatent = at('the patent is pending', 'patent'), tHeavier = at('Is it heavier', 'heavier');
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tMarket, out: tNo, cls: 'ph', html: '? ? ?' });
    E({ x: L.x + 40, y: 110, in: tNo, out: tHeavier, html: `<div class="big">0</div><div class="sub" style="margin-top:8px">similar products in market</div>` });
    E({ x: L.x + 40, y: 300, in: tPatent, out: tHeavier, rot: -6, html: '<span class="stamp">PATENT PENDING</span>' });
    const tCharging = at('need charging', 'charging'), tOvernight = at('charges overnight', 'overnight'), tWeighs = at('and weighs the same', 'weighs');
    const tReg = at('A regular helmet sells', 'regular');
    E({ x: L.x + 30, y: 110, in: tHeavier, out: tReg, html: `${sz(IC.weight, 130)}<div class="mid" style="margin-top:8px">Heavier?</div>` });
    E({ x: L.x + 220, y: 110, in: tCharging, out: tReg, html: `${sz(IC.battery, 130)}<div class="mid" style="margin-top:8px">Charging?</div>` });
    E({ x: L.x + 220, y: 300, in: tOvernight, out: tReg, html: '<span class="chip"><span class="tick">✓</span>&nbsp;Overnight</span>' });
    E({ x: L.x + 30, y: 300, in: tWeighs, out: tReg, html: '<span class="chip"><span class="tick">✓</span>&nbsp;Same weight</span>' });
    const BIG = (tin, tout, to, fmt, lbl, from) => E({ x: L.x + 30, y: 150, in: tin, out: tout,
      html: `<div class="big"><span data-to="${to}" ${from != null ? `data-from="${from}"` : ''} data-fmt="${fmt}"></span></div><div class="sub" style="margin-top:10px">${lbl}</div>` });
    BIG(t1000, t1200, 1000, '₹{n}', 'Regular helmet');
    BIG(t1200, t30, 1200, '₹{n}', 'New one: cost to make');
    BIG(t30, PH, 30, '₹{n} cr', 'R&D cost');

    // ---------------- SOLVE: tabs + number line ----------------
    const tCost = at('First is cost,', 'cost,'), tComp = at('second is competition,', 'competition,'), tVal = at('third is value.', 'value.');
    const tOut = at('Competition is out', 'out'), tCost2 = at('First is the cost.', 'cost.'), tVal2 = at('The second is the value.', 'value.');
    E({ x: 230, y: 152, in: tCost, out: END, cls: 'tab', html: '<span class="dot"></span>Cost', states: [{ t: tCost2, c: 'on' }, { t: tVal2, c: '' }] });
    E({ x: 400, y: 152, in: tComp, out: END, cls: 'tab', html: '<span class="dot"></span>Competition', states: [{ t: tOut, c: 'off' }] });
    E({ x: 650, y: 152, in: tVal, out: END, cls: 'tab', html: '<span class="dot"></span>Value', states: [{ t: tVal2, c: 'on' }] });
    const AX0 = 70, AXW = 863, AXY = 508, X = (v) => AX0 + AXW * v / 20000;
    E({ x: AX0, y: AXY, w: AXW, in: tCost, out: END, html: '<div class="axis"></div>' });
    [5000, 10000, 15000, 20000].forEach(v => E({ x: X(v), y: AXY + 14, in: tCost, out: END, cls: 'axl', html: '₹' + v.toLocaleString('en-IN') }));
    const tFloor = at("That's our floor.", 'floor.'), tCeil = at("That's our ceiling.", 'ceiling.');
    const MK = (v, tin, label, sub, tier, cls = '', hl = false) => E({ x: X(v), y: AXY - 26 - tier * 26 - 44, in: tin, out: END, m: 'drop', cls: 'mk ' + cls, z: 3,
      html: `<span class="ms">${sub}</span><span class="ml" style="position:relative">${label}${hl ? `<span class="hlbar" data-bar data-at="${tin + 0.15}" data-dur="0.3"></span>` : ''}</span><span class="stem" style="height:${26 + tier * 26}px"></span>` });
    E({ x: X(1500), y: AXY - 3, in: tCeil + 0.1, out: END, z: 1, html: `<div class="range" data-bar data-at="${tCeil + 0.1}" data-dur="0.5" style="width:${X(18000) - X(1500)}px"></div>` });
    E({ x: X(1000) - 8, y: AXY + 4, in: at('next to a 1,000 rupee helmet', '1,000'), out: END, m: 'drop', z: 3,
      html: `<div style="display:flex;align-items:flex-start;gap:6px"><span style="width:3px;height:16px;background:#B7BBCB;border-radius:2px;margin-left:6px"></span><span style="font-size:16px;font-weight:600;color:var(--grey);margin-top:6px;white-space:nowrap">Regular ₹1,000</span></div>` });
    MK(1500, tFloor, '₹1,500', 'Floor', 1);
    MK(18000, tCeil, '₹18,000', 'Ceiling', 0);
    const t4000 = at('at around 4,000 rupees', '4,000');
    MK(4000, t4000, '₹4,000', 'Our price', 2, '', true);

    // ---------------- SOLVE: cost working ----------------
    const MY = [204, 262, 320];
    const chip = (x, y, tin, tout, txt, c = '') => E({ x, y, in: tin, out: tout, html: `<span class="chip ${c}">${txt}</span>` });
    chip(60, MY[0], at('Spread over 5 years,', '5'), tVal2, 'R&D ₹30 cr ÷ 5 yrs');
    chip(330, MY[0], at('is 6 crore a year.', '6'), tVal2, '= ₹6 cr / yr', 'res');
    chip(60, MY[1], at('sell 2 lakh helmets', '2'), tVal2, '÷ 2 lakh helmets / yr');
    chip(350, MY[1], at("that's 300 rupees a helmet.", '300'), tVal2, '= ₹300 / helmet', 'res');
    const t1500 = at('about 1,500 rupees.', '1,500');
    E({ x: 60, y: MY[2], in: at('So each one costs us', 'each'), out: tVal2, html: `<div style="display:flex;align-items:center;gap:14px">
      <div class="sbar" data-bar data-at="${at('So each one costs us', 'each')}" data-dur="0.5" style="width:${600}px"><div style="width:480px;background:var(--accent)">Make ₹1,200</div><div style="width:120px;background:var(--navy)">R&amp;D ₹300</div></div>
      <div class="mid" data-in="${t1500}">= ₹1,500</div></div>` });

    // ---------------- SOLVE: value working ----------------
    const tShop = at('stands in a shop', 'shop'), tR1000 = at('next to a 1,000 rupee helmet', '1,000'), t3000 = at('about 3,000 rupees', '3,000');
    const tPurch = at('might not purchase', 'purchase'), tWho = at('So, who really cares', 'So,');
    E({ x: 60, y: 200, in: tShop, out: tWho, html: sz(IC.shop, 120) });
    E({ x: 210, y: 222, in: tR1000, out: tWho, html: `<div class="sub">Regular</div><div class="mid">₹1,000</div>` });
    E({ x: 380, y: 246, in: t3000, out: tWho, cls: 'sub', html: 'vs' });
    E({ x: 450, y: 222, in: t3000, out: tWho, html: `<div class="sub">Ours at 2× cost</div><div class="mid" style="color:var(--accent)"><span data-to="3000" data-from="1500" data-fmt="₹{n}"></span></div>` });
    E({ x: 690, y: 236, in: t3000 + 0.35, out: tWho, html: '<span class="chip res">3× the price</span>' });
    E({ x: 445, y: 268, w: 150, h: 4, in: tPurch, out: tWho, z: 4, html: '<div data-bar data-dur="0.25" style="height:4px;background:#E0524B;border-radius:2px;transform-origin:left"></div>' });
    E({ x: 612, y: 226, in: tPurch, out: tWho, m: 'pop', z: 4, html: '<div class="cross" style="font-size:56px;line-height:1">✗</div>' });
    const tWho2 = at('who really cares', 'who'), tFood = at('Food delivery companies.', 'Food'), tPilot = at('In a pilot,', 'In');
    E({ x: 200, y: 222, w: 600, h: 120, in: tWho2, out: tFood, cls: 'ph', html: '<span style="font-size:34px;letter-spacing:0">Who cares about a cool head?</span>' });
    E({ x: 70, y: 196, in: tFood, out: tPilot, html: sz(IC.scooter, 140) });
    E({ x: 230, y: 226, in: tFood, out: tPilot, cls: 'mid', html: 'Food delivery companies' });
    E({ x: 560, y: 290, in: at('slow down or log off', 'slow'), out: tPilot, html: sz(IC.sun, 70) });
    chip(650, 300, at('slow down or log off', 'slow'), tPilot, 'Slow down');
    chip(810, 300, at('slow down or log off', 'log'), tPilot, 'Log off');
    // pilot maths
    const tSkip = at("So I'd skip the shop shelf", 'So');
    E({ x: 60, y: 192, in: at('In a pilot,', 'pilot,'), out: tSkip, cls: 'lbl', html: 'Pilot · per rider' });
    chip(60, 222, at('did two extra deliveries', 'two'), tSkip, '+2 deliveries / day');
    chip(320, 222, at('about 100 hot days,', '100'), tSkip, '× 100 hot days');
    chip(540, 222, at('about 30 rupees per order.', '30'), tSkip, '× ₹30 / order');
    chip(60, 280, at("That's 200 extra orders,", '200'), tSkip, '= 200 orders', 'res');
    E({ x: 260, y: 280, in: at('or 6,000 rupees per rider', '6,000'), out: tSkip, html: `<span class="chip res">=&nbsp;<span data-to="6000" data-fmt="₹{n}"></span>&nbsp;/ rider / summer</span>` });
    const t3s = at('lasts three summers,', 'three'), t18 = at('worth 18,000 rupees', '18,000');
    E({ x: 60, y: 338, w: 300, in: t3s, out: tSkip, html: `<div class="yb">${[1, 2, 3].map(i => `<div><i data-bar data-at="${(t3s + (i - 1) * 0.18).toFixed(3)}" data-dur="0.18"></i><b style="font-size:15px">Summer ${i}</b></div>`).join('')}</div>` });
    E({ x: 380, y: 334, in: t18, out: tSkip, html: `<span class="chip dark">₹6,000 × 3 = <span data-to="18000" data-from="6000" data-at="${t18}" data-fmt="&nbsp;₹{n}"></span></span>` });
    // recommendation
    E({ x: 60, y: 194, in: at('skip the shop shelf', 'shop'), out: END, html: `<div style="position:relative;width:70px;height:70px">${sz(IC.shop, 70)}<div style="position:absolute;left:-6px;top:32px;width:82px;height:4px;background:#E0524B;border-radius:2px;transform:rotate(-30deg)"></div></div>` });
    chip(150, 206, at('straight to delivery companies', 'delivery'), END, 'Sell direct → delivery companies');
    E({ x: 60, y: 266, in: at('The company gets back', 'back'), out: END, html: '<span class="chip">Pays ₹4,000 → gets ₹18,000</span>' });
    chip(436, 266, at('more than 4 times', '4'), END, '4.5× return', 'res');
    const tMake = at('and we make about', 'make'), t2500 = at('about 2,500 on every', '2,500');
    E({ x: 60, y: 326, in: tMake, out: END, html: `<div style="display:flex;align-items:center;gap:14px">
      <div class="sbar" data-bar data-at="${tMake}" data-dur="0.5" style="width:400px"><div style="width:150px;background:var(--navy)">Cost ₹1,500</div><div style="width:250px;background:var(--accent)">Margin ₹2,500</div></div>
      <div class="mid" data-in="${t2500}">= ₹4,000</div></div>` });
    const tLakhs = at('cover lakhs of riders.', 'lakhs');
    E({ x: 690, y: 196, in: at('one contract can cover', 'contract'), out: END, cls: 'lbl', html: '1 contract →' });
    E({ x: 690, y: 226, in: tLakhs, out: END, step: 0.012, html: `<div class="grid" style="grid-template-columns:repeat(12,16px)">${'<div></div>'.repeat(60)}</div><div class="sub" style="margin-top:8px">lakhs of riders</div>` });

    // ---------------- END CARD ----------------
    const tFollow = at('Follow for part 42.', 'Follow');
    E({ x: 0, y: 92, w: 1003, in: END, html: `<div class="ec" style="margin-top:40px"><div class="s" style="font-weight:600;font-size:44px;color:var(--navy)">Solving real consultant cases</div><div class="p">Part 41</div>
      <div class="f" data-in="${tFollow}">Follow for Part 42</div></div>` });
  }
};
