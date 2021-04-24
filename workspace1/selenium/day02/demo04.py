from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# driver.find_element_by_id('kw').send_keys('BTCoin')

driver.find_element(By.ID,'kw').send_keys('BTCoin')

'''显示等待'''
# driver.find_element_by_id('su').click()
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()