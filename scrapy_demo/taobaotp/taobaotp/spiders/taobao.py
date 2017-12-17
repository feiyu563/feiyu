# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Selector


class TaobaoSpider(Spider):
    name = "taobao"
    allowed_domains = ["www.runoob.com"]
    start_urls = ['http://www.runoob.com/sqlite/sqlite-select.html']

    def parse(self, response):
        print '-'*200,response.url
        self.logger.info('begin to parse:%s' %(response.url))
        sel=Selector(response)
        sites=sel.xpath('/html/body/div[@class="container main"]/div[@class="row"]/div[@class="col left-column"]/div[@class="sidebar-box gallery-list"]/div[@id="leftcolumn"]/a[@target="_top"]/attribute::href')
        print sites