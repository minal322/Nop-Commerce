from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pytest
from pages.homepage import HomePage
from pages.login import LoginPage
from pages.account import AccountPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @staticmethod
    def generate_random_email():
        time_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f'patilminal{time_stamp}@gmail.com'

    def test_login_with_valid_credentials(self):
        homepage_obj = HomePage(self.driver)
        login_obj = homepage_obj.navigate_to_login_page()
        account_obj = login_obj.do_login("patilminal322@gmail.com","Minal@2001")
        assert account_obj.display_status_of_edit_your_account_info_option()
    
    def test_login_with_invalid_username(self):
        homepage_obj = HomePage(self.driver)
        login_obj = homepage_obj.navigate_to_login_page()
        login_obj.do_login(TestLogin.generate_random_email(), "Minal@2001")
        #to verify login is not success and got alert message
        expected_warning_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_obj.retrieve_warning_message().__contains__(expected_warning_text)
    
    def test_login_with_invalid_password(self):
        homepage_obj = HomePage(self.driver)
        login_obj = homepage_obj.navigate_to_login_page()
        login_obj.do_login("patilminal322@gmail.com","Minal@20015623")
        expected_warning_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_obj.retrieve_warning_message().__contains__(expected_warning_text)
        
    def test_login_without_entering_credentials(self):
        homepage_obj = HomePage(self.driver)
        login_obj = homepage_obj.navigate_to_login_page()
        login_obj.do_login("", "")
        # to verify login is not success and got alert message
        expected_warning_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_obj.retrieve_warning_message().__contains__(expected_warning_text)

