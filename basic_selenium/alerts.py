import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

name = "Serin"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert name in alertText
alert.accept()