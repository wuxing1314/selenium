from selenium import webdriver
from time import sleep

try:
    driver =  webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()

    sleep(2)    
    # 刷新
    driver.refresh()
    sleep(2)

    driver.find_element_by_id('kw').send_keys('空间站')

    sleep(2)
    # 后退
    driver.back()
    sleep(2)
    # 前进
    driver.forward()
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()