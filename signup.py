from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/register")

wait = WebDriverWait(driver, 10)

first_name = wait.until(EC.element_to_be_clickable((By.ID, "firstname")))
first_name.send_keys("Selin")

last_name = driver.find_element(By.ID, "lastname")
last_name.send_keys("Yilmaz")

username = driver.find_element(By.ID, "userName")
username.send_keys("Selin123")

password = driver.find_element(By.ID, "password")
password.send_keys("Sifre123!")


# reCAPTCHA iframe içine gömülü olur, önce iframe’e geçmek lazım
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))

captcha_checkbox = driver.find_element(By.ID, "recaptcha-anchor")
captcha_checkbox.click()

driver.switch_to.default_content()

register_button = driver.find_element(By.ID, "register")
register_button.click()

time.sleep(5)

driver.save_screenshot("signup_result.png")

try:
    success_message = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    print("Kayıt başarılı, mesaj:", success_message.text)
except:
    print("Kayıt başarısız ya da mesaj bulunamadı.")

driver.quit()
