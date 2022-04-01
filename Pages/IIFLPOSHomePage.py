import time
from Pages.BasePage import BasePage
from Pages.IIFLPOSPlanSelectionPage import PlanSelection

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def SelectHealthPOS(self):
        self.click("IIFLPOSRetailHealth_XPATH")
        time.sleep(2)
        planselectionpage = PlanSelection(self.driver)
        return planselectionpage




