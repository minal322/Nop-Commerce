from selenium.webdriver.common.by import By
from pages.account import AccountPage

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[contains(@class,'alert alert-danger alert-dismissible')]"

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text

    def do_login(self,email,password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_on_login_button()