from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Post, Tag

class PostSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostSerilizerFilter(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")