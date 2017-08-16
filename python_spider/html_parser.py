# _*_ coding:utf-8 _*_  
"""
@file: html_parser.py 
@time: 2017/08/16 
"""
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    # 自定义获取新URL的方法
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # href="/item/Guido%20van%20Rossum"
        # 用Python正则匹配URL
        links = soup.find_all('a', href=re.compile(r"/item/[^\"]+"))
        for link in links:
            # new_url = "https://baike.baidu.com/" + link['href']
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # 定义一个数据dict
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,  # html 文档字符串
                             'html.parser',  # html解析器
                             from_encoding='utf-8')  # html文档编码
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
