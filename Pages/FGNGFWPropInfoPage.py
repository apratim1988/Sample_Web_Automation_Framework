import time
from Pages.BasePage import BasePage

class FGNGFWPropInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputPropEmail(self, email):
        self.type("FGNGfwinputowneremail_XPATH",email)

    def InputPropDOB(self):
        self.click("FGNGfwownerdobdatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGfwownerdobmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwownerdobyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwownerdobmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwownerdobdaychoose_XPATH")
        time.sleep(1)

    def InputOwnerAdd1(self,add1):
        self.type("FGNGfwowneradd1_XPATH",add1)

    def InputOwnerPinCode(self,pincode):
        self.type("FGNGfwownerpincode_XPATH",pincode)

    def InputEnggNo(self,engno):
        self.type("FGNGfwownerenggno_XPATH",engno)

    def InputChssNo(self,chssno):
        self.type("FGNGfwownerchssgno_XPATH",chssno)

    def InputNomFname(self,nomfname):
        self.type("FGNGfwnomfname_XPATH",nomfname)

    def InputNomLname(self, nomlname):
        self.type("FGNGfwnomlname_XPATH", nomlname)

    def InputNomAge(self, nomage):
        self.type("FGNGfwnomage_XPATH", nomage)

    def SelectNomineeReln(self):
        self.click("FGNGfwnomreltndropdown_XPATH")
        time.sleep(1)
        self.click("FGNGfwnomreltnoption_XPATH")
        time.sleep(1)

    def SelectSelfDeclaration(self):
        self.click("FGNGfwselfdeclchkbox2_XPATH")
        time.sleep(1)

    def ClickSubmit4(self):
        self.click("FGNGfwclicksubmit4_XPATH")

