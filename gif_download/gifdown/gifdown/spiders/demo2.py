# -*- coding: utf-8 -*-
import scrapy
import os
import urllib2
class downItem(scrapy.Item):
    image_urls=scrapy.Field()
class Demo1Spider(scrapy.Spider):
    name = "demo2"
    download_delay=0.1
    #allowed_domains = ["www.gaoxiaogif.com"]
    start_urls = ['http://www.jj20.com/bz/nxxz/']
    def parse(self, response):
        url=response.xpath(u"//div[@class='page']/a[text()='下一页']/@href").extract_first()#获取下一页的url
        nexturl=response.urljoin(url)
        gifurl=response.xpath("//ul[@class='pic2 vvi fix']/li/a[1]/@href").extract()#获取详情页面
        for i in gifurl:
            gifmore=response.urljoin(i)
            yield scrapy.FormRequest(gifmore,callback=self.parse_gif)
        yield scrapy.Request(nexturl,callback=self.parse)

    def parse_gif(self,response):
        bigimg=response.xpath("//ul[@id='showImg']/li/a/@href").extract()#处理图片连接，生成图片连接列表
        for x in bigimg:
            nexturl=os.path.join(os.path.dirname(response.url)+'/'+x)
            yield scrapy.Request(nexturl,callback=self.parse_down)
        yield scrapy.Request(response.url,callback=self.parse_down)
    def parse_down(self,response):
        head={'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0','Referer':response.url}
        bigjpg=response.xpath("//img[@id='bigImg']/@src").extract_first()
        pathurl=bigjpg.split('/')[-1]
        request=urllib2.Request(bigjpg,headers=head)
        response=urllib2.urlopen(request,timeout=3)
        img=response.read()
        if img:
            with open("./full/"+pathurl,'wb') as f:
                f.write(img)
                f.close()
                print 'img down ok'
        else:
            print 'timeout'
        