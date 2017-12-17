#coding=utf8
#by:zjk
import hashlib
import time
session_container={}
class my_seesion(object):
    def __init__(self,request):
        self.__request = request #创建私有变量__request
        self.initialize() #执行初始化函数
    def initialize(self):
        id=self.__request.get_cookie('__my_sessionid__')
        if not id: #如果不存在cookie,则生成一个基于时间的md5 cookie
            ha=hashlib.md5()
            ha.update(str(time.time()))
            val=ha.hexdigest()
            self.__request.set_cookie('__my_sessionid__',val,expires_days=1) #设置cookie,并设置过期时间
        self.__id=id
        print 'cookie: '+id
    def __setitem__(self,key,value):
        temp={key:value}
        print temp
        session_container[self.__id]=temp
    def __getitem__(self,key):
        if session_container.has_key(self.__id):
            val=session_container[self.__id][key]
            print val
        else:
            val=None
            print val
        return val
            