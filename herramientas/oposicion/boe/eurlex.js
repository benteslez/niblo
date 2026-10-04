const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  // El proxy del entorno firma con su propia CA: se confía SOLO en esa clave.
  const ca = '/root/.ccr/agent-proxy-ca.crt', fs = require('fs'), cp = require('child_process');
  const args = fs.existsSync(ca) ? ['--ignore-certificate-errors-spki-list=' + cp.execSync(`openssl x509 -in ${ca} -pubkey -noout | openssl pkey -pubin -outform der | openssl dgst -sha256 -binary | base64`).toString().trim()] : [];
  const b = await chromium.launch({ channel:'chromium', args }); const p = await b.newPage();
  const url = process.argv[2], out = process.argv[3];
  const r = await p.goto(url, { waitUntil:'networkidle', timeout:90000 });
  for (let i = 0; i < 12; i++) { await p.waitForTimeout(2500); if ((await p.content()).length > 50000) break; }
  const html = await p.content();
  require('fs').writeFileSync(out, html);
  console.log(r && r.status(), html.length, (await p.title()));
  await b.close();
})();
