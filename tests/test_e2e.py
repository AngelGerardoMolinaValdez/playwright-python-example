from playwright.sync_api import Page
from keywords.login_keywords import LoginKeywords

def test_open_new_account(page: Page) -> None:
    """Test opening a new account in Parabank."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()
