from django.shortcuts import render
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


# Create your views here.

class ShowAll(APIView):
    permission_classes = [IsAuthenticated]

    
    def get(self, request):
        posts = Post.objects.all()
        serializers = PostSerilizer(posts, many=True)
        return Response(serializers.data)


class ShowOnePost(APIView):
    permission_classes = [IsAuthenticated]
    def ShowOnePost(request, pk):
        posts = Post.objects.get(id=pk)
        serializers = PostSerilizer(posts, many=False)
        return Response(serializers.data)

class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    def CreatePost(request):
        serializers = PostSerilizer(data=request.data)

        if serializers.is_valid():
            serializers.save()

        return Response(serializers.data)

class UpdatePost(APIView):
    def UpdatePost(request, pk):
        posts = Post.object.get(id=pk)
        serializers = PostSerilizer(instance=posts, data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)


class DeletePost(APIView):
    def DeletePost(request, pk):
        posts = Post.objects.get(id=pk)
        posts.delete()

        return Response('Item delete successfully!')

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