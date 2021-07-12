from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
User = get_user_model()
# Create your models here
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=CASCADE)
    def __str__(self):
        return self.title




