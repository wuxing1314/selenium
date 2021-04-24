from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    # 窗口最大化
    driver.maximize_window()

    # 模拟id定位
    #                             //*[@id="kw"]
    # driver.find_element_by_xpath('//input[@id="kw"]').send_keys('油泼面')
    # 模拟name定位
    # driver.find_element_by_xpath('//*[@name="wd"]').send_keys('油泼面')
    # 模拟class定位
    # driver.find_element_by_xpath('//*[@class="s_ipt"]').send_keys('油泼面')

    # driver.find_element_by_xpath('//*[@maxlength="255"]').send_keys('油泼面')

    # sleep(1)
    # driver.find_element_by_xpath('//input[@id="su"]').click()

    # 模拟link_text定位 -- 精确定位
    # driver.find_element_by_xpath('//*[text()="新闻"]').click()
    # driver.find_element_by_xpath('//*[text()="设置"]').click()

    # 模拟partial_link_text定位 -- 模糊定位
    driver.find_element_by_xpath('//*[contains(text(),"新娘父亲")]').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()