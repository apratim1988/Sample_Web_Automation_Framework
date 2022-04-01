import time
import sys
sys.path.append("../../")
import pytest
from Pages.HomePage import HomePage
from TestCases.AnandRathi.BaseTest import BaseTest
from Utilities import dataProvider


class Test_RSA_FW(BaseTest):

    @pytest.mark.parametrize(
        "model,brand,RTO,expdate,mobileno,fullname,email,regno,engno,chssno,finname,pucno,pucexpdt,prevpolno,nomname,nomage,pan,aadhar,add1,add2,pin",
        dataProvider.get_data("rsa_fourwheeler"))
    def test_RSA_FW(self, model,brand, RTO, expdate, mobileno, fullname, email, regno, engno, chssno, finname, pucno,
                    pucexpdt, prevpolno, nomname, nomage, pan, aadhar, add1, add2, pin):
        home = HomePage(self.driver)
        rsafwselectvehiclepage = home.SelectRSAFW()
        time.sleep(1)
#        self.VerifyPresence_RSAFWVhclInfoOption()
        rsafwselectvehiclepage.SelectVehicleInfo()
        time.sleep(4)
#        self.VerifyPresence_RSAFWSelectBrandButton()
        rsafwselectvehiclepage.SelectVehicleBrandName(model)
        time.sleep(1)
        rsafwselectvehiclepage.SelectBrandMaruti()
        time.sleep(1)
        rsafwselectvehiclepage.ClickNext1()
        time.sleep(1)
        rsafwselectvehiclepage.SelectVehicleModel1(brand)
        time.sleep(1)
        rsafwselectvehiclepage.ClickNext2()
        time.sleep(1)
        rsafwselectvehiclepage.SelectVehicleModel2()
        time.sleep(1)
        selectrtopage = rsafwselectvehiclepage.ClickNext3()
        self.VerifyPresence_RSAFWInputRTOTextBox()
        selectrtopage.InputRTO(RTO)
        time.sleep(3)
        selectrtopage.SelectRTO()
        time.sleep(1)
        registrationinfopage = selectrtopage.ClickNext1()
        time.sleep(2)
        registrationinfopage.SelectRegistrationDate()
        time.sleep(3)
        previouspolicystatuspage = registrationinfopage.ClickNext1()
        time.sleep(2)
        previouspolicystatuspage.InputExpiryDate(expdate)
        time.sleep(2)
        rsafwquotespage = previouspolicystatuspage.ClickNext1()
        self.VerifyPresence_RSAFWShareQuotesButton()
        time.sleep(10)
        rsafwquotespage.ClickShareQuotes()
        time.sleep(2)
        rsafwquotespage.ClickSelectAllPlan()
        time.sleep(2)
        rsafwquotespage.ClickNext1()
        time.sleep(2)
        rsafwquotespage.InputName(fullname)
        rsafwquotespage.InputEmail(email)
        rsafwquotespage.InputMobileNo(mobileno)
        time.sleep(1)
        rsafwquotespage.ClickNext2()
        time.sleep(5)
        rsafwquotespage.SelectPlanType()
        self.VerifyPresence_RSAFWProceedButton()
        rsafwproposalinfopage = rsafwquotespage.ClickProceed()
        time.sleep(3)
        rsafwproposalinfopage.InputRegNo(regno)
        rsafwproposalinfopage.InputEnggNo(engno)
        rsafwproposalinfopage.InputChssNo(chssno)
        rsafwproposalinfopage.SelectVhclOwnrshipChnged()
        rsafwproposalinfopage.SelectFinanced()
        rsafwproposalinfopage.InputFiancerName(finname)
        rsafwproposalinfopage.SelectFinancerType()
        rsafwproposalinfopage.SelectPUC()
        rsafwproposalinfopage.InputPUCNo(pucno)
        rsafwproposalinfopage.SelectPUCExpDate(pucexpdt)
        rsafwproposalinfopage.SelectPrevInsCompany()
        rsafwproposalinfopage.SelectPrevPolType()
        rsafwproposalinfopage.InputPrevPolNo(prevpolno)
        rsafwproposalinfopage.InputNomineeName(nomname)
        rsafwproposalinfopage.InputNomineeAge(nomage)
        rsafwproposalinfopage.SelectNomineeRltn()
        rsafwproposalinfopage.SelectCPACover()
        rsafwproposalinfopage.SelectPrefix()
        rsafwproposalinfopage.InputName(fullname)
        rsafwproposalinfopage.SelectGender()
        rsafwproposalinfopage.SelectCustomerDOB()
        rsafwproposalinfopage.InputPAN(pan)
        rsafwproposalinfopage.InputAadhar(aadhar)
        rsafwproposalinfopage.InputAdd1(add1)
        rsafwproposalinfopage.InputAdd2(add2)
        rsafwproposalinfopage.InputPIN(pin)
        rsafwproposalinfopage.SelectRegAddDropdown()
        rsafwproposalinfopage.InputRegAdd1(add1)
        rsafwproposalinfopage.InputRegAdd2(add2)
        rsafwproposalinfopage.InputRegPin(pin)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,0);")
        self.VerifyPresence_RSAFWProceedToReviewPageButton()
        rsatwpolicyreviewpage = rsafwproposalinfopage.ClickProceed()
        # # time.sleep(15)
        # # rsatwpolicyreviewpage.ClickShareButton()
        # # time.sleep(2)
        # # rsatwpolicyreviewpage.ClickSubmit()














