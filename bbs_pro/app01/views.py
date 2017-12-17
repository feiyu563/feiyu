# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import models
from django.http.response import HttpResponseRedirect
from django.contrib import auth
import django_comments
# Create your views here.
def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!
        
        <a href='/logout/' >Logout</a>
        
         ''' % user.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
    

def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>Re-login</a>" % user)


def Login(request):
    return render_to_response('login.html')

#------------------------------------------------------------login



def index(request):
    bbs_list=models.bbs.objects.all()
    category_list=models.category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,
                                            'user':request.user,
                                            'category':category_list
                                            })
def bbs_detail(request,bbs_id):
    bbs=models.bbs.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs,
                                                 'user':request.user,
                                                 })
def sub_comment(request):
    if request.method=='POST':
        get_data=request.POST
        detail_id=get_data['bbs_id']
        detail_data=get_data['comment_content']
        django_comments.models.Comment.objects.create(
                                content_type_id = 8,
                                object_pk= detail_id,
                                site_id = 1,
                                user = request.user,                       
                                comment =   detail_data,                   
                                                       )
    return HttpResponseRedirect('/detail/'+detail_id)
def category(request,id):
    bbs_list=models.bbs.objects.filter(category__id=id)
    category_list=models.category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,
                                            'user':request.user,
                                            'category':category_list,
                                            'now_id':int(id),
                                            })