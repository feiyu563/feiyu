# -*- coding: utf-8 -*-
import scrapy
import sqlite3
import time
import random
class Demo2Spider(scrapy.Spider):
    name = "demo2"
    download_delay = 0.3
    start_urls = ['http://1024.luj8le.net/pw/thread.php?fid=3&page=']
    def parse(self, response):
        db = sqlite3.connect("./movies_1024.db")
        cursor = db.cursor()
        sqls = ["DROP TABLE IF EXISTS movies","DROP TABLE IF EXISTS nomovies","create table movies (id integer primary key,name text)","create table nomovies (id integer primary key,url text)"]
        for sql in sqls:
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
        url=response.url
        for a in range(9):
            link=url+str(a+1)
            yield scrapy.Request(link, callback=self.ip_add)
    def ip_add(self,response):
        titles = response.xpath("//tr[@class='tr3 t_one']//h3/a")
        print len(titles)
        for title in titles:
            siteurl = title.xpath('./@href').extract_first()
            siteurl_pass="http://1024.luj8le.net/pw/"+siteurl
            yield scrapy.Request(siteurl_pass,meta={'retry': 6},callback=self.findname)
    def con(self, name,url):
        try:
            db = sqlite3.connect("./movies_1024.db")
            cursor = db.cursor()
            sql='insert into movies values (NULL ,\"'+name+'\");'
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
        except Exception,e:
            print "存储数据出现了错误 ："
        finally:
            self.nodata(url)
    def nodata(self,url):
        db = sqlite3.connect("./movies_1024.db")
        cursor = db.cursor()
        sql='insert into nomovies values (NULL ,\"'+url+'\");'
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()   
    def findname(self,response):
        sites=response.xpath("//div[@id='read_tpc']") #提取出所有文本
        times=response.meta['retry']
        titles=''
        title_old=sites.xpath(".//text()").extract()
        #url_old=sites.xpath("./a/text()").extract()
        if len(title_old)>0:
            for title in title_old:
                titles=titles+title
            self.con(titles,response.url)
        else:
            print response.url+" -------retry times "+str(7-times)
            timenext=times-1
            if timenext>0:
                yield scrapy.Request(response.url, meta={'retry': timenext},callback=self.findname)
            else:
                self.nodata(response.url)
            



