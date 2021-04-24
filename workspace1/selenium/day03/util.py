'''工具模块'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BoxDriver:

    def __init__(self,browser='Chrome'):
        '''
        browser: 浏览器类型，取值范围为 Chrome,Ie,Firfox,Safari
        '''
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Ie':
            self.driver = webdriver.Ie()
        elif browser == 'Firfox':
            self.driver = webdriver.Firefox()
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        else:
            raise NameError('没有匹配的浏览器！')

    def get(self,url):
        '''
        打开网页
        url: 网页地址
        '''
        self.driver.get(url)


    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()

    def implicitly_wait(self,second=10):
        '''
        隐式等待
        second: 最大等待时间，单位是秒
        '''
        self.driver.implicitly_wait(second)

    def convert_selector_to_locator(self,selector):
        '''
        把自定义的元素定位方式转换为selenium标准定位方式
        selector: 自定义元素定位方式 
                'id, account'  -> ('id','account')
        '''
        # 获取定位方式以及对应值
        by, value = [s.strip() for s in selector.split(',')]
        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by == 'class' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT,value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH,value)
        elif by == 'css_selector' or by == 'css':
            locator = (By.CSS_SELECTOR,value)
        else:
            raise NameError('非法的定位方式！')

        return locator

    def locate_element(self,selector):
        '''
        定位单个元素
        selector: 自定义元素定位方式 
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_element(*locator)

    def locate_elements(self,selector):
        '''
        定位多个元素
        selector: 自定义元素定位方式 
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_elements(*locator)

    def input(self,selector,text):
        '''
        输入文本
        selector: 自定义元素定位方式 
        text: 向元素中写入的文本
        '''
        self.locate_element(selector).send_keys(text)

    def click(self,selector):
        '''
        单击元素
        selector: 自定义元素定位方式 
        '''
        self.locate_element(selector).click()

    def switch_to_frame(self,selector):
        '''
        进入iframe
        selector: 自定义元素定位方式 
        '''
        element = self.locate_element(selector)
        self.driver.switch_to.frame(element)

    def select_by_index(self,selector,index):
        '''
        根据下标选择下拉选择框选项
        index: option的下标，从0开始
        '''
        element = self.locate_element(selector)
        Select(element).select_by_index(index)

    def select_by_value(self,selector,value):
        '''
        根据下标选择下拉选择框选项
        value: option的value属性的值
        '''
        element = self.locate_element(selector)
        Select(element).select_by_value(value)

    def select_by_visible_text(self,selector,visible_text):
        '''
        根据下标选择下拉选择框选项
        visible_text: option的文本
        '''
        element = self.locate_element(selector)
        Select(element).select_by_visible_text(visible_text)

    def close(self):
        '''
        关闭当前浏览器窗口
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()
    

if __name__ == "__main__":
    r = BoxDriver().convert_selector_to_locator('id, account')
    print(r)
