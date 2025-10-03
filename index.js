const { chromium } = require("playwright");
require("dotenv").config();

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({
    proxy: process.env.PROXY ? { server: process.env.PROXY } : undefined,
  });
  const page = await context.newPage();

  console.log("[INFO] Navigating to YouTube...");
  await page.goto("https://youtube.com");

  // Example action: search and play a video
  await page.fill("input#search", "lofi hip hop radio");
  await page.keyboard.press("Enter");
  await page.waitForTimeout(3000);

  await page.click("ytd-video-renderer a#thumbnail");
  console.log("[INFO] Playing video...");

  await page.waitForTimeout(15000); // watch 15s
  await browser.close();
})();
