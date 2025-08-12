from django.contrib import admin
from django.urls import path
from . import views

urlpatter = [
    path('', views.inicio)
]