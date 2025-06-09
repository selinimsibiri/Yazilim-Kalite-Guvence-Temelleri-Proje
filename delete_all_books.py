from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://demoqa.com/login")
driver.find_element(By.ID, "userName").send_keys("marmarauni")
driver.find_element(By.ID, "password").send_keys("Mar123**")
driver.find_element(By.ID, "login").click()

time.sleep(5)

try:
    delete_all_button = driver.find_element(By.XPATH, "//button[text()='Delete All Books']")
    delete_all_button.click()

    time.sleep(3)

    ok_button = driver.find_element(By.ID, "closeSmallModal-ok")
    ok_button.click()

except Exception as e:
    print("Hata oluştu:", e)

time.sleep(2)
driver.save_screenshot("after_delete_all_books.png")
driver.quit()
