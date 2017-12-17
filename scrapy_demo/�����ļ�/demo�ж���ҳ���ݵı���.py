#coding=utf8
import chardet
import urllib,urllib2,hashlib,json
'''
f = open('/path/file.txt',r)
data = f.read()
print chardet.detect(data)
'''
response = urllib2.urlopen('http://www.baidu.com')
data=response.read()
print chardet.detect(data)