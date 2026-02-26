from playwright.sync_api import expect
from pages.base_page import BasePage

class WithdrawlPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.amount_input = self.page.get_by_placeholder("amount")
        self.withdraw_submit_button = self.page.get_by_role("button", name="Withdraw", exact=True)
        self.message_label = self.page.locator(".error")

    def landing_withdrawl_page(self):
        expect(self.amount_input).to_be_visible()
        expect(self.withdraw_submit_button).to_be_visible()

    def withdraw_amount(self, amount: str):
        self.amount_input.fill(amount)
        self.withdraw_submit_button.click()

    def get_transaction_message(self) -> str:
        expect(self.message_label).to_be_visible()
        return self.message_label.inner_text()