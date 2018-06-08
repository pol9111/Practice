from forms.models import UserModel

def myuser(request):
    username = request.session.get('username', '未登入')
    user = UserModel.objects.filter(username=username).first()
    if user:
        return {'myuser': username}
    else:
        return {}
















