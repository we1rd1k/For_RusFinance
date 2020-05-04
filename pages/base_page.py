from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_displayed(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.is_displayed()
        except (NoSuchElementException):
            print("Element is not visible")
            return False
        return True

    def input(self, how, what, key):
        input = self.browser.find_element(how, what)
        input.send_keys(key)

    def button_click(self, how, what):
        button = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable((how, what))
)
        button.click()