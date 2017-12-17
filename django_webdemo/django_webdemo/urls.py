"""django_webdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo/', views.Index),
    url(r'^denglu/', views.denglu),
    url(r'^auth', views.auth),
    url(r'^getregion/$', views.getregion),
    #http://www.cnblogs.com/koka24/p/5470029.html
    #url(r'^list/(\d*)', views.userlist),
    #url(r'^list/(\d+)', views.userlist),
    url(r'^list/(?P<id>\d*)', views.userlist, {'id':'0'}),
    url(r'^model/(?P<id>\w*)', views.model),
    url(r'^login/', views.login),
    url(r'^son/$', views.son),
    url(r'^tables/(?P<id>\w*)', views.Sqlmodel),
    url(r'^menu/$', views.menu),
    url(r'^menu_user/(?P<uid>\w*)', views.menu_user),
    url(r'^menu_user_all/(?P<uid>\w*)', views.menu_user_all),
    url(r'^loginform/', views.loginform),
]
