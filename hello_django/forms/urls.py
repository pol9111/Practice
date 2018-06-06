from django.conf.urls import url, include
from django.contrib import admin

from forms import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.home, name='forms_home'),
    url(r'^login$', views.login, name='forms_login'),
    url(r'^logout$', views.logout, name='forms_logout'),
    url(r'^register$', views.register, name='forms_register'),
]