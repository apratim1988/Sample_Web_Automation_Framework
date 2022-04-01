import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from Utilities.waitelements import *
import sys
sys.path.insert(0, './FGNG')
from Utilities.waitelements import *


# @pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("selenium_driver")
@pytest.mark.usefixtures("log_on_failure")
class BaseTest:
    pass
# RSA Health Explicit Waits

