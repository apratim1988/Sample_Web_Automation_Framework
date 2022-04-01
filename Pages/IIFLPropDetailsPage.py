import time
from Pages.BasePage import BasePage


class PropDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landingpage(self):
        pass

    def InputName(self,fullname):
        self.type("IIFLInputName_XPATH",fullname)

    def ClickDOB(self):
        self.SelectDOB("IIFLInputDOB_XPATH")

    def SelectGender(self):
        self.click("IIFLInputGender_XPATH")

    def InputEmail(self,email):
        self.type("IIFLInputEmail_XPATH",email)

    def InputAltMobileNo(self,altmobileno):
        self.type("IIFLInputAltMobNo_XPATH",altmobileno)

    def ClickNext6(self):
        self.click("IIFLClickNext6_XPATH")
        time.sleep(1)

    def InputAddress(self,add1,add2):
        self.type("IIFLInputAdd1_XPATH",add1)
        self.type("IIFLInputAdd2_XPATH",add2)

    def InputPINCode(self,pin):
        self.type("IIFLInputPIN_XPATH", pin)
        time.sleep(3)

    def ClickNext7(self):
        self.click("IIFLClickNext7_XPATH")
        time.sleep(2)

    def InputHeightWeight(self,height,weight):
        self.type("IIFLInputHeight_XPATH",height)
        self.type("IIFLInputWeight_XPATH",weight)
        time.sleep(1)

    def ClickNext8(self):
        self.click("IIFLClickNext8_XPATH")
        time.sleep(2)

    def InputNomineeName(self,nomname):
        self.type("IIFLInputNomineeName_XPATH",nomname)

    def SelectNomGender(self):
        self.click("IIFLInputNomGender_XPATH")
        time.sleep(1)

    def SelectNomineeRltn(self):
        self.click("IIFLSelectRltnDropdown_XPATH")
        time.sleep(1)
        self.click("IIFLSelectRltnValue_XPATH")
        time.sleep(1)

    def ClickNext9(self):
        self.click("IIFLClickNext9_XPATH")
        time.sleep(1)


    def ClickSelfDeclChkbx(self):
        self.click("IIFLSelfDeclChkbox_XPATH")
        time.sleep(1)

    def ClickNext10(self):
        self.click("IIFLClickNext10_XPATH")
        time.sleep(2)


