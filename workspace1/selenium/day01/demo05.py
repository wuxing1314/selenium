from selenium import webdriver
from time import sleep

'''css定位'''

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element_by_css_selector('#kw').send_keys('新娘父亲')
driver.find_element_by_css_selector('#su').click()
# #\33 
#con-ar > div > div > div > table > tbody:nth-child(1) > tr:nth-child(10) > td.toplist1-td.opr-toplist1-link > a
sleep(2)
driver.close()