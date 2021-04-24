from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 添加成员
    # 点击 后台管理
    driver.find_element_by_id('s-menu-superadmin').click()

    # 切换iframe
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)

    # 点击 添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()

    for i in range(1,5):
        username = 'user%d'%i
        # 填写用户信息
        driver.find_element_by_id('account').send_keys(username)
        driver.find_element_by_id('realname').send_keys(username)

        # 性别
        # driver.find_element_by_id(random.choice(['genderm','genderf'])).click()
        driver.find_element_by_id('genderm' if i%2==0 else 'genderf').click()

        # 选择部门
        select1 = driver.find_element_by_id('dept')
        depts = Select(select1)
        depts.select_by_index(random.randint(1,6))

        # 选择角色
        select2 = driver.find_element_by_id('role')
        roles = Select(select2)
        roles.select_by_index(random.choice(range(1,17)))

        driver.find_element_by_id('password1').send_keys('123456')
        driver.find_element_by_id('password2').send_keys('123456')

        driver.find_element_by_id('email').send_keys('%s@163.com'%username)

        driver.find_element_by_id('submit').click()

        sleep(2)

        # 获取所有的用户名
        accounts = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        # 获取最后一个
        account = accounts[-1]
        # 断言
        assert account.text == username, '用户添加失败！'

        # 添加成员
        driver.find_element_by_link_text('添加成员').click()


# except Exception as e:
#     print(e)
finally:
    sleep(2)
    driver.close()