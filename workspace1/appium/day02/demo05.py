from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


# 基本配置
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

# 定位元素
mtxx = driver.find_element_by_accessibility_id('美图秀秀')
# 长按元素-移动元素-释放元素
TouchAction(driver).long_press(mtxx).move_to(x=120,y=80).release().perform()
sleep(3)
# 点击 确定
driver.tap([(600,730)],500)