'''鼠标操作'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()

    # 单击
    # element = driver.find_element_by_link_text('新闻')
    # ActionChains(driver).click(element).perform()


    # 右击
    # element = driver.find_element_by_id('kw')
    # ActionChains(driver).context_click(element).perform()

    # 双击
    # element = driver.find_element_by_id('kw')
    # element.send_keys('未央区发现疫情')
    # sleep(1)
    # ActionChains(driver).double_click(element).perform()

    # 悬停
    element = driver.find_element_by_id('s-usersetting-top')
    ActionChains(driver).move_to_element(element).perform()
    sleep(1)
    driver.find_element_by_link_text('高级搜索').click()

except Exception as e:
    print(e)
finally:
    sleep(200)
    driver.quit()