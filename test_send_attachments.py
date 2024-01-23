from playwright.sync_api import Page, expect
from pytest_bdd import scenario, given, when, then
from steps.email_login import *
from steps.send_email import Send_email
from steps.data_loader import *
import time


@scenario("./features/send_email_with_attach.feature", "Successfully attaching files and sending an email")
def test_send_email_with_attachment():
    pass

@given("the user is logged in to their email account")
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

@when("the user upload the attachment")
def attachment_upload(page: Page):
    Send_email(page).attachment_upload('1.png')
    Send_email(page).attachment_upload('2.png')

@when("the user clicks on the \"Send\" button")
def send_email(page: Page):
    time.sleep(5)        # waiting for attachment to upload
    Send_email(page).send_email()

@then("the user should see a confirmation that the email was sent")
def verify_email_sent_successfull(page: Page):
    page.wait_for_selector("text=Message sent", state="visible")
    expect(page.locator("text=Message sent")).to_be_visible()
