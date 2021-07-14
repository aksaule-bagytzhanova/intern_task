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
from .serializers import PostSerilizer
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
   


class ShowOnePost(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, pk):
        posts = Post.objects.get(id=pk)
        serializers = PostSerilizer(posts, many=False)
        return Response(serializers.data)

class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request, format=None):
        serializers = PostSerilizer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePost(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def put(self,request, pk, format=None):
        posts = self.get_object(pk)
        serializers = PostSerilizer(posts, data=request.data)
        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePost(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def delete(self,request, pk,format=None):
        posts = self.get_object(pk)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'status':'success',
            'user_id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
            })