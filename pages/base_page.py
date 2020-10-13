from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_sign_in_page(self):
        link = self.browser.find_element(*BasePageLocators.SIGN_IN_LINK)
        link.click()

    def should_be_sign_in_link(self):
        assert self.is_element_present(*BasePageLocators.SIGN_IN_LINK), "Sign in link is not presented"

    def open(self):
        self.browser.get(self.url)

    # checks for element on page for a specified period of time
    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # checks that the element does not appear on the page for a specified period of time
    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # checks that the element disappears within the specified period of time
    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
