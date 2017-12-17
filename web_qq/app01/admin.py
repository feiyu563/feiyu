# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app01 import models
# Register your models here.

admin.site.register(models.chatroom)
admin.site.register(models.chataccount)