from Pages.BasePage import BasePage
from Pages.RSAFW_RegInfoPage import RSAFWRegistrationInfo

class RSAFWSelectRTO(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRTO(self,RTO):
        self.type("RSAfwinputRTO_XPATH",RTO)

    def SelectRTO(self):
        self.click("RSAfwselectRTO_XPATH")

    def ClickNext1(self):
        self.click("rsafwreginfopage_XPATH")
        rsafwregistrationinfopage = RSAFWRegistrationInfo(self.driver)
        return rsafwregistrationinfopage