from playwright.sync_api import Page, expect

class BasePage:

    def __init__(self, page: Page):
        self.page = page

        self.header_title = self.page.get_by_text("XYZ Bank")
        self.header_full_bar = self.page.get_by_text("Home XYZ Bank Logout")
        self.home_button = self.page.get_by_role("button", name="Home")
        self.logout_button = self.page.get_by_role("button", name="Logout")

    def navigate(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        self.page.locator(selector).click()

    def fill_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)
        
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def wait_for_element(self, selector: str):
        self.page.locator(selector).wait_for(state="visible")

    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def verify_header(self):
        expect(self.header_title).to_be_visible()
        expect(self.header_full_bar).to_be_visible()
        expect(self.home_button).to_be_visible()

    def go_home_from_header(self):
        self.home_button.click()

    def verify_header_with_logout(self):
        self.verify_header()
        expect(self.logout_button).to_be_visible()