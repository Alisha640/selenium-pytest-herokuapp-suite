from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait (driver, 30)

    def _close_ad_if_present(self):
        try:
            self.driver.switch_to.frame("aswift_1")
            self.driver.switch_to.frame("ad_iframe")
            close_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "dismiss-button")))
            close_btn.click()
        except:
            pass 
        finally:
            self.driver.switch_to.default_content()

    def wait_for_element(self, locator):
        # element exists in DOM nd is VISIBLE
        # use it when element appears after an action (loading complete, form submitted)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def wait_for_presence(self, locator):
        # element exists in DOM but may be HIDDEN (display:none or opacity:0)
        # use it when element is always in DOM but hidden until triggered
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    # presence_of: finds el right away (hidden state)
    # visibility_of: waits until loading finishes (visible state)

    def wait_for_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_for_all(self, locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))
        
    def wait_for_given_text_in_element(self, locator, giventext):
        self.wait.until(EC.text_to_be_present_in_element(locator, giventext))
        return self.driver.find_element(*locator).text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_element_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except:
            return False

    def wait_for_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert

    
