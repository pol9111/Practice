from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponse('hello django!!')


def hello_python(request):
    return HttpResponse('Hello python!')


def hello_php(request):
    return HttpResponse('Hello php!')


def hello_customized(request, diy):
    return HttpResponse('Hello %s' % diy)


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def hello_django(request, name, num):
    return HttpResponse('Hello %s %s' % (name, num))


def index1(request, **kwargs):
    if kwargs.get('switch') == 'true':
        return HttpResponse('请先注册')



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

