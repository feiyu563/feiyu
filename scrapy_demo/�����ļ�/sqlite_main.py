#coding=utf8
import sqlite3
conn=sqlite3.connect('db.sqlite3')
cursor=conn.cursor()
'''sql=
CREATE TABLE demo(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   TP             BLOB
);
'''
#sql='INSERT INTO demo (ID, NAME, AGE, ADDRESS,TP) VALUES (2 ,\'dd\', 1, 1,\'ss\');'
sql='SELECT * FROM demo;'
cursor.execute(sql)
rev=cursor.fetchall()
#conn.commit() #写入或者删除数据使用
print cursor.rowcount
print rev

cursor.close()
conn.close()