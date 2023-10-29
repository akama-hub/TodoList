from django.contrib import admin
from django.urls import path
from .views import todoList

urlpatterns = [
    path('a/', todoList), #views.py ファイルを介してプロジェクトとのつなぎこみ
]