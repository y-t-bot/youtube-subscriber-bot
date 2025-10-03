import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(proxy={"server": os.getenv("PROXY")} if os.getenv("PROXY") else None)
        page = await context.new_page()

        print("[INFO] Navigating to YouTube...")
        await page.goto("https://youtube.com")

        # Example action: search and play a video
        await page.fill("input#search", "lofi hip hop radio")
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(3000)

        await page.click("ytd-video-renderer a#thumbnail")
        print("[INFO] Playing video...")

        await page.wait_for_timeout(15000)  # watch 15s
        await browser.close()

asyncio.run(run())
