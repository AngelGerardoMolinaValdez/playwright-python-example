from playwright.sync_api import Page
from keywords.login_keywords import LoginKeywords
from keywords.create_new_account_keywords import CreateNewAccountKeywords

def test_open_new_account(page: Page) -> None:
    """Test opening a new account in Parabank."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account("SAVINGS", "13344")
