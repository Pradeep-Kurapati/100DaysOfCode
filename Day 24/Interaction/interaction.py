from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

option = Options()
option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\DEVELOPMENT\geckodriver.exe", options=option)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
count = driver.find_element(By.CSS_SELECTOR, ".mp-box #articlecount a")
print(count.text)
