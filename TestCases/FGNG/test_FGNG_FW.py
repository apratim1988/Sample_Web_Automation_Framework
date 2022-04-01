import time
import sys

sys.path.append("../../")
import pytest
from Pages.FGNG_HomePage import HomePage
from TestCases.FGNG.BaseTest import BaseTest
from Utilities import dataProvider


class Test_FGNG_FW(BaseTest):

    @pytest.mark.parametrize(
        "regno,mobno,firstname,lastname,brand,model,polno,email,add1,pincode,engno,chssno,nomfname,nomlname,nomage",
        dataProvider.get_data("fgng_fourwheeler"))
    def test_FGNG_FW(self, regno, mobno, firstname, lastname, brand, model, polno, email, add1, pincode, engno, chssno,
                     nomfname, nomlname, nomage):
        home = HomePage(self.driver)
        fgngfwreginfopage = home.SelectFGNGFW()
        time.sleep(1)
        fgngfwreginfopage.landing_page()
        fgngfwreginfopage.InputRegNumber(regno)
        fgngfwreginfopage.InputMobileNo(mobno)
        fgngfwreginfopage.ClickSubmit1()
        time.sleep(10)
        fgngfwreginfopage.InputOwnerFname(firstname)
        fgngfwreginfopage.InputOwnerLname(lastname)
        time.sleep(1)
        fgngfwreginfopage.SelectCar(brand,model)
        fgngfwreginfopage.SelectManufacturingYr()
        fgngfwreginfopage.InputRegDate()
        fgngfwreginfopage.SelectPrevPolStus()
        fgngfwreginfopage.SelectPrevInsCom()
        fgngfwreginfopage.PrevPolcyExpDate()
        fgngfwreginfopage.SelectPrevPolNo(polno)
        fgngfwreginfopage.SelectIfPrevYrClaimTaken()
        fgngfwreginfopage.SelectNCBPercentage()
        planselectionpage = fgngfwreginfopage.ClickSubmit2()
        time.sleep(8)
        planselectionpage.ClickSelfDeclaChkBox()
        time.sleep(1)
        proposerinfopage = planselectionpage.ClickSubmit3()
        time.sleep(5)
        proposerinfopage.landing_page()
        proposerinfopage.InputPropEmail(email)
        proposerinfopage.InputPropDOB()
        proposerinfopage.InputOwnerAdd1(add1)
        proposerinfopage.InputOwnerPinCode(pincode)
        proposerinfopage.InputEnggNo(engno)
        proposerinfopage.InputChssNo(chssno)
        proposerinfopage.InputNomFname(nomfname)
        proposerinfopage.InputNomLname(nomlname)
        proposerinfopage.InputNomAge(nomage)
        proposerinfopage.SelectNomineeReln()
        proposerinfopage.SelectSelfDeclaration()
        proposerinfopage.ClickSubmit4()
        time.sleep(5)



