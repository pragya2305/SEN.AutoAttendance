from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prof_sec', views.loginView),
    path('index/', views.index),
    path('getqr/', views.getqr),
]