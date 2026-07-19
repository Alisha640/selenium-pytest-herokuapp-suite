import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    config.option.htmlpath = "reports/report.html"
    config.option.self_contained_html = True