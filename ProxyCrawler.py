#!/usr/bin/env python
# coding:utf-8
import requests
from lxml import etree
from config import CRAWLER_CONFIG


class Crawler(object):

    def _proxysite(self):
        proxysites = [
            {
                'url': 'http://www.kuaidaili.com/free/',
                'range': ['index'] + range(2, 11),
                'pattern': '(?P<ip>(?:\d{1,3}\.){3}\d{1,3})</td>\n?\s*<td.*?>\s*(?P<port>\d{1,4})'
            }]
        return proxysites

    def crawl(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        sites = self._proxysite()
        url = sites[0]['url']
        proxy = []
        r = requests.get(url, headers=headers, timeout=CRAWLER_CONFIG['TIMEOUT'])
        selector = etree.HTML(r.text)
        proxy_ip = selector.xpath("//*[@data-title='IP']/text()")
        proxy_port = selector.xpath("//*[@data-title='PORT']/text()")
        proxy_type = selector.xpath(u"//*[@data-title='匿名度']/text()")
        proxy_protocol = selector.xpath(u"//*[@data-title='类型']/text()")
        proxy_loc = selector.xpath(u"//*[@data-title='位置']/text()")
        for i in range(len(proxy_ip)):
            proxy_temp = [
                proxy_ip[i], proxy_port[i], proxy_type[i],proxy_protocol[i], proxy_loc[i]
            ]
            proxy.append(proxy_temp)
        print proxy


if __name__ == '__main__':
    Crawler().crawl()