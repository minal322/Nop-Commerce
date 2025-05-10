import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pytest
from pages.homepage import HomePage
from pages.register import RegisterPage
from pages.accountSuccess import  AccountSuccessPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def generate_random_email(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return f'patilminal{time_stamp}@gmail.com'

    def test_register_with_mandatory_valid_credentials(self):
        homepage_obj = HomePage(self.driver)
        homepage_obj.click_on_my_account_drop_menu()
        homepage_obj.click_on_register_drop_menu()

        register_obj = RegisterPage(self.driver)
        register_obj.enter_firstname("dimple")
        register_obj.enter_lastname("Kukreja")
        register_obj.enter_email_address(self.generate_random_email())
        register_obj.enter_telephone("9874561230")
        register_obj.enter_password("123456")

        register_obj.enter_confirm("123456")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        register_obj.select_agreement_checkbox_option()
        register_obj.click_on_continue_button()

        expected_text = "Your Account Has Been Created!"
        acc_success_obj = AccountSuccessPage(self.driver)
        assert acc_success_obj.retrieve_account_creation_message().__eq__(expected_text)



    def test_register_with_all_mandatory_valid_credentials(self):
        homepage_obj = HomePage(self.driver)
        homepage_obj.click_on_my_account_drop_menu()
        homepage_obj.click_on_register_drop_menu()

        register_obj = RegisterPage(self.driver)
        register_obj.enter_firstname("dimple")
        register_obj.enter_lastname("Kukreja")
        register_obj.enter_email_address(self.generate_random_email())
        register_obj.enter_telephone("9874561230")
        register_obj.enter_password("123456")
        register_obj.enter_confirm("123456")
        register_obj.select_agreement_checkbox_option()
        #optional fields
        register_obj.select_news_radio_button()
        register_obj.click_on_continue_button()

        expected_text = "Your Account Has Been Created!"
        acc_success_obj = AccountSuccessPage(self.driver)
        assert acc_success_obj.retrieve_account_creation_message().__eq__(expected_text)


    def test_register_with_already_registered_email(self):
        homepage_obj = HomePage(self.driver)
        homepage_obj.click_on_my_account_drop_menu()
        homepage_obj.click_on_register_drop_menu()

        register_obj = RegisterPage(self.driver)
        register_obj.enter_firstname("Minal")
        register_obj.enter_lastname("Patil")
        register_obj.enter_email_address("patilminal322@gmail.com")
        register_obj.enter_telephone("9874561230")
        register_obj.enter_password("123456")
        register_obj.enter_confirm("123456")
        register_obj.select_agreement_checkbox_option()
        register_obj.select_news_radio_button()
        register_obj.click_on_continue_button()

        expected_text = "Warning: E-Mail Address is already registered!"
        assert register_obj.retrieve_duplicate_warning_message().__eq__(expected_text)



    def test_register_without_entering_any_fields(self):
        homepage_obj = HomePage(self.driver)
        homepage_obj.click_on_my_account_drop_menu()
        homepage_obj.click_on_register_drop_menu()

        register_obj = RegisterPage(self.driver)
        register_obj.enter_firstname("")
        register_obj.enter_lastname("")
        register_obj.enter_email_address("")
        register_obj.enter_telephone("")
        register_obj.enter_password("")
        register_obj.enter_confirm("")
        register_obj.select_news_radio_button()
        register_obj.click_on_continue_button()

        expected_policy_message = "Warning: You must agree to the Privacy Policy!"
        assert register_obj.retrieve_privacy_policy_warning_message().__eq__(
            expected_policy_message)

        expected_firstname_warn_message = "First Name must be between 1 and 32 characters!"
        assert register_obj.retrieve_firstname_warning_message().__eq__(
            expected_firstname_warn_message)

        expected_lastname_warn_message = "Last Name must be between 1 and 32 characters!"
        assert register_obj.retrieve_lastname_warning_message().__eq__(
            expected_lastname_warn_message)

        expected_email_warn_message = "E-Mail Address does not appear to be valid!"
        assert register_obj.retrieve_email_warning_message().__eq__(
            expected_email_warn_message)

        expected_telephone_warn_message = "Telephone must be between 3 and 32 characters!"
        assert register_obj.retrieve_telephone_warning_message().__eq__(
            expected_telephone_warn_message)

        expected_password_warn_message = "Password must be between 4 and 20 characters!"
        assert register_obj.retrieve_password_warning_message().__eq__(
            expected_password_warn_message)
