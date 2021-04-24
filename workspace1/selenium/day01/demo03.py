
from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('D:\workspace\selenium\day01\sample.html')

    '''
    xpath定位
    xml 路径定位
    '''
    '''绝对路径'''
    # driver.find_element_by_xpath('/html/body/div/ul/li[1]/a').click()
    '''相对路径'''
    driver.find_element_by_xpath('//div[@id="abc"]/ul/li[1]/a').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()