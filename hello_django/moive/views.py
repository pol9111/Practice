from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


lst = ['0', '1', 'z']
dt = {'a': 1, 'b': 2}


def mt1(request, name):
    return render(request, 'mt1.html',
                  context={
                      'name1':name,
                      'list':lst,
                      'dict':dt,
                      'html': '<h1>hello django</h1>',
                      'ts1' : 'change'
                  })


def test(request):
    return HttpResponse('test page!!!!')


def new(request, aaa):
    return HttpResponse('这是新的页面')


def base(request):
    return render(request, 'base.html')


def zi(request):
    return render(request, 'zi.html')


