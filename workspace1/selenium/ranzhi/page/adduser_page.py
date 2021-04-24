from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage

# class AddUserPage(BasePage):
class AddUserPage(LoginPage):

    def adduser(self):
        # 登陆
        # driver = LoginPage().login('admin','123456')

        driver = self.driver

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

        # 关闭浏览器
        driver.close()

if __name__ == "__main__":
    adduer = AddUserPage()
    adduer.adduser()