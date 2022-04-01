import time
from Pages.BasePage import BasePage

class FGNGTWPropInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputPropEmail(self, email):
        self.type("FGNGtwinputowneremail_XPATH",email)

    def InputPropDOB(self):
        self.click("FGNGtwownerdobdatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGtwownerdobmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwownerdobyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwownerdobmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwownerdobdaychoose_XPATH")
        time.sleep(1)

    def InputOwnerAdd1(self,add1):
        self.type("FGNGtwowneradd1_XPATH",add1)

    def InputOwnerPinCode(self,pincode):
        self.type("FGNGtwownerpincode_XPATH",pincode)

    def InputEnggNo(self,engno):
        self.type("FGNGtwownerenggno_XPATH",engno)

    def InputChssNo(self,chssno):
        self.type("FGNGtwownerchssgno_XPATH",chssno)

    def InputNomFname(self,nomfname):
        self.type("FGNGtwnomfname_XPATH",nomfname)

    def InputNomLname(self, nomlname):
        self.type("FGNGtwnomlname_XPATH", nomlname)

    def InputNomAge(self, nomage):
        self.type("FGNGtwnomage_XPATH", nomage)

    def SelectNomineeReln(self):
        self.click("FGNGtwnomreltndropdown_XPATH")
        time.sleep(1)
        self.click("FGNGtwnomreltnoption_XPATH")
        time.sleep(1)

    def SelectSelfDeclaration(self):
        self.click("FGNGtwselfdeclchkbox2_XPATH")
        time.sleep(1)

    def ClickSubmit4(self):
        self.click("FGNGtwclicksubmit4_XPATH")

