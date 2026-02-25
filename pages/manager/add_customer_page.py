from playwright.sync_api import expect
from pages.base_page import BasePage

class AddCustomerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.add_customer_tab = self.page.locator("button[ng-click='addCust()']")
        self.open_account_tab = self.page.locator("button[ng-click='openAccount()']")
        self.customers_tab = self.page.locator("button[ng-click='showCust()']")
        self.first_name_input = self.page.get_by_placeholder("First Name")
        self.last_name_input = self.page.get_by_placeholder("Last Name")
        self.post_code_input = self.page.get_by_placeholder("Post Code")
        self.submit_button = self.page.locator("button[type='submit']")

    def landing_add_customer_page(self):
        self.header.verify_header()
        expect(self.add_customer_tab).to_be_visible()
        expect(self.open_account_tab).to_be_visible()
        expect(self.customers_tab).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.post_code_input).to_be_visible()
        expect(self.submit_button).to_be_visible()

    def add_new_customer(self, first_name: str, last_name: str, post_code: str) -> str:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.post_code_input.fill(post_code)
        
        alert_text = []
        self.page.on("dialog", lambda dialog: (alert_text.append(dialog.message), dialog.accept()))
        
        self.submit_button.click()
        
        self.page.wait_for_timeout(500) 
        return alert_text[0] if alert_text else ""