import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from TestCases.AnandRathi.BaseTest import BaseTest
from Pages.InsuredDetailsPage import InsuredDetailsPage


class HealthInsurancePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        time.sleep(3)

    def InputPin(self,pin):
        self.type("pin_XPATH",pin)

    def SelectSum(self,sumvalue):
        self.SelectSumInsured(sumvalue)

    def InputMobileNo(self,mobileno):
        self.type("contactnum_XPATH",mobileno)

    def ClickNext(self):
        self.click("next1_XPATH")
        insureddetailspage = InsuredDetailsPage(self.driver)
        return insureddetailspage
