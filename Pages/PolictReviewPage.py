import time

from Pages.BasePage import BasePage


class PolictReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def GetName(self):
        policyholdername = self.getText("namevalidation_XPATH")
        return policyholdername

    def GetPhoneNo(self):
        policyholderphone = self.getText("phonevalidation_XPATH")
        return policyholderphone

    def GetEmail(self):
        policyholderemail = self.getText("emaivalidation_XPATH")
        return policyholderemail

    def FinalSubmit(self):
        self.click("finalsubmit_XPATH")

    def SharePolicy(self):
        self.click("share_XPATH")










