
import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#action.context_click(driver.find_element(By.XPATH, "//a[text()='Top']")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//a[text()='Reload']")).perform()
