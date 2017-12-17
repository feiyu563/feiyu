#coding=utf8
# with open('c:\\22.txt') as f:
#     for i in f.readlines():
#         print i
# while 1==1:
#     print 'i m'
import urllib2

c=urllib2.urlopen('http://192.168.30.25:5000/v2/_catalog')


print c.read()
