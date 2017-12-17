#coding=utf8
'''
urllib2库构建heads属性
'''
import urllib
import urllib2

key={"name":"admin","password":"511zjk","autologin":0,"enter":"Sign in"}#登录参数
data=urllib.urlencode(key) #格式化字符串为 name=admin&password=511zjk。。。。。
url="http://172.16.15.140/zabbix/index.php"
referer='http://172.16.15.140/zabbix/'
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64)'  #设置heads的User-Agent属性
headers={'User-Agent':user_agent,'Referer':referer}#设置heads的User-Agent属性
request=urllib2.Request(url,data,headers)#代入heads的User-Agent属性
response=urllib2.urlopen(request)
print response.read()
#urllib2下载图片
url="http://pic.jj20.com/up/allimg/811/0H514115008/140H5115008-2.jpg"
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64)'
referer='http://www.jj20.com/bz/nxxz/nxmt/7244.html'
headers={'User-Agent':user_agent,'Referer':referer}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
with open('1.jpg','w+') as f:
    f.write(response.read())
    f.close()