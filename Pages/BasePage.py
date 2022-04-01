import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from Utilities.LogUtil import Logger
from Utilities import configReader


log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on an Element " + str(locator))

    def clear(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).clear()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).clear()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).clear()
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).clear()
        log.logger.info("Clicking on an Element " + str(locator))

    def clickIndex(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(By.XPATH, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_elements(By.CSS_SELECTOR, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(By.ID, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_elements(By.CLASS_NAME, configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on an Element " + str(locator) + "with index : " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(value))

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element " + str(locator) + ":" + " " + text)
        elif str(locator).endswith("_CSS"):
            text = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element " + str(locator) + ":" + " " + text)
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element " + str(locator) + ":" + " " + text)
        elif str(locator).endswith("_CLASS_NAME"):
            text = self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).text
            log.logger.info("Getting text from an element " + str(locator) + ":" + " " + text)
        return text


    def SelectDOB(self, locator):
        if str(locator).endswith("_XPATH"):
            a = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
            a.click()
            a.send_keys(Keys.UP)
            time.sleep(2)
            a.send_keys(Keys.ENTER)



    def SelectSumInsured(self, sumvalue):
        sumdropdown = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname = 'income']"))
        suminsured = sumdropdown.select_by_visible_text(sumvalue)
        return suminsured

    def Scroll(self):
        self.driver.execute_script("window.scrollTo(0,1000)")



