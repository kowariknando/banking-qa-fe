from playwright.sync_api import expect
from pages.base_page import BasePage

class AddCustomerPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        
        self.add_customer_tab = self.page.get_by_role("button", name="Add Customer").first
        
        self.first_name_label = self.page.get_by_text("First Name :")
        self.last_name_label = self.page.get_by_text("Last Name :")
        self.post_code_label = self.page.get_by_text("Post Code :")
        self.first_name_input = self.page.get_by_role("textbox", name="First Name")
        self.last_name_input = self.page.get_by_role("textbox", name="Last Name")
        self.post_code_input = self.page.get_by_role("textbox", name="Post Code")
        
        self.submit_button = self.page.get_by_role("form").get_by_role("button", name="Add Customer")

    def landing_add_customer_page(self):
        self.verify_header()
        expect(self.add_customer_tab).to_be_visible()
        expect(self.first_name_label).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_label).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.post_code_label).to_be_visible()
        expect(self.post_code_input).to_be_visible()
        expect(self.submit_button).to_be_visible()

    def add_new_customer(self, first_name: str, last_name: str, post_code: str) -> str:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.post_code_input.fill(post_code)
        
        dialog_message = []

        def handle_dialog(dialog):
            dialog_message.append(dialog.message)
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.submit_button.click()
        return dialog_message[0]