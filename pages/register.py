from pages.accountSuccess import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        self.driver = driver

    firstname_field_id = "input-firstname"
    lastname_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agreement_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_radio_option_xpath = "//input[@name='newsletter'][@value='1']"
    warning_message_duplicate_email_xpath = "//div[contains(@class,'alert alert-danger alert-dismissible')]"

    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath =  "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_firstname(self, firstname):
        self.Type(firstname,"firstname_field_id",self.firstname_field_id)

    def enter_lastname(self, lastname):
        self.Type(lastname, "lastname_field_id", self.lastname_field_id)

    def enter_email_address(self, email):
        self.Type(email,"email_field_id", self.email_field_id)

    def enter_telephone(self, telephone):
        self.Type(telephone,"telephone_field_id", self.telephone_field_id)

    def enter_password(self, password):
        self.Type(password,"password_field_id", self.password_field_id)

    def enter_confirm(self, confirm_password):
        self.Type(confirm_password, "confirm_password_field_id", self.confirm_password_field_id)

    def select_agreement_checkbox_option(self):
        self.element_click("agreement_option_name",self.agreement_option_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_news_radio_button(self):
        self.element_click("newsletter_radio_option_xpath",self.newsletter_radio_option_xpath)

    def register_an_account(self,firstname,lastname,email,telephone,password,confirm_password,yes_newsletter,yes_privacy):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email_address(email)
        self.enter_telephone(telephone)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.enter_password(password)
        self.enter_confirm(confirm_password)

        if yes_newsletter:
            self.select_news_radio_button()
        if yes_privacy.__eq__("select"):
         self.select_agreement_checkbox_option()

        return self.click_on_continue_button()

    def retrieve_duplicate_warning_message(self):
        return self.element_text_fetch("warning_message_duplicate_email_xpath",self.warning_message_duplicate_email_xpath)

    def retrieve_privacy_policy_warning_message(self):
        return self.element_text_fetch("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath)

    def retrieve_firstname_warning_message(self):
        return self.element_text_fetch("first_name_warning_xpath",self.first_name_warning_xpath)

    def retrieve_lastname_warning_message(self):
        return self.element_text_fetch("last_name_warning_xpath ",self.last_name_warning_xpath)

    def retrieve_email_warning_message(self):
        return self.element_text_fetch("email_warning_xpath",self.email_warning_xpath)

    def retrieve_telephone_warning_message(self):
        return self.element_text_fetch("telephone_warning_xpath",self.telephone_warning_xpath)

    def retrieve_password_warning_message(self):
        return self.element_text_fetch("password_warning_xpath", self.password_warning_xpath)

    def verify_all_warnings(self,expected_policy_message,expected_firstname_warn_message,expected_lastname_warn_message,
                            expected_email_warn_message,expected_telephone_warn_message,expected_password_warn_message):
        actual_policy_message = self.retrieve_privacy_policy_warning_message()
        actual_firstname_warn_message = self.retrieve_firstname_warning_message()
        actual_lastname_warn_message= self.retrieve_lastname_warning_message()
        actual_email_warn_message = self.retrieve_email_warning_message()
        actual_telephone_warn_message = self.retrieve_telephone_warning_message()
        actual_password_warn_message = self.retrieve_password_warning_message()

        status = False
        if expected_policy_message.__contains__(actual_policy_message):
            if expected_firstname_warn_message.__eq__(actual_firstname_warn_message):
                if expected_lastname_warn_message.__eq__(actual_lastname_warn_message):
                    if expected_email_warn_message.__eq__(actual_email_warn_message):
                        if expected_telephone_warn_message.__eq__(actual_telephone_warn_message):
                            if expected_password_warn_message.__eq__(actual_password_warn_message):
                                status = True

        return status




