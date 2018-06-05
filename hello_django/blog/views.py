from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse

# Create your views here.
from blog.form import AddForm
from blog.models import BlogModel
from .models import User


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
    blog_list = BlogModel.objects.all()
    return render(request, 'demo_list.html',
                  context={
                      'blog_list': blog_list,
                  })


def detail(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id) # 关键 id=传入的参数
    return render(request, 'demo_detail.html',
                  context={
                      'blog': blog,
                  })


def edit(request, blog_id):
    if request.method == 'GET':
        blog = BlogModel.objects.get(id=blog_id)
        return render(request, 'demo_edit.html',
                      context={'blog': blog,})
    elif request.method == 'POST':
        blog = BlogModel.objects.get(id=blog_id)
        if blog:
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog.title = title
            blog.content = content
            blog.save()
            return HttpResponse('修改成功')
        else:
            return HttpResponse('没有此博客')
    else:
        return HttpResponse('不能被处理的操作')


def delete(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if blog:
        blog.delete()
        return redirect(reverse('blog_list'))
    else:
        return HttpResponse('没了')


def add1(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # a = form.cleaned_data['a']
            # b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']
            rs = User.objects.filter(username=c)
            if rs:
                return HttpResponse('用户已存在')
            else:
                User.objects.create(username=c, password=d)
                # return HttpResponse(str(int(a) + int(b)))
                return HttpResponse('注册成功')

    else:
        form = AddForm
    return render(request, 'add1.html', {'form': form})


def t1(request):
    return HttpResponse('1')

