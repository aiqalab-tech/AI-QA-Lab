from playwright.sync_api import sync_playwright

def analyze_application(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url)

        html = page.content()

        browser.close()

        return html