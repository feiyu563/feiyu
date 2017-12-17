# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TaobaotpPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json  
import codecs  
class TaobaotpPipeline(object):  
    def __init__(self):  
        self.file = codecs.open('firstspi.json', 'wb', encoding='utf-8')  
  
    def process_item(self, item, spider):  
        print item
        #line = json.dumps(dict(item)) + '\n'  
        line = json.dumps(dict(item),encoding='utf-8', ensure_ascii=False) + '\n'  
        #print line
        self.file.write(line)
        return item
