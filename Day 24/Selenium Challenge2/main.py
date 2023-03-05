from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\DEVELOPMENT\geckodriver.exe", options=option)

driver.get('https://web.archive.org/web/20190201181142/http://secure-retreat-92358.herokuapp.com:80/')
first = driver.find_element(By.NAME, "fName")
first.click()
first.send_keys("Pradeep")

last = driver.find_element(By.NAME, "lName")
last.click()
last.send_keys("Kurapati")

mail = driver.find_element(By.NAME, "email")
mail.click()
mail.send_keys("pradeep0@gmail.com")

signup = driver.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-block")
signup.click()


