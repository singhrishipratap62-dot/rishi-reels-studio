const { chromium } = require(process.env.HOME + '/.npm/_npx/9833c18b2d85bc59/node_modules/playwright-core');
(async () => {
  const exe = require('child_process').execSync("find ~/Library/Caches/ms-playwright/chromium_headless_shell-1248 -name chrome-headless-shell -type f | head -1").toString().trim();
  const b = await chromium.launch({ executablePath: exe });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.setContent('<div style="font:600 52px \'Avenir Next\'">Avenir test ₹1,500</div>');
  const t0 = Date.now(); for (let i = 0; i < 20; i++) await p.screenshot({ omitBackground: true, type: 'png' });
  console.log('ok', exe, (Date.now() - t0) / 20, 'ms/frame');
  await b.close();
})();
