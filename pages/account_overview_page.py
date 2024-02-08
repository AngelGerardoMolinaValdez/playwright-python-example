from playwright.sync_api import Page

class AccountOverviewPage:
    """Account Overview Page into the Parabank application."""

    def __init__(self, page: Page):
        """Initialize the account overview page object."""
        self.page = page
    
    def select_option(self) -> None:
        """Select in the menu the option to open the account overview."""
        self.page.locator('//a[contains(text(), "Accounts Overview")]').click()
        self.__account_overview_page_should_be_open()

    def __account_overview_page_should_be_open(self) -> bool:
        """Check if the account overview page was opened."""
        return self.page.locator('h1.title').is_visible()

    def open_overview_to_account(self, account_id: str) -> None:
        """Click on the account id to open the account overview."""
        self.page.locator(f'text={account_id}').click()
        self.__account_overview_page_should_be_open()
    
    def __account_overview_page_should_be_open(self) -> bool:
        """Check if the account overview page was opened."""
        return self.page.locator('td#accountId').is_visible()
    
