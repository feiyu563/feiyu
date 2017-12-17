# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class monitor_user(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=50,unique=True)
    createtime=models.DateField(auto_now_add=True)
    login_ip=models.GenericIPAddressField()
    def __unicode__(self):  #订制字符串显示返回值类型
        return self.username
class moniter_servergroup(models.Model):
    group_name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):  #订制字符串显示返回值类型
        return self.group_name
class moniter_server(models.Model):
    host_name=models.CharField(max_length=20,unique=True)
    host_ip=models.GenericIPAddressField()
    host_group=models.ForeignKey(moniter_servergroup)
    cpu_num=models.IntegerField()
    mem_num=models.IntegerField()
    host_status=models.IntegerField(default=1)#主机状态,0为正常在线,1为离线,2为资源占用过高
    def __unicode__(self):  #订制字符串显示返回值类型
        return self.host_name

class moniter_conf(models.Model):
    pass
class moniter_task(models.Model):
    task_name=models.CharField(max_length=20,unique=True)
    task=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    start_time=models.DateTimeField()
    host=models.ManyToManyField(moniter_server)
    def __unicode__(self):  #订制字符串显示返回值类型
        return self.task_name