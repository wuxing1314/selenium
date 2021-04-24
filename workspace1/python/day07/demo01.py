import requests
from lxml import etree

# 将爬虫伪装成浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

# 发出请求，并接收响应
r = requests.get('https://www.baidu.com/', headers=headers)
# 设置编码集
r.encoding = 'utf-8'
# 将文本格式的网页转换为电子树格式
selector = etree.HTML(r.text)

# 定位元素
result = selector.xpath('//*[@id="s_lg_img"]/@src')
print(result)
src = result[0]
# 下载图片
response = requests.get('https:'+src)

# 保存图片
with open('logo.png','wb') as file:
    file.write(response.content)