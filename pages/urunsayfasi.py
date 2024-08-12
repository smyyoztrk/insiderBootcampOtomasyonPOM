from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.pagebase import Pagebase

class Urunsayfasi(Pagebase):
    SEPETE_EKLE_BUTONU = (By.CSS_SELECTOR,"input[id='add-to-cart-button']")
    URUN_DETAY_SAYFASINDA_URUN_BASLIGI = (By.ID,"title")

    def __init__(self,driver):
        self.driver = driver
    def sepete_ekle_butonu_var_mi(self):
        return self.wait_element_of_presence(20,self.SEPETE_EKLE_BUTONU)
    def detay_sayfasinda_urun_ismini_ver(self):
        return self.wait_element_of_presence(20,self.URUN_DETAY_SAYFASINDA_URUN_BASLIGI).text
    def urun_detay_sayfasindaki_sepete_ekle_butonuna_git_ve_tikla(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.sepete_ekle_butonu_var_mi()).click().perform()

