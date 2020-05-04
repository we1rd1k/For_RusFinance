from .base_page import BasePage
from .locators import LoginPageLocators
from .inputs import Inputs
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_displayed(*LoginPageLocators.EMAIL_FIELD), "Email field not able"
        assert self.is_element_displayed(*LoginPageLocators.PASS_FIELD), "Pass field not able"

    def submit_correct_auth_form(self):
        self.input(*LoginPageLocators.EMAIL_FIELD, Inputs.correct_login)
        self.input(*LoginPageLocators.PASS_FIELD, Inputs.correct_pass)
        self.button_click(*LoginPageLocators.LOGIN_BUTTON)


    '''def submit_correct_auth_form(self):
        try:
            self.input(*LoginPageLocators.EMAIL_FIELD, Inputs.correct_login)
            self.input(*LoginPageLocators.PASS_FIELD, Inputs.correct_pass)
            self.button_click(*LoginPageLocators.LOGIN_BUTTON)
        except (NoSuchElementException):
            return False
            print("Disable to submit form")
        return True'''


    '''def input_login(self):
        self.input(*LoginPageLocators.EMAIL_FIELD, Inputs.correct_login)

    def input_pass(self):
        self.input(*LoginPageLocators.PASS_FIELD, Inputs.correct_pass)'''



