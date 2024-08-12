from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.pagebase import Pagebase

class AramaSonuclariSayfasi(Pagebase):
    SONUC_METNI = (By.CSS_SELECTOR,"span[class='a-color-state a-text-bold']")
    URUN_LISTESI = (By.CSS_SELECTOR, "span.a-text-normal")
    SAYFALAR = (By.CSS_SELECTOR,"a[class*='s-pagination-item s-pagination'],span[class*='s-pagination-item s-pagination']")
    SECILEN_SAYAFADAKI_5_SUTUNDAKI_1_URUN = (By.CSS_SELECTOR,"div[data-component-type='s-search-result']:not([class*='AdHolder']):nth-child(25) h2 a")
    # SECILEN_SAYAFADAKI_5_SUTUNDAKI_1_URUN = (By.CSS_SELECTOR,"div[data-component-type='s-search-result']:not([class*='AdHolder']):nth-of-type(5) h2 a")
    
    def __init__(self,driver):
        self.driver = driver
    def liste_ver(self,locator):
        return self.wait_element_visibility_of_all(10,locator)
    def sayfa_sec(self,sayfa_no):
        action = ActionChains(self.driver)
        sayfa_numaralari_liste = self.wait_elements_of_presence(30,self.SAYFALAR)
        action.move_to_element(sayfa_numaralari_liste[sayfa_no]).click().perform()
        sleep(2)
    def urun_text_al_ve_tikla(self):
        secilen_sayfadaki_5_sutundaki_urun = self.wait_element_of_presence(30,self.SECILEN_SAYAFADAKI_5_SUTUNDAKI_1_URUN)
        action = ActionChains(self.driver)
        urunun_ismi = secilen_sayfadaki_5_sutundaki_urun.text
        action.move_to_element(secilen_sayfadaki_5_sutundaki_urun).click().perform()
        return urunun_ismi

