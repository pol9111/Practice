from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [
    # r'^$' != r'' 前者就等于用blog当首页，后者下面的链接都被r''覆盖
    url(r'^$', views.index, name='blog_index'),
    url(r'^add/$', views.add, name='blog_add'),
    url(r'^list/$', views.list, name='blog_list'),
    url(r'^detail/$', views.detail, name='blog_detail'),
    url(r'^t1/$', views.t1),
]