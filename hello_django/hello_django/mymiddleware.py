from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyException(MiddlewareMixin):
    def process_exception(self,request,exception):
        return HttpResponse(exception)
# 当视图抛出异常时调用，在每个请求上调用，
# 返回一个HttpResponse对象


from forms.models import UserModel
# forms里面的views的home做变动
class UserMiddleware(MiddlewareMixin):
    def __init(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request到达view之前执行的代码
        username = request.session.get('username','未登入')
        user = UserModel.objects.filter(username=username).first()
        if user and not hasattr(request, 'myuser'):
            setattr(request, 'myuser', user)
            # 给request设置一个新的属性，调用这个属性返回user
        else:
            setattr(request, 'myuser', '游客')
            # 如果没有此user就赋予request游客属性
        response = self.get_response(request)
        # response到达用户浏览器之前执行的代码
        return response
















