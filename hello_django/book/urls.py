"""hello_django URL Configuration

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

from book import views

urlpatterns = [
    # url(r'^$', views.index1),
    url(r'article/$', views.article),
    url(r'index/$', views.article1, name='book_article1'),
    url(r'^article_new/$', views.article_new, name='book_article_new'),
    url(r'outer_html/$', views.outer_html),
    url(r'^t1/$', views.t1),
    url(r'^t2/$', views.t2),
    url(r'^t3/$', views.t3),
]







