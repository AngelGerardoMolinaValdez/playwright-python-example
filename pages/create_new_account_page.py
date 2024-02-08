from playwright.sync_api import Page

class CreateNewAccountPage:
    """Create New Account Page into the Parabank application."""

    def __init__(self, page: Page):
        """Initialize the create new account page object."""
        self.page = page
        self.account_type: str = "select#type"
        self.initial_deposit: str = "select#fromAccountId"
        self.open_new_account_button: str = "input[value=\"Open New Account\"]"
    
    def select_option(self) -> None:
        """Select in the menu the option to create a new account."""
        self.page.locator('//a[contains(text(), "Open New Account")]').click()
        self.__create_new_account_page_should_be_open()
    
    def __create_new_account_page_should_be_open(self) -> bool:
        """Check if the create new account page was opened."""
        return self.page.locator('h1.title').is_visible()

    def select_account_type(self, account_type: str) -> None:
        """Select the account type from the dropdown."""
        self.page.locator(self.account_type).select_option(account_type)
    
    def select_existing_account(self, account_id: str) -> None:
        """Select the existing account from the dropdown."""
        self.page.locator(self.initial_deposit).select_option(account_id)
    
    def open_new_account(self) -> None:
        """Click on the Open New Account button."""
        self.page.locator(self.open_new_account_button).click()
        self.__new_account_should_be_opened()
    
    def __new_account_should_be_opened(self) -> bool:
        """Check if the new account was opened."""
        return self.page.locator('text=Account Opened!').is_visible()
