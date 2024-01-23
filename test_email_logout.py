from steps.data_loader import *
from steps.email_login import *
from steps.email_logout import Logout
from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, expect

# Load email credentials from a JSON file
gmail_password = credentials["password"]
gmail_username = credentials["username"]

@scenario("./features/logout_from_email.feature", "Verify logout")
def test_valid_logout():
    pass

@given("the user is logged in to their email account")
def login_to_email(page: Page):
    Login(page).login(gmail_password, gmail_username)

@when("the user click on profile picture button")
def click_profile_picture(page: Page):
    Logout(page).click_profile_picture()
    
@when("the user click on Log out button")
def click_logout_button(page: Page):
    Logout(page).click_logout_button()

@then("the user should be logout and redirected to the email welcome page")
def ferify_logout_successful(page: Page):
    expect(page.get_by_role("link", name="Sign in")).to_be_visible()