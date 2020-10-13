import pytest
from faker import Faker
from .pages.my_account_page import MyAccountPage
from .pages.account_creation_page import AccountCreationPage

@pytest.mark.test_assignment
class TestCreateNewAccount():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://automationpractice.com/index.php?controller=authentication&back=my-account/"
        self.my_account_page = MyAccountPage(browser, self.link)
        self.my_account_page.open()

    def test_guest_should_see_create_account_form_elements(self, browser):
        self.my_account_page.should_be_create_account_form_elements()

    def test_account_creation(self, browser):
        f = Faker()
        self.email = f.email()
        self.first_name = f.first_name()
        self.last_name = f.last_name()
        self.password = f.password()
        self.address = f.street_name()
        self.city = f.city()
        self.state = f.state()
        self.zip_code = f.postalcode()
        self.phone = f.msisdn()

        self.my_account_page.check_email_valid(self.email)
        self.my_account_page.create_new_account_email()
        self.account_creation_page = AccountCreationPage(browser, browser.current_url)
        self.account_creation_page.should_be_account_creation_page()
        self.account_creation_page.should_be_customer_firstname_valid(self.first_name)
        self.account_creation_page.should_be_customer_lastname_valid(self.last_name)
        self.account_creation_page.should_be_password_valid(self.password)
        self.account_creation_page.should_be_data_valid(self.address, self.city, self.state, self.zip_code, self.phone)
        self.account_creation_page.should_be_success_creation_account()
