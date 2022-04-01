from Pages.BasePage import BasePage
from Pages.RSATW_ProposalInfoPage import RSATWProposalInfoPage
class RSATWQuotesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ClickShareQuotes(self):
        self.click("RSAtwsharequotes_XPATH")

    def ClickSelectAllPlan(self):
        self.click("RSAtwselectallplan_XPATH")

    def ClickNext1(self):
        self.click("RSAtwsharequotespage_XPATH")

    def InputName(self,fullname):
        self.type("RSAtwsharequotesname_XPATH",fullname)

    def InputEmail(self,email):
        self.type("RSAtwsharequotesemail_XPATH",email)

    def InputMobileNo(self,mobileno):
        self.type("RSAtwsharequotesmobile_XPATH",mobileno)

    def ClickNext2(self):
        self.click("RSAtwselectplanpage_XPATH")

    def SelectPlanType(self):
        self.click("RSAtwselectcomprehensive_XPATH")

    def ClickProceed(self):
        self.click("RSAtwproposalinfopage_XPATH")
        rsatwproposalinfopage = RSATWProposalInfoPage(self.driver)
        return rsatwproposalinfopage

