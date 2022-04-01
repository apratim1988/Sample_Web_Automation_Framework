import time
import sys

sys.path.append("../../")
import pytest
from Pages.IIFLPOSHomePage import HomePage
from TestCases.IIFLPOS.BaseTest import BaseTest
from Utilities import dataProvider

class Test_IIFLPOS(BaseTest):

    @pytest.mark.parametrize(
        "pin,mobileno,fullname,email,altmobileno,add1,add2,height,weight,nomname",
        dataProvider.get_data("iiflpos"))
    def test_IIFLPOS(self, pin, mobileno, fullname, email, altmobileno, add1, add2, height, weight, nomname,):
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
        propdetailspage = policyselectionpage.SelectTenure()
        propdetailspage.landingpage()
        time.sleep(2)
        propdetailspage.InputName(fullname)
        self.VerifyPresence_IIFLPOSPropDOB()
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
        self.VerifyPresence_IIFLPOSNomDOB()
        time.sleep(1)
        propdetailspage.ClickDOB()
        time.sleep(2)
        propdetailspage.SelectNomGender()
        propdetailspage.SelectNomineeRltn()
        propdetailspage.ClickNext9()
        time.sleep(2)



