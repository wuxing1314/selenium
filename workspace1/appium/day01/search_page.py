from util import BoxDriver
from time import sleep
from common_page import CommonPage

class SearchPage(CommonPage):

    def search(self,key):
        driver = self.driver
        # 点击 搜索框
        driver.click('id,com.baidu.wenku:id/h5_search_edit_text')
        sleep(5)
        # 输入信息
        driver.input('id,com.baidu.wenku:id/h5_search_edit_text_inside',key)
        sleep(3)
        # 点击 搜索按钮
        driver.click('id,com.baidu.wenku:id/h5_search_operate_text')
        sleep(20)

    def get_texts(self):
        # 获取搜多结果文本
        elements = self.driver.locate_elements('c,android.view.View')
        return [e.text for e in elements]

    def cancel(self):
        # 点击取消
        self.driver.click('id,com.baidu.wenku:id/h5_search_operate_text')

if __name__ == "__main__":
    SearchPage().search()
