#coding=utf8
'''
Created on 2017年5月15日
数据库查询接口（传统）
@author: Administrator
'''
import MySQLdb
def getlist(sql):
    db=MySQLdb.connect('127.0.0.1','zjk','511573','db_account',3306)
    cursor=db.cursor() #获取数据游标
    cursor.execute(sql) #执行sql语句
    data=cursor.fetchall() #获取所以执行后返回的数据
    cursor.close()
    db.close()
    return data
def getsingle(sql):
    db=MySQLdb.connect('127.0.0.1','zjk','511573','db_account',3306)
    cursor=db.cursor() #获取数据游标
    cursor.execute(sql) #执行sql语句
    data=cursor.fetchone() #获取所以执行后返回的数据
    db.close()
    return data