from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK_DESKTOP = (By.XPATH, "//div[contains(@class, 'navbar__wrapper')]//div[contains (@class, 'navbar__links ')]/a[@id = 'ember33']")
    LOGIN_LINK_MOB = (By.XPATH, "//div[contains(@class, 'navbar__wrapper')]//div[@class = 'navbar__head ']/a[@id = 'ember17']")
    PROFILE_NAME = (By.XPATH, "//div[@id = 'ember569']//span[contains(@class, 'firstname')]")


class LoginPageLocators():
    EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'sign-form')]//input[@name = 'login']")
    PASS_FIELD = (By.XPATH, "//div[contains(@class, 'sign-form')]//input[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//div[@class = 'box']//form[contains(@id, 'login_form')]//button[contains(@class, 'button')]")
    ERROR_MESSAGE = (By.XPATH, "//form[@id = 'login_form']//ul[contains(@class, 'messages')]/li")
