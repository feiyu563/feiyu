# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from app01 import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
# columns = Column.objects.all()
# articles = Article.objects.all()
def index(request):
    return_data = models.userinfo.objects.all()
    paginator = Paginator(return_data, 10) #每页数据条数
    page = request.GET.get('page')
    if page:
        article_list = paginator.page(page).object_list
    else:
        article_list = paginator.page(1).object_list
    try:
        cus_list = paginator.page(page)
    except PageNotAnInteger:
        cus_list = paginator.page(1)
    except EmptyPage:
        cus_list = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'cus_list': cus_list, 'article_list': article_list})

def data(request):
    for i in range(2000):
        p=models.userinfo(username='zjk'+str(i),email='zjk'+str(i)+'@cctv.com',phone=str(i))  #写入数据库数据
        p.save()    #保存写入数据
        print 'save zjk'+str(i)+'ok!'
    return HttpResponse('ok')