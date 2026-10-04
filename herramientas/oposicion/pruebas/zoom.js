const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:300,height:520}, deviceScaleFactor:3 });
  await p.goto('file:///tmp/claude-0/-home-user-niblo/d4a06324-57c5-5c80-9659-94fd013c3913/images/4.png');
  await p.screenshot({ path:'z1.png', clip:{x:0,y:0,width:290,height:520} });
  await p.setViewportSize({width:300,height:1100});
  await p.screenshot({ path:'z2.png', clip:{x:0,y:480,width:290,height:540} });
  await b.close();
})();
