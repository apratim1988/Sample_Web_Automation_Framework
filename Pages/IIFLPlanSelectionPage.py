import time
from Pages.BasePage import BasePage
from Pages.IIFLPolSelectionPage import PolicySelection
from selenium.webdriver.common.keys import Keys

class PlanSelection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landingpage(self):
        pass

    def SelectRisingHealthCosts(self):
        self.click("IIFLSelectRisingHealth_XPATH")
        time.sleep(1)

    def ClickNext1(self):
        self.click("IIFLClickNext1_XPATH")
        time.sleep(1)

    def SelectMemberDetails(self):
        self.click("IIFLSelectMemSelf_XPATH")
        time.sleep(1)
        self.click("IIFLSelectMemAgeDropdown_XPATH")
        time.sleep(1)
        self.click("IIFLSelectMemAge_XPATH")
        time.sleep(1)

    # def Enter(self):
    #     enter = Keys.ENTER
    #     time.sleep(1)
    #     return enter

    def CLickNext2(self):
        self.click("IIFLClickNext2_XPATH")
        time.sleep(2)

    def SelectCity(self):
        self.click("IIFLSelectCity_XPATH")
        time.sleep(2)

    def ClickNext3(self):
        self.click("IIFLClickNext3_XPATH")
        time.sleep(2)

    def CLickNext4(self):
        self.click("IIFLClickNext4_XPATH")
        time.sleep(2)

    def InputMobileNo(self,mobileno):
        self.type("IIFLInputMobileNo_XPATH",mobileno)
        time.sleep(1)

    def ClickNext5(self):
        self.click("IIFLClickNext5_XPATH")
        time.sleep(2)

    def SelectCallOption(self):
        self.click("IIFLSelectCallOption_XPATH")
        time.sleep(8)
        policyselectionpage = PolicySelection(self.driver)
        return policyselectionpage



