import time

from Pages.BasePage import BasePage
from Pages.QuestionariesPage import QuestionariesPage

class SelfDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputSelfFirstName(self,firstname):
        self.type("selffname_XPATH",firstname)

    def InputSelfLastName(self,lastname):
        self.type("selflname_XPATH",lastname)

    def InputSelfDOB(self,dob):
        self.type("selfdob_XPATH",dob)

    def SelectSelfGender(self):
        self.click("selfgender_XPATH")

    def InputSelfHeight(self,height):
        self.type("selfheight_XPATH",height)

    def InputSelfWeight(self,weight):
        self.type("selfweight_XPATH",weight)

    def InputSelfDesignation(self,designation):
        self.type("selfdesignation_XPATH",designation)

    def InputNomineeFName(self,nomfirstname):
        self.type("nomfname_XPATH",nomfirstname)

    def InputNomineeLName(self,nomlastname):
        self.type("nomlname_XPATH",nomlastname)

    def InputNomineeDOB(self,nomdob):
        self.type("nomdob_XPATH",nomdob)

    def SelectNomineeGender(self):
        self.click("nomgender_XPATH")

    def SelectNomineeRltnDropdown(self):
        self.click("nomrelation_XPATH")

    def SelectNomineeRelation(self):
        self.click("nomrelationvalue_XPATH")

    def ClickNext(self):
        self.click("next6_XPATH")
        questionariespage = QuestionariesPage(self.driver)
        return questionariespage








