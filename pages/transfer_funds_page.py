from playwright.sync_api import Page

class TransferFundsPage:
    """Class to interact with the transfer funds page of Parabank using keyword driven testing."""

    def __init__(self, page: Page):
        """Initialize the TransferFundsPage object."""
        self.page = page

    def select_option(self) -> None:
        """Select the Transfer Funds option from the navigation menu."""
        self.page.click("//a[contains(text(), \"Transfer Funds\")]")
        self.__transfer_funds_page_should_be_open()
    
    def __transfer_funds_page_should_be_open(self) -> bool:
        """Check if the transfer funds page was opened."""
        return self.page.locator('h1.title').is_visible()

    def input_amount(self, amount: str) -> None:
        """Input the amount to transfer using the provided amount."""
        self.page.fill("#amount", amount)

    def select_from_account(self, account_id: str) -> None:
        """Select the account to transfer funds from using the provided account id."""
        self.page.select_option("#fromAccountId", value=account_id)

    def select_to_account(self, account_id: str) -> None:
        """Select the account to transfer funds to using the provided account id."""
        self.page.select_option("#toAccountId", value=account_id)

    def submit_transfer(self) -> None:
        """Submit the transfer of funds."""
        self.page.click("input[value=\"Transfer\"]")
        self.__transfer_should_be_completed()
    
    def __transfer_should_be_completed(self) -> bool:
        """Check if the transfer of funds was completed."""
        return self.page.locator('span#fromAccountId').is_visible()
