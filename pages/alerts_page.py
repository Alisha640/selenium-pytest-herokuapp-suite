from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AlertsPage(BasePage):
    CLICK_FOR_JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    CLICK_FOR_JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    CLICK_FOR_JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT = (By.ID, "result")

    def result_message(self):
        return self.wait_for_element(self.RESULT_TEXT).text

    # same logic for all btns summed up together 
    def click_btn(self, text):
        return self.wait_for_clickable((By.XPATH, f"//button[text()='{text}']")).click()

    # see base_page to know how to store an alert nd js alerts return an object

    # following are the methods applied w js alerts:
    def accept_alert(self):
        self.wait_for_alert().accept()
        # for clicking 'ok'

    def dismiss_alert(self):
        self.wait_for_alert().dismiss()
        # for clicking 'cancel'
        
    def get_alert_prompt(self, prompt):
        self.wait_for_alert().send_keys(prompt)
    
