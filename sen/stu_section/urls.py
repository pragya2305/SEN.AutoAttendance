from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('stu_sec/', views.loginView),
    path('scan/', views.scan),
    path('test/', views.test),
]