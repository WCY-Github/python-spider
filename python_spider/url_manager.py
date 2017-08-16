# _*_ coding:utf-8 _*_  
"""
@file: url_manager.py 
@time: 2017/08/16 
"""


class UrlManager(object):
    def __init__(self):
        # 待爬取url
        self.new_urls = set()
        # 已爬取url
        self.old_urls = set()

    # 添加一个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加多个url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 待爬取列表
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 取出新的URL进行爬取
    def get_new_url(self):
        # 将刚取出的url从未爬取列表中弹出
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

