from playwright.sync_api import Page
from keywords.login_keywords import LoginKeywords
from keywords.create_new_account_keywords import CreateNewAccountKeywords
from keywords.account_overview_keywords import AccountOverviewKeywords
from keywords.transfer_funds_keywords import TransferFundsKeywords

def test_open_new_account(page: Page) -> None:
    """Test opening a new account in Parabank."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account("SAVINGS", "13344")

def test_account_overview(page: Page) -> None:
    """Test the account overview page in Parabank."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview("13344")

def test_transfer_funds(page: Page) -> None:
    """Test transferring funds in Parabank."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds("100", "13344", "13344")
