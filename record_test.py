# from playwright.sync_api import Playwright, sync_playwright, expect
#
# def test_successful_login(playwright: Playwright) -> None :
#     # Browser Launch
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     #to create a new session in browser
#     context = browser.new_context()
#     #to open a new page
#     page = context.new_page()
#     #to go to the website
#     page.goto("https://www.saucedemo.com/")
#
#     #fill the field with credential for log in
#     page.fill("#user-name", "standard_user")
#     page.fill("#password", "secret_sauce")
#     page.click("#login-button")
#
#     # Verify Login is successful
#     expect
#
#
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     test_successful_login(playwright)