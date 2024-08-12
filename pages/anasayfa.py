from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.pagebase import Pagebase

class Anasayfa(Pagebase):
    ARMAMA_MOTORU = (By.ID,"twotabsearchtextbox")
    
    
    def __init__(self,driver):
        self.driver = driver
    def urun_arat(self,urun):
        arama_motoru = self.wait_element_visibility_of(10,self.ARMAMA_MOTORU)
        arama_motoru.send_keys(urun)
        arama_motoru.send_keys(Keys.ENTER)
    
        
    

        
    

        