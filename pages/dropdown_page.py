from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")
    OPTION_ONE = (By.XPATH, "//option[@value='1']")
    OPTION_TWO = (By.XPATH, "//option[@value='2']")

    def select_option_one(self):
        select = Select(self.wait_for_element(self.DROPDOWN))
        # the solution to select an option in native 'select' html dropdowns
        select.select_by_visible_text("Option 1")

    def get_option(self, value):
        return self.wait_for_element((By.XPATH, f"//option[@value='{value}']"))

    def select_option_two(self):
        select = Select(self.wait_for_element(self.DROPDOWN))
        select.select_by_visible_text("Option 2")