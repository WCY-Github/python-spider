# _*_ coding:utf-8 _*_
"""
@file: spider_main.py 
@time: 2017/08/16
"""
# 在Mac osx下使用pycharm时，用alt+enter添加方法
from python_spider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()
        # 解析器
        self.parser = html_parser.HtmlParser()

    # 爬虫调度程序
    def craw(self, root_url):
        # url计数器
        count = 1
        # 添加根URL
        self.urls.add_new_url(root_url)
        # 有未爬取得url时循环
        while self.urls.has_new_url:
            try:
                # 取URL
                new_url = self.urls.get_new_url()
                # 输出序号和当前URL
                print 'craw %d : %s' %(count, new_url)
                # 下载页面内容
                html_cont = self.downloader.download(new_url)
                # 解析URL中的新URL和内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 添加新URL
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                # 判断循环次数
                if count == 10:
                    break

                count = count+1
            # 在pycharm中会提醒捕获的异常过于广泛，如果程序没错的话不影响
            except:
                print 'craw failed.'
        # 输出收集好的数据
        self.outputer.output_html()


if __name__ == "__main__":
    # 根URL
    root_url = "http://baike.baidu.com/item/Python/407313?fr=aladdin"
    # 创建
    obj_spider = SpiderMain()
    # craw方法启动爬虫
    obj_spider.craw(root_url)
