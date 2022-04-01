import time

from Pages.BasePage import BasePage
from Pages.RSAFW_SelectRTOPage import RSAFWSelectRTO


class RSAFWSelectVehiclePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def SelectVehicleInfo(self):
        self.click("RSAfwselectvhclinfo_XPATH")

    def SelectVehicleBrandName(self,model):
        self.type("RSAfwsearchbrand_XPATH",model)

    def SelectBrandMaruti(self):
        self.click("RSAfwselectbrandpage1_XPATH")

    def ClickNext1(self):
        self.click("RSAfwselectmodelpage2_XPATH")

    def SelectVehicleModel1(self,brand):
        self.type("RSAfwselectmodel_XPATH",brand)
        time.sleep(2)
        self.click("RSAfwselectbrand_XPATH")
        time.sleep(1)

    def ClickNext2(self):
        self.click("RSAfwclickmodelpage3_XPATH")

    def SelectVehicleModel2(self):
        self.click("RSAfwselectmodel800_XPATH")

    def ClickNext3(self):
        self.click("RSAfwselectrtopage_XPATH")
        rsafwselectrtopage = RSAFWSelectRTO(self.driver)
        return rsafwselectrtopage


