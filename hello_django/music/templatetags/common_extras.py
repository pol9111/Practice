from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


def mycut(value, arg):
    return value.replace(arg, '')

# 需要注册才能使用，方法一
register.filter('mycut', mycut)

# 方法二
@register.filter(name='mylower') # 可以不加名字使用默认函数名
def mylower(value):
    return value.lower()


@register.filter # 可以不加名字使用默认函数名
@stringfilter
def mylower1(value):
    return value.lower()











