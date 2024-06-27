from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Search..."]')
    ONE_STREAMER = (By.XPATH, '//p[@title="starcraft ii - stream 2"]')

    def scroll_down(self):
        for _ in range(2):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")

    def enter_search_query(self, query):
        self.send_keys(*self.SEARCH_INPUT, query)

    def select_one_streamer(self):
        self.click(*self.ONE_STREAMER)
