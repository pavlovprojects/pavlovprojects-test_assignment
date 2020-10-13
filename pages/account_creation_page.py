from .base_page import BasePage
from .locators import AccountCreationPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class AccountCreationPage(BasePage):
    def should_be_account_creation_page(self):
        self.should_be_account_creation_url()
        self.should_be_account_creation_form()

    def should_be_account_creation_url(self):
        assert 'account-creation' in self.browser.current_url, "Cant find word account-creation in url"

    def should_be_account_creation_form(self):
        assert self.is_element_present(
            *AccountCreationPageLocators.ACCOUNT_CREATION_FORM), "Account creation form is not presented"

    def should_be_customer_firstname_valid(self, first_name):
        self.browser.find_element(*AccountCreationPageLocators.CUSTOMER_FIRSTNAME).send_keys(first_name, Keys.TAB)
        # self.browser.find_element(*AccountCreationPageLocators.ACCOUNT_CREATION_FORM).click()
        assert self.is_element_present(*AccountCreationPageLocators.FIRSTNAME_VALID), "First name is not valid"

    def should_be_customer_lastname_valid(self, last_name):
        self.browser.find_element(*AccountCreationPageLocators.CUSTOMER_LASTNAME).send_keys(last_name, Keys.TAB)
        # self.browser.find_element(*AccountCreationPageLocators.ACCOUNT_CREATION_FORM).click()
        assert self.is_element_present(*AccountCreationPageLocators.LASTNAME_VALID), "Last name is not valid"

    def should_be_password_valid(self, password):
        self.browser.find_element(*AccountCreationPageLocators.PASSWORD).send_keys(password, Keys.TAB)
        # self.browser.find_element(*AccountCreationPageLocators.ACCOUNT_CREATION_FORM).click()
        assert self.is_element_present(*AccountCreationPageLocators.PASSWORD_VALID), "Password is not valid"

    def should_be_data_valid(self, address, city, state, zip_code, phone):
        self.browser.find_element(*AccountCreationPageLocators.ADDRESS).send_keys(address)
        self.browser.find_element(*AccountCreationPageLocators.CITY).send_keys(city)
        self.select = Select(self.browser.find_element(*AccountCreationPageLocators.DROPDOWN_STATE))
        self.select.select_by_visible_text(state)
        self.browser.find_element(*AccountCreationPageLocators.ZIP_CODE).send_keys(zip_code)
        self.browser.find_element(*AccountCreationPageLocators.PHONE).send_keys(phone)
        self.browser.find_element(*AccountCreationPageLocators.ACCOUNT_CREATION_FORM).click()

    def should_be_success_creation_account(self):
        self.browser.find_element(*AccountCreationPageLocators.SUBMIT_ACCOUNT).click()
        self.should_not_be_danger_message()
        self.should_be_success_account_creation_message()

    def should_not_be_danger_message(self):
        assert self.is_not_element_present(
            *AccountCreationPageLocators.ALERT_DANGER), "Displayed alert with validation errors"

    def should_be_success_account_creation_message(self):
        assert "Welcome to your account" in self.browser.find_element(
            *AccountCreationPageLocators.SUCCESS_MESSAGE).text, "Success account creation message is not presented"
