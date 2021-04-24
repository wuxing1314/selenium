'''元素定位'''


from selenium import webdriver
from time import sleep

# 创建浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.baidu.com')

# 定位搜索框
'''id定位'''
# search = driver.find_element_by_id('kw')
'''name定位'''
# search = driver.find_element_by_name('wd')
'''class定位'''
search = driver.find_element_by_class_name('s_ipt')
'''
tag_name定位

class_name 和tag_name 一般不用于单个元素定位
因为他们的值一般不唯一，会返回定位到的所有元素中的第一个元素
'''
# search = driver.find_element_by_tag_name('input')
print(search)
# 向搜索框里写入搜索关键字
search.send_keys('UK病毒')

sleep(2)

# 定位 “百度一下”
btn = driver.find_element_by_id('su')

# 单击：click()
btn.click()

# 关闭当前浏览器窗口
# driver.close()
# 退出浏览器
driver.quit()