import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pages.dropdown_page import DropdownPage
from pages.alerts_page import AlertsPage
from pages.windows_page import WindowsPage
from pages.upload_page import UploadPage
from config import DROPDOWN_URL, JS_ALERT_URL, WINDOWS_URL, FILE_UPLOAD_URL

def test_dropdown(driver):
    driver.get(DROPDOWN_URL)
    dropdown_page = DropdownPage(driver)
    dropdown_page.select_option_one()
    # get_attribute() checks for an attr in el, that dynamically appear on some action
    assert dropdown_page.get_option('1').get_attribute("selected")
    dropdown_page.select_option_two()
    assert dropdown_page.get_option('2').get_attribute("selected")

def test_javascript_alerts(driver):
    driver.get(JS_ALERT_URL)
    alerts_page = AlertsPage(driver)
    alerts_page.click_btn("Click for JS Alert")
    alerts_page.accept_alert()
    assert alerts_page.result_message() == "You successfully clicked an alert"
    alerts_page.click_btn("Click for JS Confirm")
    alerts_page.dismiss_alert()
    assert alerts_page.result_message() == "You clicked: Cancel"
    alerts_page.click_btn("Click for JS Confirm")
    alerts_page.accept_alert()
    assert alerts_page.result_message() == "You clicked: Ok"
    alerts_page.click_btn("Click for JS Prompt")
    alerts_page.get_alert_prompt("Alisha")
    alerts_page.accept_alert()
    assert "Alisha" in alerts_page.result_message()

def test_multiple_windows(driver):
    driver.get(WINDOWS_URL)
    windows_page = WindowsPage(driver)
    # selenium gives unique id to each tab
    # current_window_handle is the id for main window/tab1 - storing it for reference to return
    main_window = driver.current_window_handle
    windows_page.click_link()
    # switched to tab2
    windows_page.switch_to_new_window(main_window)
    # now assertions will work as focus of selenium shifted to tab2
    assert "New Window" in windows_page.page_heading()
    # driver.close() closes the current tab
    driver.close()
    # switching back to tab1 via reference id
    driver.switch_to.window(main_window)
    assert windows_page.get_main_content()

def test_file_upload(driver):
    driver.get(FILE_UPLOAD_URL)
    upload_page = UploadPage(driver)
    # programmatically creating a file nd writing in it
    file_name = "test_file.txt"
    with open(file_name, "w") as file:
        file.write("selenium automation test")
    # os.path.abspath(filename) converts relative to absolute path which is needed by browser
    path_of_file = os.path.abspath(file_name)
    try:
        # most asked QA question; "how do you handle file upload in Selenium without interacting with the OS dialog?" nd the ans is; "To upload a file without opening the browse dialog find input[type='file'] and send_keys(file_path) directly to it"
        # Inshort, input[type='file'] is the key locator for file uploads
        upload_page.file_uploader(path_of_file)
        # send_keys(absolute_path) bypasses the browse dialog entirely
        upload_page.click_upload_btn()
        assert "File Uploaded!" in upload_page.get_success_msg()
        assert upload_page.get_uploaded_file_name() == file_name
    except:
        driver.save_screenshot("file_upload_failure.png")
        raise
