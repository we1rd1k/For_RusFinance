import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.inputs import URL
import time

#@pytest.mark.skip
def test_can_go_to_login_page(browser):
    page = MainPage(browser, URL.mainPage_url, 15)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


#@pytest.mark.skip
def test_successful_login(browser):
    login = LoginPage(browser, URL.loginPage_url)
    login.open()
    login.should_be_login_form()
    login.submit_correct_auth_form()
    login.should_be_mainPage_url(URL.mainPage_url)
    login.successful_login()

#@pytest.mark.skip
def test_login_with_wrong_pass(browser):
    login = LoginPage(browser, URL.loginPage_url)
    login.open()
    login.should_be_login_form()
    login.submit_incorrect_auth_form()
    login.wrong_email_pass()
