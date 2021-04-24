from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 登陆
    driver.find_element_by_id('account').send_keys('tom')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 验证登陆是否成功
    # 获取用户真名
    realname = driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[1]/li/a').text
    # 比较
    # if realname == 'Tom Cruse':
    #     print('登陆测试用例成功！')
    # else:
    #     print('登陆测试用例失败！')    

    # 断言
    assert realname == 'Tom Cruse', '登陆测试用例失败！'

    # 获取当前页面的url
    current_url = driver.current_url
    print(current_url)
    url = 'http://localhost/ranzhi/www/sys/index.html'

    assert current_url == url, '登陆测试用例失败！'

    # 获取页面的标题
    title = driver.title
    assert title == '然之协同','登陆测试用例失败！'

    print('用例执行结束')


    
# except Exception as e:
#     print(e)
finally:
    sleep(2)
    driver.close()