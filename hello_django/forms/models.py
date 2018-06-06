from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=100,
                                unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username











