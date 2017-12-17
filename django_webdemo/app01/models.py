#coding=utf8
'''
创建数据库字段及属性

先在settings.py中添加上models所在的web app项目名，如
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]

python manage.py createsuperuser 创建django默认admin管理页面的管理员

2.继续执行下面命令
python manage.py makemigrations app01  #django数据库更新
python manage.py migrate  #更新数据库

参数属性:
max_length 最大长度
default    是默认值
null       是否允许为空
auto_now_add    为添加时的时间，更新对象时不会有变动。
auto_now        无论是你添加还是修改对象，时间为你添加或者修改的时间。
max_digits      最大整数长度
decimal_places  小数位保留长度
primary_key    主键
auto_created   自动递增
'''
from django.db import models
from app01.views import login
class account_group(models.Model):
    groupname=models.CharField(max_length=20)
    
class sex_model(models.Model):
    sex_x=models.CharField(max_length=3)
    def __unicode__(self):  #订制字符串显示返回值类型
        return self.sex_x
    
class db_account(models.Model):
    #nid=models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=20)#CharField创建varchar属性字段
    passwd=models.CharField(max_length=20)
    sex=models.ForeignKey(sex_model)#mysql外键froeign key如果一个实体的某个字段指向另一个实体的主键,就称为外键
    group=models.ManyToManyField(account_group)
    #models.OneToOneField()一对一
    #models.ManyToManyField()多对多
    card=models.IntegerField(default=100000000)
    age=models.IntegerField(default=1)
    isstduent=models.BooleanField(default=False) #NullBooleanField 是可以为空的布尔类型
    phone=models.CharField(null=True,max_length=11)
    create_time=models.DateField(auto_now_add=True)
    login_time=models.DateTimeField(auto_now=True)
    money=models.DecimalField(max_digits=10,decimal_places=2)#小数型
    login_ip=models.GenericIPAddressField()