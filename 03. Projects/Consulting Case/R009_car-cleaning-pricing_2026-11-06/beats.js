// R009 car-cleaning pricing — beat config for engine/board.html. Times anchored to spoken words via at(phrase, word).
const IC = {
  car: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M12 58L22 36Q25 30 32 30H68Q75 30 78 36L88 58V74H12Z"/>
    <path class="s" d="M12 58L22 36Q25 30 32 30H68Q75 30 78 36L88 58V74H12Z"/><path class="s" d="M24 52L30 38H70L76 52Z"/>
    <path class="s" d="M20 74a8 8 0 1 0 16 0M64 74a8 8 0 1 0 16 0"/><path class="s" d="M12 62H22M78 62H88"/>
    <path class="s" d="M84 14L84 24M79 19H89M70 10L70 16M67 13H73"/></svg>`,
  cal: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M16 24H84V86H16Z"/><path class="s" d="M16 24H84V86H16Z"/>
    <path class="s" d="M16 40H84"/><path class="s" d="M32 14V30M68 14V30"/><path class="s" d="M32 56H44M56 56H68M32 70H44"/></svg>`,
  spray: `<svg class="ic" viewBox="0 0 100 100"><path class="f" d="M34 40H62V88H34Z"/><path class="s" d="M34 40H62V88H34Z"/>
    <path class="s" d="M40 40V28H58L70 22V34L58 30"/><path class="s" d="M76 22L86 18M76 28L88 28M76 34L86 38"/><path class="s" d="M34 58H62"/></svg>`,
};
const sz = (svg, px) => svg.replace('<svg class="ic"', `<svg class="ic" style="width:${px}px;height:${px}px"`);

