from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetLogger
import unittest
from parameterized import parameterized

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BoxDriver('http://localhost/ranzhi/www/sys/user-login.html')
        cls.page = LoginPage(cls.driver)
        # 创建日志
        cls.logger = GetLogger(r'D:\workspace\selenium\ranzhi\report\rhzhi.log')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @parameterized.expand(GetExcel.get(r'selenium\ranzhi\config\data.xlsx','login_success'))
    def test_login_success(self,account,password,realname):
        '''登陆成功功能测试用例'''
        try:
            self.page.login(account,password)
            self.logger.info('登陆完毕')
            self.assertEqual(self.page.get_realname(),realname,'断言失败')
            self.logger.warning('断言成功')
        except Exception as e:
            raise NameError('登陆成功用例失败！')
        finally:
            self.page.logout()
            self.logger.info('退出登陆')

    @parameterized.expand(GetExcel.get(r'selenium\ranzhi\config\data.xlsx','login_fail'))
    def test_login_fail(self,username,password):
        '''登陆失败功能测试用例'''
        try:
            self.page.login(username,password)
            self.logger.info('登陆完毕')
            msg = self.page.get_msg()
            self.assertIn('登录失败',msg,'断言失败！')
            self.logger.warning('断言成功')
        # except Exception as e:
        #     raise NameError('登陆失败用例失败，代码错误！')
        finally:
            self.page.confirm()
            self.logger.info('确认完成')


if __name__ == "__main__":
    unittest.main()