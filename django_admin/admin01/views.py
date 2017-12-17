from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
import json
from django.template.context import RequestContext
def login(request):
    rel={'resp':''}
    if request.method=='POST':
        postdata=request.POST
        username=postdata.get('username')
        password=postdata.get('password')
        print username
        if username=='admin' and password=='123':
            rel['resp']='OK'
        else:
            rel['resp']='Error'
    print rel
    return render_to_response('login.html',rel)