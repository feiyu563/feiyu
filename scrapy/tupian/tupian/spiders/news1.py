# -*- coding: utf-8 -*-
import scrapy

    
class News1Spider(scrapy.Spider):
    name = "news1"
    #allowed_domains = ["anhuinews.com"]
    start_urls = ['http://www.cnblogs.com/wupeiqi/articles/4938499.html']
    
    def parse(self, response):
        links=response.xpath("//div[@id='cnblogs_post_body']/ul[1]/li/a/@href").extract()
        for link in links:
            yield 