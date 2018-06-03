from django.conf.urls import url, include
from django.contrib import admin

from model1 import views

urlpatterns = [
    url(r'^add_user/$', views.add_user),
    url(r'^search_user/$', views.search_user),
    url(r'^update_user/$', views.update_user),
    url(r'^delete_user/$', views.delete_user),
    url(r'^add_info/$', views.add_info),
    url(r'^search_info/$', views.search_info),
]
