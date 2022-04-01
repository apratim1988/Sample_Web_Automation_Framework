import time
from Pages.BasePage import BasePage

class RSATWPolicyReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    # def GetRegNo(self):
    #     self.getText("RSAtwverifyregno_XPATH")
    #
    # def GetEngNo(self):
    #     self.getText("RSAtwverifyengno_XPATH")
    #
    # def GetChssNo(self):
    #     self.getText("RSAtwverifychssno_XPATH")

    def ClickShareButton(self):
        self.click("RSAtwfinalsharebutton_XPATH")

    def ClickSubmit(self):
        self.click("RSAtwfinalsubmitbutton_XPATH")

