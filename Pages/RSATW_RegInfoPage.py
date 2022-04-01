import time
from Pages.BasePage import BasePage
from Pages.RSATW_PrevPolicyStatusPage import RSATWPreviousPolicyStatus

class RSATWRegistrationInfo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def SelectRegistrationDate(self):
        self.click("RSAtwregdatepicker_XPATH")
        time.sleep(1)
        self.click("RSAtwmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwmonthchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwdaychoose_XPATH")
        time.sleep(1)

    def ClickNext1(self):
        self.click("RSAtwpolstspage_XPATH")
        rsatwpreviouspolicystatuspage = RSATWPreviousPolicyStatus(self.driver)
        return rsatwpreviouspolicystatuspage