from selenium import webdriver
from time import sleep


try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    '''link_text定位,精确匹配'''
    # 定位 "贴吧" ,并点击
    # driver.find_element_by_link_text('贴吧').click()

    '''partial_link_text定位,模糊匹配'''
    driver.find_element_by_partial_link_text('贴').click()  
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()