'''工具模块'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time,yaml,logging,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from appium import webdriver as app_webdriver


class BoxDriver:

    def __init__(self,url,browser='Chrome'):
        '''
        browser: 浏览器类型，取值范围为 Chrome,Ie,Firfox,Safari
        '''
        # 基本配置
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.baidu.wenku",
            "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
            "deviceName": "127.0.0.1:62001"
        }
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Ie':
            self.driver = webdriver.Ie()
        elif browser == 'Firfox':
            self.driver = webdriver.Firefox()
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        elif browser == 'App':
            self.driver = app_webdriver.Remote(url,desired_capabilities=desired_capabilities)
        else:
            raise NameError('没有匹配的浏览器！')

        # 创建浏览器
        self.implicitly_wait()
        if browser != 'App':
            self.maximize_window()
            self.get(url)

        self.wait(1)

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


    def wait(self,second):
        '''
        休眠
        second： 休眠的时间，单位是秒
        '''
        time.sleep(second)

    def implicitly_wait(self,second=30):
        '''
        隐式等待
        second: 最大等待时间，单位是秒
        '''
        self.driver.implicitly_wait(second)

    def webdriver_wait(self,selector):
        '''
        显示等待
        '''
        locator = self.locate_element(selector)
        return WebDriverWait(self.driver).until(EC.presence_of_element_located(locator))

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
        element = self.locate_element(selector)
        # 先清除一下文本框
        element.clear()
        element.send_keys(text)

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

class BasePage:

    def __init__(self,driver:BoxDriver):
        self.driver = driver

class GetYaml:

    @staticmethod # 静态方法
    def get(path):
        '''
        读取yaml格式的数据文件
        '''
        with open(path,'r',encoding='utf-8') as file:
            return yaml.load(file.read(),Loader=yaml.SafeLoader)

class GetExcel:

    @staticmethod
    def get(workbook,worksheet):
        '''
        获取Excel数据
        workbook 工作簿
        wroksheet 工作表
        cell    单元格
        '''
        import openpyxl

        # 打开工作簿
        workbook = openpyxl.load_workbook(workbook)
        # 获取指定的工作表
        sheet = workbook[worksheet]

        data = [tuple(cell.value for cell in row) for row in sheet]
        return data[1:] # 去掉表头，然后返回数据

class GetCSV:

    @staticmethod
    def get(path):
        '''
        获取CSV格式的数据
        path, 文件名
        '''
        # 打开文件
        with open(path,'r',encoding='utf-8') as file:
            return [tuple(e.strip() for e in line.split(',')) for line in file.readlines()]

'''
logging python内置的日志模块
日志等级
    debug       -信息量最丰富
    info
    warning
    error
    critical    -信息量最少
'''
class GetLogger:

    def __init__(self,path,level=logging.DEBUG):
        '''
        path: 日志文件路径
        level: 日志级别，默认是DEBUG
        '''
        self.path = path
        # 创建日志
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(level)
        # 指定日志输出的内容与格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def __console(self,level,message):
        '''
        输出日志到文件中
        level: 日志级别
        message: 日志输出的信息
        '''
        # 创建FileHandler对象，将日志写到文件中
        fh = logging.FileHandler(self.path,mode='a',encoding='utf-8')
        # 设置日志等级
        fh.setLevel(logging.DEBUG)
        # 设置日志输出内容与格式
        fh.setFormatter(self.formatter)
        # 添加文件处理器到日志中
        self.logger.addHandler(fh)

        # 创建StreamHandler对象，将日志输出到控制台
        sh = logging.StreamHandler(sys.stdout)
        # 设置日志等级
        sh.setLevel(logging.DEBUG)
        # 设置日志输出内容与格式
        sh.setFormatter(self.formatter)
        # 添加控制台处理器到日志中
        self.logger.addHandler(sh)

        # 根据日志级别，进行响应的输出
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        fh.close()
        
    def debug(self,message):
        self.__console('debug',message)

    def info(self,message):
        self.__console('info', message)

    def warning(self,message):
        self.__console('warning', message)

    def error(self,message):
        self.__console('error', message)

    def critical(self,message):
        self.__console('critical', message)


class Email:

    @staticmethod
    def send(receivers,subject=None,content=None,path=None,sender='jingying0037@163.com',smtpserver='smtp.163.com',port=25,password='AVNCNFWSUJQEALFA'):
        '''
        发送电子邮件
        receivers:  收件人地址
        subject:    主题
        content:    邮件正文
        path:       附件路径
        smtpserver: 设置邮件服务器地址
        port        设置邮件服务器端口
        password:   授权码
        sender:     发件人地址
        '''

        '''创建邮件'''
        # 创建邮件对象
        mail = MIMEMultipart()
        # 初始化发件人
        mail['from'] = sender
        # 初始化收件人
        mail['to'] = receivers
        # 添加主题
        mail['subject'] = subject

        '''添加附件'''
        # 读取附件
        print(path)
        with open(path,'rb') as file:
            report = file.read()

        # 对附件进行编码
        attchment = MIMEText(report,'base64','utf-8')
        # 设置附件的类型
        attchment['Content-Type'] = 'application/octet-stream'
        # 设置附件的处理方式
        attchment['Content-Disposition'] = 'attchment;filename=%s'%path.split('\\')[-1]
        # 添加附件
        mail.attach(attchment)

        '''添加正文'''
        # 对正文进行编码
        body = MIMEText(content,'html','utf-8')
        # 添加正文
        mail.attach(body)

        '''发送邮件'''
        # 创建smtp对象
        smtp = smtplib.SMTP()
        # 连接邮件服务器
        smtp.connect(smtpserver,port)
        # 登陆服务器
        smtp.login(sender,password)
        # 发送邮件
        smtp.sendmail(sender,receivers.split(';'),mail.as_string())
        # 关闭服务器
        smtp.close()
        print('邮件发送完毕！')


if __name__ == "__main__":
    receivers = 'jingying0037@163.com;wzy944454197@163.com;l15591464532@163.com'
    subject = 'Ran之自动化测试报告'
    content = '''
    <h3>Dear All,</h3>
    <p>这是Ranzhi项目的测试报告，请您查收！</p>

    <p>此致，</p>
    <p>敬礼，Tom</p>
    '''
    path = r'selenium\ranzhi\report\report_2021-01-12_11-03-11.html'
    Email.send(receivers,subject,content,path)