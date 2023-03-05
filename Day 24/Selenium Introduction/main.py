# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# driver.get('https://www.amazon.in/JBL-Cancellation-Playtime-Adjustable-Bluetooth/dp/B09HGR1DVC/?_encoding=UTF8'
#            '&pd_rd_w=xGelI&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd'
#            '-563ae12c2d96&pf_rd_r=A7C3BTE5EK08R2TZR4HS&pd_rd_wg=2donN&pd_rd_r=6157d6c0-e5a9-4c71-b8c1-c36500af3d45'
#            '&ref_=pd_gw_ci_mcx_mr_hp_atf_m')
#
# price = driver.find_element(by="class", value="a-price-whole")
# print(price.text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.amazon.in/JBL-Cancellation-Playtime-Adjustable-Bluetooth/dp/B09HGR1DVC/?_encoding=UTF8'
           '&pd_rd_w=xGelI&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd'
           '-563ae12c2d96&pf_rd_r=A7C3BTE5EK08R2TZR4HS&pd_rd_wg=2donN&pd_rd_r=6157d6c0-e5a9-4c71-b8c1-c36500af3d45'
           '&ref_=pd_gw_ci_mcx_mr_hp_atf_m')

price = driver.find_element(By.CLASS_NAME, "a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_killswitch_csa_logger_372963-c a-aui_launch_2021_ally_fixes_392482-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate")
print(price.text)

