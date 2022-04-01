import time

from Pages.BasePage import BasePage

from Pages.HealthInsurancePage import HealthInsurancePage
from Pages.RSATW_SelectVehiclePage import RSATWSelectVehiclePage
from Pages.RSAFW_SelectVehiclePage import RSAFWSelectVehiclePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def SelectHealth(self):
        self.click("health_XPATH")
        healthinsuranepage = HealthInsurancePage(self.driver)
        return healthinsuranepage

    def SelectRSATW(self):
        self.click("RSAtwowheeler_XPATH")
        rsatwselectvehiclepage = RSATWSelectVehiclePage(self.driver)
        return rsatwselectvehiclepage

    def SelectRSAFW(self):
        self.click("RSAfourwheeler_XPATH")
        rsafwselectvehiclepage = RSAFWSelectVehiclePage(self.driver)
        return rsafwselectvehiclepage




