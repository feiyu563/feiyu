# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
class App01Pipeline(object): 
#     def __init__(self):  
#         self.file = codecs.open('firstspi.json', 'wb', encoding='utf-8')  
    def process_item(self, item, spider):
        print item 
#         #line = json.dumps(dict(item)) + '\n'  
#         line = item['title']
#         print line
#         self.file.writelines(line)
#         self.file.close()
#         return item
        pass
#     def josndown(self):
#         
#     def jpgedown(self):

