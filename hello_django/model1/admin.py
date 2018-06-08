from django.contrib import admin

# Register your models here.


from .models import User, Department, Student, Course


# admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(Department)
# admin.site.register(Course)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['d_id','d_name'] # 显示字段，可以点击列头进行排序
    list_display_link = ['d_id','d_name']
    list_filter = ['d_id'] # 过滤字段，过滤框会出现在右侧
    search_fields = ['d_name'] # 搜索字段，搜索框会出现在上侧
    list_per_page = 5 # 分页每页显示5条


class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_id', 's_name']
    list_display_links = ['s_id', 's_name']
    # fields = ['s_name','course','department'] 修改页的顺序
    fieldsets = [
        ('一组', {'fields':['s_name']}),
        ('二组', {'fields':['department','course']}),
    ] # 修改页分组


class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_id','c_name']
    list_display_links = ['c_id','c_name']
    list_per_page = 5



admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course,CourseAdmin)



