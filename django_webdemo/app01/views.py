#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render

from django.views.decorators.csrf import requires_csrf_token
from django.template.context import RequestContext
import json
import models

from forms.accountform import LoginForm
from django.contrib.auth.decorators import login_required


html_area = {
        '北京':['朝阳区', '昌平区', '怀柔区', '海淀区'],
        '山东':['菏泽市', '威海市', '淄博市', '济南市', '德州市'],
        '安徽':['六安市', '合肥市', '安庆市', '阜阳市', '巢湖市', '芜湖市', '马鞍山市', '黄山市', '蚌埠市', '宿州市']
        }
'''
html_area = {
        'beijing':['chaoyang', 'changpin', 'huairou', 'haidian'],
        'shandong':['heze', 'weihai', 'zibo', 'jinan', 'dezhou'],
        'anhui':['luan', 'hefei', 'anqing', 'fuyang', 'chaohu', 'wuhu', 'maanshan', 'huangshan', 'bongbu', 'suzhou']
        }'''
        
def Index(request):
    return HttpResponse(r'<h1>Hello World !</h1>')  # #return text func
#----------------------------------------------------
def denglu(request):
    return render_to_response('index.html')  # return html func
    print request.GET
#----------------------------------------------------
def auth(request):
    print request.GET
    if request.GET['username'] == 'admin' and request.GET['password'] == '1234':
        return HttpResponse('welcome you !your name:' + request.GET['username'] + '\nyour password:' + request.GET['password'])
    else:
        return HttpResponse('Wrong username or password!Get f**k out of my site!')
#----------------------------------------------------
def getregion(request):
    if request.GET['val'] == 'All':
        rel = json.dumps(html_area)
    else:
        rel = json.dumps(html_area[request.GET['val'].encode('utf-8')])  #字符编码问题解决.encode('utf-8') 
    return HttpResponse(rel)
#----------------------------------------------------
def userlist(request,id):
    namelist=['zjk','ddx','xxd']
    print id
    if id:
        if int(id)>=0 and int(id)<len(namelist):
            val='<br />'+namelist[int(id)]
            return HttpResponse('<h1>'+val+'</h1>')
    val='<br />'.join(namelist)  #join 拼接字符串，将数组中的元素分别拼接到字符串中
    return HttpResponse('<h1>'+val+'</h1>')
#----------------------------------------------------
def model(request,id):
    print id
    return render_to_response('model.html',{'key1':id,'key2':id,'item_list':['xiaomi','meizu','apple','iphone','huawei','chuizi']}) #模版语言传递参数
#----------------------------------------------------
#老的login方式
def login(request):
    data={'login_status':''}
    if request.method=='POST':
        postdata=request.POST
        csrf_val=postdata.get('csrfmiddlewaretoken')
        username=postdata.get('username')
        password=postdata.get('password')
        print username,password
        if username or password:
            check=models.db_account.objects.filter(name=username,passwd=password).count()
            if check>=1:
                return redirect('/menu')  #跳转到
            else:
                data['login_status']='用户名密码错误！'
        else:
            data['login_status']='帐号密码不能为空'
             
    return render(request,'login/login.html',data)
    #return render_to_response('login.html',data,context_instance=RequestContext(request))
#新的login方式
def loginform(request):
    if request.method == 'POST':
        data=request.POST
        logindata=LoginForm(data)
        logindata.as_table
        if logindata.is_valid():
            return render(request,'loginform.html',{'user_data':request.META})
        else:
            return render(request,'loginform.html',{'login_status':logindata})
    logindata=LoginForm()
    return render(request,'loginform.html',{'login_status':logindata})
#----------------------------------------------------
def son(request):  #html模版继承
    return render_to_response('master/son.html')

def Sqlmodel(request,id):
    print type(id)
    if id=='1':
        p=models.sex_model(sex_x='y')  #写入数据库数据
        p.save()    #保存写入数据
    elif id=='2':
        p=models.sex_model.objects.get(id='3') #查询ID=3的记录
        p.sex_x='c' #设置sex_x=c
        p.save() #保存写入数据
    elif id=='3':
        p=models.sex_model.objects.filter(id='2').update(sex_x='公') #更新数据，返回的是影响条数
    elif id=='4':
        p=models.sex_model.objects.filter(sex_x__contains='白').update(sex_x='黑') #模糊匹配更新sex_x是字段  __contains固定后缀
    elif id=='5':
        p=models.sex_model.objects.filter(sex_x__contains='y').delete() #删除，返回影响行数 3{u'app01.sex_model': 3L}
    elif id=='6':
        p=models.sex_model.objects.filter(sex_x__contains='n').count() #[0]返回第N条，[0:2]前两条
    else:
        p=models.sex_model(sex_x=id)
        p.save()
    return HttpResponse(p)

def menu(request):
#     if id=='1':
#         return redirect('/menu_user')
    return render_to_response('login/menu_index.html')

def menu_user(request,uid):
    if uid!='0':
        return redirect('/menu_user_all/'+uid)
    else:
        p=models.db_account.objects.all()
        return render_to_response('login/menu_user.html',{'user_data':p})
def menu_user_all(request,uid):
    print uid
    m=models.db_account.objects.get(id=int(uid))
    return render_to_response('login/menu_user_all.html',{'item':m})