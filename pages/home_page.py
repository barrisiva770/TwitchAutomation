from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, 'a[aria-label="Search"]')

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def input_search_term(self, term):
        self.send_keys(*self.SEARCH_INPUT, term)
