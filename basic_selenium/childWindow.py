from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == (driver.find_element(By.TAG_NAME, "h3").text)








driver.find_element(By.ID, "country").send_keys("rom")
wait = WebDriverWait(driver,10).until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "Romania"))
)



driver.find_element(By.LINK_TEXT, "Romania").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

