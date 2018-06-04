from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'User<id=%s,name=%s,age=%s>\n'%(self.id,self.name,self.age)


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30)

    def __str__(self):
        return 'Department<d_id=%s, d_name=%s>\n' % (self.d_id,
                                                     self.d_name)

class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30)

    def __str__(self):
        return 'Course<c_id=%s,c_name=%s>' % (self.c_id,
                                              self.c_name)


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    department = models.ForeignKey('Department', related_name='student')
    course = models.ManyToManyField('Course')

    def __str__(self):
        return 'Student<s_id=%s, s_name=%s>\n' % (self.s_id,
                                                  self.s_name)

class Stu_detail(models.Model):
    s_id = models.OneToOneField('Student') # 主键对应
    age = models.IntegerField()
    gender = models.BooleanField(default=1)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return 'Stu_detail<s_id=%s,age=%s,gender=%s,country=%s>' % (
            self.s_id, self.age, self.gender, self.city
        )




