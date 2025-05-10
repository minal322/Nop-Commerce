from selenium.webdriver.common.by import By


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

    def select_news_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_option_xpath).click()

    def retrieve_duplicate_warning_message(self):
        self.driver.find_element(By.XPATH, self.warning_message_duplicate_email_xpath).click()

    def retrieve_privacy_policy_warning_message(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).click()

    def retrieve_firstname_warning_message(self):
        self.driver.find_element(By.XPATH, self.first_name_warning_xpath).click()

    def retrieve_lastname_warning_message(self):
        self.driver.find_element(By.XPATH, self.last_name_warning_xpath).click()

    def retrieve_email_warning_message(self):
        self.driver.find_element(By.XPATH, self.email_warning_xpath).click()

    def retrieve_telephone_warning_message(self):
        self.driver.find_element(By.XPATH, self.telephone_warning_xpath).click()

    def retrieve_password_warning_message(self):
        self.driver.find_element(By.XPATH, self.password_warning_xpath).click()