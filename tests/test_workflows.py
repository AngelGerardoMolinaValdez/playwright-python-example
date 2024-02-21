from playwright.sync_api import Page
import pytest
from keywords.login_keywords import LoginKeywords
from keywords.create_new_account_keywords import CreateNewAccountKeywords
from keywords.account_overview_keywords import AccountOverviewKeywords
from keywords.transfer_funds_keywords import TransferFundsKeywords

@pytest.fixture
def login(page: Page) -> None:
    """Fixture to log in to the application."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

def test_open_new_account_and_transfer_funds(login, page: Page) -> None:
    """Test opening a new account and transferring funds in Parabank."""
    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account("SAVINGS", "13344")

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds("100", "13344", "13344")

def test_open_account_and_view_overview(login, page: Page) -> None:
    """Test opening an account and viewing the account overview in Parabank."""
    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account("SAVINGS", "13344")

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview("13344")

def test_open_new_account_transfer_funds_and_view_overview(login, page: Page) -> None:
    """Test opening a new account, transferring funds, and viewing the account overview in Parabank."""
    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account("SAVINGS", "13344")

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds("100", "13344", "13344")

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview("13344")
