from playwright.sync_api import expect
from pages.base_page import BasePage

class ActionCustomerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_customer_input = self.page.get_by_placeholder("Search Customer")
        self.customer_table_rows = self.page.locator("tbody tr")

    def landing_action_customer_page(self):
        self.header.verify_header()
        expect(self.search_customer_input).to_be_visible()

    def search_customer(self, name: str):
        self.search_customer_input.fill(name)

    def delete_customer(self, first_name: str):
        row = self.customer_table_rows.filter(has_text=first_name)
        
        delete_button = row.get_by_role("button", name="Delete")
        delete_button.click()

    def verify_customer_not_in_list(self, first_name: str):
        row = self.customer_table_rows.filter(has_text=first_name)
        expect(row).to_have_count(0)