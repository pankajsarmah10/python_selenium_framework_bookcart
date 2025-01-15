from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.action_methods import click_element,send_keys_to_element, get_text_from_element
class LoginPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.__txt_username = (By.CSS_SELECTOR, 'input[placeholder=Username]')
        self.__txt_password = (By.CSS_SELECTOR, 'input[placeholder=Password]')
        self.__btn_login = (By.XPATH, '//button//span[text()="Login"]')
        self.__login_error = (By.CSS_SELECTOR, "mat-error")

    def enter_username(self, username):
        send_keys_to_element(self.driver, *self.__txt_username, username)


    def enter_password(self, password):
        send_keys_to_element(self.driver, *self.__txt_password, password)

    def click_login(self):
        click_element(self.driver, *self.__btn_login)

    def get_login_error_message(self):
        return get_text_from_element(self.driver, *self.__login_error)