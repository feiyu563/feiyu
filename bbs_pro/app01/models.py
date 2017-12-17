# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class bbs(models.Model):  #bbs列表系统表
    category=models.ForeignKey('category')
    title=models.CharField(max_length=64)
    summary=models.CharField(max_length=256,blank=True,null=True)
    content=models.TextField()
    author=models.ForeignKey('bbs_user')
    view_count=models.IntegerField()
    ranking=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class category(models.Model):
    name=models.CharField(max_length=32,unique=True) #unique属性，该字段内容唯一
    administrators=models.ForeignKey('bbs_user')
    def __unicode__(self):
        return self.name
class bbs_user(models.Model): #bbs用户表
    user=models.OneToOneField(User)
    signature=models.CharField(max_length=128,default='这家伙太懒，什么都没留下')
    photo=models.ImageField(upload_to='upload_imgs/',default='upload_imgs/1.gif')
    def __unicode__(self):
        return self.user.username
    

