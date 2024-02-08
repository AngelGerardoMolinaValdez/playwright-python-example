from playwright.sync_api import Page
from pages.create_new_account_page import CreateNewAccountPage

class CreateNewAccountKeywords:
    """Class to interact with the create new account page of Parabank using keyword driven testing."""

    def __init__(self, page: Page):
        """Initialize the CreateNewAccountKeywords object."""
        self.create_new_account_page = CreateNewAccountPage(page)

    def create_new_account(self, account_type: str, account_id: str) -> None:
        """Create a new account using the provided account type and account id."""
        self.create_new_account_page.select_option()
        self.create_new_account_page.select_account_type(account_type)
        self.create_new_account_page.select_existing_account(account_id)
        self.create_new_account_page.open_new_account()
