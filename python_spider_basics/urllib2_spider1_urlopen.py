#coding=utf8
'''
urllib2库基本用法
'''
import urllib2
response=urllib2.urlopen('http://www.win4000.com/wallpaper_2285_0_0_1.html')#普通方式打开一个网页
print response.read()#读取网页内容

#request写法（推荐）
request=urllib2.Request('http://www.win4000.com/wallpaper_2285_0_0_1.html')
response=urllib2.urlopen(request)
print response.read()