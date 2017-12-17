# -*- coding: utf-8 -*-
import scrapy
import sqlite3

class Demo1Spider(scrapy.Spider):
    name = "demo1"
    #allowed_domains = ["www.kuaidaili.com"]
    start_urls = ['http://www.kuaidaili.com/free/inha/']

    def parse(self, response):
        db = sqlite3.connect("./proxy_ip.db")
        cursor = db.cursor()
        sql = "DROP TABLE proxy_ipaddrs"
        cursor.execute(sql)
        db.commit()
        sql = "create table proxy_ipaddrs (id integer primary key,IP varchar(30))"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

        url=response.url
        for a in range(1655):
            link=url+str(a+1)
            yield scrapy.FormRequest(link, callback=self.ip_add)
    def con(self,addrs):
        db = sqlite3.connect("./proxy_ip.db")
        cursor = db.cursor()
        for a in addrs:
            val=a
            sql = "insert into proxy_ipaddrs values (NULL,'"+val+"')"
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
    def ip_add(self,response):
        proxy_ip = []
        titles = response.xpath('//tbody/tr')
        for title in titles:
            ipaddr = title.xpath('./td[1]/text()').extract_first()
            portaddr = title.xpath('./td[2]/text()').extract_first()
            proxy_ip.append(ipaddr + ":" + portaddr)
        self.con(proxy_ip)


