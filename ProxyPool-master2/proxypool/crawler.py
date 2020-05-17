import json
import re
from .utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    # def crawl_USIP(self):
    #     """
    #     美国ip
    #     :param self:
    #     :return: 代理
    #     """
    #     with open('/home/links/Jay/clarity-crawler-python/ProxyPool-master/iplist.txt') as f:
    #         ip = f.readlines()
    #         for proxy in ip:
    #             yield proxy


    # def crawl_xdaili(self):
    #     """
    #     获取讯代理
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=72adc4feaaa64247a1ac5e1afcda025f&returnType=2&count=1'
    #     html = get_page(url)
    #     if html:
    #         result = json.loads(html)
    #         proxies = result.get('RESULT')
    #         for proxy in proxies:
    #             yield proxy.get('ip') + ':' + proxy.get('port')

    # def crawl_xdaili(self):
    #     """
    #     获取讯代理独享秒切
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=72adc4feaaa64247a1ac5e1afcda025f&orderno=DX2019940917DyEYyY&returnType=2&count=1&machineArea='
    #     html = get_page(url)
    #     if html:
    #         result = json.loads(html)
    #         proxies = result.get('RESULT')
    #         for proxy in proxies:
    #             yield proxy.get('ip') + ':' + proxy.get('port')

    # def crawl_xdaili(self):
    #     """
    #     极光代理
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'http://d.jghttp.golangapi.com/getip?num=71&type=2&pro=&city=0&yys=0&port=11&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    #     html = get_page(url)
    #     if html:
    #         result = json.loads(html)
    #         proxies = result.get('RESULT')
    #         for proxy in proxies:
    #             yield proxy.get('ip') + ':' + proxy.get('port')
    #
    # def crawl_yiniuyun(self):
    #     """
    #     yiniuyun
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'http://ip.16yun.cn:817/myip/pl/4bbfc1a4-f321-40ce-9db0-5233b5fe77b8/?s=kydgcsbxlv&u=Jay'
    #     html = get_page(url)
    #     if html:
    #         result = html.split('\n')
    #         for proxy in result:
    #             yield proxy
    #
    # def crawl_dailiyun(self):
    #     """
    #     yiniuyun
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'http://fool123.v4.dailiyun.com/query.txt?key=NPEFD6E50D&word=&count=10&rand=false&detail=false'
    #     html = get_page(url)
    #     if html:
    #         result = html.split('\n')
    #         for proxy in result:
    #             yield proxy
    #
    def crawl_xiongmao(self):
        """
        xiongmao
        :param self:
        :return: 代理
        """
        url = 'http://pandavip.xiongmaodaili.com/xiongmao-web/vip/gbip?secret=ead888ef20668c6c248a6ec54d629947&orderNo=VGB20190919140437MV6EWgXi&count=10&isTxt=0&proxyType=1'
        html = get_page(url)
        if html:
            result = json.loads(html)
            proxies = result.get('obj')
            for proxy in proxies:
                yield proxy.get('ip') + ':' + proxy.get('port')
    #
    # def crawl_2808(self):
    #     """
    #     2808
    #     :param self:
    #     :return: 代理
    #     """
    #     url = 'https://api.2808proxy.com/proxy/unify/get?token=B5BHGMV2PO785RTVSPJ3O32YBTCA4FDH&amount=1&proxy_type=http&format=json&splitter=rn&expire=60'
    #     html = get_page(url)
    #     if html:
    #         result = json.loads(html)
    #         proxies = result.get('data')
    #         for proxy in proxies:
    #             yield str(proxy.get('ip')) + ':' + str(proxy.get('http_port_secured'))