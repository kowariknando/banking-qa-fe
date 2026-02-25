from playwright.sync_api import expect
from pages.base_page import BasePage

class DepositPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.deposit_tab_button = self.page.get_by_role("button", name="Deposit").first
        self.amount_label = self.page.get_by_text("Amount to be Deposited :")
        self.amount_input = self.page.get_by_placeholder("amount")
        self.submit_deposit_button = self.page.get_by_role("form").get_by_role("button", name="Deposit")
        self.desposit_success_message = self.page.get_by_text("Deposit Successful")


    def landing_deposit_page(self):
        self.header.verify_header_with_logout()
        expect(self.deposit_tab_button).to_be_visible()
        expect(self.amount_label).to_be_visible()
        expect(self.amount_input).to_be_visible()
        expect(self.submit_deposit_button).to_be_visible()

    def make_deposit(self, amount: str):
        self.amount_input.fill(amount)
        self.submit_deposit_button.click()
        expect(self.desposit_success_message).to_be_visible()
