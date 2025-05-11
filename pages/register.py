from jinja2.lexer import ignore_if_empty
from selenium.webdriver.common.by import By
from pages.accountSuccess import AccountSuccessPage


class RegisterPage:
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
        self.driver.find_element(By.ID, self.firstname_field_id).click()
        self.driver.find_element(By.ID, self.firstname_field_id).clear()
        self.driver.find_element(By.ID, self.firstname_field_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_field_id).click()
        self.driver.find_element(By.ID, self.lastname_field_id).clear()
        self.driver.find_element(By.ID, self.lastname_field_id).send_keys(lastname)

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)
        
    def enter_confirm(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password)

    def select_agreement_checkbox_option(self):
        self.driver.find_element(By.NAME, self.agreement_option_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def select_news_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_option_xpath).click()

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
        return self.driver.find_element(By.XPATH, self.warning_message_duplicate_email_xpath).text

    def retrieve_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_firstname_warning_message(self):
        return  self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text

    def retrieve_lastname_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text

    def retrieve_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_warning_xpath).text

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




