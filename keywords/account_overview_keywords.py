from playwright.sync_api import Page
from pages.account_overview_page import AccountOverviewPage

class AccountOverviewKeywords:
    """Class to interact with the account overview page of Parabank using keyword driven testing."""

    def __init__(self, page: Page):
        """Initialize the AccountOverviewKeywords object."""
        self.account_overview_page = AccountOverviewPage(page)

    def open_account_overview(self, account_id: str) -> None:
        """Open the account overview page using the provided account id."""
        self.account_overview_page.select_option()
        self.account_overview_page.open_overview_to_account(account_id)
