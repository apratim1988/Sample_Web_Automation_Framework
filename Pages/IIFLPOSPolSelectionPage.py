import time
from Pages.BasePage import BasePage
from Pages.IIFLPOSPropDetailsPage import PropDetails

class PolicySelection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landingpage(self):
        pass

    def SelectPlan(self):
        self.click("IIFLSelectPlan_XPATH")
        time.sleep(4)

    def ClickProceed1(self):
        self.click("IIFLClickProceed1_XPATH")
        time.sleep(1)

    def SelectTenure(self):
        self.click("IIFLPOSSelectTenure_XPATH")
        time.sleep(2)
        propdetailspage = PropDetails(self.driver)
        return propdetailspage
