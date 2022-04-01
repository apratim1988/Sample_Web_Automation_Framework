import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from Utilities.waitelements import *
from selenium.webdriver.common.keys import Keys

import sys
sys.path.insert(0, './IIFL')
from Utilities.waitelements import *


# @pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("selenium_driver")
@pytest.mark.usefixtures("log_on_failure")
class BaseTest:
    pass
# RSA Health Explicit Waits

# IIFLPOS Explicit Waits

    def VerifyPresence_IIFLPropDOB(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='date']")))
        self.driver.execute_script("arguments[0].value = arguments[1]", element, "2004-03-18")


    def VerifyPresence_IIFLNomDOB(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='date']")))
        self.driver.execute_script("arguments[0].value = arguments[1]", element, "2004-03-18")
