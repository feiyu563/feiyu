# -*- coding: utf-8 -*-
import scrapy


class Demo1Spider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["blog.csdn.net/kkkloveyou/article/details/6416094"]
    start_urls = ['http://blog.csdn.net/kkkloveyou/article/details/6416094/']

    def parse(self, response):
        pass
