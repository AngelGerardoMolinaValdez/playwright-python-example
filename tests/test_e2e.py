from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_open_new_account(page: Page) -> None:
    """Test opening a new account in Parabank."""
    login = LoginPage(page)
    login.open_login_page("https://parabank.parasoft.com/parabank/index.htm")
    login.input_username("john")
    login.input_password("demo")
    login.submit_credentials()
