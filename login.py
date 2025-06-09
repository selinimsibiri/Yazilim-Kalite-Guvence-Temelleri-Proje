from pandas import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/login")

username_input = driver.find_element(By.ID, "userName")
username_input.send_keys("Selin123")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Sifre123")

driver.save_screenshot("login_result.png")

login_button = driver.find_element(By.ID, "login")
login_button.click()

time.sleep(2)

driver.save_screenshot("login_result2.png")

try:
    welcome_message = driver.find_element(By.ID, "userName-value")
    print("Giriş başarılı, kullanıcı:", welcome_message.text)
except:
    print("Giriş başarısız veya sayfa değişmedi.")


time.sleep(3)
driver.quit()
