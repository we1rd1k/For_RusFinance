from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK_DESKTOP = (By.XPATH, "//div[contains(@class, 'navbar__wrapper')]//div[contains (@class, 'navbar__links ')]/a[@id = 'ember33']")
    LOGIN_LINK_MOB = (By.XPATH, "//div[contains(@class, 'navbar__wrapper')]//div[@class = 'navbar__head ']/a[@id = 'ember17']")


class LoginPageLocators():
    EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'sign-form')]//input[@name = 'login']")
    PASS_FIELD = (By.XPATH, "//div[contains(@class, 'sign-form')]//input[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@id, 'login_form')]//button[contains(@class, 'button')]")
