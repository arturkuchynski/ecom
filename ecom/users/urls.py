from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    
    path('change-password/', views.change_password, name="change_password"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('register/', views.user_register, name="user_register"),
]
