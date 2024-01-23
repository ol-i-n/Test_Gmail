from playwright.sync_api import Page, expect
from pytest_bdd import scenario, given, when, then
from steps.data_loader import *
from steps.email_login import *
from steps.send_email import Send_email

# Load email credentials from a JSON file
gmail_password = credentials["password"]
gmail_username = credentials["username"]

@scenario("./features/send_email.feature", "Successfully sending an email")
def test_send_email():
    pass

@given("the user is logged into their Gmail account")
def login_to_email(page: Page):
    Login(page).login(gmail_password, gmail_username)

@when("the user clicks on the \"Compose\" button")
def new_email(page: Page):
    Send_email(page).new_email()

@when("the user fills in the \"To\" field with the recipient's email address")
def fill_recipient(page: Page):
    Send_email(page).fill_recipient()

@when("the user fills in the \"Subject\" field")
def fill_subject(page: Page):
    Send_email(page).fill_subject()

@when("the user writes the email body")
def fill_email_body(page: Page):
    Send_email(page).fill_email_body()

@when("the user clicks on the \"Send\" button")
def send_email(page: Page):
    Send_email(page).send_email()

@then("the user should see a confirmation that the email was sent")
def verify_email_sent_successfull(page: Page):
    expect(page.get_by_text("Message sent"))

