'''常用api'''

from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    # 窗口最大化
    driver.maximize_window()
    # 获取窗口尺寸
    print(driver.get_window_size())

    driver.find_element_by_id('kw').send_keys('拼多多员工猝死')
    sleep(2)
    # 清除文本框内容
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('空间站')
    driver.find_element_by_id('su').click()

    sleep(1)
    # 百度百科
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    
    sleep(1)

    # 获取窗口handle
    handles = driver.window_handles
    print(handles)
    # 切换页面
    driver.switch_to.window(handles[1])
    sleep(1)
    
    driver.find_element_by_partial_link_text('讨论').click()
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()