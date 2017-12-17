# -*- coding: utf-8 -*-
import scrapy

class downItem(scrapy.Item):
    image_urls=scrapy.Field()
class Demo1Spider(scrapy.Spider):
    name = "demo1"
    download_delay=3
    #allowed_domains = ["www.gaoxiaogif.com"]
    start_urls = ['http://www.win4000.com/wallpaper_2285_0_0_1.html']
    def parse(self, response):
        nexturl=response.xpath(u"//a[@class='after']/@href").extract_first()#获取下一页的url
        #nexturl=response.urljoin(url)
        gifurl=response.xpath("//ul[@class='main-img clearfix']/li/a/@href").extract()#获取详情页面
        for i in gifurl:
            #gifmore=response.urljoin(i)
            yield scrapy.FormRequest(i,callback=self.parse_gif)
        yield scrapy.Request(nexturl,callback=self.parse)

    def parse_gif(self,response):
        item=downItem()
        bigimg=response.xpath("//ul[@class='ulBigPic']/li/img/@src").extract()#处理图片连接，生成图片连接列表
        item['image_urls']=bigimg
#         for x in bigimg:
#             print x  #只是为了显示图片地址
            #nexturl=os.path.join(os.path.dirname(response.url)+'/'+x)
            #yield scrapy.Request(nexturl,callback=self.parse_down)
        return item    #返回给pipelines处理，return的item一定要是个列表
#     def parse_down(self,response):
#         item=downItem()
#         bigjpg=response.xpath("//img[@id='bigImg']/@src").extract()
#         item['image_urls']=bigjpg
#         return item

        