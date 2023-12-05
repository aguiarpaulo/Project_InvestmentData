from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = 'https://statusinvest.com.br/acoes/busca-avancada'

print('getting web url')
driver = webdriver.Chrome()
driver.get(URL)
sleep(1)

print('Searching Elements')
button_search = driver.find_elements(By.CLASS_NAME,
    'find'
)
if button_search:
    # Click on the first element in the list
    button_search[0].click()
else:
    print("No elements found with the specified criteria.")
sleep(2)

#print('Closing Adds')
#button_close = driver.find_elements(By.CLASS_NAME,
#    'btn-close'
#)
#if button_close:
#    # Click on the first element in the list
#    button_close[0].click()
#else:
#    print("No elements found with the specified criteria.")
#sleep(2)

print('Download Elements')
button_download = driver.find_elements(By.CLASS_NAME,
    'btn-download'
)
if button_download:
    # Click on the first element in the list
    button_download[0].click()
else:
    print("No elements found with the specified criteria.")
sleep(2)