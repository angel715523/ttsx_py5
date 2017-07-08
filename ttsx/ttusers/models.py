#coding=utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=30)
    ucode = models.CharField(default='', max_length=10)#邮编
    uphone = models.CharField(default='', max_length=15)
    uman = models.CharField(default='', max_length=20)#收件人
    uaddress = models.CharField(default='', max_length=100)

