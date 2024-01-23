from steps.data_loader import *
from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, expect
from steps.email_login import *

# Load email credentials from a JSON file
gmail_password = credentials["password"]
gmail_username = credentials["username"]


# Testcase invalid login with invalid username - negative test
@scenario("./features/login_to_email_inv_name.feature", "Unsuccessful login with invalid username")
def test_invalid_username_login():
    pass

@given("the user is on the email login page")
def open_login_page(page: Page):
    Login(page).open_login_page()

@when("the user provides the invalid email")
def enter_invalid_email(page: Page):
    Login(page).enter_email("invalid@example.com")

@then("the user should see an error message indicating invalid username")
def verify_invalid_username_error(page: Page):
    expect(page.locator("input[name='Passwd']")).to_be_visible()


# Testcase invalid login with invalid password - negative test
@scenario("./features/login_to_email_inv_pswrd.feature", "Unsuccessful login with invalid password")
def test_invalid_password_login():
    pass

@given("the user is on the email login page")
def open_login_page(page: Page):
    Login(page).open_login_page()

@when("the user provides the valid email")
def enter_email(page: Page):
    Login(page).enter_email(gmail_username)

@when("the user provides the invalid password")
def enter_invalid_password(page: Page):
    Login(page).enter_password("wrongpassword")
    
@then("the user should see an error message indicating incorrect password")
def verify_incorrect_password_error(page: Page):
    expect(page.get_by_role("button", name="Compose")).to_be_visible()
