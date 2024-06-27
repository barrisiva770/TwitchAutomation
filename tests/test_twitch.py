import pytest
import allure
from utils.driver import get_mobile_driver
from pages.home_page import HomePage
from pages.search_result_page import SearchResultsPage 
from pages.streamer_page import StreamerPage

@pytest.fixture(scope="module")
def driver():
    driver = get_mobile_driver()
    driver.get("https://m.twitch.tv/")
    yield driver
    driver.quit()

@allure.feature("Twitch Search and Stream")
@allure.story("Search for a game and select a streamer")
def test_search_and_select_streamer(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    streamer_page = StreamerPage(driver)

    with allure.step("Click on the search icon"):
        home_page.click_search_icon()

    with allure.step("Enter 'StarCraft II' in the search input"):
        search_results_page.enter_search_query("StarCraft II")
    
    with allure.step("Scroll down twice"):
        search_results_page.scroll_down()
    
    with allure.step("Select the streamer"):
        search_results_page.select_one_streamer()
    
    with allure.step("Wait for the streamer page to load"):
        streamer_page.handle_popup()
        streamer_page.wait_until_loaded()
    
    with allure.step("Take a screenshot"):
        driver.save_screenshot("streamer_page.png")
        allure.attach.file("streamer_page.png", attachment_type=allure.attachment_type.PNG)