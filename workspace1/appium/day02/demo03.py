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

# 使用UiAutomator定位方式
# 使用text属性定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("同意并继续")').click()
# 使用resource-id属性定位
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.wenku:id/tv_agree")').click()
# 使用class属性定位
# driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')[3].click()

# 组合定位
# driver.find_element_by_android_uiautomator('className("android.widget.TextView").text("同意并继续")').click()
# driver.find_element_by_android_uiautomator('className("android.widget.TextView").resourceId("com.baidu.wenku:id/tv_agree").text("同意并继续")').click()

# 模糊定位
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("同意并继")').click()

# 通过父元素进行定位
# driver.find_element_by_android_uiautomator('className("android.widget.LinearLayout").childSelector(text("同意并继续"))').click()
# 通过兄弟关系进行定位
driver.find_element_by_android_uiautomator('text("不同意").fromParent(text("同意并继续"))').click()

# driver.close_app()

# 打开美图秀秀
# content-desc
# driver.find_element_by_android_uiautomator('new UiSelector().description("美图秀秀")').click()