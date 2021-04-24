import requests,sqlite3
from lxml import etree
from time import sleep
from multiprocessing import Pool,Manager

class Downloader:
    
    def __init__(self,title_selector,chapter_selector,ctitle_selector,content_selector,url=None,encoding='utf-8'):
        '''
        title_selector: 小说标题定位方式
        chapter_selector:   章节地址定位方式 
        ctitle_selector: 章节标题定位方式
        content_selector:   章节内容定位方式
        url: 网站地址
        '''
        self.title_selector = title_selector
        self.chapter_selector = chapter_selector
        self.ctitle_selector = ctitle_selector
        self.content_selector = content_selector
        self.url = url
        self.encoding = encoding

        #连接到SQlite数据库
        #数据库文件是test.db，不存在，则自动创建
        self.conn = sqlite3.connect('temp.db')
        #创建一个cursor：
        self.cursor = self.conn.cursor()
        self.cursor.execute('''create table if not exists info(
            title varchar(50)
        )''')
        self.cursor.execute('''create table if not exists novel (
            link varchar(100),
            content text,
            flag int
        ) ''')

    def download_chapter_list(self,url):
        '''爬取小说的全部章节地址'''
        try:
            # 获取章节列表页面
            response = requests.get(url)
            # 指定编码集
            response.encoding = self.encoding
            # print(response.text)
            # 将文本格式页面转换为etree对象格式
            selector = etree.HTML(response.text)
            # 获取小说名称
            title = selector.xpath(self.title_selector)[0]
            if title == '503 Service Temporarily Unavailable':
                raise NameError('503异常')

            # 获取所有的章节地址
            links = selector.xpath(self.chapter_selector)

            # 用列表生成式补全章节地址
            links = ['https://www.tsxs.org'+link for link in links]
            # return title,links
            # 将数据保存进数据库
            self.cursor.execute('insert into info(title) values(?)',(title,))
            for link in links:
                r = self.cursor.execute('select * from novel where link=?',(link,))
                if not r.fetchone():
                    self.cursor.execute("insert into novel(link,flag) values (?,?)",(link,0))
                    self.conn.commit()
        except Exception as e:
            print(e)
            self.download_chapter_list(url)

    def download_chapter_content(self,args):
        '''下载指定章节的内容'''
        d = args[0]
        link = args[1]
        try:
        # 下载章节
            sleep(2) # 休息2秒，避免给对方服务器过大的压力
            response = requests.get(link)
            response.encoding = self.encoding
            selector = etree.HTML(response.text)
            ctitle = selector.xpath(self.ctitle_selector)[0]
            if ctitle == '503 Service Temporarily Unavailable':
                raise NameError('503异常')
            print('正在下载...%s'%ctitle)
            # 获取正文内容-方式一
            content = selector.xpath(self.content_selector)
            result = ''.join(content)

            # 保存到字典中
            d[link] = ctitle+'\n'+result
        except Exception as e:
            print(e)
            self.download_chapter_content(args)

    def save_content(self,title,links,d):
        '''保存小说内容到文件中'''
        with open('%s.txt'%title,mode='a',encoding='utf-8') as file:
            for link in links:
                file.write(d[link])
            
    def main(self,url):
        '''下载指定的小说'''
        # 获取小说标题和所有章节的地址
        title, links = self.download_chapter_list(url)
        print('开始下载小说-%s...'%title)
        # links = links[1:]
        # 使用多进程下载
        with Manager() as manager:
            d = manager.dict()
            args = [(d,link) for link in links]
            pool = Pool(1) # 创建进程池，初始化10个进程
            pool.map(self.download_chapter_content,args)
            pool.close()
            pool.join()

            # 保存
            self.save_content(title,links,d)
            print('下载小说-%s下载完毕'%title)

    def biquge(self,url):
        '''下载指定的网站'''
        # pages = [url+'/%s.html'%i for i in range(1,3086)]
        pages = [url+'/%s.html'%i for i in range(1,2)]
        
        for page in pages:
            response = requests.get(page)
            selector = etree.HTML(response.text)
            novels = selector.xpath(self.url)
        return novels

if __name__ == "__main__":
    title_selector = '//*[@id="maininfo"]/div[1]/h1/text()'
    chapter_selector = '//*[@id="chapterlist"]/li/a/@href'
    ctitle_selector = '//*[@id="mains"]/div[1]/h1/text()'
    content_selector = '//*[@id="book_text"]/text()'
    downloader = Downloader(title_selector,chapter_selector,ctitle_selector,content_selector,encoding='gbk')
    # main('http://www.biquge.info/0_383/')
    # links = downloader.biquge('http://www.biquge.info/paihangbang_allvisit')
    # for link in links:
    #     downloader.main(link)


    # downloader.main('https://www.tsxs.org/70/70026/')
    downloader.download_chapter_list('https://www.tsxs.org/70/70026/')