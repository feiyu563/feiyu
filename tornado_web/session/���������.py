#coding=utf8
#by:zjk
session_container={}
class mydict(object):
    
    def __init__(self):
        dict={}
#     def __getitem__(self,key):
#         print '__getitem__'
#         print key
#     def __setitem__(self,key,value):
#         print '__setitem__'
#         print key,value
    def __delitem__(self,key):
        print key
    def __setitem__(self,key,value):
        temp={key:value}
        session_container[key]=temp
    def __getitem__(self,key):
        val=session_container[key]
        return val
    
m=mydict()
m[1]='zjk'  #执行的是__setitem__函数
print m[1]  #执行的是__getitem__函数