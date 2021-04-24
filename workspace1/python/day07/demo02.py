import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

# 下载并保存章节
def chapter_downloader(name,url):
    '''
    url 章节地址
    '''
    try:
        # 发出请求
        response = requests.get(url,headers=headers)
        # 指定编码集
        response.encoding = 'utf-8'
        if 'Unavailable' in response.text:
            raise NameError('503异常')
        selector = etree.HTML(response.text)

        # 获取章节标题
        ctitle = selector.xpath('//h1/text()')[0]
        print('开始下载章节%s...'%ctitle)

        # 获取章节内容
        content = selector.xpath('//*[@id="content"]/text()')
        content = ''.join(content)
        

        with open('%s.txt'%name,'a',encoding='utf-8') as file:
            file.write(ctitle+'\n'+content+'\n')
    except Exception:
        # 如果发生异常，重新下载当前章节
        print('发生异常，重新下载...')
        chapter_downloader(name,url)

# 下载小说
def novel_downloader(name,link):
    '''
    link 小说的地址
    '''
    try:
        # 获取小说章节列表页面
        response = requests.get(link,headers=headers)
        response.encoding = 'utf-8'
        if 'Unavailable' in response.text:
                raise NameError('503异常')
        selector = etree.HTML(response.text)
        # 获取所有的章节地址列表
        urls = selector.xpath('//*[@id="list"]/dl/dd/a/@href')
        urls = ['http://www.xbiquge.la'+url for url in urls]

        # 遍历地址列表，下载所有章节
        for url in urls[:5]:
            chapter_downloader(name,url)
    except Exception:
        print('发生异常，重新下载...')
        novel_downloader(name,link)

def spider(href):
    # 获取所有小说地址页面
    response = requests.get(href,headers=headers)
    response.encoding = 'utf-8'
    selector = etree.HTML(response.text)
    # 获取所有小说的地址列表
    names = selector.xpath('//*[@id="main"]/div[@class="novellist"]/ul/li/a/text()')
    links = selector.xpath('//*[@id="main"]/div[@class="novellist"]/ul/li/a/@href')
    # 遍历地址列表，下载所有小说
    for name,link in zip(names,links):
        print('开始下载小说%s'%name)
        novel_downloader(name,link)

if __name__ == "__main__":
    spider('http://www.xbiquge.la/xiaoshuodaquan/')

