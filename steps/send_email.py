from steps.email_login import *
from playwright.sync_api import expect
from steps.data_loader import *
import os

recipient = email_details["recipient"]
subject = email_details["subject"]
body = email_details["body"]

class Send_email:
    def __init__(self, page):
        self.page = page

    def new_email(self):
        self.page.get_by_role("button", name="Compose").click()

    def fill_recipient(self):
        self.page.get_by_role("combobox").click()
        self.page.get_by_role("combobox").fill(recipient)
        self.page.get_by_role("option", name=recipient).click()

    def fill_subject(self):   
        self.page.fill("input[name='subjectbox']", subject)

    def fill_email_body(self):
        self.page.fill("div[aria-label='Message Body']", body)

    def send_email(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.locator("div[aria-label='Send ‪(Ctrl-Enter)‬']").click()


    def attachment_upload(self, filename):
        base_dir = "D:\\Programovanie\\Indra avitech\\tests\\data\\attachment"
        file_path = os.path.join(base_dir, filename)
        
        # Wait for the file chooser and click the attach button
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_label("Attach files").click()
        file_chooser = fc_info.value
        
        # Set the file to be uploaded
        file_chooser.set_files(file_path)
        