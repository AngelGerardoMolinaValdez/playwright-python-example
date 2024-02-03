from playwright.sync_api import Page
from pages.login_page import LoginPage

class LoginKeywords:
    """Class to interact with the login page of Parabank using keyword driven testing."""

    def __init__(self, page: Page):
        """Initialize the LoginKeywords object"""
        self.login_page = LoginPage(page)

    def login_in_to_the_application(self) -> None:
        """Login to the application using the provided username and password."""
        self.login_page.open_login_page("https://parabank.parasoft.com/parabank/index.htm")
        self.login_page.input_username("john")
        self.login_page.input_password("demo")
        self.login_page.submit_credentials()
