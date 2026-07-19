import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pages.login_page import LoginPage
from config import LOGIN_URL, LOGIN_USERNAME, LOGIN_PASSWORD

@pytest.mark.parametrize("username, password, expected", [
    (LOGIN_USERNAME, LOGIN_PASSWORD, "secure area"),
    (LOGIN_USERNAME, "wrongpassword", "invalid password"),
    ("wronguser", "wrongpassword", "invalid credentials")
])

def test_user_login(driver,username, password, expected):
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.hit_login()
    if expected == "secure area":
        assert "secure area" in login_page.get_flash_msg()
        # could have used wait_for_url_contains() of base page- but using base page methods directly in test files violates POM
        assert "secure" in login_page.driver.current_url
        login_page.hit_logout()
        assert "login" in login_page.driver.current_url 
        # was matching the  url to LOGIN_URL exactly but sometimes the url has a trailing slash so matching for "login" in the url is more robust
    elif expected == "invalid password":
        assert "password is invalid!" in login_page.get_flash_msg()
    else:
        assert "username is invalid!" in login_page.get_flash_msg()

    