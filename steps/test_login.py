import json
from playwright.sync_api import Page
from behave import given, when, then
from pages.login_page import LoginPage


@given('el navegador se abre en la url del sistema')
def open_page_login(context):
    context.page.goto("https://parabank.parasoft.com/parabank/index.htm")
    # context.page.login_page = LoginPage(context.page)

@when('escribo el username y password')
def type_credentials(context):
    context.page.get_by_role("input", name="username").fill("john")
    context.page.get_by_role("input", name="password").fill("demo")
    context.page.locator('input[value="Log In"]').click()

# @then('debe verse el menu de opciones del usuario')
# def validate_login_session(context):
    # ...