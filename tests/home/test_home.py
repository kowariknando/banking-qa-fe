import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.regression
def test_home_page_initial_load(home_page: HomePage):
    home_page.landing_home_page()