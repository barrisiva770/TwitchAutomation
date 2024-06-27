from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_mobile_driver():
    mobile_emulation = {
        "deviceName": "Pixel 2"
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-popup-blocking")

    service = Service("external_files/drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
