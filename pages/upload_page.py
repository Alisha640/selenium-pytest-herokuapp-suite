from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class UploadPage(BasePage):
    INPUT_FIELD = (By.XPATH, "//input[@type='file']")
    UPLOAD_BTN = (By.ID, "file-submit")
    UPLOADED_CONTENT= (By.ID, "content")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div.example h3")
    FILE_NAME_APPEAR = (By.ID, "uploaded-files")

    def file_uploader(self, file_path):
        self.wait_for_element(self.INPUT_FIELD).send_keys(file_path)

    def click_upload_btn(self):
        self.wait_for_clickable(self.UPLOAD_BTN).click()
        self.wait_for_element(self.UPLOADED_CONTENT)

    def get_success_msg(self):
        return self.wait_for_element(self.SUCCESS_MSG).text

    def get_uploaded_file_name(self):
        return self.wait_for_element(self.FILE_NAME_APPEAR).text