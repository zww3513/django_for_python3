from django.db import models


# Create your models here.
class User(models.Model):
    """用户表"""
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    role = models.IntegerField(default='0')
    nickname = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.IntegerField(default='0')

    def __str__(self):
        return  self.username
