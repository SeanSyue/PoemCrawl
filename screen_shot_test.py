"""
login and get screen shot
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("C:\\Users\\Sean\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://crl.ptopenlab.com:8800/poem/sub?3")
driver.maximize_window()

driver.implicitly_wait(20)
driver.find_element_by_id("topictb").send_keys("发现")
driver.find_element_by_id("startButton").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'title')))
driver.get_screenshot_as_file("./screenshot/screenshot.png")

print(driver.current_url)

driver.quit()
