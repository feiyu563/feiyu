# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User,Group
from Serializers import UserSerializer,GroupSerializer
from app01 import models
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET','PUT','POST','DELETE'])
def djangousers(request,id=None):
    if request.method=='POST':
        data=request.POST #get response :<QueryDict: {u'username': [u'zjkbb'], u'is_staff': [u'0'], u'email': [u'jikun.zhang@pactera.com']}>
        user_obj=UserSerializer(data=data)
        if user_obj.is_valid():
            user_obj.save()
            return HttpResponse('Save ok')
        else:
            return Response(user_obj.errors,status=500)
    elif request.method=='PUT':
        data=request.data
        user_object=User.objects.get(id=id)
        user_obj=UserSerializer(user_object,data=data)
        if user_obj.is_valid():
            user_obj.save()
            return HttpResponse('Update ok')
        else:
            return Response(user_obj.errors,status=500)
    