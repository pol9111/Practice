from django.conf.urls import url, include
from django.contrib import admin

from music import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^music2/$', views.music2),

        ]
