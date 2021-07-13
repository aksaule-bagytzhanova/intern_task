from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('show_all/', views.ShowAll.as_view(), name='showAll'),
    path('show_one/<int:pk>/', views.ShowOnePost.as_view(), name='OnePost'),
    path('create_post/', views.CreatePost.as_view(), name='Create_Post'),
    path('update_post/<int:pk>/', views.UpdatePost.as_view(), name='Update_Post'),
    path('delete_post/<int:pk>/', views.DeletePost.as_view(), name='Delete_Post'),
    path('token/verify/', TokenVerifyView().as_view(), name='token_verify'),
    
]