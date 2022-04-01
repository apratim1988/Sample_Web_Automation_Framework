import time

from Pages.BasePage import BasePage
from Pages.FGNGFWRegInfoPage import FGNGFWRegInfo
from Pages.FGNGTWRegInfoPage import FGNGTWRegInfo

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def SelectFGNGFW(self):
        self.click("FGNGfw_XPATH")
        fgngfwreginfopage = FGNGFWRegInfo(self.driver)
        return fgngfwreginfopage

    def SelectFGNGTW(self):
        self.click("FGNGtw_XPATH")
        fgngtwreginfopage = FGNGTWRegInfo(self.driver)
        return fgngtwreginfopage