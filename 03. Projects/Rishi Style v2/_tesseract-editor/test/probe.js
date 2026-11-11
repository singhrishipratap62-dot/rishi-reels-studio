const { chromium } = require(process.env.HOME + '/.npm/_npx/9833c18b2d85bc59/node_modules/playwright-core');
const fs=require('fs');
(async()=>{
  const exe=require('child_process').execSync("find ~/Library/Caches/ms-playwright/chromium-1248 -name 'Google Chrome for Testing' -type f -path '*MacOS*' | head -1").toString().trim();
  const b=await chromium.launch({executablePath:exe,headless:true,args:['--enable-unsafe-webgpu','--enable-features=Vulkan,WebGPU','--use-angle=metal']});
  for(const mode of ['edit']){
    const p=await b.newPage(); p.setDefaultTimeout(150000);
    await p.goto('http://127.0.0.1:8767/test/probe.html'); await p.waitForFunction('window.ready===true');
    const r=await p.evaluate(m=>window.run(m),mode);
    if(r.b64){ fs.writeFileSync(`test/saved_${mode}.tsrct`,Buffer.from(r.b64,'base64')); delete r.b64; }
    console.log(mode, JSON.stringify(r)); await p.close();
  }
  await b.close();
})().catch(e=>{console.error('FAIL',e.message);process.exit(1)});
