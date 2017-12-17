#06606e782a4c7fad25dd5da35ae5dacd483ecf095539db825fcf550e6c7ab262
#coding=utf8
'''
urllib2库基本用法
'''
import urllib2
response=urllib2.urlopen('http://192.168.112.116:5000/v2/images/06606e782a4c7fad25dd5da35ae5dacd483ecf095539db825fcf550e6c7ab262/json')#普通方式打开一个网页
print response.read()#读取网页内容

#request写法（推荐）
# request=urllib2.Request('http://www.win4000.com/wallpaper_2285_0_0_1.html')
# response=urllib2.urlopen(request)
# print response.read()