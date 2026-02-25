from playwright.sync_api import expect
from pages.base_page import BasePage

class CustomerLoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.user_dropdown = self.page.locator("#userSelect")
        self.submit_login_button = self.page.locator("button[type='submit']") 
        self.your_name_label = self.page.locator("label")

    def landing_customer_login_page(self):
        self.header.verify_header()
        expect(self.your_name_label).to_have_text("Your Name :")
        expect(self.user_dropdown).to_be_visible()

    def select_first_user(self):
        self.user_dropdown.select_option("1")

    def click_login_button(self):
        self.submit_login_button.click()