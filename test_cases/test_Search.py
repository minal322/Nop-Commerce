from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.search import SearchPage
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        homepage_obj = HomePage(self.driver)
        #select product
        homepage_obj.enter_product_into_search_box_field("HP")
        #click on button
        homepage_obj.click_on_search_button()
        #to check if product is displayed or not on Search page
        search_obj = SearchPage(self.driver)
        assert search_obj.display_status_of_valid_product()
    
    def test_search_for_an_invalid_product(self):
        homepage_obj = HomePage(self.driver)
        # select product
        homepage_obj.enter_product_into_search_box_field("Maruti suzuki")
        # click on button
        homepage_obj.click_on_search_button()
        search_obj = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        actual_text = search_obj.retrieve_no_product_message()
        assert actual_text == expected_text
    
    def test_search_without_entering_any_product(self):
        homepage_obj = HomePage(self.driver)
        # click on button
        homepage_obj.click_on_search_button()
        search_obj = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_obj.retrieve_no_product_message().__eq__(expected_text)

    
