from selenium import webdriver
from time import sleep


try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    sleep(1)

    '''获取元素的属性的值 get_attribute(属性名)'''
    # 定位 视频
    # video  = driver.find_element_by_link_text('视频')
    # 获取属性的值
    # href = video.get_attribute('href')
    # print(href)

    # driver.get(href)

    '''获取元素的文本'''
    
    news = driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[4]/a/span[2]')
    text = news.text
    print(text)

except Exception as e:
    print(e)
finally:
    sleep(200)
    driver.quit()