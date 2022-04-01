import time
from Pages.BasePage import BasePage
from Pages.RSAFW_PolicyReviewPage import RSAFWPolicyReviewPage


class RSAFWProposalInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRegNo(self,regno):
        self.type("RSAfwvhclregno_XPATH",regno)

    def InputEnggNo(self,engno):
        self.type("RSAfwvhclenggno_XPATH",engno)

    def InputChssNo(self,chssno):
        self.type("RSAfwvhclchssno_XPATH",chssno)

    def SelectVhclOwnrshipChnged(self):
        self.click("RSAfwvhclownershipdropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwvhclownershipoption_XPATH")
        time.sleep(1)

    def SelectFinanced(self):
        self.click("RSAfwvhclfinancedropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwvhclfinanceoption_XPATH")
        time.sleep(1)

    def InputFiancerName(self,finname):
        self.type("RSAfwvhclfinanciername_XPATH",finname)

    def SelectFinancerType(self):
        self.click("RSAfwvhclfintypedropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwvhclfintypeoption_XPATH")
        time.sleep(1)

    def SelectPUC(self):
        self.click("RSAfwpucdropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwpucoption_XPATH")
        time.sleep(1)

    def InputPUCNo(self,pucno):
        self.type("RSAfwpucnumber_XPATH",pucno)

    def SelectPUCExpDate(self,pucexpdt):
        self.type("RSAfwpucexpdatepicker_XPATH",pucexpdt)

    def SelectPrevInsCompany(self):
        self.click("RSAfwprevinscomdropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwprevinscomoption_XPATH")
        time.sleep(1)

    def SelectPrevPolType(self):
        self.click("RSAfwprevpoltypedropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwprevpoltypeoption_XPATH")
        time.sleep(1)

    def InputPrevPolNo(self,prevpolno):
        self.type("RSAfwprevpolnumber_XPATH",prevpolno)

    def InputNomineeName(self,nomname):
        self.type("RSAfwnomineename_XPATH",nomname)

    def InputNomineeAge(self,nomage):
        self.type("RSAfwnomineeage_XPATH",nomage)

    def SelectNomineeRltn(self):
        self.click("RSAfwnomineerltndropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwnomineerltnoption_XPATH")
        time.sleep(1)

    def SelectCPACover(self):
        self.click("RSAfwcpacoverdropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwcpacoveroption_XPATH")
        time.sleep(1)

    def SelectPrefix(self):
        self.click("RSAfwcustomertitledropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwcustomertitleoption_XPATH")
        time.sleep(1)

    def InputName(self,fullname):
        self.type("RSAfwcustomername_XPATH",fullname)

    def SelectGender(self):
        self.click("RSAfwcustomergenderdropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwcustomergenderoption_XPATH")
        time.sleep(1)

    def SelectCustomerDOB(self):
        self.click("RSAfwdobdatepicker_XPATH")
        time.sleep(1)
        self.click("RSAfwdobmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwdobyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwdobmonthchoose_XPATH")
        time.sleep(1)
        self.click("RSAfwdobdaychoose_XPATH")
        time.sleep(1)

    def InputPAN(self,pan):
        self.type("RSAfwcustomerpan_XPATH",pan)

    def InputAadhar(self,aadhar):
        self.type("RSAfwcustomeraadhar_XPATH",aadhar)

    def InputAdd1(self,add1):
        self.type("RSAfwcustomeradd1_XPATH",add1)

    def InputAdd2(self,add2):
        self.type("RSAfwcustomeradd2_XPATH",add2)

    def InputPIN(self,pin):
        self.type("RSAfwcustomerpin_XPATH",pin)

    def SelectRegAddDropdown(self):
        self.click("RSAfwregadddropdown_XPATH")
        time.sleep(1)
        self.click("RSAfwSelectOption_XPATH")
        time.sleep(1)

    def InputRegAdd1(self,add1):
        self.type("RSAfwRegAddLine1_XPATH",add1)

    def InputRegAdd2(self,add2):
        self.type("RSAfwRegAddLine2_XPATH",add2)

    def InputRegPin(self,pin):
        self.type("RSAfwRegPinCode_XPATH",pin)

    def ClickProceed(self):
        self.click("RSAfwpolreviewpage_XPATH")
        rsafwpolicyreviewpage = RSAFWPolicyReviewPage(self.driver)
        return rsafwpolicyreviewpage


