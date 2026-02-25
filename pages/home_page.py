from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.main_heading = self.page.locator(".mainHeading")
        self.customer_login_button = self.page.locator("button[ng-click='customer()']")
        self.bank_manager_login_button = self.page.locator("button[ng-click='manager()']")

    def landing_home_page(self):
        self.verify_header()
        expect(self.customer_login_button).to_be_visible()
        expect(self.bank_manager_login_button).to_be_visible()
    
    def click_customer_login(self):
        self.customer_login_button.click()

    def click_bank_manager_login(self):
        self.bank_manager_login_button.click()