class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = "id=username"
        self.password_field = "id=password"
        self.login_button = "id=login"

    async def login(self, username, password):
        await self.page.fill(self.username_field, username)
        await self.page.fill(self.password_field, password)
        await self.page.click(self.login_button)
