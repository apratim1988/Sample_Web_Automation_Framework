import time

from Pages.BasePage import BasePage
from Pages.PolictReviewPage import PolictReviewPage

class QuestionariesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def landing_page(self):
        pass

    def ClickNext(self):
        self.click("next7_XPATH")
        policyreviewpage = PolictReviewPage(self.driver)
        return policyreviewpage










