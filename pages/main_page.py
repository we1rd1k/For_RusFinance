from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import ElementNotInteractableException

class MainPage(BasePage):
    def go_to_login_page(self):
        try:
            '''login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_DESKTOP)
            login_link.click()'''
            self.button_click(*MainPageLocators.LOGIN_LINK_DESKTOP)
        except (ElementNotInteractableException, Exception):
            print("Desktop Link is not clickable")
            '''login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_MOB)
            login_link.click()'''
            self.button_click(*MainPageLocators.LOGIN_LINK_MOB)



    def should_be_login_link(self):
        assert self.is_element_displayed(*MainPageLocators.LOGIN_LINK_DESKTOP), "Login link is not displayed"