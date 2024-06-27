from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class StreamerPage(BasePage):
    POPUP_CLOSE = (By.CSS_SELECTOR, 'button[data-a-target="modal-close-button"]')
    VIDEO_PLAYER = (By.CSS_SELECTOR, 'h2[title="StarCraft II - Stream 2"]')
    def handle_popup(self):
        try:
            self.click(*self.POPUP_CLOSE)
        except:
            pass  # If the pop-up is not present, just continue

    def wait_until_loaded(self):
        self.wait_until_visible(*self.VIDEO_PLAYER)

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)
