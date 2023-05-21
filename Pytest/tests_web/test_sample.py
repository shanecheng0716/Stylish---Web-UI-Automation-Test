import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging
import allure
from allure_commons.types import AttachmentType

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
options = Options() 
#options.add_argument('--headless')  # 啟動Headless 無頭
options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome()
driver.maximize_window()

def test_sample():
      try:
            driver.get('http://54.201.140.239/')
            logger.info("Opening the website.")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header__logo")))
            logo = driver.find_element(By.CSS_SELECTOR, ".header__logo")
            assert logo.is_displayed(), "Stylish logo is not displayed."
            logger.info("Stylish logo is displayed.")
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
      finally:
           driver.quit()