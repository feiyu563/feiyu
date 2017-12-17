# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from zhuangshiqi import Filteradd
# Create your views here.
def before(request):
#     host=request.META
#     print host
#     if host=='127.0.0.1':
#         return None
#     else:
#         return redirect('http://www.baidu.com')
    return HttpResponse('<h1>500</h1>')
    return HttpResponse('<h1>500</h1>')

def after(request):
#     print 'we doing well!'
    pass
@Filteradd(before, after)
def index(request):
#     z='zjk'
#     raise Exception(z)
#     return HttpResponse(z)
    pass
