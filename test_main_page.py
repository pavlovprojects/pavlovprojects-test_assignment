import pytest
from .pages.main_page import MainPage
from .pages.my_account_page import MyAccountPage


@pytest.mark.test_assignment
class TestGoToAccountPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://automationpractice.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()

    def test_guest_can_go_to_my_account_page(self, browser):
        self.page.go_to_sign_in_page()
        self.my_account_page = MyAccountPage(browser, browser.current_url)
        self.my_account_page.should_be_create_account_page()

    def test_guest_should_see_sign_in_link(self, browser):
        self.page.should_be_sign_in_link()
