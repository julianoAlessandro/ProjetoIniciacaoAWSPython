from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
import os
import time
import pyautogui as py

class SeleniumAutomatizar:
         
      
    def get_driver(self, url):       
        chrome_options = Options()
        #chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized') 
        chrome_options.add_argument('--start-fullscreen')
        #chrome_options.add_argument('--single-process')
        chrome_options.add_argument("--user-data-dir=C:\\Users\\Juliano\\AppData\\Local\\Google\\Chrome\\User Data")

        # Construa o caminho para o chromedriver.exe
        driver_path = os.path.join(os.path.dirname(__file__), '..', 'DriverGoogle', 'chromedriver.exe')

        # Crie o objeto Service corretamente
        serv = ChromeService(driver_path)

        # Inicialize o driver usando o caminho e as opções fornecidas
        driver = webdriver.Chrome(options=chrome_options, service=serv)
        driver.get(url)
        for numero in range(1,6):
            driver.find_element(By.XPATH , f'//*[@id="parent-fieldname-text"]/ul[{numero}]/li/a').click()
            time.sleep(4)
        time.sleep(60)

        for numero in range(6,11):
            driver.find_element(By.XPATH , f'//*[@id="parent-fieldname-text"]/ul[{numero}]/li/a').click()
            time.sleep(4)


        time.sleep(140)

      
      

        
    
        
          
        
    
    

       
     
         
       
   