from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def element_text_fetch(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text

    def element_displayed_status(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_css_selector"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def Type(self,text,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)
