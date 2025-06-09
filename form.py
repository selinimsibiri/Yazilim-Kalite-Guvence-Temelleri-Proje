from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://demoqa.com/automation-practice-form")
print("📝 Form sayfasına geçildi.")
time.sleep(2)

driver.execute_script("document.querySelector('footer').remove();")
driver.execute_script("document.getElementById('fixedban').remove();")

driver.find_element(By.ID, "firstName").send_keys("Selin")
driver.find_element(By.ID, "lastName").send_keys("Yıldız")
driver.find_element(By.ID, "userEmail").send_keys("selin@example.com")

gender = driver.find_element(By.XPATH, "//label[text()='Female']")
gender.click()

driver.find_element(By.ID, "userNumber").send_keys("5551234567")

subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Math")
subjects_input.send_keys("\n")

driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Music']").click()

driver.find_element(By.ID, "currentAddress").send_keys("Istanbul, Turkey")

driver.execute_script("window.scrollBy(0, 300)")  # Alana ulaşmak için scroll
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys("\n")

driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys("\n")

time.sleep(3)

driver.find_element(By.ID, "submit").click()
time.sleep(2)

driver.save_screenshot("form_submitted.png")
time.sleep(2) 

driver.quit()