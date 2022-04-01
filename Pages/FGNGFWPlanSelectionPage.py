import time
from Pages.BasePage import BasePage
from Pages.FGNGFWPropInfoPage import FGNGFWPropInfoPage

class FGNGFWPlanSelectionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ClickSelfDeclaChkBox(self):
        self.click("FGNGfwselfdeclchkbox1_XPATH")

    def ClickSubmit3(self):
        self.click("FGNGfwclicksubmit3_XPATH")
        proposerinfopage = FGNGFWPropInfoPage(self.driver)
        return proposerinfopage

