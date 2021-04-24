'''单元测试'''

import unittest

# 必须继承TestCase类
class Test01(unittest.TestCase):

    '''
    setUpClass方法在所有测试用例前执行，并且只会执行一次
    '''
    @classmethod    # 类方法
    def setUpClass(cls):
        print('-----在所有用例前执行-----')

    @classmethod
    def tearDownClass(cls):
        print('-----在所有用例后执行-----')

    # 重写父类的setUp方法
    # setUp方法会自动的在每一个测试用例前运行
    def setUp(self):
        print('start...')

    # 重写父类的teatDown方法
    # setUp方法会自动的在每一个测试用例后运行
    def tearDown(self):
        print('end...')

    '''
    测试用例方法名必须以test开头
    用例执行的先后顺序遵循用例名字在ASCII码表中的字符顺序
    '''
    def testademo04(self):
        print('-----testademo04()-----')

    def testAdemo04(self):
        print('-----testAdemo04()-----')

    def test01(self):
        print('-----test01()-----')

    def test02(self):
        print('-----test02()-----')

    def test03(self):
        print('-----test03()-----')

        

if __name__ == "__main__":
    unittest.main()