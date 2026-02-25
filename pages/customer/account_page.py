from playwright.sync_api import expect
from pages.base_page import BasePage

class CustomerAccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = self.page.get_by_text("Welcome ")
        self.account_dropdown = self.page.locator("#accountSelect")
        self.account_number_label = self.page.get_by_text("Account Number : ")
        self.balance_label = self.page.get_by_text("Balance : ")
        self.currency_label = self.page.get_by_text("Currency : ")
        
        self.transactions_tab = self.page.get_by_role("button", name="Transactions")
        self.deposit_tab = self.page.get_by_role("button", name="Deposit")
        self.withdrawl_tab = self.page.get_by_role("button", name="Withdrawl") # Note: Typo exists in the original website

    def landing_customer_account_page(self):
        self.verify_header_with_logout()
        expect(self.welcome_message).to_be_visible()
        expect(self.account_dropdown).to_be_visible()
        expect(self.account_number_label).to_be_visible()
        expect(self.balance_label).to_be_visible()
        expect(self.currency_label).to_be_visible()
        expect(self.transactions_tab).to_be_visible()
        expect(self.deposit_tab).to_be_visible()
        expect(self.withdrawl_tab).to_be_visible()