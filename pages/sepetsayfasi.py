from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.pagebase import Pagebase

class Sepetsayfasi(Pagebase):
    SEPETE_EKLENDİ_YAZISI = (By.CSS_SELECTOR,"h1[class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")
    AMAZON_LOGO = (By.CSS_SELECTOR,"a[class='nav-logo-link nav-progressive-attribute']")

    def __init__(self,driver):
        self.driver = driver
    def sepete_eklendi_yazisini_ver(self):
        return self.webelement_textini_ver(self.SEPETE_EKLENDİ_YAZISI)
    def amazonun_logoya_tikla(self):
        self.wait_element_of_presence(20,self.AMAZON_LOGO).click()
    
        
