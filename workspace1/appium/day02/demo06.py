from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# 基本配置
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.baidu.wenku",
    "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
    "deviceName": "127.0.0.1:62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

# 按下 HOME键
driver.press_keycode(3)
# 按下音量键
driver.long_press_keycode(24)
driver.long_press_keycode(25)

# 安装app
driver.install_app(r'd:\com.mt.mtxx.mtxx.apk')

sleep(10)
# 卸载app
driver.remove_app('com.mt.mtxx.mtxx')