from playwright.sync_api import Page
from pages.transfer_funds_page import TransferFundsPage

class TransferFundsKeywords:
    """Class to interact with the transfer funds page of Parabank using keyword driven testing."""
    
    def __init__(self, page: Page):
        """Initialize the TransferFundsKeywords object."""
        self.transfer_funds_page = TransferFundsPage(page)

    def transfer_funds(self, amount: str, from_account_id: str, to_account_id: str) -> None:
        """Transfer funds using the provided amount, from account id, and to account id."""
        self.transfer_funds_page.select_option()
        self.transfer_funds_page.input_amount(amount)
        self.transfer_funds_page.select_from_account(from_account_id)
        self.transfer_funds_page.select_to_account(to_account_id)
        self.transfer_funds_page.submit_transfer()
