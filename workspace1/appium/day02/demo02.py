from appium import webdriver
from time import sleep


# 基本配置
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

driver.find_element_by_accessibility_id('百度文库').click()
sleep(5)

'''点击 同意并继续'''
# 使用class定位
# elements = driver.find_elements_by_class_name('android.widget.TextView')
# elements[-1].click()

# 使用text定位
# 精确匹配
# driver.find_element_by_xpath('//*[@text="同意并继续"]').click()
# 模糊匹配
# driver.find_element_by_xpath('//*[contains(@text,"同意并继")]').click()

# 使用resource-id定位
driver.find_element_by_xpath('//*[@resource-id="com.baidu.wenku:id/tv_agree"]').click()