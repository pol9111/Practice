from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.


def index(request):
    int('xxx')
    return HttpResponse('hello')


def home(request):
    print(request.myuser)
    username = request.myuser
    # username = request.session.get('username', '未登入') # 到session表get，默认值'未登入'
    return render(request, 'home.html',
                  {'username': username})


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username')
#         request.session['username'] = username
#         return redirect(reverse('forms_home'))
#
#
# def logout(request):
#     # request.session['username'] = None
#     del request.session['username'] # 删除当前会话(登出)
#     # request.session.clear() # 删除当前所有会话
#     # request.session.flush() # 删除当前的会话数据并删除会话的Cookie(数据库的也删了)
#     return redirect(reverse('forms_home'))

from .models import UserModel
from .form import LoginForm,RegisterForm


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html',
                      context={'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            password_repeat = form.cleaned_data.get('password_repeat', None)
            email = form.cleaned_data.get('email', None)
            if UserModel.objects.filter(username=username):
                return HttpResponse('用户已存在')
            elif password == password_repeat:
                user = UserModel()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                return HttpResponse('注册成功')

            else:
                return HttpResponse('注册失败')
        else:
            return HttpResponse('注册失败')


def login(request):
    if request.method == 'GET': # get就返回login页面传入空白表单
        form = LoginForm()
        return render(request, 'login.html',
                      context={'form': form})

    elif request.method == 'POST': # 通过request.method获取用户上传的数据
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            userModel = UserModel.objects.filter(username=username,
                                                 password=password)
            if userModel: # 保持用户登入状态
                request.session['username'] = username
                return redirect(reverse('forms_home'))
            else:
                return redirect(reverse('forms_register'))

def logout(request):
    request.session.flush() # 清空session包括数据库里的
    return redirect(reverse('forms_home'))





















