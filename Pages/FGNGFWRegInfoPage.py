import time
from Pages.BasePage import BasePage
from Pages.FGNGFWPlanSelectionPage import FGNGFWPlanSelectionPage


class FGNGFWRegInfo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def InputRegNumber(self,regno):
        self.type("FGNGfwinputregistrationno_XPATH",regno)

    def InputMobileNo(self,mobno):
        self.type("FGNGfwinputmobileno_XPATH",mobno)

    def ClickSubmit1(self):
        self.click("FGNGfwclicksubmit1_XPATH")

    def InputOwnerFname(self,firstname):
        self.type("FGNGfwinputownerfname_XPATH",firstname)

    def InputOwnerLname(self,lastname):
        self.type("FGNGfwinputownerlname_XPATH",lastname)

    def SelectCar(self,brand,model):
        self.click("FGNGfwselectcarbrandbutton_XPATH")
        time.sleep(2)
        self.type("FGNGfwinputcarbrand_XPATH",brand)
        time.sleep(1)
        self.click("FGNGfwselectcarbrandoption_XPATH")
        time.sleep(1)
        self.type("FGNGfwinputcarmodel_XPATH",model)
        time.sleep(1)
        self.click("FGNGfwselectcarmodeloption_XPATH")
        time.sleep(1)
        self.click("FGNGfwselectcmodelvariant_XPATH")
        time.sleep(1)

    def SelectManufacturingYr(self):
        self.click("FGNGfwselectmanufcyrdropdown_XPATH")
        time.sleep(1)
        self.click("FGNGfwselectmanufcyrvalue_XPATH")
        time.sleep(1)

    def InputRegDate(self):
        self.click("FGNGfwselectregdatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGfwregmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwregyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwregmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwregdaychoose_XPATH")
        time.sleep(1)

    def SelectPrevPolStus(self):
        self.click("FGNGfwselectprevpolstus_XPATH")

    def SelectPrevInsCom(self):
        self.click("FGNGfwprevinscomdropdown_XPATH")
        time.sleep(1)
        self.click("FGNGfwprevinscomoption_XPATH")
        time.sleep(1)

    def PrevPolcyExpDate(self):
        self.click("FGNGfwselectprevpoldatepicker_XPATH")
        time.sleep(1)
        self.click("FGNGfwpolmonthyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwpolyearchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwpolmonthchoose_XPATH")
        time.sleep(1)
        self.click("FGNGfwpoldaychoose_XPATH")
        time.sleep(1)


    def SelectPrevPolNo(self,polno):
        self.type("FGNGfwprevpolno_XPATH",polno)

    def SelectIfPrevYrClaimTaken(self):
        self.click("FGNGfwprevyrclaimtaken_XPATH")

    def SelectNCBPercentage(self):
        self.click("FGNGfwselectncbperctg_XPATH")

    def ClickSubmit2(self):
        self.click("FGNGfwclicksubmit2_XPATH")
        time.sleep(5)
        planselectionpage = FGNGFWPlanSelectionPage(self.driver)
        return planselectionpage






