from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DynamicPage(BasePage):
    HELLO_WORLD_TEXT = (By.CSS_SELECTOR, "div#finish h4")
    LOADING_BAR_DISPLAY = (By.ID, "loading")
    START_BTN = (By.CSS_SELECTOR, "div#start button")
    NAV_ITEMS = (By.XPATH, "//div[@class='example']/ul/li")
    # gets all checkboxes/input tags in form
    CHECKBOXES = (By.XPATH, "//form[@id='checkboxes']/input")
    # *[3] points to 3rd child of ANY type
    # div[3] → 3rd div child only 
    FIRST_IMG = (By.XPATH, "//div[@class='example']/*[3]")
    FIRST_IMG_CAPTION = (By.XPATH, "//div[@class='example']/div[1]/div/h5")

    def click_start_btn(self):
        self.wait_for_clickable(self.START_BTN).click()
        self.wait_for_element(self.LOADING_BAR_DISPLAY)

    def get_hello_world(self):
        return self.wait_for_element(self.HELLO_WORLD_TEXT).text

    def refresh_and_wait(self):
        self.driver.refresh()
        self.wait_for_element(self.NAV_ITEMS)
        
    def get_nav_items_count(self):
        return len(self.wait_for_all(self.NAV_ITEMS))

    # is_selected checks if asked checkbox is checked or not nd returns a boolen
    def is_element_selected(self, index):
        checkboxes = self.wait_for_all(self.CHECKBOXES)
        return checkboxes[index].is_selected()

    def click_checkbox(self, index):
        checkboxes = self.wait_for_all(self.CHECKBOXES)
        checkboxes[index].click()

    def get_first_figure(self):
        return self.wait_for_element(self.FIRST_IMG)

    def get_first_figure_cap(self):
        self._close_ad_if_present()
        return self.wait_for_element(self.FIRST_IMG_CAPTION).text