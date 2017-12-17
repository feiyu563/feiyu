#coding=utf8
from app01 import DataSQL
sql='select * from h_hqrjacc;'
data=DataSQL.getlist(sql)
#a=[i for i in data] #非迭代器
#print a
# b=(i for i in data) #迭代器
# print len(data)
# print b.next()
for i in data:
    print i[0]