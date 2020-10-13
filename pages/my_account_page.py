from .base_page import BasePage
from .locators import MyAccountPageLocators
from selenium.webdriver.common.keys import Keys


class MyAccountPage(BasePage):
    def should_be_create_account_page(self):
        self.should_be_my_account_url()
        self.should_be_create_account_form()

    def should_be_create_account_form_elements(self):
        self.should_be_email_create_fild()
        self.should_be_submit_create_button()

    def should_be_my_account_url(self):
        assert 'my-account' in self.browser.current_url, "Cant find word my-account in url"

    def should_be_create_account_form(self):
        assert self.is_element_present(*MyAccountPageLocators.CREATE_ACCOUNT_FORM), "Register form is not presented"

    def should_be_email_create_fild(self):
        assert self.is_element_present(*MyAccountPageLocators.EMAIL_CREATE_FILD), "Email create fild is not presented"

    def should_be_submit_create_button(self):
        assert self.is_element_present(
            *MyAccountPageLocators.SUBMIT_CREATE_BUTTON), "Submit create button is not presented"

    def check_email_valid(self, email):
        self.browser.find_element(*MyAccountPageLocators.EMAIL_CREATE_FILD).send_keys(email, Keys.TAB)
        assert self.is_element_present(*MyAccountPageLocators.EMAIL_VALID), "Email is not valid"

    def create_new_account_email(self):
        self.browser.find_element(*MyAccountPageLocators.SUBMIT_CREATE_BUTTON).click()
        assert self.is_disappeared(
            *MyAccountPageLocators.SUBMIT_CREATE_BUTTON), "Account creation page takes too long to load"
