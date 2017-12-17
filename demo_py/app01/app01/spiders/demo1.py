# -*- coding: utf-8 -*-
'''
爬取http://blog.csdn.net/kkkloveyou博客的所有文章，暂时没有写爬取下一页内容。

'''
import scrapy
import os
import codecs
class App01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()

class Demo1Spider(scrapy.Spider):
    name = "demo1"
    download_delay=0.1#每次爬取延迟0.1秒
    allowed_domains = ["blog.csdn.net"]
    start_urls = ['http://blog.csdn.net/kkkloveyou']
    def parse(self, response):
        sel=response.xpath("//div[@class='article_title']/h1/span[@class='link_title']/a")
        items=[]
        
        #extract_first()= extract()[0],extract()返回的是列表，extract_first()返回的是extract()列表中的第一个
        for site in sel:
            title=site.xpath('./text()').extract_first()#         分布式系统常见的事务处理机制
            fname=title.strip()# title的内容有空格，需要通过strip()去掉空格，否则无法生成文件名
            link=site.xpath('./@href').extract_first()
            '''原始的site.xpath('./@href')是[<Selector xpath='./@href' data=u'/kkkloveyou/article/details/72615103'>]
            通过extract_first()转换为u'/kkkloveyou/article/details/50942275'数据'''
            #links=os.path.join(os.path.dirname(response.url)+link) response.urljoin替代
            links=response.urljoin(link)
            yield scrapy.Request(links,meta={'item': fname},callback=self.savepipelines)
            #yield scrapy.Request(links,meta={'item': fname},callback=self.savehtml) #save html
            #yield scrapy.Request(links,meta={'item': fname},callback=self.savelog)#meta={'item': fname}是向下传递到response的参数，子程序通过response.meta['item']接收
    def savehtml(self,response):
        title=response.meta['item']
        print title
        file=open(title+'.html','w+')
        file.write(response.body)
        file.close()
    def savelog(self,response):
        res=response.xpath("//div[@id='article_content']//text()").extract()
        title=response.meta['item']
        print title
        file = codecs.open(title+'.html', 'w+', encoding='utf-8')
        for line in res:
            file.write(line)
        file.write('-'*150)
    def savepipelines(self,response):
        res=response.xpath("//div[@id='article_content']//text()").extract()
        title=response.meta['item']
        item=App01Item()        
        item['title']=title
        item['link']=res
        return item
        
        
        
        
        
        