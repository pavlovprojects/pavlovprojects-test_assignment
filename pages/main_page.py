from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_sign_in_link(self):
        assert self.is_element_present(*MainPageLocators.SIGN_IN_LINK), "Sign in link is not presented"

    def go_to_sign_in_page(self):
        self.browser.find_element(*MainPageLocators.SIGN_IN_LINK).click()
