import time

from Pages.BasePage import BasePage
from Pages.RSATW_PolicyReviewPage import RSATWPolicyReviewPage
class RSATWProposalInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRegNo(self,regno):
        self.type("RSAtwvhclregno_XPATH",regno)

    def InputEnggNo(self,engno):
        self.type("RSAtwvhclenggno_XPATH",engno)

    def InputChssNo(self,chssno):
        self.type("RSAtwvhclchssno_XPATH",chssno)

    def SelectVhclOwnrshipChnged(self):
        self.click("RSAtwvhclownershipdropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwvhclownershipoption_XPATH")
        time.sleep(1)

    def SelectFinanced(self):
        self.click("RSAtwvhclfinancedropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwvhclfinanceoption_XPATH")
        time.sleep(1)

    def InputFiancerName(self,finname):
        self.type("RSAtwvhclfinanciername_XPATH",finname)

    def SelectFinancerType(self):
        self.click("RSAtwvhclfintypedropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwvhclfintypeoption_XPATH")
        time.sleep(1)

    def SelectPUC(self):
        self.click("RSAtwpucdropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwpucoption_XPATH")
        time.sleep(1)

    def InputPUCNo(self,pucno):
        self.type("RSAtwpucnumber_XPATH",pucno)

    def SelectPUCExpDate(self,pucexpdt):
        self.type("RSAtwpucexpdatepicker_XPATH",pucexpdt)

    def SelectPrevInsCompany(self):
        self.click("RSAtwprevinscomdropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwprevinscomoption_XPATH")
        time.sleep(1)

    def SelectPrevPolType(self):
        self.click("RSAtwprevpoltypedropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwprevpoltypeoption_XPATH")
        time.sleep(1)

    def InputPrevPolNo(self,prevpolno):
        self.type("RSAtwprevpolnumber_XPATH",prevpolno)

    def InputNomineeName(self,nomname):
        self.type("RSAtwnomineename_XPATH",nomname)

    def InputNomineeAge(self,nomage):
        self.type("RSAtwnomineeage_XPATH",nomage)

    def SelectNomineeRltn(self):
        self.click("RSAtwnomineerltndropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwnomineerltnoption_XPATH")
        time.sleep(1)

    def SelectCPACover(self):
        self.click("RSAtwcpacoverdropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwcpacoveroption_XPATH")
        time.sleep(1)

    def SelectPrefix(self):
        self.click("RSAtwcustomertitledropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwcustomertitleoption_XPATH")
        time.sleep(1)

    def InputName(self,fullname):
        self.type("RSAtwcustomername_XPATH",fullname)

    def SelectGender(self):
        self.click("RSAtwcustomergenderdropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwcustomergenderoption_XPATH")
        time.sleep(1)

    def SelectCustomerDOB(self):
        self.click("RSAtwdobdatepicker_XPATH")
        time.sleep(1)
        self.click("RSAtwdobmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwdobyearchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwdobmonthchoose_XPATH")
        time.sleep(1)
        self.click("RSAtwdobdaychoose_XPATH")
        time.sleep(1)

    def InputPAN(self,pan):
        self.type("RSAtwcustomerpan_XPATH",pan)

    def InputAadhar(self,aadhar):
        self.type("RSAtwcustomeraadhar_XPATH",aadhar)

    def InputAdd1(self,add1):
        self.type("RSAtwcustomeradd1_XPATH",add1)

    def InputAdd2(self,add2):
        self.type("RSAtwcustomeradd2_XPATH",add2)

    def InputPIN(self,pin):
        self.type("RSAtwcustomerpin_XPATH",pin)

    def SelectRegAddDropdown(self):
        self.click("RSAtwregadddropdown_XPATH")
        time.sleep(1)
        self.click("RSAtwSelectOption_XPATH")
        time.sleep(1)

    def InputRegAdd1(self,add1):
        self.type("RSAtwRegAddLine1_XPATH",add1)

    def InputRegAdd2(self,add2):
        self.type("RSAtwRegAddLine2_XPATH",add2)

    def InputRegPin(self,pin):
        self.type("RSAtwRegPinCode_XPATH",pin)

    def ClickProceed(self):
        self.click("RSAtwpolreviewpage_XPATH")
        rsatwpolicyreviewpage = RSATWPolicyReviewPage(self.driver)
        return rsatwpolicyreviewpage


