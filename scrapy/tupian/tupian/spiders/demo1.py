# -*- coding: utf-8 -*-
import scrapy


class Demo1Spider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["www.meizitu.com"]
    start_urls = ['http://www.meizitu.com']

    def parse(self, response):
        sel=scrapy.Selector(response)
        sites=sel.xpath("//div[@id='maincontent']")
        for site in sites:
            image=site.xpath("//div[@class='metaRight']//a/text()").extract()
            image_urls=site.xpath("//div[@class='postContent']//a/@href").extract()
            print image,image_urls
            
        
