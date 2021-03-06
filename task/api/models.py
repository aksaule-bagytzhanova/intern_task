from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User


# Create your models here
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title




