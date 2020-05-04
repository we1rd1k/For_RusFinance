from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

def test_can_go_to_login_page(browser):
    link = "https://stepik.org/"
    page = MainPage(browser, link, 15)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    time.sleep(5)

def test_successful_login(browser):
    link = "https://stepik.org/catalog?auth=login"
    page = MainPage(browser, link)
    page.open()
    login = LoginPage(browser, link)
    login.should_be_login_form()
    login.submit_correct_auth_form()
    time.sleep(20)
