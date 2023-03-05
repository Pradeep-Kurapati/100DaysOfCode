from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r"C:\DEVELOPMENT\geckodriver.exe", options=options)
driver.get(
    'https://www.amazon.in/OnePlus-Bluetooth-Wireless-co-Created-Cancellation/dp/B0BRSLXGCN/?_encoding=UTF8&pd_rd_w'
    '=yVj68&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96'
    '&pf_rd_r=7V7FB5S0JQTJX068TD3R&pd_rd_wg=foPVv&pd_rd_r=875ac722-e670-44bb-aa2a-d18aa4d34d69&ref_'
    '=pd_gw_ci_mcx_mr_hp_atf_m')

price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_text = price_element.text
print(price_text)


