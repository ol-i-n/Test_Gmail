from steps.data_loader import *
from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, expect
from steps.email_login import *

# Load email credentials from a JSON file
gmail_password = credentials["password"]
gmail_username = credentials["username"]

# Testcase successful login
@scenario("./features/login_to_email.feature", "Verify login with valid email and password")
def test_valid_login():
    pass

@given("the user is on the email login page")
def open_login_page(page: Page):
    Login(page).open_login_page()

@when("the user provides the valid email")
def enter_email(page: Page):
    Login(page).enter_email(gmail_username)

@when("the user provides the valid password")
def enter_password(page: Page):
    Login(page).enter_password(gmail_password)

@then("the user should be logged in and see their mailbox")
def verify_login_successful(page: Page):
    expect(page.get_by_role("button", name="Compose")).to_be_visible()

