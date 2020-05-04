from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
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

    def successful_login(self):
        assert self.is_element_present(*MainPageLocators.PROFILE_NAME), "There is no profile name"

    def submit_incorrect_auth_form(self):
        self.input(*LoginPageLocators.EMAIL_FIELD, Inputs.correct_login)
        self.input(*LoginPageLocators.PASS_FIELD, Inputs.incorrect_pass)
        self.button_click(*LoginPageLocators.LOGIN_BUTTON)

    def wrong_email_pass(self):
        assert self.is_element_displayed(*LoginPageLocators.ERROR_MESSAGE), "No error message for incorrect email/pass"



