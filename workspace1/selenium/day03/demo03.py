from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random
from util import BoxDriver

class AddUser:

    def add_user(self):
        try:
            # driver = webdriver.Chrome()
            driver = BoxDriver()
            driver.get('http://localhost/ranzhi/www/sys/user-login.html')
            driver.maximize_window()
            driver.implicitly_wait(10)

            # 登陆
            driver.input('id,account','admin')
            driver.input('id,password','123456')
            driver.click('id,submit')

            # 添加成员
            # 点击 后台管理
            driver.click('id,s-menu-superadmin')

            # 切换iframe
            driver.switch_to_frame('id,iframe-superadmin')

            # 点击 添加成员
            driver.click('x,//*[@id="shortcutBox"]/div/div[1]/div/a')

            for i in range(7,9):
                username = 'user%d'%i
                # 填写用户信息
                driver.input('id,account',username)
                driver.input('id,realname',username)

                # 性别
                driver.click('id,genderm' if i%2==0 else 'id,genderf')

                # 选择部门
                driver.select_by_index('id, dept',random.randint(1,6))

                # 选择角色
                driver.select_by_index('id,role',random.choice(range(1,17)))

                driver.input('id,password1','123456')
                driver.input('id,password2','123456')

                driver.input('id,email','%s@163.com'%username)

                driver.click('id,submit')

                sleep(2)

                # 获取所有的用户名
                accounts = driver.locate_elements('x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
                # 获取最后一个
                account = accounts[-1]
                # 断言
                assert account.text == username, '用户添加失败！'

                # 添加成员
                driver.click('l,添加成员')

        except Exception as e:
            print(e)
        finally:
            sleep(2)
            driver.close()

if __name__ == "__main__":
    adduer = AddUser()
    adduer.add_user()