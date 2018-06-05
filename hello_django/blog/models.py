from django.db import models

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=16, blank=False)


