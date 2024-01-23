from steps.data_loader import *
from playwright.sync_api import sync_playwright
import pytest

# Load email credentials from a JSON file
gmail_password = credentials["password"]
gmail_username = credentials["username"]

# Choose a browser, open a new page and after the test is done, close the browser
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        context = playwright.firefox.launch(headless=False)  # or use 'chromium'
        page = context.new_page()
        yield page
        context.close()


# Call the login page and enter the email and password
class Login:
    def __init__(self, page):
        self.page = page
        self.login_page_URL = "https://mail.google.com/"

    def open_login_page(self):
        self.page.goto(self.login_page_URL)

    def enter_email(self, name):
        self.page.fill("input[name='identifier']", name)
        self.page.locator("div[id='identifierNext']").click()

    def enter_password(self, password):
        self.page.fill("input[name='Passwd']", password)
        self.page.locator("div[id='passwordNext']").click()

    def login(self,password, name):
        self.open_login_page()
        self.enter_email(name)
        self.enter_password(password)