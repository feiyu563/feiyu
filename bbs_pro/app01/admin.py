# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app01 import models
# Register your models here.
class bbs_admin(admin.ModelAdmin):
    #定义列名
    list_display=('title','summary','author','view_count','signature','ranking','created_at','update_at')
    #定义筛选
    list_filter=('created_at',)
    #定义搜索
    search_fields=('title','author__user__username',)
    def signature(self,obj):
        return obj.author.signature
admin.site.register(models.bbs,bbs_admin)
admin.site.register(models.bbs_user)
admin.site.register(models.category)