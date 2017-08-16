# _*_ coding:utf-8 _*_  
"""
@file: html_downloader.py 
@time: 2017/08/16 
"""
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        # 判断是否正常访问该url
        if response.getcode() != 200:
            return None
        # 返回url对应的HTML。注：read（）的内容存储于缓存器
        return response.read()
