import time
from Pages.BasePage import BasePage
from Pages.RSAFW_PrevPolicyStatusPage import RSAFWPreviousPolicyStatus

class RSAFWRegistrationInfo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def SelectRegistrationDate(self):
        self.click("RSAfwregdatepicker_XPATH")
        time.sleep(1)
        self.click("RSAfwmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwmonthchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwdaychoose_XPATH")
        time.sleep(1)

    def ClickNext1(self):
        self.click("RSAfwpolstspage_XPATH")
        rsafwpreviouspolicystatuspage = RSAFWPreviousPolicyStatus(self.driver)
        return rsafwpreviouspolicystatuspage