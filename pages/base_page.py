from playwright.sync_api import Page
from pages.components.header import HeaderComponent

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        
        self.header = HeaderComponent(page)

    def navigate(self, url: str):
        self.page.goto(url)