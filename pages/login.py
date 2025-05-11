from pages.account import AccountPage
from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[contains(@class,'alert alert-danger alert-dismissible')]"

    def enter_email_address(self, email):
        self.Type(email,"email_field_id",self.email_field_id)

    def enter_password(self, password):
        self.Type(password,"password_field_id",self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.element_text_fetch("warning_message_xpath",self.warning_message_xpath)

    def do_login(self,email,password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_on_login_button()