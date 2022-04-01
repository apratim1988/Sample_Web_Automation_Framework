import time
from Pages.BasePage import BasePage
from Pages.FGNGTWPropInfoPage import FGNGTWPropInfoPage

class FGNGTWPlanSelectionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ClickSelfDeclaChkBox(self):
        self.click("FGNGtwselfdeclchkbox1_XPATH")

    def ClickSubmit3(self):
        self.click("FGNGtwclicksubmit3_XPATH")
        proposerinfopage = FGNGTWPropInfoPage(self.driver)
        return proposerinfopage

