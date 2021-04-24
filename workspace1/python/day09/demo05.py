from selenium import webdriver
import time

# 创建chrome浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.baidu.com')
time.sleep(3)
# 关闭浏览器
driver.close()