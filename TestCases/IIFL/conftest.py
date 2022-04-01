import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from Utilities.filepath import *


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        rep.nodeid = docstring
    return rep


@pytest.fixture(scope="function")
def selenium_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('disable-infobars')
    s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    url = "https://diy.iiflinsurance.com"
    driver.get(url)
    driver.maximize_window()
    driver.set_window_size(1200, 600)
    time.sleep(3)
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture()
def log_on_failure(request, selenium_driver):
    yield
    item = request.node
    driver = selenium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

