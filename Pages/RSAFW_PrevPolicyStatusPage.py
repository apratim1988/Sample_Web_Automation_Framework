from Pages.BasePage import BasePage
from Pages.RSAFW_QuotesPage import RSAFWQuotesPage

class RSAFWPreviousPolicyStatus(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputExpiryDate(self,expdate):
        self.type("RSAfwexpdate_XPATH",expdate)

    def ClickNext1(self):
        self.click("RSAfwquotespage_XPATH")
        rsafwquotespage = RSAFWQuotesPage(self.driver)
        return rsafwquotespage


    # def InputMobileNo(self,mobileno):
    #     self.type("RSAtwinputmobile_XPATH",mobileno)
    #
    # def ClickSubmit(self):
    #     self.click("RSAtwquotespage_XPATH")
    #     quotespage = QuotesPage(self.driver)
    #     return quotespage

