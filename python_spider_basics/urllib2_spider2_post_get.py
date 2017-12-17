#coding=utf8
'''
urllib2库post and get
'''
import urllib
import urllib2

#post方法
#----------------------------------------------
key={"name":"admin","password":"511zjk","autologin":0,"enter":"Sign in"}#登录参数
data=urllib.urlencode(key) #格式化字符串为 name=admin&password=511zjk。。。。。
url="http://172.16.15.140/zabbix/index.php"
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()
#---------------------------------------------
#get方法
#---------------------------------------------
key={}
key["name"]="admin"
key["password"]="511zjk"
key["autologin"]=1
key["enter"]="Sign in"
data=urllib.urlencode(key)
url="http://172.16.15.140/zabbix/index.php"
geturl=url+"?"+data
request=urllib2.Request(geturl)
response=urllib2.urlopen(request)
print response.read()
#----------------------------------------
#put or delete 方法
#------------------------------------------
key={"name":"admin","password":"511zjk","autologin":0,"enter":"Sign in"}#登录参数
data=urllib.urlencode(key)
url="http://172.16.15.140/zabbix/index.php"
request = urllib2.Request(url, data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)