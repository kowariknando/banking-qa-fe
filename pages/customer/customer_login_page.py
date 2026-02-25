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

    def select_user_by_id(self, user_id: str):
        self.user_dropdown.select_option(value=user_id)

    def get_selected_user_text(self) -> str:
        return self.user_dropdown.evaluate("el => el.options[el.selectedIndex].text")