from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.send_keys(text)

    def wait_until_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_until_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_for_all_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))
