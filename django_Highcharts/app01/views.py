# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
import json
import time
import random
from django.http.response import HttpResponse


# Create your views here.
def data(request):
    '''
    [[1147651200000,67.79],
[1147737600000,64.98],
[1147824000000,65.26],
[1147910400000,63.18],
[1147996800000,64.51],
[1148256000000,63.38],
[1148342400000,63.15],
[1148428800000,63.34],
[1148515200000,64.33],
[1148601600000,63.55],
[1148947200000,61.22],
[1149033600000,59.77],]
    
    '''
    return_data=[]
    day_time=86400
    for i in range(100000):
        return_data.append([(time.time()-day_time)*1000,random.randrange(100)])
        day_time-=1
    return HttpResponse(json.dumps(return_data))
def index(request):
    return render_to_response('index.html')
