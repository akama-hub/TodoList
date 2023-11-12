from django.contrib import admin
from django.urls import path
from .views import TodoList

urlpatterns = [
    #views.py ファイルを介してプロジェクトとのつなぎこみ
    path('list/', TodoList.as_view())
]