from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=6, label='请输入用户名')

    password = forms.CharField(max_length=8, min_length=6,
                widget=forms.PasswordInput(
                attrs={'placeholder': u'请输入密码'}),
                error_messages = {'min_length': '密码长度小于6',
                                'max_length': '密码长度超过8了'}
            )
    password_repeat = forms.CharField(max_length=8, min_length=6,
                widget=forms.PasswordInput(
                attrs={'placeholder': u'请输入密码'},),
                error_messages = {'min_length': '密码长度小于6',
                                'max_length': '密码长度超过8了'}
                                      )
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',
    	widget = forms.PasswordInput(attrs={'placeholder': u'请输入密码 '}))










