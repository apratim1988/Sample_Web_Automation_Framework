from Pages.BasePage import BasePage
from Pages.RSATW_QuotesPage import RSATWQuotesPage

class RSATWPreviousPolicyStatus(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputExpiryDate(self,expdate):
        self.type("RSAtwexpdate_XPATH",expdate)

    def ClickNext1(self):
        self.click("RSAtwquotespage_XPATH")
        rsatwquotespage = RSATWQuotesPage(self.driver)
        return rsatwquotespage


    # def InputMobileNo(self,mobileno):
    #     self.type("RSAtwinputmobile_XPATH",mobileno)
    #
    # def ClickSubmit(self):
    #     self.click("RSAtwquotespage_XPATH")
    #     quotespage = QuotesPage(self.driver)
    #     return quotespage

