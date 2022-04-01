import time
from Pages.BasePage import BasePage
from Pages.FGNGTWPlanSelectionPage import FGNGTWPlanSelectionPage

class FGNGTWRegInfo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRegNumber(self,regno):
        self.type("FGNGtwinputregistrationno_XPATH",regno)

    def InputMobileNo(self,mobno):
        self.type("FGNGtwinputmobileno_XPATH",mobno)

    def ClickSubmit1(self):
        self.click("FGNGtwclicksubmit1_XPATH")

    def InputOwnerFname(self,firstname):
        self.type("FGNGtwinputownerfname_XPATH",firstname)

    def InputOwnerLname(self,lastname):
        self.type("FGNGtwinputownerlname_XPATH",lastname)

    def SelectCar(self,brand,model):
        self.click("FGNGtwselectcarbrandbutton_XPATH")
        time.sleep(2)
        self.type("FGNGtwinputcarbrand_XPATH",brand)
        time.sleep(1)
        self.click("FGNGtwselectcarbrandoption_XPATH")
        time.sleep(1)
        self.type("FGNGtwinputcarmodel_XPATH",model)
        time.sleep(1)
        self.click("FGNGtwselectcarmodeloption_XPATH")
        time.sleep(1)
        self.click("FGNGtwselectcmodelvariant_XPATH")
        time.sleep(1)

    def SelectManufacturingYr(self):
        self.click("FGNGtwselectmanufcyrdropdown_XPATH")
        time.sleep(1)
        self.click("FGNGtwselectmanufcyrvalue_XPATH")
        time.sleep(1)

    def InputRegDate(self):
        self.click("FGNGtwselectregdatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGtwregmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwregyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwregmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwregdaychoose_XPATH")
        time.sleep(1)

    def SelectPrevPolStus(self):
        self.click("FGNGtwselectprevpolstus_XPATH")

    def SelectPrevInsCom(self):
        self.click("FGNGtwprevinscomdropdown_XPATH")
        time.sleep(1)
        self.click("FGNGtwprevinscomoption_XPATH")
        time.sleep(1)

    def PrevPolcyExpDate(self):
        self.click("FGNGtwselectprevpoldatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGtwpolmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwpolyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwpolmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGtwpoldaychoose_XPATH")
        time.sleep(1)


    def SelectPrevPolNo(self,polno):
        self.type("FGNGtwprevpolno_XPATH",polno)

    def SelectIfPrevYrClaimTaken(self):
        self.click("FGNGtwprevyrclaimtaken_XPATH")

    def SelectNCBPercentage(self):
        self.click("FGNGtwselectncbperctg_XPATH")

    def ClickSubmit2(self):
        self.click("FGNGtwclicksubmit2_XPATH")
        time.sleep(5)
        planselectionpage = FGNGTWPlanSelectionPage(self.driver)
        return planselectionpage






