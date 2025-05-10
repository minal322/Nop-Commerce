import pytest
from selenium import webdriver
from utils import read_configs
driver = None

@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = read_configs.read_config_data("basic info","browser")
    if browser.__eq__("chrome") or  browser.__eq__("Chrome") :
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox") or  browser.__eq__("Firefox") :
        driver = webdriver.Firefox()
    elif browser.__eq__("Edge") or  browser.__eq__("edge") :
        driver = webdriver.Edge()
    else:
        print("Provide valid browser name from this list Chrome / Firefox / Edge")
        driver = webdriver.Chrome()
    url = read_configs.read_config_data("basic info", "url")

    driver.get(url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()