'''键盘操作'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()

    driver.find_element_by_id('kw').send_keys('空间站')
    sleep(1)
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
    driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
    sleep(1)
    driver.find_element_by_id('kw').send_keys(Keys.ENTER)

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()