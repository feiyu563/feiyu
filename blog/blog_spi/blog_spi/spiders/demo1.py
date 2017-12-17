# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import requests
class Demo1Spider(CrawlSpider):
    name = "demo1"
    download_delay=0.2
    #allowed_domains = ["news.china.com"]
    start_urls = ['http://news.china.com/morepage/1007/index.html']
    linkrule=LinkExtractor(allow=('index'),restrict_xpaths=("//a[@class='nextPage']"))
    rules=[Rule(linkrule,callback='parse_item',follow=True),]
#     def parse(self, response):
#         pass
    def parse_item(self,response):
        links=response.xpath("//div[@class='item-tit']/a/@href").extract()
        for link in links:
            print link