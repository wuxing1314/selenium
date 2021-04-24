from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

'''
3种等待方式：
1. sleep(second) 强制等待
2. implicitly_wait(second) 隐式等待 - 等待页面加载完成
3. WebDriverWait 显示等待 - 等待某个元素加载完成
'''
try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10) # 最多等10秒钟

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    # sleep(2)
    # 添加成员
    # 点击 后台管理
    driver.find_element_by_id('s-menu-superadmin').click()

    # 切换iframe
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)

    # 点击 添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()

    # 填写用户信息
    driver.find_element_by_id('account').send_keys('tom')
    driver.find_element_by_id('realname').send_keys('Tom Cruse')
    driver.find_element_by_id('genderm').click()

    # 选择部门
    # 方法一：直接选择
    # driver.find_element_by_xpath('//*[@id="dept"]/option[3]').click()
    # 方法二：使用Select类辅助选择
    select1 = driver.find_element_by_id('dept')
    depts = Select(select1)
    # 根据下标进行选择，下标从0开始
    # depts.select_by_index(1)
    # 根据value属性的值来选择
    # depts.select_by_value('13')
    # 根据选项的文本进行选择
    depts.select_by_visible_text('/开发部')

    # 选择角色
    select2 = driver.find_element_by_id('role')
    roles = Select(select2)
    roles.select_by_value('pm')

    driver.find_element_by_id('password1').send_keys('123456')
    driver.find_element_by_id('password2').send_keys('123456')

    driver.find_element_by_id('email').send_keys('tom@163.com')

    driver.find_element_by_id('submit').click()

    # 点击删除按钮
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
    # 点击 取消
    driver.switch_to.alert.dismiss()
    
    # 点击 确定
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
    driver.switch_to.alert.accept()
except Exception as e:
    print(e)
finally:
    driver.close()