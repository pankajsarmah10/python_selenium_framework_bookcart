from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.action_methods import get_text_from_element
class HomePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.__lbl_user = (By.CSS_SELECTOR, "app-nav-bar>mat-toolbar .mdc-button__label:nth-child(4)>span")


    def get_user_logged_in_label_text(self):
        return get_text_from_element(self.driver, *self.__lbl_user)
