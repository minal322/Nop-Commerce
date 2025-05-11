from datetime import datetime
from pages.homepage import HomePage
from test_cases.BaseTest import BaseTest

class TestRegister(BaseTest):

    def test_register_with_mandatory_valid_credentials(self):
        homepage_obj = HomePage(self.driver)
        register_obj= homepage_obj.navigate_to_register_page()
        acc_success_obj = register_obj.register_an_account("dimple","Kukreja",self.generate_random_email(),
                                                           "9874561230","123456","123456",False,"select")
        expected_text = "Your Account Has Been Created!"
        assert acc_success_obj.retrieve_account_creation_message().__eq__(expected_text)

    def test_register_with_all_mandatory_valid_credentials(self):
        homepage_obj = HomePage(self.driver)
        register_obj= homepage_obj.navigate_to_register_page()
        acc_success_obj = register_obj.register_an_account("dimple","Kukreja",self.generate_random_email(),
                                                           "9874561230","123456","123456",True,"select")
        expected_text = "Your Account Has Been Created!"
        assert acc_success_obj.retrieve_account_creation_message().__eq__(expected_text)

    def test_register_with_already_registered_email(self):
        homepage_obj = HomePage(self.driver)
        register_obj= homepage_obj.navigate_to_register_page()
        register_obj.register_an_account("Minal", "Patil", "patilminal322@gmail.com",
                                                           "9874561230", "123456", "123456", True, "select")
        expected_text = "Warning: E-Mail Address is already registered!"
        assert register_obj.retrieve_duplicate_warning_message().__eq__(expected_text)

    def test_register_without_entering_any_fields(self):
        homepage_obj = HomePage(self.driver)
        register_obj= homepage_obj.navigate_to_register_page()
        register_obj.register_an_account("", "", "",
                                         "", "", "", False, "")

        expected_policy_message = "Warning: You must agree to the Privacy Policy!"
        expected_firstname_warn_message = "First Name must be between 1 and 32 characters!"
        expected_lastname_warn_message = "Last Name must be between 1 and 32 characters!"
        expected_email_warn_message = "E-Mail Address does not appear to be valid!"
        expected_telephone_warn_message = "Telephone must be between 3 and 32 characters!"
        expected_password_warn_message = "Password must be between 4 and 20 characters!"

        assert register_obj.verify_all_warnings(expected_policy_message,expected_firstname_warn_message,expected_lastname_warn_message,
                            expected_email_warn_message,expected_telephone_warn_message,expected_password_warn_message)
