class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

class InventoryPage:
    def __init__(self,page):
        self.page = page
        self.cart_btn = page.locator(".shopping_cart_link")

    def add_item(self,item_id):
        self.page.locator(f"#add-to-cart-{item_id}").click()

    def remove_item(self, item_id):
        self.page.locator(f"#remove-{item_id}").click()
