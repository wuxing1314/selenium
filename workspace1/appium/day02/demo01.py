from appium import webdriver
from time import sleep


# 基本配置
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.baidu.wenku",
    "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
    "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(3)
# 关闭app
driver.close_app()

# 打开美图秀秀
# accessibility_id 相当于 content-desc
driver.find_element_by_accessibility_id('美图秀秀').click()
sleep(2)
