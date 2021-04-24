from util import BoxDriver,BasePage

class CommonPage(BasePage):

    def common(self):
        '''操作app之前的前置操作'''

        driver = self.driver
        # 点击同意
        driver.click('id,com.baidu.wenku:id/tv_agree')
        driver.wait(10)

        # 点击关闭升级
        driver.click('id,com.baidu.wenku:id/dialog_pic_close')
        driver.wait(10)