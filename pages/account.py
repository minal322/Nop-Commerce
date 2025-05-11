from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_info_option_link_text = "Edit your account information"

    def display_status_of_edit_your_account_info_option(self):
        return self.element_displayed_status("edit_your_account_info_option_link_text",self.edit_your_account_info_option_link_text)