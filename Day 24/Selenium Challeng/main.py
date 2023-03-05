from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\DEVELOPMENT\geckodriver.exe", options=option)

driver.get('https://www.python.org/')

times_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
times = [x.text for x in times_element]

events_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li a")
events = [x.text for x in events_list]

final_dictionary = {x: y for x, y in zip(times, events)}
print(final_dictionary)

driver.quit()

