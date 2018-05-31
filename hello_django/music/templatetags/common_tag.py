import datetime
from django import template

register = template.Library()
# register.tag('current_time', do_current_time)

# 简单标签，方法一
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


# 简单标签，方法二
@register.simple_tag(takes_context=True)
def current_time2(context): # 注意这里要不context传入
    tm = context['format_string']
    return datetime.datetime.now().strftime(tm)


# 包含标签
@register.inclusion_tag('show_tag.html', takes_context=True)
def show_results(context):
    # li = ['python','java','c++']
    lst1 = context['lst']
    return  {'choices':lst1}


# 分配标签(别名)
@register.assignment_tag
def current_time_1(format_string):
    return datetime.datetime.now().strftime(format_string)










