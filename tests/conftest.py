from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# @pytest.fixture(scope="class") # class başında bir kere çalışır tüm testler koşar kapanır.
@pytest.fixture() # her test için çalışır
def setUp(request):
    base_url = 'www.amazon.com.tr/'
    chrome_options = Options()
    chrome_options.add_argument("--disable-cookies") # firefox 'da başka birsey kullanılıyor
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")  # Reklam engelleyici uzantılar için
    # service = Service('C:\Users\Kullanıcı\.wdm\drivers\chromedriver\win64\120.0.6099.71\chromedriver-win32\chromedriver.exe')

    
    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amazon.com.tr/")
    driver.delete_all_cookies()
    driver.maximize_window()
    request.cls.base_url = base_url
    request.cls.driver = driver # bu fixture kullanan class lar driver çağırdığında driver = webdriver.Chrome() u ver dedik.  
    driver.implicitly_wait(10)
    yield
    driver.quit()



