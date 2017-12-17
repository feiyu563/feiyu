# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    #allowed_domains = ["www.cnblogs.com/wupeiqi/articles/4938499.html"]
    start_urls = ['http://www.cnblogs.com/wupeiqi/articles/5433893.html']

    def parse(self, response):
        links=response.xpath("//div[@id='cnblogs_post_body']/ul[1]/li/a")
        for linkid in links:
            link=linkid.xpath("./@href").extract_first()
            name=linkid.xpath("./text()").extract_first()
            yield scrapy.Request(link,meta={'title': name},callback=self.downhtml)
    def downhtml(self,response):
        filename=response.meta['title']
        with open(filename+'.html','w+') as f:
            f.write(response.body)
        