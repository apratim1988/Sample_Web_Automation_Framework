import time

from Pages.BasePage import BasePage
from Pages.SelfDetailsPage import SelfDetailsPage

class PropDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputFirstName(self,firstname):
        self.type("firstname_XPATH",firstname)

    def InputLastName(self,lastname):
        self.type("lastname_XPATH",lastname)

    def InputDOB(self,dob):
        self.type("dob_XPATH",dob)

    def SelectPropGender(self):
        self.click("propgender_XPATH")

    def InputEmailId(self,email):
        self.type("emailid_XPATH",email)

    # def InputContactNo(self,mobileno):
    #     self.type("contactno_XPATH",mobileno)

    def InputIncome(self,income):
        self.type("income_XPATH",income)

    def InputPANCard(self,pan):
        self.type("pan_XPATH",pan)

    def SelectOccupationDropdown(self):
        self.click("occudropdown_XPATH")

    def SelectOccupation(self):
        self.click("occupation_XPATH")

    def InputDesignation(self,designation):
        self.type("designation_XPATH",designation)

    def SelectMaritalStatusDropdown(self):
        self.click("statusdropdown_XPATH")

    def SelectMaritalStatus(self):
        self.click("status_XPATH")

    def SelectEducationDropdown(self):
        self.click("educationdropdown_XPATH")

    def SelectQualification(self):
        self.click("qualification_XPATH")

    def SelectTPANameDropdown(self):
        self.click("tpanamedropdown_XPATH")

    def SelectTPA(self):
        self.click("tpaname_XPATH")

    def InputAdd1(self,add1):
        self.type("add1_XPATH",add1)

    def InputAdd2(self,add2):
        self.type("add2_XPATH",add2)

    def ClickNext(self):
        self.click("next5_XPATH")
        selfdetailspage = SelfDetailsPage(self.driver)
        return selfdetailspage






