from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import BlogModel


def index(request):
    return render(request, 'demo_index.html')


# 发布博客
def add(request):
    if request.method == 'GET':
        return render(request, 'demo_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title, content)
        blog = BlogModel(title=title, content=content)
        blog.save()
        return HttpResponse('获取数据')


def list(request):
    return render(request, 'demo_list.html')


def detail(request):
    return render(request, 'demo_detail.html')


def t1(request):
    return HttpResponse('1')