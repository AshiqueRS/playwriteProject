
from playwright.sync_api import expect, sync_playwright
from config import *
from page_objects import *

def test_flow(playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()

     #Initializing pages
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    #Test Flow
    page.goto(BASE_URL)
    login_page.login(VALID_USER, VALID_PASS)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")

    inventory_page.add_item("sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    inventory_page.remove_item("sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_be_hidden()

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        test_flow(playwright)