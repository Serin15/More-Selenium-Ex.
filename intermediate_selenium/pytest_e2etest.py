import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

def test_checkout(driver):
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    driver.find_element(By.ID, "country").send_keys("rom")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Romania")))
    driver.find_element(By.LINK_TEXT, "Romania").click()

    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()


    success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in success_text