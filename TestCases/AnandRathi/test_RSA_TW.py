import time
import sys
sys.path.append("../../")
import pytest
from Pages.HomePage import HomePage
from TestCases.AnandRathi.BaseTest import BaseTest
from Utilities import dataProvider

class Test_RSA_TW(BaseTest):


    @pytest.mark.parametrize("model,brand,RTO,expdate,mobileno,fullname,email,regno,engno,chssno,finname,pucno,pucexpdt,prevpolno,nomname,nomage,pan,aadhar,add1,add2,pin", dataProvider.get_data("rsa_twowheeler"))
    def test_RSA_TW(self,model,brand,RTO,expdate,mobileno,fullname,email,regno,engno,chssno,finname,pucno,pucexpdt,prevpolno,nomname,nomage,pan,aadhar,add1,add2,pin):
        home = HomePage(self.driver)
        rsatwselectvehiclepage = home.SelectRSATW()
        self.VerifyPresence_RSATWVhclInfoOption()
        rsatwselectvehiclepage.SelectVehicleInfo()
        time.sleep(4)
#        self.VerifyPresence_RSATWSelectBrandButton()
        rsatwselectvehiclepage.SelectVehicleBrand(brand)
        time.sleep(2)
        rsatwselectvehiclepage.ClickNext1()
        time.sleep(2)
        rsatwselectvehiclepage.InputVehicleModel(model)
        time.sleep(2)
        rsatwselectvehiclepage.SelectVehicleModel135()
        rsatwselectvehiclepage.ClickNext2()
        time.sleep(1)
        rsatwselectvehiclepage.SelectVehicleModel()
        selectrtopage = rsatwselectvehiclepage.ClickNext3()
        self.VerifyPresence_RSATWInputRTOTextBox()
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
        rsatwquotespage = previouspolicystatuspage.ClickNext1()
        self.VerifyPresence_RSATWShareQuotesButton()
        time.sleep(10)
        rsatwquotespage.ClickShareQuotes()
        time.sleep(2)
        rsatwquotespage.ClickSelectAllPlan()
        time.sleep(2)
        rsatwquotespage.ClickNext1()
        time.sleep(2)
        rsatwquotespage.InputName(fullname)
        rsatwquotespage.InputEmail(email)
        rsatwquotespage.InputMobileNo(mobileno)
        time.sleep(1)
        rsatwquotespage.ClickNext2()
        time.sleep(5)
        rsatwquotespage.SelectPlanType()
        self.VerifyPresence_RSATWProceedButton()
        rsatwproposalinfopage = rsatwquotespage.ClickProceed()
        time.sleep(3)
        rsatwproposalinfopage.InputRegNo(regno)
        rsatwproposalinfopage.InputEnggNo(engno)
        rsatwproposalinfopage.InputChssNo(chssno)
        rsatwproposalinfopage.SelectVhclOwnrshipChnged()
        rsatwproposalinfopage.SelectFinanced()
        rsatwproposalinfopage.InputFiancerName(finname)
        rsatwproposalinfopage.SelectFinancerType()
        rsatwproposalinfopage.SelectPUC()
        rsatwproposalinfopage.InputPUCNo(pucno)
        rsatwproposalinfopage.SelectPUCExpDate(pucexpdt)
        rsatwproposalinfopage.SelectPrevInsCompany()
        rsatwproposalinfopage.SelectPrevPolType()
        rsatwproposalinfopage.InputPrevPolNo(prevpolno)
        rsatwproposalinfopage.InputNomineeName(nomname)
        rsatwproposalinfopage.InputNomineeAge(nomage)
        rsatwproposalinfopage.SelectNomineeRltn()
        rsatwproposalinfopage.SelectCPACover()
        rsatwproposalinfopage.SelectPrefix()
        rsatwproposalinfopage.InputName(fullname)
        rsatwproposalinfopage.SelectGender()
        rsatwproposalinfopage.SelectCustomerDOB()
        rsatwproposalinfopage.InputPAN(pan)
        rsatwproposalinfopage.InputAadhar(aadhar)
        rsatwproposalinfopage.InputAdd1(add1)
        rsatwproposalinfopage.InputAdd2(add2)
        rsatwproposalinfopage.InputPIN(pin)
        rsatwproposalinfopage.SelectRegAddDropdown()
        rsatwproposalinfopage.InputRegAdd1(add1)
        rsatwproposalinfopage.InputRegAdd2(add2)
        rsatwproposalinfopage.InputRegPin(pin)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,0);")
        self.VerifyPresence_RSATWProceedToReviewPageButton()
        rsatwpolicyreviewpage = rsatwproposalinfopage.ClickProceed()
        # time.sleep(15)
        # rsatwpolicyreviewpage.ClickShareButton()
        # time.sleep(2)
        # rsatwpolicyreviewpage.ClickSubmit()








        





