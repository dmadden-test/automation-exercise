from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    if 'UI' in scenario.tags:
        context.playwright = sync_playwright().start()
        context.browser = context.playwright.chromium.launch()
        context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if 'UI' in scenario.tags:
        context.page.close()
        context.browser.close()
        context.playwright.stop()
