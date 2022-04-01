import time
import sys

sys.path.append("../../")
import pytest
from Pages.IIFLHomePage import HomePage
from TestCases.IIFL.BaseTest import BaseTest
from Utilities import dataProvider

class Test_IIFL(BaseTest):

    @pytest.mark.parametrize(
        "pin,mobileno,fullname,email,altmobileno,add1,add2,height,weight,nomname",
        dataProvider.get_data("iiflpos"))
    def test_IIFL(self, pin, mobileno, fullname, email, altmobileno, add1, add2, height, weight, nomname,):
        home = HomePage(self.driver)
        planselectionpage = home.SelectHealthPOS()
        planselectionpage.landingpage()
        planselectionpage.SelectRisingHealthCosts()
        planselectionpage.ClickNext1()
        planselectionpage.SelectMemberDetails()
        planselectionpage.CLickNext2()
        planselectionpage.SelectCity()
        planselectionpage.ClickNext3()
        planselectionpage.CLickNext4()
        planselectionpage.InputMobileNo(mobileno)
        planselectionpage.ClickNext5()
        policyselectionpage = planselectionpage.SelectCallOption()
        policyselectionpage.landingpage()
        policyselectionpage.SelectPlan()
        policyselectionpage.ClickProceed1()
        time.sleep(2)
        propdetailspage = policyselectionpage.SelectTenure()
        time.sleep(3)
        propdetailspage.landingpage()
        time.sleep(3)
        propdetailspage.InputName(fullname)
        self.VerifyPresence_IIFLPropDOB()
        time.sleep(1)
        propdetailspage.ClickDOB()
        time.sleep(2)
        propdetailspage.SelectGender()
        propdetailspage.InputEmail(email)
        propdetailspage.InputAltMobileNo(altmobileno)
        time.sleep(2)
        propdetailspage.ClickNext6()
        time.sleep(2)
        propdetailspage.InputAddress(add1,add2)
        propdetailspage.InputPINCode(pin)
        propdetailspage.ClickNext7()
        time.sleep(2)
        propdetailspage.InputHeightWeight(height,weight)
        propdetailspage.ClickNext8()
        time.sleep(2)
        propdetailspage.InputNomineeName(nomname)
        self.VerifyPresence_IIFLNomDOB()
        time.sleep(1)
        propdetailspage.ClickDOB()
        time.sleep(2)
        propdetailspage.SelectNomGender()
        propdetailspage.SelectNomineeRltn()
        propdetailspage.ClickNext9()
        time.sleep(2)


