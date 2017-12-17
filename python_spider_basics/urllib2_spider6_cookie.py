#coding=utf8
'''
urllib2库构建proxy
'''
import urllib
import urllib2
import cookielib

# #声明一个cookiejar对象实例来保存cookie
# cookie=cookielib.CookieJar()
#    
# #利用urllib2的httpcookieProcessor对象来创建cookie处理器
#    
# handler=urllib2.HTTPCookieProcessor(cookie)
#    
# #通过handler构建opener
#    
# opener=urllib2.build_opener(handler)
#    
# respons=opener.open("http://www.baidu.com")
#    
# for item in cookie:
#     print "Name = "+item.name
#     print "Value = "+item.value
    
    
    
#--------------------------------------------------------------------
#保存Cookie到文件
#---------------------------------------------------------------------
#设置保存cookie的文件
filename='cokie.txt'
key={"name":"admin","password":"511zjk","autologin":0,"enter":"Sign in"}#登录参数
data=urllib.urlencode(key)
url="http://172.16.15.140/zabbix/index.php"
#声明一个MozillaCookieJar对象实例来保存cookie

cookie=cookielib.MozillaCookieJar(filename)
  
#利用urllib2的HTTPCookieProcessor对象类创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
  
#通过handler构建opener
opener=urllib2.build_opener(handler)
  
response=opener.open(url,data)
  
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True) 
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来
#ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入



#-------------------------------------------------------------------------
#从文件获取cookie并访问
#---------------------------------------------------------------------
url="http://172.16.15.140/zabbix/index.php"
#创建MozillaCookieJar实例对象
cookie=cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cokie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req=urllib2.Request(url)
#利用urllib2的build_opener方法创建一个opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open(req)
print response.read()















