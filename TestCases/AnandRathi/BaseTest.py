import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from Utilities.waitelements import *
import sys
sys.path.insert(0, './AnandRathi')
from Utilities.waitelements import *


# @pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("selenium_driver")
@pytest.mark.usefixtures("log_on_failure")
class BaseTest:

    # RSA Health Explicit Waits

    def VerifyPresence_PinCodeTextBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.PinCodeTextBox)))
        return element

    def VerifyPresence_SelfCheckBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.SelfCheckBox)))
        return element

    def VerifyPresence_SelfAgeTextBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.SelfAgeTextBox)))
        return element

    def VerifyPresence_ShareQuotesButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.ShareQuotesButton)))
        return element

    def VerifyPresence_SelectAllQuotesCheckBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.SelectAllQuotesCheckBox)))
        return element

    def VerifyPresence_NameTextBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.NameTextBox)))
        return element

    def VerifyPresence_CloseButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.CloseButton)))
        return element

    def VerifyPresence_RSAPlanSelectButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.RSAPlanSelectButton)))
        return element

    def VerifyPresence_NextButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.NextButton)))
        return element

    def VerifyPresence_FirstNameTextBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.FirstNameTextBox)))
        return element

    def VerifyPresence_SelectOccupationOption(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.SelectOccupationOption)))
        return element

    def VerifyPresence_MaritalStatusOption(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.MaritalStatusOption)))
        return element

    def VerifyPresence_QualificationOption(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.QualificationOption)))
        return element

    def VerifyPresence_TPANameOption(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.TPANameOption)))
        return element

    def VerifyPresence_SelfFirstNameTextBox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.SelfFirstNameTextBox)))
        return element

    def VerifyPresence_NomRelationOption(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WaitElements.NomRelationOption)))
        return element

    def VerifyPresence_QuestPageButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.QuestPageButton)))
        return element

    def VerifyPresence_NameValidationText(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WaitElements.NameValidationText)))
        return element

    def VerifyPresence_ShareButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.ShareButton)))
        return element

    # RSA Two Wheeler Explicit Waits

    def VerifyPresence_RSATWOption(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWOption)))
        return element

    def VerifyPresence_RSATWVhclInfoOption(self):
        element = WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWVhclInfoOption)))
        return element

    def VerifyPresence_RSATWSelectBrandButton(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWSelectBrandButton)))
        return element

    def VerifyPresence_RSATWInputBrndTxtBox(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWInputBrndTxtBox)))
        return element

    def VerifyPresence_RSATWInputRTOTextBox(self):
        element = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWInputRTOTextBox)))
        return element

    def VerifyPresence_RSATWPrevPolStsTextBox(self):
        element = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWPrevPolStsTextBox)))
        return element

    def VerifyPresence_RSATWShareQuotesButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWShareQuotesButton)))
        return element

    def VerifyPresence_RSATWShareQuotesNameTxtBox(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWShareQuotesNameTxtBox)))
        return element

    def VerifyPresence_RSATWRSAComButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWRSAComButton)))
        return element

    def VerifyPresence_RSATWProceedButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWProceedButton)))
        return element

    def VerifyPresence_RSATWVhclOwnrshpChngedOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWVhclOwnrshpChngedOption)))
        return element

    def VerifyPresence_RSATWFinancedOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWFinancedOption)))
        return element

    def VerifyPresence_RSATWFinancerTypeOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWFinancerTypeOption)))
        return element

    def VerifyPresence_RSATWPUCOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWPUCOption)))
        return element

    def VerifyPresence_RSATWPrevInsComOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWPrevInsComOption)))
        return element

    def VerifyPresence_RSATWPrevPolTypeOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWPrevPolTypeOption)))
        return element

    def VerifyPresence_RSATWNomineeRltnOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWNomineeRltnOption)))
        return element

    def VerifyPresence_RSATWCPACoverOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWCPACoverOption)))
        return element

    def VerifyPresence_RSATWPrefixOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWPrefixOption)))
        return element

    def VerifyPresence_RSATWGenderOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWGenderOption)))
        return element

    def VerifyPresence_RSATWProceedToReviewPageButton(self):
        element = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWProceedToReviewPageButton)))
        return element

    def VerifyPresence_RSATWVerifyRegNoText(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWVerifyRegNoText)))
        return element

    def VerifyPresence_RSATWFinalShareButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSATWFinalShareButton)))
        return element


    # RSA four Wheeler Explicit Waits

    def VerifyPresence_RSAFWOption(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWOption)))
        return element

    def VerifyPresence_RSAFWVhclInfoOption(self):
        element = WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWVhclInfoOption)))
        return element

    def VerifyPresence_RSAFWSelectBrandButton(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWSelectBrandButton)))
        return element

    def VerifyPresence_RSAFWInputBrndTxtBox(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWInputBrndTxtBox)))
        return element

    def VerifyPresence_RSAFWInputRTOTextBox(self):
        element = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWInputRTOTextBox)))
        return element

    def VerifyPresence_RSAFWPrevPolStsTextBox(self):
        element = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWPrevPolStsTextBox)))
        return element

    def VerifyPresence_RSAFWShareQuotesButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWShareQuotesButton)))
        return element

    def VerifyPresence_RSAFWShareQuotesNameTxtBox(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWShareQuotesNameTxtBox)))
        return element

    def VerifyPresence_RSAFWRSAComButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWRSAComButton)))
        return element

    def VerifyPresence_RSAFWProceedButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWProceedButton)))
        return element

    def VerifyPresence_RSAFWVhclOwnrshpChngedOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWVhclOwnrshpChngedOption)))
        return element

    def VerifyPresence_RSAFWFinancedOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWFinancedOption)))
        return element

    def VerifyPresence_RSAFWFinancerTypeOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWFinancerTypeOption)))
        return element

    def VerifyPresence_RSAFWPUCOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWPUCOption)))
        return element

    def VerifyPresence_RSAFWPrevInsComOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWPrevInsComOption)))
        return element

    def VerifyPresence_RSAFWPrevPolTypeOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWPrevPolTypeOption)))
        return element

    def VerifyPresence_RSAFWNomineeRltnOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWNomineeRltnOption)))
        return element

    def VerifyPresence_RSAFWCPACoverOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWCPACoverOption)))
        return element

    def VerifyPresence_RSAFWPrefixOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWPrefixOption)))
        return element

    def VerifyPresence_RSAFWGenderOption(self):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWGenderOption)))
        return element

    def VerifyPresence_RSAFWProceedToReviewPageButton(self):
        element = WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWProceedToReviewPageButton)))
        return element

    def VerifyPresence_RSAFWVerifyRegNoText(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWVerifyRegNoText)))
        return element

    def VerifyPresence_RSAFWFinalShareButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WaitElements.RSAFWFinalShareButton)))
        return element
