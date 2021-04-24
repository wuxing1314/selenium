import os,sys
sys.path.append(os.getcwd()+'\\selenium\\ranzhi')
import unittest,time
from base.HTMLTestRunner import HTMLTestRunner
from base.util import Email

class TestRunner:

    def runner(self):
        '''运行指定的测试用例并生成测试报告'''
        # 创建测试套件
        suit = unittest.TestSuite()
        # 添加测试用例
        # 参数1： 用例所在的路径
        # 参数2： 用例过滤条件
        suit.addTests(unittest.TestLoader().discover('./selenium/ranzhi/test/',pattern='login_test.py'))

        # 创建一个时间戳
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S') 
        path = './selenium/ranzhi/report/report_%s.html'%timestamp
        # 创建测试报告
        report = open(path,mode='wb')

        # 创建用例运行器
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi自动化测试报告！',description='报告详细描述....')
        # 运行用例
        test_runner.run(suit)
        # 发送邮件
        receivers = 'jingying0037@163.com;wzy944454197@163.com;l15591464532@163.com'
        subject = 'Ran之自动化测试报告'
        content = '''
        <h3>Dear All,</h3>
        <p>这是Ranzhi项目的测试报告，请您查收！</p>

        <p>此致，</p>
        <p>敬礼，Tom</p>
        '''
        Email.send(receivers,subject,content,path)

if __name__ == "__main__":
    TestRunner().runner()
    # pwd: print working directory
    # getcwd: get current working directory
    # print(os.getcwd()) 
    # print(sys.path)