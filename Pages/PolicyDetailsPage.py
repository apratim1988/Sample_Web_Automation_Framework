import time

from Pages.BasePage import BasePage
from Pages.PropDetailsPage import PropDetailsPage


class PolicyDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ConfirmTenure(self):
        self.click("next4_XPATH")
        propdetailspage = PropDetailsPage(self.driver)
        return propdetailspage


