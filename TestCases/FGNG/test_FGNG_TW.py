import time
import sys

sys.path.append("../../")
import pytest
from Pages.FGNG_HomePage import HomePage
from TestCases.FGNG.BaseTest import BaseTest
from Utilities import dataProvider


class Test_FGNG_TW(BaseTest):

    @pytest.mark.parametrize(
        "regno,mobno,firstname,lastname,brand,model,polno,email,add1,pincode,engno,chssno,nomfname,nomlname,nomage",
        dataProvider.get_data("fgng_twowheeler"))
    def test_FGNG_TW(self, regno, mobno, firstname, lastname, brand, model, polno, email, add1, pincode, engno, chssno,
                     nomfname, nomlname, nomage):
        home = HomePage(self.driver)
        fgngtwreginfopage = home.SelectFGNGTW()
        time.sleep(1)
        fgngtwreginfopage.landing_page()
        fgngtwreginfopage.InputRegNumber(regno)
        fgngtwreginfopage.InputMobileNo(mobno)
        fgngtwreginfopage.ClickSubmit1()
        time.sleep(10)
        fgngtwreginfopage.InputOwnerFname(firstname)
        fgngtwreginfopage.InputOwnerLname(lastname)
        time.sleep(1)
        fgngtwreginfopage.SelectCar(brand,model)
        fgngtwreginfopage.SelectManufacturingYr()
        fgngtwreginfopage.InputRegDate()
        fgngtwreginfopage.SelectPrevPolStus()
        fgngtwreginfopage.SelectPrevInsCom()
        fgngtwreginfopage.PrevPolcyExpDate()
        fgngtwreginfopage.SelectPrevPolNo(polno)
        fgngtwreginfopage.SelectIfPrevYrClaimTaken()
        fgngtwreginfopage.SelectNCBPercentage()
        planselectionpage = fgngtwreginfopage.ClickSubmit2()
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



