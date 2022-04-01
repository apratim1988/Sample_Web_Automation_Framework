import time
from Pages.BasePage import BasePage


class PropDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landingpage(self):
        pass

    def InputName(self,fullname):
        self.type("IIFLPOSInputName_XPATH",fullname)

    def ClickDOB(self):
        self.SelectDOB("IIFLPOSInputDOB_XPATH")

    def SelectGender(self):
        self.click("IIFLPOSInputGender_XPATH")

    def InputEmail(self,email):
        self.type("IIFLPOSInputEmail_XPATH",email)

    def InputAltMobileNo(self,altmobileno):
        self.type("IIFLPOSInputAltMobNo_XPATH",altmobileno)

    def ClickNext6(self):
        self.click("IIFLPOSClickNext6_XPATH")
        time.sleep(1)

    def InputAddress(self,add1,add2):
        self.type("IIFLPOSInputAdd1_XPATH",add1)
        self.type("IIFLPOSInputAdd2_XPATH",add2)

    def InputPINCode(self,pin):
        self.type("IIFLPOSInputPIN_XPATH", pin)
        time.sleep(3)

    def ClickNext7(self):
        self.click("IIFLPOSClickNext7_XPATH")
        time.sleep(2)

    def InputHeightWeight(self,height,weight):
        self.type("IIFLPOSInputHeight_XPATH",height)
        self.type("IIFLPOSInputWeight_XPATH",weight)
        time.sleep(1)

    def ClickNext8(self):
        self.click("IIFLPOSClickNext8_XPATH")
        time.sleep(2)

    def InputNomineeName(self,nomname):
        self.type("IIFLInputNomineeName_XPATH",nomname)

    def SelectNomGender(self):
        self.click("IIFLPOSInputNomGender_XPATH")
        time.sleep(1)

    def SelectNomineeRltn(self):
        self.click("IIFLPOSSelectRltnDropdown_XPATH")
        time.sleep(1)
        self.click("IIFLPOSSelectRltnValue_XPATH")
        time.sleep(1)

    def ClickNext9(self):
        self.click("IIFLPOSClickNext9_XPATH")
        time.sleep(1)


    def ClickSelfDeclChkbx(self):
        self.click("IIFLPOSSelfDeclChkbox_XPATH")
        time.sleep(1)

    def ClickNext10(self):
        self.click("IIFLPOSClickNext10_XPATH")
        time.sleep(2)


