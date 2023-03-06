from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ------------------------------- Creating client ------------------------------- #

option = Options()
option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\DEVELOPMENT\geckodriver.exe", options=option)

# ------------------------------- Accessing Webpage ------------------------------- #

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Finding the cookie
cookie = driver.find_element(By.ID, "cookie")

# Storing all the upgrades


