from playwright.sync_api import Playwright, sync_playwright, expect

def test_successful_login(playwright: Playwright) -> None :
    # Browser Launch
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    #to create a new session in browser
    context = browser.new_context()
    #to open a new page
    page = context.new_page()

    # 1. Login
    print("\n-- 1. Login Test--")
    #to go to the website
    page.goto("https://www.saucedemo.com/")
    #fill the field with credential for log in
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    # Verify Login is successful 1
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    # Verify Login is successful 2
    expect(page.locator("#shopping_cart_container")).to_be_visible()
    print("✅ Login Test Passed")

    # 2. Add to cart Test
    print("\n-- 2. Add to Cart Test--")
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")
    print("Item Added to cart")

    #3. Remove From Cart
    print("\n-- 3. Remove From the Cart Test--")
    page.locator("#remove-sauce-labs-backpack").click()
    expect(cart_badge).to_be_hidden()
    print("Item Remove from the cart")

    #4 Cart Checkout
    print("\n-- 4. Cart Checkout Test")
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".cart_item")).to_have_count(1)
    print("Cart Verification Successful")

    #5 Search/Filter
    print("\n-- 5. Search/Filter Test")
    page.goto("https://www.saucedemo.com/inventory.html")
    page.locator(".product_sort_container").select_option("za")
    first_item = page.locator(".inventory_item_name").first
    expect(first_item).to_have_text("Test.allTheThings() T-Shirt (Red)")
    print("Filter (Z-A) works correctly ")






    browser.close()


with sync_playwright() as playwright:
    test_successful_login(playwright)