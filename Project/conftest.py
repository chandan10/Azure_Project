import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Optional, handles driver installation

# Test Setup
@pytest.fixture(autouse=True)
def driver():
    # Setup Chrome driver (you can use Firefox or another browser too)
    options = Options()
    options.add_argument('--headless')
    # options.headless = True  # Optional: run the browser in the background without UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://rahulshettyacademy.com/")
    driver.maximize_window()
    yield driver
    driver.quit()