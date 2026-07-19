import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pages.dynamic_page import DynamicPage
from config import DYNAMIC_LOADING_URL, DISAPPEARING_EL_URL, CHECKBOX_URL, HOVER_URL

def test_dynamic_loading(driver):
    driver.get(DYNAMIC_LOADING_URL)
    dynamic_page = DynamicPage(driver)
    dynamic_page.click_start_btn()
    assert 'Hello World!' in dynamic_page.get_hello_world()

def test_disappearing_elements(driver):
    driver.get(DISAPPEARING_EL_URL)
    dynamic_page = DynamicPage(driver)
    assert dynamic_page.get_nav_items_count() > 0
    dynamic_page.refresh_and_wait()
    assert dynamic_page.get_nav_items_count() > 0

def test_checkboxes(driver):
    driver.get(CHECKBOX_URL)
    dynamic_page = DynamicPage(driver)
    # if expecting True → use assert method() if expecting False → use assert not method()
    assert not dynamic_page.is_element_selected(0)
    assert dynamic_page.is_element_selected(1)
    dynamic_page.click_checkbox(0)
    assert dynamic_page.is_element_selected(0)
    dynamic_page.click_checkbox(1)
    assert not dynamic_page.is_element_selected(1)

def test_hover_interaction(driver):
    driver.get(HOVER_URL)
    dynamic_page = DynamicPage(driver)
    actions = ActionChains(driver)
    # .perform() executes the action chain and before it we can queue up multiple actions like move_to_element, click, send_keys etc. and then execute them all at once using perform()
    actions.move_to_element(dynamic_page.get_first_figure()).perform() 
    assert "name: user1" in dynamic_page.get_first_figure_cap()