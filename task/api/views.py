from django.db.models.query import QuerySet
from django.shortcuts import render
from django_filters import filters, filterset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenVerifyView
import api
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from .serializers import PostSerilizer, PostSerilizerFilter, UserSerializer
from .models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from django.http import Http404
from rest_framework import status
from .service import get_client_ip, PostFilter
from django.db import models
# Create your views here.

class ShowAll(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter
    queryset = Post.objects.filter()
    serializer_class = PostSerilizer
   


class ShowOnePost(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter()
    serializer_class = PostSerilizer

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerilizer
    

class UpdatePost(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    


class DeletePost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer