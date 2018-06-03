from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


# def index(request):
#     return HttpResponse('hello django!!')
#
#
# def hello_python(request):
#     return HttpResponse('Hello python!')
#
#
# def hello_php(request):
#     return HttpResponse('Hello php!')
#
#
# def hello_customized(request, diy):
#     return HttpResponse('Hello %s' % diy)
#
#
# def add(request, a, b):
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
#
#
# def hello_django(request, name, num):
#     return HttpResponse('Hello %s %s' % (name, num))
#
#
# def index1(request, **kwargs):
#     if kwargs.get('switch') == 'true':
#         return HttpResponse('请先注册')
#
#
#
def article(request, **kwargs):
    return HttpResponse('这是文章首页')


def article1(request, **kwargs):
    if kwargs.get('switch') == 'true':
        return redirect(reverse('book_article_new'))
    return HttpResponse('这是文章首页')

def article_new(request,**kwargs):
    return HttpResponse('这是新的文章首页')


def outer_html(request, **kwargs):
    return render(request, 'pic-move.html')


def t1(request, **kwargs):
    return render(request, 't1.html')


def hello():
    return 'django'


class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        return 'haha'


ap = Fruits('apple', 'red')
lst = ['x', 'y', 'z']
dt = {'a': 1, 'b': 2}


def t2(request):
    return render(request, 't2.html',
                  context={
                   'books_name':'python', #字符串
                   'hello':hello, # 函数
                   'fruits_say':ap.say, # 方法
                   'fruits':ap, # 类对象
                   'list':lst, # 列表
                   'dict':dt, # 字典

                  })



def t3(request):
    test2 = 'THIS IS A LIST!'
    return render(request, 't3.html',
                  context={
                      'test': 'HEAT',
                      'test2': test2,
                      'xx': '',
                      'ss': None,
                      'num1': 1,
                      'num2': 2,
                      'list': lst,
                      'now': datetime.now(),
                      'html': '<h1>hello django</h1>',
                      'float': 3.1415926,
                  })
























