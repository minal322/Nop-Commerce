
from pages.homepage import HomePage
from test_cases.BaseTest import BaseTest

class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        homepage_obj = HomePage(self.driver)
        search_obj= homepage_obj.search_for_a_product("HP")
        #to check if product is displayed or not on Search page
        assert search_obj.display_status_of_valid_product()
    
    def test_search_for_an_invalid_product(self):
        homepage_obj = HomePage(self.driver)
        search_obj = homepage_obj.search_for_a_product("Maruti suzuki")
        expected_text = "There is no product that matches the search criteria."
        actual_text = search_obj.retrieve_no_product_message()
        assert actual_text == expected_text
    
    def test_search_without_entering_any_product(self):
        homepage_obj = HomePage(self.driver)
        # click on button
        search_obj = homepage_obj.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria.xyz"
        assert search_obj.retrieve_no_product_message().__eq__(expected_text)

    
