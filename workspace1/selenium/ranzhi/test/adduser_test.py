from page.adduser_page import AddUserPage
from page.login_page import LoginPage
from base.util import BoxDriver


class AddUserTest:

    def adduser_test(self):
        '''
        添加成员测试用例
        '''
        # driver = BoxDriver()
        #登陆
        # login = LoginPage(driver)
        # login.login('admin','123456')
        #添加用户
        # add = AddUserPage(driver)
        # add.adduser()

        add = AddUserPage(BoxDriver('http://localhost/ranzhi/www/sys/user-login.html'))
        add.login('admin','123456')
        add.adduser()


if __name__ == "__main__":
    AddUserTest().adduser_test()