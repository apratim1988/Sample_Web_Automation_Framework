import time
from Pages.BasePage import BasePage
from Pages.IIFLPOSPolSelectionPage import PolicySelection
from selenium.webdriver.common.keys import Keys

class PlanSelection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landingpage(self):
        pass

    def SelectRisingHealthCosts(self):
        self.click("IIFLPOSSelectRisingHealth_XPATH")
        time.sleep(1)

    def ClickNext1(self):
        self.click("IIFLPOSClickNext1_XPATH")
        time.sleep(1)

    def SelectMemberDetails(self):
        self.click("IIFLPOSSelectMemSelf_XPATH")
        time.sleep(1)
        self.click("IIFLPOSSelectMemAgeDropdown_XPATH")
        time.sleep(1)
        self.click("IIFLPOSSelectMemAge_XPATH")
        time.sleep(1)

    # def Enter(self):
    #     enter = Keys.ENTER
    #     time.sleep(1)
    #     return enter

    def CLickNext2(self):
        self.click("IIFLPOSClickNext2_XPATH")
        time.sleep(2)

    def SelectCity(self):
        self.click("IIFLPOSSelectCity_XPATH")
        time.sleep(2)

    def ClickNext3(self):
        self.click("IIFLPOSClickNext3_XPATH")
        time.sleep(2)

    def CLickNext4(self):
        self.click("IIFLPOSClickNext4_XPATH")
        time.sleep(2)

    def InputMobileNo(self,mobileno):
        self.type("IIFLPOSInputMobileNo_XPATH",mobileno)
        time.sleep(1)

    def ClickNext5(self):
        self.click("IIFLPOSClickNext5_XPATH")
        time.sleep(2)

    def SelectCallOption(self):
        self.click("IIFLPOSSelectCallOption_XPATH")
        time.sleep(8)
        policyselectionpage = PolicySelection(self.driver)
        return policyselectionpage



