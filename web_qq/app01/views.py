# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from app01 import models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json

msg_dic={}
# Create your views here.
def login(request):
    if request.method=='POST':
        username,password=request.POST.get('username'),request.POST.get('password')
        req=auth.authenticate(username=username,password=password)
        if req is not None:
            auth.login(request, req)
            return redirect('/index')
        else:
            return render_to_response('login.html',{'login_error':'用户名或密码错误!'})
    else:
        return render_to_response('login.html')
def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>返回首页</a>" % user)

#----------------------------------上面是django自带的登录验证-------------------------------------

def index(request):
    rooms=models.chatroom.objects.all()
    return render_to_response('index.html',{'rooms':rooms,'user':request.user})

@login_required #导入装饰器,配置url
def room(request,id):
    models.chataccount.objects.filter(user=request.user).delete()
    roomobj=models.chatroom.objects.get(id=id)
    c=models.chataccount(room=roomobj,user=request.user)
    c.save()
    memberlist=models.chataccount.objects.filter(room=roomobj)
    return render_to_response('room.html', {'roomobj':roomobj,'memberlist':memberlist,'user':request.user})

def savemsg(request):
    id,msg,sendtime,roomid,user=request.POST.get('id'),request.POST.get('msg'),request.POST.get('sendtime'),request.POST.get('roomid'),request.POST.get('user')
    if msg_dic.has_key(int(roomid)):
        msg_dic[int(roomid)].append([id,msg,sendtime,user])
    else:
        msg_dic[int(roomid)]=[[id,msg,sendtime,user],]
    return HttpResponse('ok')
def getmsg(request):
    roomid=request.GET.get('roomid')
    msglist=[]
    if msg_dic.has_key(int(roomid)):
        msglist=msg_dic[int(roomid)] 
    return HttpResponse(json.dumps(msglist))