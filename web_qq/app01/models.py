# -*- coding: utf-8 -*-
'''
django admin 
用户名 root
密码    511573zjk

创建数据库字段及属性
先在settings.py中添加上models所在的web app项目名，如
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]

python manage.py createsuperuser 创建django默认admin管理页面的管理员

2.继续执行下面命令
python manage.py makemigrations app01  #django数据库更新
python manage.py migrate  #更新数据库

参数属性:
max_length 最大长度
default    是默认值
null       是否允许为空
auto_now_add    为添加时的时间，更新对象时不会有变动。
auto_now        无论是你添加还是修改对象，时间为你添加或者修改的时间。
max_digits      最大整数长度
decimal_places  小数位保留长度
primary_key    主键
auto_created   自动递增
'''
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class chatroom(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name
class chataccount(models.Model):
    room=models.ForeignKey(chatroom)
    user=models.ForeignKey(User)
    def __unicode__(self):
        return self.room