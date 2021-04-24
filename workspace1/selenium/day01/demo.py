


from selenium import webdriver
from time import sleep
import requests

try:
    driver = webdriver.Chrome()
    driver.get('http://jandan.net/pic/MjAyMTAxMDQtMTk3#comments')
    driver.maximize_window()
    divs = driver.find_elements_by_xpath('//div/div/div[2]/p/div')
    print(divs)
    for div in divs:
        div.click()
except Exception as e:
    print(e)
finally:
    driver.quit()