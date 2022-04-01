import time

from Pages.BasePage import BasePage
from Pages.PolicyDetailsPage import PolicyDetailsPage


class QuotesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ShareQuotes(self):
        self.click("sharequotes_XPATH")

    def SelectAllQuotes(self):
        self.click("selectallquotes_XPATH")

    def ClickNext1(self):
        self.click("next3_XPATH")

    def InputName(self,fullname):
        self.type("name_XPATH",fullname)

    def InputEmail(self,email):
        self.type("email_XPATH",email)

    def InputMobileNo(self,mobileno):
        self.type("mobno_XPATH",mobileno)

    def ClickSubmit(self):
        self.click("submit_XPATH")

    def ClickCloseButton(self):
        self.click("closebutton_XPATH")

    def RSAPlanSelect(self):
        self.Scroll()
        time.sleep(5)
        self.click("rsaplanselect_XPATH")
        policydetailspage = PolicyDetailsPage(self.driver)
        return policydetailspage
