import time

from Pages.BasePage import BasePage
from Pages.RSATW_SelectRTOPage import RSATWSelectRTO
class RSATWSelectVehiclePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def SelectVehicleInfo(self):
        self.click("RSAtwselectvhclinfo_XPATH")

    def SelectVehicleBrand(self,brand):
        self.type("RSAtwselectbrand_XPATH",brand)
        time.sleep(2)
        self.click("RSAtwselectbrandbajaj_XPATH")

    def ClickNext1(self):
        self.click("RSAtwselectmodelpage_XPATH")

    def InputVehicleModel(self,model):
        self.type("RSAtwinputmodel_CSS",model)

    def SelectVehicleModel135(self):
        self.click("RSAtwselectmodel_XPATH")

    def ClickNext2(self):
        self.click("RSAtwclickmodelpage_XPATH")

    def SelectVehicleModel(self):
        self.click("RSAtwselectmodel135_XPATH")

    def ClickNext3(self):
        self.click("RSAtwselectrtopage_XPATH")
        rsatwselectrtopage = RSATWSelectRTO(self.driver)
        return rsatwselectrtopage


