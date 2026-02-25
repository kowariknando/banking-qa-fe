import pytest
from typing import Generator
from playwright.sync_api import Page
from pages.home_page import HomePage



@pytest.fixture
def home_page(page: Page) -> Generator[HomePage, None, None]:
    # ==========================================
    # 1. SETUP (setup before test ejecution)
    # ==========================================
    home = HomePage(page)
    home.navigate("#/login")
    
    home.landing_home_page()
    
    # ==========================================
    # 2. YIELD (test ejecution)
    # ==========================================
    
    yield home
    
    # ==========================================
    # 3. TEARDOWN (clean up after test ejecution)
    # ==========================================
    page.context.clear_cookies()
    page.evaluate("window.localStorage.clear()")
    page.evaluate("window.sessionStorage.clear()")