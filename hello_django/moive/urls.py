from django.conf.urls import url, include
from django.contrib import admin

from moive import views

urlpatterns = [
    url(r'^mt1/([a-z]+)/$', views.mt1),
    url(r'test/$', views.test, name='test'),
    url(r'^new/(?P<aaa>\w+)/$', views.new,name='mnew'),
    url(r'^base/$', views.base),
    url(r'^zi/$', views.zi),

]