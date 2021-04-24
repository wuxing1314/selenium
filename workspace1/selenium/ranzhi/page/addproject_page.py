from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

class AddProject:

    def add_project(self):
        try:
            driver = webdriver.Chrome()
            driver.get('http://localhost/ranzhi/www/sys/user-login.html')
            driver.maximize_window()
            driver.implicitly_wait(10)

            # 登陆
            driver.find_element_by_id('account').send_keys('admin')
            driver.find_element_by_id('password').send_keys('123456')
            driver.find_element_by_id('submit').click()

            # 点击后台管理
            driver.find_element_by_id('s-menu-3').click()

            # 进入iframe
            iframe = driver.find_element_by_id('iframe-3')
            driver.switch_to.frame(iframe)
            sleep(1)

            for i in range(7,10):
                # 点击 添加区块
                driver.find_element_by_xpath('//*[@id="dashboard"]/div[2]/a').click()
                # 选择区块
                block = random.choice(['task','project'])
                blocks = Select(driver.find_element_by_id('blocks'))
                blocks.select_by_value(block)
                # 区块名称
                driver.find_element_by_id('title').send_keys('project%d'%i)
                # 宽度
                grids = Select(driver.find_element_by_id('grid'))
                grids.select_by_index(random.randint(0,5))
                # 颜色
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button').click()
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%random.randint(1,6)).click()
                if block == 'task':
                    # 类型
                    driver.find_element_by_id('paramstype_chosen').click()
                    driver.find_element_by_xpath('//*[@id="paramstype_chosen"]/div/ul/li[%d]'%random.randint(1,5)).click()
                # 数量
                driver.find_element_by_id('params[num]').clear()
                driver.find_element_by_id('params[num]').send_keys(random.randint(10,30))
                # 排序
                driver.find_element_by_id('paramsorderBy_chosen').click()
                driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%random.randint(1,6)).click()
                
                # 任务状态
                if block == 'task':
                    n = random.randint(1,3)
                    indexes = [1,2,3,4,5,6]
                    for j in range(n):
                        index = random.randint(0,len(indexes)-1)
                        print(indexes)
                        print(index)
                        driver.find_element_by_id('paramsstatus_chosen').click()
                        driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%indexes[index]).click()
                        indexes.pop(index)
                if block == 'project':
                    driver.find_element_by_id('paramsstatus_chosen').click()
                    driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%random.randint(1,4)).click()
                
                # 保存
                driver.find_element_by_id('submit').click()
                sleep(2)
        except Exception as e:
            print(e)
        finally:
            sleep(20)
            driver.close()

if __name__ == "__main__":
    AddProject().add_project()