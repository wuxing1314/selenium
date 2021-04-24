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

# 根据坐标选择元素
driver.tap([(450,850)],100)
sleep(5)
# 关闭升级
driver.tap([(360,950)],100)
sleep(5)

# 滑动
driver.swipe(360,1000,360,500,1000)
sleep(5)
driver.close_app()

# 点击美图秀秀
# driver.tap([(500,470)])