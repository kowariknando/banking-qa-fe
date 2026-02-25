from pages.base_page import BasePage

class AccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.deposit_menu_button = "button[ng-click='deposit()']"
        self.withdraw_menu_button = "button[ng-click='withdrawl()']" # Using the exact typo from the web
        self.amount_input = "input[ng-model='amount']"
        self.submit_action_button = "button[type='submit']"
        self.success_message = "span[ng-show='message']"
        self.account_info_values = "strong.ng-binding"

    
    def go_to_deposit(self):
        self.click_element(self.deposit_menu_button)
        self.page.get_by_text("Amount to be Deposited").wait_for()
        
    def go_to_withdraw(self):
        self.click_element(self.withdraw_menu_button)
        self.page.get_by_text("Amount to be Withdrawn").wait_for()
        
    def enter_amount(self, amount: str):
        self.fill_text(self.amount_input, amount)
        
    def submit_transaction(self):
        self.click_element(self.submit_action_button)
        
    def get_transaction_message(self) -> str:
        return self.get_text(self.success_message)
        
    def get_balance(self) -> str:
        return self.page.locator(self.account_info_values).nth(1).inner_text()