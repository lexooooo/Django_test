from django.db import models
import random



class Users(models.Model):
    username = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=30, null=False, unique=False)
    userid = models.CharField(max_length=30, null=False, unique=True)
    createDate = models.CharField(max_length=30)
    id = random.randint(0, 10)