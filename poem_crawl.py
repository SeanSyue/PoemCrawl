"""
An incomplete poem crawl with `selenium`
"""
# -------------------------------------------------------------------------------------#
# Type in
# -------------------------------------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\Sean\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://crl.ptopenlab.com:8800/poem/sub?3")

driver.implicitly_wait(20)
driver.find_element_by_id("topictb").send_keys("发现")
driver.find_element_by_id("startButton").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'title')))
url = driver.current_url
driver.quit()

# -------------------------------------------------------------------------------------#
# Get character
# -------------------------------------------------------------------------------------#
import urllib.request

res = urllib.request.urlopen(url).read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(res, from_encoding="RTF-8")

body = soup.body
print(body.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.contents)
print(body.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.contents[1])
