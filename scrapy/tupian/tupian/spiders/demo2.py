# -*- coding: utf-8 -*-
import scrapy
import os

class demo2item(scrapy.Item):
    image_urls=scrapy.Field()
    image=scrapy.Field()

class Demo2Spider(scrapy.Spider):
    name = "demo2"
    allowed_domains = ["www.meizitu.com"]
    start_urls = ['http://www.meizitu.com/a/list_1_1.html']
    
    def parse(self, response):
        exp=u"//div[@id='wp_page_numbers']//a[text()='下一页']/@href"
        next1=response.xpath(exp).extract_first()
        next_page=os.path.join(os.path.dirname(response.url)+'/'+next1)
        print response.url
        for p in response.xpath("//li[@class='wp-item']//div[@class='pic']//a/@href").extract():
           yield scrapy.FormRequest(p,callback=self.downpic)
        yield scrapy.FormRequest(next_page,callback=self.parse)
    def downpic(self,response):
        print response.url
        item=demo2item()
        urls=response.xpath("//div[@id='maincontent']//img/@src").extract()
        if urls!='http://www.meizitu.com/images/erweima.jpg':
            item['image_urls']=urls
            return item
        