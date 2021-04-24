from base.util import BoxDriver,BasePage,GetYaml
import yaml


class LoginPage(BasePage):

    # 默认的构造方法
    # def __init__(self,driver):
    #     super().__init__(driver)

    config = GetYaml.get(r'selenium\ranzhi\config\config.yaml')

    def login(self,username,password):
        '''
        登陆操作流程
        '''
        driver = self.driver

        # 登陆
        driver.input(self.config['LoginPage']['ACCOUNT'],username)
        driver.input(self.config['LoginPage']['PASSWORD'],password)
        driver.click(self.config['LoginPage']['SUBMIT'])

        driver.wait(1)

    def logout(self):
        '''签退'''
        self.driver.click('l,签退')
        self.driver.wait(1)

    def confirm(self):
        '''失败时点击 '确认' '''
        self.driver.click('x,/html/body/div[2]/div/div/div[2]/button')
        self.driver.wait(1)

    def get_realname(self):
        '''获取用户真名'''
        element = self.driver.locate_element('x,//*[@id="mainNavbar"]/div/ul[1]/li/a')
        return element.text

    def get_msg(self):
        '''获取失败时的提示信息'''
        element = self.driver.locate_element('x,/html/body/div[2]/div/div/div[1]/div')
        return element.text

if __name__ == "__main__":
    url = 'http://localhost/ranzhi/www/sys/user-login.html'
    LoginPage(BoxDriver(url)).login('admin','123456')
