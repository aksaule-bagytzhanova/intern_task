import api
from django.db.models.query import QuerySet
from django.shortcuts import render
from django_filters import filters, filterset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, serializers
from rest_framework_simplejwt.views import TokenVerifyView
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
from .service import get_client_ip, PostFilter, PaginationMovies
from django.db import models
# Create your views here.


class PostsWithNoPK(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter()
    serializer_class = PostSerilizer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter
    pagination_class = PaginationMovies

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostsWithPK(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter()
    serializer_class = PostSerilizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer