from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Pagebase:
    def __init__(self,driver):
        self.driver = driver
    def wait_element_visibility_of(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_element_located(locator))
        return element
    def wait_element_visibility_of_all(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.visibility_of_all_elements_located(locator))
        return element
    def webelement_textini_ver(self,locator):
        return self.wait_element_visibility_of(20,locator).text
    def sayfa_url_ini_ver(self):
        return self.driver.current_url
    def wait_element_of_presence(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(locator))
        return element
    def wait_elements_of_presence(self,seconds,locator):
        element = WebDriverWait(self.driver,seconds).until(EC.presence_of_all_elements_located(locator))
        return element
    def get_current_url(self):
        return self.driver.current_url
    