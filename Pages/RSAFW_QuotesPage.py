from Pages.BasePage import BasePage
from Pages.RSAFW_ProposalInfoPage import RSAFWProposalInfoPage


class RSAFWQuotesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ClickShareQuotes(self):
        self.click("RSAfwsharequotes_XPATH")

    def ClickSelectAllPlan(self):
        self.click("RSAfwselectallplan_XPATH")

    def ClickNext1(self):
        self.click("RSAfwsharequotespage_XPATH")

    def InputName(self,fullname):
        self.type("RSAfwsharequotesname_XPATH",fullname)

    def InputEmail(self,email):
        self.type("RSAfwsharequotesemail_XPATH",email)

    def InputMobileNo(self,mobileno):
        self.type("RSAfwsharequotesmobile_XPATH",mobileno)

    def ClickNext2(self):
        self.click("RSAfwselectplanpage_XPATH")

    def SelectPlanType(self):
        self.click("RSAfwselectcomprehensive_XPATH")

    def ClickProceed(self):
        self.click("RSAfwproposalinfopage_XPATH")
        rsafwproposalinfopage = RSAFWProposalInfoPage(self.driver)
        return rsafwproposalinfopage

