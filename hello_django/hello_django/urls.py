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
from django.conf.urls import url, include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^book/', include('book.urls')),
    url(r'^moive/', include('moive.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^model1/', include('model1.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^forms/', include('forms.urls')),
    # url(r'^hello/$', views.index),
    # url(r'^hello_python/$', views.hello_python),
    # url(r'^hello_php/$', views.hello_php),
    # url(r'^hello_customized/([A-Za-z0-9]+)/$', views.hello_customized),
    # url(r'^add/(\d+)/(\d+)$', views.add),
    # url(r'^hello/(?P<name>\w+)/(?P<num>\d+)/$', views.hello_django),


]














