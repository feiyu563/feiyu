# coding=utf8
from __future__ import unicode_literals

from django.contrib import admin
from monitor import models
# Register your models here.
class monitor_user(admin.ModelAdmin):
    #定义列名
    list_display=('username','password','createtime','login_ip')
    #定义筛选
    list_filter=('login_ip',)
    #定义搜索
    search_fields=('username',)
    def signature(self,obj):
        return obj.author.signature

class moniter_server(admin.ModelAdmin):
    #定义列名
    list_display=('host_name','host_ip','host_group','host_status')
    #定义筛选
    list_filter=('host_name',)
    #定义搜索
    search_fields=('host_name',)
    def signature(self,obj):
        return obj.author.signature
class moniter_task(admin.ModelAdmin):
    #定义列名
    list_display=('task_name','task','create_time','start_time')
    #定义筛选
    list_filter=('start_time',)
    #定义搜索
    search_fields=('start_time',)
    def signature(self,obj):
        return obj.author.signature
admin.site.register(models.monitor_user,monitor_user)
admin.site.register(models.moniter_servergroup)
admin.site.register(models.moniter_server,moniter_server)
admin.site.register(models.moniter_task,moniter_task)