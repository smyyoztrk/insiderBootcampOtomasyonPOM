# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
import pytest
from pages.anasayfa import Anasayfa
from pages.pagebase import Pagebase
from pages.aramasonuclarisayfasi import AramaSonuclariSayfasi
from pages.urunsayfasi import Urunsayfasi
from pages.sepetsayfasi import Sepetsayfasi

class TestUrunAramaVeSepeteEkleme:
    urun = "samsung"
    sayfa_no = 2
    sayfa_no_url = f"page={sayfa_no}"
    sepete_eklendi_yazisi = "Sepete Eklendi"
    
    @pytest.mark.usefixtures("setUp")
    def test_urun_arama_ve_sepete_ekleme(self):
        pagebase= Pagebase(self.driver)
        anasayfa = Anasayfa(self.driver)
        aramasonuclarisayfasi = AramaSonuclariSayfasi(self.driver)
        urunsayfasi = Urunsayfasi(self.driver)
        sepetsayfasi = Sepetsayfasi(self.driver)

        # Ana sayfaya yönlendirme kontrolü
        assert self.base_url in pagebase.get_current_url(), "Ana sayfaya yönlendirme başarısız."

        # Ürün arama işlemi
        anasayfa.urun_arat(self.urun)

        # "samsung" ile ilgili sonuçların yer aldığını doğrula
        assert self.urun in pagebase.webelement_textini_ver(aramasonuclarisayfasi.SONUC_METNI).lower(), "Arama sonuçlarında 'samsung' kelimesi bulunamadı."

        # Ürünlerin listelendiği yerde "samsung" kelimesini kontrol et
        urun_listesi = aramasonuclarisayfasi.liste_ver(aramasonuclarisayfasi.URUN_LISTESI)
        assert any(self.urun in urun.text.lower() for urun in urun_listesi), "Arama sonuçlarında 'samsung' ürünü bulunamadı."
        
        # Arama sonuçlarından 2. sayfaya tıklanıp ve açılan sayfada 
        # 2. sayfanin şu an gösterimde olduğu onaylatılacak.
        aramasonuclarisayfasi.sayfa_sec(self.sayfa_no)
        current_url = pagebase.sayfa_url_ini_ver()
        # expected_url_fragment = f"page={self.sayfa_no}"
        assert self.sayfa_no_url in current_url, f"{self.sayfa_no}.sayfaya geçiş başarısız."

        # Üstten 5. Satır 1. Sütun içerisindeki ürüne tıklanacak. 
        # (ürün site yapısındaki anlık değişiklere göre farklılık gösterebilir)
        urunun_ismi = aramasonuclarisayfasi.urun_text_al_ve_tikla()

        #Ürün sayfasında olduğumuz doğrulanacak.
        # "Sepete Ekle" butonunun sayfada olup olmadığını ve 
        # Ürün adının sayfada görünür olup olmadığını kontrol et
        sepete_ekle_butonu_element = urunsayfasi.sepete_ekle_butonu_var_mi()
        assert sepete_ekle_butonu_element.is_displayed(), "'Sepete Ekle' butonu sayfada görünür değil."
        urun_detay_sayfasinde_urun_ismi = urunsayfasi.detay_sayfasinda_urun_ismini_ver()
        assert urunun_ismi == urun_detay_sayfasinde_urun_ismi, "Ürün ismi ürün detay sayfasında eşleşmiyor."

        # Ürün sepete eklenir. (sepete ekle butonuna tıklanır.)
        # urunsayfasi.urun_detay_sayfasindaki_sepete_ekle_butonuna_tikla()
        sepete_ekle_butonu_element.click()

        # Sepet sayfasında olduğumuz doğrulanır
        assert self.sepete_eklendi_yazisi in sepetsayfasi.sepete_eklendi_yazisini_ver(), "'Sepete Eklendi' mesajı sepet sayfasında bulunamadı."

        # Logo’ya tıklanarak ana sayfaya geri dönüş sağlanır
        sepetsayfasi.amazonun_logoya_tikla()

        #anasayfaya dönüldüğünü doğrula
        assert self.base_url in pagebase.get_current_url(), "Ana sayfaya dönüş başarısız."













    

        


