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

for key,value in [('软件测试','- 解析'),('牛宝宝','牛宝宝取名大全 - 百度文库')]:
    # 输入信息
    driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').clear()
    driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').send_keys(key)
    sleep(3)
    # 点击 搜索按钮
    driver.find_element_by_id('com.baidu.wenku:id/h5_search_operate_text').click()
    sleep(20)

    # 获取搜多结果文本
    elements = driver.find_elements_by_class_name('android.view.View')
    titles = [e.text for e in elements]
    # titles = [e.get_attribute('text') for e in elements]
    print(titles)

    # 断言
    assert value in titles, '断言失败'

