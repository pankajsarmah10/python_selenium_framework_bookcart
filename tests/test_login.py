import os

from pages.login_page import LoginPage
from pages.home_page import HomePage
from dotenv import load_dotenv
from utils.custom_assertions import CustomAssertions
import pytest

load_dotenv()


@pytest.mark.smoke
def test_login_valid(driver):
    login_page = LoginPage(driver)
    login_page.open_url(os.getenv('URL')+os.getenv('LOGIN_PAGE'))
    login_page.enter_username(os.getenv('USER_EMAIL'))
    login_page.enter_password(os.getenv('USER_PASSWORD'))
    login_page.click_login()
    home_page = HomePage(driver)
    user_logged_in_text = home_page.get_user_logged_in_label_text()
    CustomAssertions.assert_equal(user_logged_in_text, os.getenv('USER_EMAIL'))


@pytest.mark.regression
def test_login_invalid(driver):
    login_page = LoginPage(driver)
    login_page.open_url(os.getenv('URL')+os.getenv('LOGIN_PAGE'))
    login_page.enter_username(os.getenv('USER_EMAIL'))
    login_page.enter_password(os.getenv('USER_PASSWORD') + 'invalid')
    login_page.click_login()
    login_error_message = login_page.get_login_error_message()
    CustomAssertions.assert_equal(login_error_message, "Username or Password is incorrect.")

