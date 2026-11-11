#!/usr/bin/env node
// Deterministic overlay renderer. Writes concatenated PNG frames to stdout (pipe into ffmpeg -f image2pipe).
// usage: node render.js <projectDir> <fromFrame> <toFrame(excl)> [--alpha] [--still out.png --t seconds]
const fs = require('fs'), path = require('path'), { execSync } = require('child_process');
const { chromium } = require(process.env.HOME + '/.npm/_npx/9833c18b2d85bc59/node_modules/playwright-core');
const [proj, a0, b0] = process.argv.slice(2);
const alpha = process.argv.includes('--alpha');
const si = process.argv.indexOf('--still'), stillOut = si > 0 ? process.argv[si + 1] : null;
const ti = process.argv.indexOf('--t'), stillT = ti > 0 ? process.argv.slice(ti + 1).map(Number) : null;
const FPS = 30000 / 1001;
(async () => {
  const exe = execSync("find ~/Library/Caches/ms-playwright -name chrome-headless-shell -type f | sort | tail -1").toString().trim();
  const b = await chromium.launch({ executablePath: exe });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.join(__dirname, 'board.html'));
  const words = fs.readFileSync(path.join(proj, 'words.json'), 'utf8');
  const img = 'data:image/jpeg;base64,' + fs.readFileSync(path.join(proj, 'hook.jpg')).toString('base64');
  let root = __dirname; while (!fs.existsSync(path.join(root, '.studio-root')) && root !== path.dirname(root)) root = path.dirname(root);
  const mbbF = path.join(root, '05. Asset Library/stickers/mbb_logos_trim.png');
  const mbb = fs.existsSync(mbbF) ? 'data:image/png;base64,' + fs.readFileSync(mbbF).toString('base64') : 'none';
  const beats = fs.readFileSync(path.join(proj, 'beats.js'), 'utf8').replace('HOOKIMG', img).replace('MBBIMG', mbb);
  await p.addScriptTag({ content: `var WORDS=${words};\n${beats}` });
  await p.evaluate(() => document.fonts.ready);
  const phr = await p.evaluate(() => window.__ready());
  fs.writeFileSync(path.join(proj, 'captions.txt'), phr.join('\n'));
  await p.waitForTimeout(200);
  const ei = process.argv.indexOf('--events');
  if (ei > 0) {  // dump visual events for the sound pass (sfx.py)
    const ev = await p.evaluate(() => ({
      s1End: CFG.s1End, s2End: CFG.s2End,
      els: ELS.map(e => ({ t: e.in, out: e.out ?? null, cls: e.cls || '', m: e.m || '', svg: e.paths.length > 0,
        count: e.counts.length > 0, bar: e.bars.length > 0, grid: e.units.length > 0, subs: e.subs.map(s => +s.dataset.in),
        bars: e.bars.map(b => +(b.dataset.at || e.in)), states: (e.states || []).map(s => s.t), moves: (e.moves || []).map(m => m.t),
        text: e.node.textContent.replace(/\s+/g, ' ').trim().slice(0, 40) })),
      caps: PHR.map(ph => ph.map(i => WORDS[i].s)), hookWords: QW.map((q, k) => WORDS[k].s) }));
    fs.writeFileSync(process.argv[ei + 1], JSON.stringify(ev, null, 1)); await b.close(); return;
  }
  if (stillOut) {
    for (const t of stillT) { await p.evaluate(t => seek(t), t); await p.screenshot({ path: stillOut.replace('%t', t.toFixed(2)), omitBackground: alpha }); }
  } else {
    // headless-shell screenshots occasionally hang (lesson E1.11): short timeout, force a repaint, retry.
    const shot = async (t) => {
      for (let k = 0; k < 6; k++) {
        try { return await p.screenshot({ omitBackground: alpha, type: 'png', timeout: 4000, animations: 'disabled', caret: 'initial' }); }
        catch (e) {
          process.stderr.write(`retry screenshot t=${t.toFixed(3)} (${k + 1})\n`);
          await p.evaluate(t => { document.body.style.outline = document.body.style.outline ? '' : '0px solid transparent'; seek(t); }, t).catch(() => {});
          await p.waitForTimeout(150);
        }
      }
      throw new Error('screenshot failed 6x at t=' + t);
    };
    for (let f = +a0; f < +b0; f++) {
      await p.evaluate(t => seek(t), f / FPS);
      const buf = await shot(f / FPS);
      if (!process.stdout.write(buf)) await new Promise(r => process.stdout.once('drain', r));
      if (f % 300 === 0) process.stderr.write(`frame ${f}\n`);
    }
  }
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
