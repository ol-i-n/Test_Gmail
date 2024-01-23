from steps.email_login import *

class Logout:
    def __init__(self, page):
        self.page = page

    def click_profile_picture(self):
        self.page.get_by_label(
            "Google Account: O K \n(oliver.kost23@gmail.com)"
        ).click()

    def click_logout_button(self):
        self.page.frame_locator('iframe[name="account"]').get_by_role(
            "link", name="Sign out"
        ).click()

    def logout(self):
        self.click_profile_picture()
        self.click_logout_button()