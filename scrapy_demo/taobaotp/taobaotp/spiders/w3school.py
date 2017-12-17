#coding=utf8
import scrapy
from scrapy import Selector
from items import w3school

class W3schoolSpider(scrapy.Spider):
    name = "w3school"
    allowed_domains = ["www.w3school.com.cn"]
    start_urls = ['http://www.w3school.com.cn/xml/xml_syntax.asp']

    def parse(self, response):
        print '-'*50,response.url
        self.logger.info('begin to parse:%s' %(response.url))
        sel=Selector(response) #创建Selector
        #print dir(sel)
        #执行xpath筛选
        sites=sel.xpath("//div[@id='wrapper']/div[@id='navsecond']/div[@id='course']/ul[1]/li")
        items=[]
        for site in sites:
            #print site
            item=w3school()
            title=site.xpath('a/text()').extract()
            link=site.xpath('a/@href').extract()
            desc=site.xpath('a/@title').extract()
#             item['title']=[t.encode('utf-8') for t in title]
#             item['link']=[l.encode('utf-8') for l in title]
#             item['desc']=[d.encode('utf-8') for d in title]
            item['title']=title
            item['link']=link
            item['desc']=desc
            #print title,link,desc
            items.append(item)
            self.log('appending item!')
        self.logger.info('append done!')
        return items
            