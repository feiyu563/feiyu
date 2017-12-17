#coding=utf8
import sqlite3

db=sqlite3.connect("./proxy_ip.db") #文件形式创建
'''
db=sqlite3.connect("./db3.db") #文件形式创建
db=sqlite3.connect(":memory:")#内存创建
数据库连接对象
打开数据库时返回的对象db就是一个数据库连接对象，它可以有以下操作：
commit()--事务提交    
rollback()--事务回滚   
close()--关闭一个数据库连接   
cursor()--创建一个游标 
    关于commit()，如果isolation_level隔离级别默认，那么每次对数据库的操作，
都需要使用该命令，你也可以设置isolation_level=None，这样就变为自动提交模式。
      游标对象有以下的操作：
        execute()--执行sql语句   
        executemany--执行多条sql语句   
        close()--关闭游标   
        fetchone()--从结果中取一条记录，并将游标指向下一条记录   
        fetchmany()--从结果中取多条记录   
        fetchall()--从结果中取出所有记录   
        scroll()--游标滚动  
'''
cursor=db.cursor()
# sql="create table sipdercata (id integer primary key,name varchar(10) UNIQUE,url text,resures text NULL)"
val='192.168.11.32:8080'
sql="insert into proxy_ipaddrs values (3,"+val+")"
#sql="select * from proxy_ipaddrs"
# sql="update sipdercata set name='Boy' where id = 0"
# sql="delete from sipdercata where id = 1"
#sql="create table proxy_ipaddrs (id integer primary key,IP varchar(30) UNIQUE)"

cursor.execute(sql)
db.commit()
#print cursor.fetchall()

cursor.close()

db.close()