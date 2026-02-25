import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.manager import add_customer_page
from pages.manager.manager_page import ManagerPage
from pages.manager.add_customer_page import AddCustomerPage
from utils.data_generator import generate_random_string, generate_random_postcode

def navigate_to_bank_manager_page(page: Page, home_page: HomePage) -> ManagerPage:
    home_page.click_bank_manager_login()
    manager_page = ManagerPage(page)
    manager_page.landing_manager_page() 
    return manager_page

def navigate_to_add_customer_page(page: Page, home_page: HomePage) -> AddCustomerPage:
    manager_page = navigate_to_bank_manager_page(page, home_page)
    
    manager_page.navigate_to_add_customer_page()
    add_customer_page = AddCustomerPage(page)
    add_customer_page.landing_add_customer_page()
    return add_customer_page

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.manager
def test_manager_page_initial_load(page: Page, home_page: HomePage):
    navigate_to_bank_manager_page(page, home_page)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.manager
def test_add_customer_page_initial_load(page: Page, home_page: HomePage):
    navigate_to_add_customer_page(page, home_page)

@pytest.mark.regression
@pytest.mark.manager
def test_add_new_customer_successfully(page: Page, home_page: HomePage):    
    add_customer_page = navigate_to_add_customer_page(page, home_page)
    

    random_first_name = generate_random_string(5).capitalize()
    random_last_name = generate_random_string(7).capitalize()
    random_postcode = generate_random_postcode()
    
    alert_text = add_customer_page.add_new_customer(
        random_first_name, 
        random_last_name, 
        random_postcode
    )
    
    assert "Customer added successfully" in alert_text, f"The text in the pop up alert was: {alert_text}"