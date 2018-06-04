from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from model1.models import User, Department, Course, Student


# 使用类对象，类的实例化做修改或添加，如get查找赋值(get出s1 = d1)，而不用内置的函数都要加上save()
# 增加数据
def add_user(request):
    # # 方法一： 简单方法
    # tizi = User(name='tizi', age=18)
    # tizi.save()
    # # 方法二： 类的实例化
    # xm = User()
    # xm.name = 'xiaoming'
    # xm.age = 19
    # xm.save()
    # # 方法三： 内置类方法
    # User.objects.create(name='xiaohong', age=20)
    # # 方法四： 有则查无则增
    User.objects.get_or_create(name='xiahua', age=21)
    return HttpResponse('成功')


# 查找数据
def search_user(request):
    # # 查询所有记录对象
    # rs = User.objects.all() # queryset
    # 查询一个记录对象 get返回的对象具有唯一性质，如果符合条件的对象有多个，则get报错！
    # rs = User.objects.get(id=1) # 类的对象
    # # 获取满足条件的对象 根据参数提供的提取条件，获取一个过滤后的QuerySet。
    # rs = User.objects.filter(name='xiaoming') # queryset
    # 排除name等于xiaoming的记录：
    # rs = User.objects.exclude(name='xiaoming')
    # 对结果排序order_by：
    # rs = User.objects.order_by('age')
    # 多项排序：
    # rs = User.objects.order_by('age', 'id')
    # 逆向排序：
    # rs = User.objects.order_by('-age')
    # 将返回来的QuerySet中的Model转换为字典
    # rs = User.objects.all().values()
    # 获取当前查询到的数据的总数：
    # rs = User.objects.count()


    # 查询对象的条件  -----------都要加__
    # exact相当于等于号：
    # rs = User.objects.filter(name__exact='xiaoming')
    # iexact：跟exact，只是忽略大小写的匹配。
    # contains包含：
    # rs = User.objects.filter(name__contains='xiao')
    # icontains跟contains，唯一不同是忽略大小写。
    # startwith以什么开始：
    # rs = User.objects.filter(name__startswith='xiao')
    # istartswith：同startswith，忽略大小写。
    # endswith：同startswith，以什么结尾。
    # iendswith：同istartswith，以什么结尾，忽略大小写。

    # in 成员所属：
    # rs = User.objects.filter(age__in=[18, 19, 20])
    # gt大于：
    # rs = User.objects.filter(age__gt=20)
    # gte大于等于：
    # rs = User.objects.filter(age__gte=20)
    # lt小于：
    # rs = User.objects.filter(age__lt=20)
    # lte小于等于：
    # rs = User.objects.filter(age__lte=20)
    # range区间：
    # rs = User.objects.filter(age__range=(18, 20))
    # isnull判断是否为空：
    # rs = User.objects.filter(country__isnull=True)
    # 切片： 注意:不能使用负数作为切片。
    rs= User.objects.all()[:2]
    print(rs)
    return HttpResponse('成功')


# 更新数据
def update_user(request):
    # 法一，只能改一个
    # rs = User.objects.get(name='tizi')
    # rs.name = 'TiZi'
    # rs.save()
    # 法二，可以改多个
    # User.objects.filter(name='xm').update(name='xiaoming')
    # 法三，改全部,没有条件主要用来为新建的属性添加值
    User.objects.all().update(city='xiamen')
    return HttpResponse('成功')


# 删除数据
def delete_user(request):
    User.objects.get(id=2).delete()
    return HttpResponse('successful!')


def add_info(request):
    d1 = Department(d_name='ZC')
    d1.save()
    # 一对多关系加内容
    s1 = Student(s_name='xiaoming')
    s1.department = d1 # 一个学生是ZC学校
    s1.save()
    # 多对多关系添加内容
    c1 = Course(c_name='python')
    s1 = Student.objects.first()
    c1.save()
    s1.course.add(c1) # 一个学生不属于一个科目，要add
    return HttpResponse('succeed')


def search_info(request):
    # rs = Student.objects.all()[0]
    # 一对多的查询
    # print(rs.department)
    # 多对多的正向查询
    # print(rs.course.all())
    # cs = Course.objects.first()
    # 多对多反向查询
    # print(cs.student_set.all())

    # 前向查询
    # s1 = Student.objects.get(s_id=1)
    # print(s1)
    # print(s1.department)

    # 直接赋值修改需要save
    # dx = Department.objects.get(d_id=4)
    # s1.department = dx
    # s1.save()
    # 反向查询
    # d1 = Department.objects.get(d_id=1)
    # d1.student_set.all()

    # add 添加
    # d1 = Department.objects.get(d_id=1)
    # s1 = Student.objects.get(s_id=4)
    # d1.student.add(s1) # 设置了别名 不然需要student_set
    # print(s1.department)

    # c1 = Course.objects.get(c_id=3)
    # s1.course.add(c1)
    # print(s1.course)

    # create(**kwargs) 创建并添加
    # s5 = Student.objects.get(s_id=3)
    # s5.course.create(c_name='php')
    # print(s5.course.all())

    # remove
    # cs = s5.course.all()[0]
    # s5.course.remove(cs)

    # clear
    # s5.course.clear()

    # 直接赋值 中间表赋值不用save
    c_all = Course.objects.all()
    s5 = Student.objects.get(s_id=3)
    s5.course = c_all
    s5.course.all()

    # 多表查询
    # 查询学院名字为‘BD’的学生的信息
    Student.objects.filter(department__d_name='BD')
    # 查询学生名字中包含‘xiao’的学生的学院信息
    Department.objects.filter(student__s_name='xiao')
    # 查询报了'python'课程的的学生的所属学院的信息
    Department.objects.filter(student__course__c_name='python')
    return HttpResponse('succeed')







