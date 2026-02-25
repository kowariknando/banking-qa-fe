from playwright.sync_api import Page, expect

class HeaderComponent:

    def __init__(self, page: Page):
        self.page = page
        self.header_title = self.page.get_by_text("XYZ Bank")
        self.home_button = self.page.get_by_role("button", name="Home")
        self.logout_button = self.page.get_by_role("button", name="Logout")
        
    def verify_header(self):
        expect(self.header_title).to_be_visible()
        expect(self.home_button).to_be_visible()

    def verify_header_with_logout(self):
        self.verify_header()
        expect(self.logout_button).to_be_visible()

    def click_home(self):
        self.home_button.click()

    def click_logout(self):
        self.logout_button.click()