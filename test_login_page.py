import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

#@pytest.mark.skip
def test_can_go_to_login_page(browser):
    link = "https://stepik.org/"
    page = MainPage(browser, link, 15)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time.sleep(5)

#@pytest.mark.skip
def test_successful_login(browser):
    link = "https://stepik.org/catalog?auth=login"
    login = LoginPage(browser, link)
    login.open()
    login.should_be_login_form()
    login.submit_correct_auth_form()
    login.should_be_mainPage_url()
    login.successful_login()

#@pytest.mark.skip
def test_login_with_wrong_pass(browser):
    link = "https://stepik.org/catalog?auth=login"
    login = LoginPage(browser, link)
    login.open()
    login.should_be_login_form()
    login.submit_incorrect_auth_form()
    login.wrong_email_pass()
