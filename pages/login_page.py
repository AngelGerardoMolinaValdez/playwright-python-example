from playwright.async_api import Page

class LoginPage:
    """Class to interact with the login page of Parabank."""

    def __init__(self, page: Page):
        """Initialize the login page object"""
        self.page = page
        self.username: str = "input[name=\"username\"]"
        self.password_field: str = "input[name=\"password\"]"
        self.login_button: str = "input[value=\"Log In\"]"
    
    def open_login_page(self, url: str) -> None:
        self.page.goto(url)
        self.__login_page_should_be_open()

    def __login_page_should_be_open(self) -> bool:
        return self.page.locator(self.username).is_visible()

    def input_username(self, username: str) -> None:
        self.page.locator(self.username).fill(username)
    
    def input_password(self, password: str) -> None:
        self.page.locator(self.password_field).fill(password)
    
    def submit_credentials(self) -> None:
        self.page.locator(self.login_button).click()
        self.__login_should_be_successful()
    
    def __login_should_be_successful(self) -> bool:
        return self.page.locator('text=Account Services').is_visible()
