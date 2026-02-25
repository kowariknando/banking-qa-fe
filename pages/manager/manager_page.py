from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.manager.add_customer_page import AddCustomerPage

class ManagerPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        
        self.add_customer_tab = self.page.get_by_role("button", name="Add Customer")
        self.open_account_tab = self.page.get_by_role("button", name="Open Account")
        self.customers_tab = self.page.get_by_role("button", name="Customers")

    def landing_manager_page(self):
        self.verify_header()
        expect(self.add_customer_tab).to_be_visible()
        expect(self.open_account_tab).to_be_visible()
        expect(self.customers_tab).to_be_visible()

    def navigate_to_add_customer_page(self):
        self.add_customer_tab.click()
        return AddCustomerPage(self.page)

    def navigate_to_open_account_page(self):
        self.open_account_tab.click()

    def navigate_to_customers_page(self):
        self.customers_tab.click()