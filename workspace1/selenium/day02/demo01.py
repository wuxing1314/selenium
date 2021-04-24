'''实现滚动操作'''
from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()

    driver.find_element_by_xpath('//*[contains(text(),"河北新增14例")]').click()
    sleep(1)

    # 切换窗口
    driver.switch_to.window(driver.window_handles[1])

    # 定位目标元素
    element = driver.find_element_by_link_text('帮助')
    # 滚动页面的JavaScript代码
    js = 'arguments[0].scrollIntoView();'
    # 滚动到目标元素所在的位置
    driver.execute_script(js,element)

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()