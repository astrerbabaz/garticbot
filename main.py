import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent

async def process_page(user_url, user_agent):
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Kullanıcının girdiği URL'ye git
    await page.goto(user_url)
    print(f'Sayfa başarıyla yüklendi: {user_url}')
    await page.waitForSelector('.btYellowBig.ic-playHome')
    await page.click('.btYellowBig.ic-playHome')
    # "btYellowBig ic-yes" sınıfına sahip butona tıkla
    await page.waitForSelector('.btYellowBig.ic-yes')
    await page.click('.btYellowBig.ic-yes')
    # "exit" ID'li elemente tıkla
    await page.waitForSelector('#exit')
    await page.click('#exit')
    # "btYellowBig smallButton ic-yes" sınıfına sahip butona tıkla
    await page.waitForSelector('.btYellowBig.smallButton.ic-yes')
    await page.click('.btYellowBig.smallButton.ic-yes')
    

    # Kullanıcı tarafından belirtilen kullanıcı ajanını kullan
    await page.setUserAgent(user_agent)

    # "btYellowBig ic-playHome" sınıfına sahip butona tıkla
    

    # Tarayıcıyı kapat
    await browser.close()

async def main():
    user_url = input('Lütfen gitmek istediğiniz sayfanın URL\'sini girin: ')

    if not user_url:
        print('Geçerli bir URL girilmedi. İşlem iptal edildi.')
        return

    ua = UserAgent()

    while True:
        user_agent = ua.random
        print(f"Kullanılan Kullanıcı Ajanı: {user_agent}")

        # Tarayıcı işlemlerini gerçekleştir
        await process_page(user_url, user_agent)

if __name__ == "__main__":
    asyncio.run(main())
