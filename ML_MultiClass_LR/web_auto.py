import selenium
import select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import *
import time
import datetime

class web_auto():
    def __init__(self):
        self.driver = webdriver.Firefox()
    # logging
    def log(self, msg):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "LOG     : " + msg)

    def log_info(self, msg):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  " + "INFO    : " + str(msg))

    def log_error(self, msg):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  " + "ERROR   : " + msg)

    def log_cmd(self, msg):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  " + "CMD     : " + msg)

    def log_warning(self, msg):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  " + "WARNING : " + msg)

    def open_url(self, url):
        self.driver.get(url)

    def WaitForXpath(self, xpath, timeout=15):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            self.log_error("unable to find " + xpath)

    def enterTextInXpath(self, xpath, txt):
        # self.WaitForXpath(self.driver, xpath)
        elem = self.driver.find_element_by_xpath(xpath)
        elem.clear()
        elem.send_keys(txt)
        self.log_info("Entered " + txt + " in " + xpath)

    def clickXpath(self, xpath, sleep = 0):
        time.sleep(sleep)
        try:
            # element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.click()
            self.log_info("clicked on "+xpath)
        except TimeoutException:
            self.log_error("Click failed due to Time out error "+xpath)
            self.log_rerun()
            self.driver.quit()
            sys.exit()
        except ElementNotVisibleException:
            self.log_error("Element is not visible .. check the xpath")
            self.log_rerun()
            self.driver.quit()
            sys.exit()

    def GetTextInXpath(self, xpath, sleep=0):
        self.waitForXpath(xpath)
        time.sleep(sleep)
        elem = self.driver.find_element_by_xpath(xpath)
        self.log_info("found text  " + elem.text + " in " + xpath)
        return elem.text

    def CheckIfXpathExist(self, xpath, sleep=0):
        time.sleep(sleep)
        try:
            elem = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            self.log_info("xpath " + xpath + " does not exist")
            return False
        self.log_info("xpath " + xpath + " exists")
        return True

    def waitForXpath(self, xpath, timeout=15):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            self.log_error("unable to find " + xpath)

    def getHreffromXpath(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        return elem.get_attribute('href')

    def SendEnterKey(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        elem.send_keys(Keys.RETURN)