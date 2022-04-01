import time

from Pages.BasePage import BasePage
from Pages.QuotesPage import QuotesPage

class InsuredDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def SelectMemberSelf(self):
        self.click("self_XPATH")

    def InputAge(self,selfage):
        self.type("age_XPATH",selfage)

    def ClickNext(self):
        self.click("next2_XPATH")
        quotespage = QuotesPage(self.driver)
        return quotespage
