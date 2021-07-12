from django.shortcuts import render
from rest_framework import serializers
import api
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework import status
from .serializers import PostSerilizer
from .models import Post
# Create your views here.


@api_view(['GET'])
def ShowAll(request):
    posts = Post.objects.all()
    serializers = PostSerilizer(posts, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ShowOnePost(request, pk):
    posts = Post.objects.get(id=pk)
    serializers = PostSerilizer(posts, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def CreatePost(request):
    serializers = PostSerilizer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def UpdatePost(request, pk):
    posts = Post.object.get(id=pk)
    serializers = PostSerilizer(instance=posts, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def DeletePost(request, pk):
    posts = Post.objects.get(id=pk)
    posts.delete()

    return Response('Item delete successfully!')

