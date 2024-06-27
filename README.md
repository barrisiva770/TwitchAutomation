# Twitch Automation Test

This project is a Selenium-based automation test for a mobile emulator using Python. The test navigates to Twitch, searches for "StarCraft II", scrolls down, selects a streamer, waits for the stream to load, and takes a screenshot of the streamer's page.

## Project Structure

.
├── pages
│ ├── base_page.py
│ ├── home_page.py
│ ├── search_results_page.py
│ └── streamer_page.py
├── tests
│ ├── test_twitch.py
├── utils
│ ├── driver.py
├── screenshots
│ └── streamer_page.png
├── requirements.txt
└── README.md


## Setup

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Ensure you have ChromeDriver installed and accessible in your PATH.

## Running the Test

1. Run the tests using pytest:
    ```sh
    python -m pytest --alluredir=allure-results tests/test_twitch.py
    ```

## Notes

- The test uses a mobile emulator for Google Chrome.
- It includes handling for potential pop-ups or modals that might appear before the video loads.
- Screenshots are saved.
