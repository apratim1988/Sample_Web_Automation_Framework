import time
from Pages.BasePage import BasePage
from Pages.IIFLPlanSelectionPage import PlanSelection

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def SelectHealthPOS(self):
        self.click("IIFLRetailHealth_XPATH")
        time.sleep(2)
        planselectionpage = PlanSelection(self.driver)
        return planselectionpage




