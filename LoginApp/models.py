from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserName = models.CharField(max_length=24)
    UserPwd = models.CharField(max_length=24)
