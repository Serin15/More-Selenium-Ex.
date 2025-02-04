import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(2)


driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    #print(productName)
    if productName == "Blackberry":
        product.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()


driver.find_element(By.ID, "country").send_keys("rom")
wait = WebDriverWait(driver,10).until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "Romania"))
)



driver.find_element(By.LINK_TEXT, "Romania").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
success_text = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible'] strong").text

assert "Success!" in success_text
print(success_text)