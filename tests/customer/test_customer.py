import pytest
from playwright.sync_api import Page
from pages.customer.customer_login_page import CustomerLoginPage
from pages.customer.account_page import CustomerAccountPage
from pages.home_page import HomePage


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
    customer_login_page.click_login_button()

    account_page = CustomerAccountPage(page)
    account_page.landing_customer_account_page()

@pytest.mark.regression
@pytest.mark.customer
def test_from_customer_page_go_back_to_home_page(page: Page, home_page: HomePage):
    customer_login_page = navigate_to_customer_login(page, home_page)
    
    customer_login_page.go_home_from_header()
    
    home_page.landing_home_page()

@pytest.mark.regression
@pytest.mark.customer
def test_create_new_user_login_with_new_user(page: Page) -> None:
    pass