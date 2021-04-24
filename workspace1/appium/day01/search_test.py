import unittest
from parameterized import parameterized
from util import BoxDriver,GetExcel
from search_page import SearchPage

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BoxDriver('http://127.0.0.1:4723/wd/hub','App')
        cls.page = SearchPage(driver)
        # 执行前置操作
        cls.page.common()

    @parameterized.expand(GetExcel.get(r'appium\day01\data.xlsx','search'))
    def test_search(self,key,value):
        self.page.search(key)

        # 断言
        titles = self.page.get_texts()
        self.assertIn(value,titles,'断言失败')

        # 点击取消
        self.page.cancel()

if __name__ == "__main__":
    unittest.main()