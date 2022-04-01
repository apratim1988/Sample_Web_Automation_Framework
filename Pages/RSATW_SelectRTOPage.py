from Pages.BasePage import BasePage
from Pages.RSATW_RegInfoPage import RSATWRegistrationInfo

class RSATWSelectRTO(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRTO(self,RTO):
        self.type("RSAtwinputRTO_XPATH",RTO)

    def SelectRTO(self):
        self.click("RSAtwselectRTO_XPATH")

    def ClickNext1(self):
        self.click("RSAtwreginfopage_XPATH")
        rsatwregistrationinfopage = RSATWRegistrationInfo(self.driver)
        return rsatwregistrationinfopage