var CFG = {
  part: 44, hookImg: 'HOOKIMG', mbbImg: 'MBBIMG', capMaxW: 680, capMaxWords: 4, s1CapTop: 632, bgVideo: true,
  hookQ: 'How do you price a service that cleans your car every morning before you wake up?',
  s1End: 151 / (30000/1001), s2End: 230 / (30000/1001),
  els: [],
  init(at) {
    const E = (o) => (this.els.push(o), o);
    const PH = at('So how do we price it?', 'So');               // phase switch
    const END = at('This is part 44', 'This');                  // end card
    this.endT = END;
    const L = { x: 36, w: 400 };
    const RX = 470;

    // ---------------- FACTS: pre-root (full card) ----------------
    const tClient = at('Your client is a startup', 'client'), tSt = at('Your client is a startup', 'startup');
    const tRoot = at('what should we charge per month?', 'what');
    const tObj = at('what is the objective of the client?', 'objective');
    E({ x: RX, y: 104, in: tClient, out: tRoot, cls: 'lbl', html: 'Client' });
    E({ x: RX, y: 132, in: tSt, out: tRoot, cls: 'h1', html: 'Car-care startup' });
    E({ x: RX, y: 206, in: at('a startup in Gurgaon', 'Gurgaon'), out: tRoot, html: '<span class="pill">Gurgaon</span>' });
    E({ x: RX, y: 266, in: at('wash your car daily,', 'daily,'), out: tRoot, html: '<span class="pill">Trained cleaner · daily wash</span>' });
    E({ x: RX, y: 326, in: at('a full interior clean every week.', 'interior'), out: tRoot, html: '<span class="pill">Interior clean · weekly</span>' });
    E({ x: RX, y: 400, in: at('The founder has asked you:', 'founder'), out: tRoot, cls: 'lbl', html: 'Founder asks' });
    E({ x: L.x + 80, y: 110, w: 260, h: 260, in: at('sends a trained cleaner', 'trained'), out: tObj, html: sz(IC.car, 260) });

    // ---------------- FACTS: tree (right) ----------------
    E({ x: RX, y: 84, w: 500, h: 64, fs: 26, in: tRoot, out: END, cls: 'qbox', html: 'What to charge per month?',
      moves: [{ t: PH, x: 251, y: 78, w: 500, h: 56, fs: 24 }] });
    E({ x: RX, y: 162, in: at('ask clarifying questions,', 'clarifying'), out: PH, cls: 'lbl', html: 'Clarifying questions' });
    const rowY = [194, 242, 290, 338, 386, 434, 482], QX = RX, AX = RX + 198;
    const ROW = (r, cl, q, tq, a, ta) => {
      E({ x: QX, y: rowY[r], in: tq, out: PH, cls: cl, html: q });
      E({ x: AX - 22, y: rowY[r], in: ta, out: PH, cls: 'arrow', html: '→' });
      E({ x: AX, y: rowY[r], in: ta, out: PH, cls: cl === 'qp' ? 'ap' : 'fv', html: a });
    };
    const tProf = at('it has to become profitable', 'profitable');
    const tAny = at('Is there anything like it in the market?', 'anything');
    const tLocal = at('She said local cleaners charge', 'local'), t600 = at('charge about 600 rupees a month,', '600');
    const tSkip = at('they skip days', 'skip'), tWipe = at('only wipe from the outside.', 'wipe');
    const tCostQ = at('what does it cost us?', 'cost'), t15k = at('a cleaner earns 15,000 rupees', '15,000');
    const tSpread = at('If the cars are spread across', 'spread'), t20 = at('do about 20 cars a day,', '20');
    const tSoc = at('in one housing society', 'society'), t30 = at('he can do about 30.', '30.');
    const tSup = at('Supplies and app cost us', 'Supplies'), t200 = at('about 200 rupees per car a month.', '200');
    const tWin = at('Winning a customer through online ads', 'Winning'), t2k = at('costs about 2,000 rupees,', '2,000');
    const tCamp = at('through a camp inside a society', 'camp'), t500c = at('only about 500.', '500.');
    const tStays = at('A customer stays about 10 months.', 'stays'), t10 = at('A customer stays about 10 months.', '10');
    ROW(0, 'qp', 'Objective?', tObj, 'Profitable in yr 1–2', tProf);
    ROW(1, 'qp', 'Anything like it?', tAny, 'Local cleaners · ₹600 / mo', t600);
    ROW(2, 'qp', 'Our costs?', tCostQ, 'Cleaner ₹15,000 / mo', t15k);
    ROW(3, 'fl', 'Cars / cleaner / day', tSpread, `20 homes<span data-in="${t30}">&nbsp;· 30 society</span>`, t20);
    ROW(4, 'fl', 'Supplies + app', tSup, '₹200 / car / mo', t200);
    ROW(5, 'fl', 'Win a customer', tWin, `Ad ₹2,000<span data-in="${t500c}">&nbsp;· Camp ₹500</span>`, t2k);
    ROW(6, 'fl', 'Customer stays', tStays, '10 months', t10);

    // ---------------- FACTS: left beat visuals ----------------
    E({ x: L.x + 20, y: 112, in: tObj, out: tAny, cls: 'lbl', html: 'Client wants' });
    E({ x: L.x + 30, y: 150, in: tProf, out: tAny, html: sz(IC.cal, 120) });
    E({ x: L.x + 170, y: 176, in: tProf, out: tAny, html: '<span class="chip res">Profitable · yr 1–2</span>' });
    E({ x: L.x + 40, y: 130, w: 320, h: 170, in: tAny, out: tLocal, cls: 'ph', html: '? ? ?' });
    E({ x: L.x + 20, y: 112, in: tLocal, out: tCostQ, cls: 'lbl', html: 'Local cleaner' });
    E({ x: L.x + 20, y: 150, in: t600, out: tCostQ, html: `<div class="big"><span data-to="600" data-from="200" data-fmt="₹{n}"></span></div><div class="sub" style="margin-top:10px">per month</div>` });
    E({ x: L.x + 20, y: 290, in: tSkip, out: tCostQ, html: '<span class="chip"><span class="cross">✗</span>&nbsp;Skips days</span>' });
    E({ x: L.x + 20, y: 350, in: tWipe, out: tCostQ, html: '<span class="chip"><span class="cross">✗</span>&nbsp;Outside wipe only</span>' });
    E({ x: L.x + 20, y: 150, in: t15k, out: tSpread, html: `<div class="big"><span data-to="15000" data-from="8000" data-fmt="₹{n}"></span></div><div class="sub" style="margin-top:10px">cleaner · per month</div>` });
    E({ x: L.x + 20, y: 116, in: tSpread, out: tSup, cls: 'lbl', html: 'Cars per cleaner / day' });
    const SB = (y, tl, lbl, w, tb, txt) => E({ x: L.x + 20, y, in: tl, out: tSup, html: `<div style="display:flex;align-items:center;gap:14px">
      <div class="sub" style="width:130px;color:var(--ink);font-weight:600">${lbl}</div><div style="width:240px;height:46px;border-radius:10px;background:var(--acc-xl);overflow:hidden">
      <div class="sbar" data-bar data-at="${tb}" data-dur="0.5" style="width:${w}px"><div style="width:${w}px;background:var(--accent)">${txt}</div></div></div></div>` });
    SB(156, tSpread, 'Scattered', 160, t20, '20 cars');
    SB(226, tSoc, 'One society', 240, t30, '30 cars');
    E({ x: L.x + 20, y: 150, in: t200, out: tWin, html: `<div class="big"><span data-to="200" data-from="50" data-fmt="₹{n}"></span></div><div class="sub" style="margin-top:10px">supplies + app · per car / mo</div>` });
    E({ x: L.x + 20, y: 116, in: tWin, out: tStays, cls: 'lbl', html: 'Cost to win a customer' });
    const WT = (x, t, lbl, val, tv) => E({ x, y: 156, w: 180, in: t, out: tStays, html:
      `<div style="display:flex;flex-direction:column;gap:8px"><div class="sub">${lbl}</div><div class="mid" data-in="${tv}">${val}</div></div>` });
    WT(L.x + 20, at('through online ads', 'online'), 'Online ad', '₹2,000', t2k);
    WT(L.x + 220, tCamp, 'Society camp', '₹500', t500c);
    E({ x: L.x + 20, y: 150, in: t10, out: PH, html: `<div class="big"><span data-to="10" data-from="0" data-fmt="{n} months"></span></div><div class="sub" style="margin-top:10px">a customer stays</div>` });

    // ---------------- SOLVE: tabs + number line ----------------
    const tCost = at('First, cost;', 'cost;'), tComp = at('second, competition;', 'competition;'), tVal = at('and third, value.', 'value.');
    const tCost2 = at('First is the cost approach.', 'cost'), tComp2 = at('Second is the competition.', 'Second');
    const tVal2 = at('And third is value.', 'third'), tRec = at("So I'd price it", 'So');
    E({ x: 230, y: 152, in: tCost, out: END, cls: 'tab', html: '<span class="dot"></span>Cost', states: [{ t: tCost2, c: 'on' }, { t: tComp2, c: '' }] });
    E({ x: 400, y: 152, in: tComp, out: END, cls: 'tab', html: '<span class="dot"></span>Competition', states: [{ t: tComp2, c: 'on' }, { t: tVal2, c: '' }] });
    E({ x: 650, y: 152, in: tVal, out: END, cls: 'tab', html: '<span class="dot"></span>Value', states: [{ t: tVal2, c: 'on' }, { t: tRec, c: '' }] });
    const AX0 = 70, AXW = 863, AXY = 508, X = (v) => AX0 + AXW * v / 3000;
    E({ x: AX0, y: AXY, w: AXW, in: tCost, out: END, html: '<div class="axis"></div>' });
    [0, 2000].forEach(v => E({ x: X(v), y: AXY + 14, in: tCost, out: END, cls: 'axl', html: '₹' + v.toLocaleString('en-IN') }));
    const t1150 = at("That's 1,150 rupees.", '1,150'), tFloor = at("That's about 750 rupees.", '750'), tCeil = at("That's our ceiling.", 'ceiling.');
    const tThou = at('close to a thousand or twelve hundred', 'thousand'), tTw = at('close to a thousand or twelve hundred', 'twelve');
    const MK = (v, tin, label, sub, tier, hl = false) => E({ x: X(v), y: AXY - 26 - tier * 26 - 44, in: tin, out: END, m: 'drop', cls: 'mk', z: 3,
      html: `<span class="ms">${sub}</span><span class="ml" style="position:relative">${label}${hl ? `<span class="hlbar" data-bar data-at="${tin + 0.15}" data-dur="0.3"></span>` : ''}</span><span class="stem" style="height:${26 + tier * 26}px"></span>` });
    const GM = (v, tin, txt, right = false) => E({ x: right ? X(v) - 160 : X(v) - 8, y: AXY + 4, w: right ? 168 : null, in: tin, out: END, m: 'drop', z: 3,
      html: `<div style="display:flex;align-items:flex-start;gap:6px;${right ? 'flex-direction:row-reverse' : ''}"><span style="width:3px;height:16px;background:#B7BBCB;border-radius:2px;${right ? 'margin-right:6px' : 'margin-left:6px'}"></span><span style="font-size:16px;font-weight:600;color:var(--grey);margin-top:6px;white-space:nowrap">${txt}</span></div>` });
    GM(1150, t1150, 'Homes ₹1,150');
    MK(750, tFloor, '₹750', 'Floor', 1);
    const tL600 = at('A local cleaner is about 600 rupees,', '600');
    GM(600, tL600, 'Local ₹600', true);
    E({ x: X(750), y: AXY - 3, in: tCeil + 0.1, out: END, z: 1, html: `<div class="range" data-bar data-at="${tCeil + 0.1}" data-dur="0.5" style="width:${X(2600) - X(750)}px"></div>` });
    MK(2600, tCeil, '₹2,600', 'Ceiling', 1);
    E({ x: X(1000), y: AXY - 3, in: tTw, out: END, z: 2, html: `<div data-bar data-at="${tTw}" data-dur="0.3" style="width:${X(1200) - X(1000)}px;height:10px;border-radius:5px;background:var(--accent);transform-origin:left"></div>` });
    MK(1000, tThou, '₹1,000', 'Our price', 2, true);

    // ---------------- SOLVE: cost working ----------------
    const chip = (x, y, tin, tout, txt, c = '') => E({ x, y, in: tin, out: tout, html: `<span class="chip ${c}">${txt}</span>` });
    E({ x: 60, y: 196, in: tCost2, out: tComp2, cls: 'lbl', html: 'Scattered homes' });
    E({ x: 530, y: 196, in: at('Inside one society,', 'Inside'), out: tComp2, cls: 'lbl', html: 'One society' });
    chip(60, 226, at('the cleaner costs 750 rupees per car,', '750'), tComp2, '₹15,000 ÷ 20 = ₹750');
    chip(60, 282, at('plus 200 for supplies,', '200'), tComp2,
      `+ ₹200 supplies<span data-in="${at('plus 200 a month to win', '200')}">&nbsp;+ ₹200 to win</span>`);
    chip(60, 338, t1150, tComp2, '= ₹1,150 / mo', 'res');
    chip(530, 226, at('the cleaner cost drops to 500,', '500,'), tComp2, '₹15,000 ÷ 30 = ₹500');
    chip(530, 282, at('costs just 50 rupees a month.', '50'), tComp2, '+ ₹200 supplies + ₹50 to win');
    chip(530, 338, tFloor, tComp2, '= ₹750 / mo', 'res');

    // ---------------- SOLVE: competition working ----------------
    E({ x: 70, y: 196, in: tL600, out: tVal2, html: sz(IC.spray, 90) });
    E({ x: 180, y: 206, in: tL600, out: tVal2, html: '<div class="sub">Local cleaner</div><div class="mid">₹600 / mo</div>' });
    chip(480, 220, at('customers will compare us to that itself.', 'compare'), tVal2, 'Customers compare us to this', 'res');

    // ---------------- SOLVE: value working ----------------
    chip(60, 210, at('A weekly interior clean', 'weekly'), tRec, `Car-wash interior ₹500 / wk`);
    chip(460, 210, at('which is 2,000 rupees a month.', '2,000'), tRec, '× 4 = ₹2,000 / mo', 'res');
    chip(60, 280, at('Add 600 rupee local cleaner,', 'Add'), tRec, '+ ₹600 local cleaner');
    chip(360, 280, at('would otherwise spend 2,600 rupees.', '2,600'), tRec, '= ₹2,600 they’d spend', 'dark');

    // ---------------- SOLVE: recommendation ----------------
    const t1000 = at('At 1,000 rupees,', '1,000');
    chip(60, 204, tThou, END, 'Price ≈ ₹1,000 – ₹1,200', 'dark');
    chip(60, 266, at('well below the 2,600', 'below'), t1000, '✓ Well below ₹2,600');
    chip(420, 266, at('close enough to the local cleaner', 'enough'), t1000, `✓ Near local ₹600<span data-in="${at('with slightly more premium.', 'premium.')}">&nbsp;· slight premium</span>`);
    E({ x: 420, y: 216, in: t1000, out: END, cls: 'lbl', html: 'At ₹1,000 / month' });
    chip(60, 266, at('loses us about 150 rupees', '150'), END, '<span style="color:#E0524B">Scattered home&nbsp;−₹150 / mo</span>');
    chip(470, 266, at('makes about 250 rupees.', '250'), END, 'Society&nbsp;+₹250 / mo', 'res');
    chip(60, 326, at('launch in societies', 'societies'), END, `Launch in societies<span data-in="${at('at least 30 cars sign up.', '30')}">&nbsp;· ≥ 30 cars</span>`, 'dark');
    chip(520, 326, at('a 25% margin,', '25%'), END, '25% margin', 'res');
    E({ x: 700, y: 336, in: at('every new customer in the same building', 'new'), out: END, cls: 'sub', html: '↑ each new car in<br>the building' });

    // ---------------- END CARD ----------------
    const tFollow = at('Follow for part 45.', 'Follow');
    E({ x: 0, y: 92, w: 1003, in: END, html: `<div class="ec" style="margin-top:40px"><div class="s" style="font-weight:600;font-size:44px;color:var(--navy)">Solving real consultant cases</div><div class="p">Part 44</div>
      <div class="f" data-in="${tFollow}">Follow for Part 45</div></div>` });
  }
};
