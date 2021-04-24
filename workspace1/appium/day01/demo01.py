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
# 隐式等待
driver.implicitly_wait(30)
sleep(10)

# 点击同意
driver.find_element_by_id('com.baidu.wenku:id/tv_agree').click()
sleep(10)

# 点击关闭升级
driver.find_element_by_id('com.baidu.wenku:id/dialog_pic_close').click()
sleep(5)

# 点击 搜索框
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text').click()
sleep(5)

# 输入信息
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').send_keys('软件测试面试都问啥')
sleep(3)
# 点击 搜索按钮
driver.find_element_by_id('com.baidu.wenku:id/h5_search_operate_text').click()
sleep(20)

# 点击搜索结果中的百度文库
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View[1]').click()

sleep(5)
