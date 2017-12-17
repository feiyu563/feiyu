# -*- coding: utf-8 -*-

def page(baseurl,totalnum,currentpage):
    perpage=20 # 每页显示条数
    pagenum=11 #页面显示多少页
    temp=divmod(totalnum, perpage) #计算商也余数
    totalpage=temp[0]
    if temp[1]:   #如果存在余数,加一页
        totalpage+=1
    start=1
    if currentpage>6:
        start=currentpage-5