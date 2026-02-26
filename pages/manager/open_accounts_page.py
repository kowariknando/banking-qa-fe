from playwright.sync_api import expect
from pages.base_page import BasePage

class OpenAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.customer_dropdown = self.page.locator("#userSelect")
        self.currency_dropdown = self.page.locator("#currency")
        self.process_button = self.page.locator("button[type='submit']")

    def landing_open_account_page(self):
        self.header.verify_header()
        expect(self.customer_dropdown).to_be_visible()
        expect(self.currency_dropdown).to_be_visible()
        expect(self.process_button).to_be_visible()

    def process_new_account(self, customer_id: str, currency: str = "Dollar") -> str:
        self.customer_dropdown.select_option(value=customer_id)
        self.currency_dropdown.select_option(label=currency)
        
        alert_text = []
        self.page.on("dialog", lambda dialog: (alert_text.append(dialog.message), dialog.accept()))
        
        self.process_button.click()
        self.page.wait_for_timeout(500) 
        
        return alert_text[0] if alert_text else ""