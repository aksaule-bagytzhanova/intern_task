from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('show_all/', views.ShowAll, name='showAll'),
    path('show_one/<int:pk>/', views.ShowOnePost, name='OnePost'),
    path('create_post/', views.CreatePost, name='Create_Post'),
    path('update_post/<int:pk>/', views.UpdatePost, name='Update_Post'),
    path('delete_post/<int:pk>/', views.DeletePost, name='Delete_Post'),
    
]