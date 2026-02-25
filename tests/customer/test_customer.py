import pytest
import re
from playwright.sync_api import Page
from pages.customer.customer_login_page import CustomerLoginPage
from pages.customer.account_page import CustomerAccountPage
from pages.home_page import HomePage
from pages.manager.add_customer_page import AddCustomerPage
from pages.manager.manager_page import ManagerPage
from utils.data_generator import generate_random_postcode, generate_random_string

def navigate_to_customer_login(page: Page, home_page: HomePage) -> CustomerLoginPage:
    home_page.click_customer_login()
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.landing_customer_login_page()
    return customer_login_page

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.customer
def test_customer_page_initial_load(page: Page, home_page: HomePage):
    navigate_to_customer_login(page, home_page)

@pytest.mark.regression
@pytest.mark.customer
def test_login_with_existing_user(page: Page, home_page: HomePage):
    customer_login_page = navigate_to_customer_login(page, home_page)

    customer_login_page.select_first_user()
    
    user_name = customer_login_page.get_selected_user_text()
    
    customer_login_page.click_login_button()

    account_page = CustomerAccountPage(page)
    account_page.landing_customer_account_page(user_name)

@pytest.mark.regression
@pytest.mark.customer
def test_from_customer_page_go_back_to_home_page(page: Page, home_page: HomePage):
    customer_login_page = navigate_to_customer_login(page, home_page)
    customer_login_page.header.click_home()
    home_page.landing_home_page()

@pytest.mark.regression
@pytest.mark.customer
def test_create_new_user_login_with_new_user(page: Page, home_page: HomePage):
    home_page.click_bank_manager_login()
    manager_page = ManagerPage(page)
    manager_page.landing_manager_page()

    manager_page.navigate_to_add_customer_page()
    add_customer_page = AddCustomerPage(page)
    
    add_customer_page.landing_add_customer_page()

    first_name = generate_random_string(5).capitalize()
    last_name = generate_random_string(7).capitalize()
    postcode = generate_random_postcode()

    alert_text = add_customer_page.add_new_customer(first_name, last_name, postcode)

    match = re.search(r'\d+', alert_text)
    assert match is not None, "Could not find the Customer ID in the alert text!"
    customer_id = match.group()

    add_customer_page.header.click_home()
    home_page.landing_home_page()

    home_page.click_customer_login()
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.landing_customer_login_page()

    customer_login_page.select_user_by_id(customer_id)

    displayed_name = customer_login_page.get_selected_user_text()
    expected_full_name = f"{first_name} {last_name}"

    assert displayed_name == expected_full_name, f"Expected {expected_full_name} in dropdown, but found {displayed_name}"

    customer_login_page.click_login_button()
    account_page = CustomerAccountPage(page)
    
    account_page.landing_welcome_customer_account_page(displayed_name)