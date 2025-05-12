import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utils import read_configs
#driver = None


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


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        # Assuming `driver` is the WebDriver you use to take a screenshot
        screenshot = driver.get_screenshot_as_png()  # Replace with actual screenshot logic
        allure.attach(screenshot, name="failed_test", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport (item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    _test_reports = getattr(item.module, '_test_reports', {})
    _test_reports[(item.nodeid, rep.when)] = rep
    item.module._test_reports = _test_reports
